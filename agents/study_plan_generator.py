import os
import json
from openai import OpenAI
from dotenv import load_dotenv

load_dotenv()

def load_learner(learner_id: str) -> dict:
    with open("data/learner_profiles.json", "r") as f:
        data = json.load(f)
    for learner in data["learners"]:
        if learner["id"] == learner_id:
            return learner
    raise ValueError(f"Learner {learner_id} not found")

def load_certification(cert_id: str) -> dict:
    with open("data/certifications.json", "r") as f:
        data = json.load(f)
    for cert in data["certifications"]:
        if cert["id"] == cert_id:
            return cert
    raise ValueError(f"Certification {cert_id} not found")

def run_study_plan_generator(learner_id: str) -> str:
    client = OpenAI(
        base_url="https://models.inference.ai.azure.com",
        api_key=os.environ["GITHUB_TOKEN"],
    )

    # Load learner and their target certification
    learner = load_learner(learner_id)
    cert = load_certification(learner["certification_target"])

    system_prompt = """
You are a Study Plan Generator for an enterprise certification programme.
Your job is to create a realistic, week-by-week study schedule.

Rules:
- Never exceed the learner's available hours per week
- Always include weekly assessment checkpoints
- Front-load foundational topics, advanced topics come later
- Flag if the learner's timeline is too tight to realistically pass
- Be specific about what to study each week
- Target 75% practice score before recommending the exam
"""

    user_message = f"""
Create a study plan for this learner:

LEARNER PROFILE:
- ID: {learner['id']}
- Role: {learner['role']}
- Target Certification: {learner['certification_target']}
- Hours available per week: {learner['hours_available_per_week']}
- Weeks until exam: {learner['weeks_until_exam']}
- Current practice score: {learner['current_score']}%

CERTIFICATION DETAILS:
- Title: {cert['title']}
- Required Skills: {', '.join(cert['skills'])}
- Recommended total hours: {cert['recommended_hours']}
- Difficulty: {cert['difficulty']}

Produce:
1. Week-by-week study plan
2. Hours per topic
3. Checkpoint assessments
4. Exam readiness prediction
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
    result = run_study_plan_generator("L-1001")
    print("=== STUDY PLAN GENERATOR AGENT ===")
    print(result)