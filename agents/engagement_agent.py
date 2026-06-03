import os
import json
from openai import OpenAI
from dotenv import load_dotenv

load_dotenv()

def load_work_signals(learner_id: str) -> dict:
    with open("data/work_signals.json", "r") as f:
        data = json.load(f)
    for emp in data["employees"]:
        if emp["learner_id"] == learner_id:
            return emp
    raise ValueError(f"No work signals found for {learner_id}")

def load_learner(learner_id: str) -> dict:
    with open("data/learner_profiles.json", "r") as f:
        data = json.load(f)
    for learner in data["learners"]:
        if learner["id"] == learner_id:
            return learner
    raise ValueError(f"Learner {learner_id} not found")

def run_engagement_agent(learner_id: str) -> str:
    client = OpenAI(
        base_url="https://models.inference.ai.azure.com",
        api_key=os.environ["GITHUB_TOKEN"],
    )

    signals = load_work_signals(learner_id)
    learner = load_learner(learner_id)

    system_prompt = """
You are an Engagement Agent for an enterprise learning system.
Your job is to keep learners on track without disrupting their work.

Rules:
- Never schedule reminders during peak work days if avoidable
- Respect the learner's preferred learning time slot
- If meeting hours exceed 20 per week, flag as capacity-constrained
- If study streak is 0, use a gentle re-engagement tone
- If study streak is 5+, use a motivational reinforcement tone
- Suggest specific days and times for study sessions
- Keep reminders human and supportive, not robotic
- Suggest realistic session lengths based on available focus hours
"""

    user_message = f"""
Create an engagement plan for this learner based on their work context:

LEARNER PROFILE:
- ID: {learner['id']}
- Role: {learner['role']}
- Target Certification: {learner['certification_target']}
- Current Score: {learner['current_score']}%
- Hours needed per week: {learner['hours_available_per_week']}

WORK SIGNALS:
- Meeting hours per week: {signals['meeting_hours_per_week']}
- Focus hours per week: {signals['focus_hours_per_week']}
- Preferred learning slot: {signals['preferred_learning_slot']}
- Peak work days: {', '.join(signals['peak_work_days'])}
- Current study streak: {signals['current_study_streak_days']} days
- Last study session: {signals['last_study_session']}

Produce:
1. Capacity assessment (is workload manageable for study?)
2. Recommended study windows this week (specific days + times)
3. Personalised reminder message for this learner
4. Risk flag if workload makes study unrealistic
"""

    response = client.chat.completions.create(
        model=os.environ["MODEL_NAME"],
        messages=[
            {"role": "system", "content": system_prompt},
            {"role": "user", "content": user_message}
        ]
    )

    return response.choices[0].message.content


if __name__ == "__main__":
    # Test all 3 learners to show different engagement styles
    for learner_id in ["L-1001", "L-1002", "L-1003"]:
        print(f"\n{'='*60}")
        print(f"  ENGAGEMENT AGENT — {learner_id}")
        print(f"{'='*60}")
        result = run_engagement_agent(learner_id)
        print(result)