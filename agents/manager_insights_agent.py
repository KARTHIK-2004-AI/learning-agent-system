import os
import json
from openai import OpenAI
from dotenv import load_dotenv

load_dotenv()

def load_all_learners() -> list:
    with open("data/learner_profiles.json", "r") as f:
        data = json.load(f)
    return data["learners"]

def run_manager_insights_agent() -> str:
    client = OpenAI(
        base_url="https://models.inference.ai.azure.com",
        api_key=os.environ["GITHUB_TOKEN"],
    )

    learners = load_all_learners()
    team_data = json.dumps(learners, indent=2)

    system_prompt = """
You are a Manager Insights Agent for an enterprise certification programme.
Your job is to analyse team-level learning data and surface actionable insights.

Rules:
- Never expose sensitive personal data — refer to learners by ID and role only
- Identify risk patterns across the team
- Flag learners who are behind schedule
- Highlight capacity constraints
- Give the manager clear, prioritised actions
- Be concise and structured — managers are busy
"""

    user_message = f"""
Analyse the following team learning data and produce a manager insights report:

TEAM DATA:
{team_data}

Produce:
1. Team readiness summary (overall health)
2. At-risk learners and why
3. Capacity analysis (hours available vs needed)
4. Top 3 recommended manager actions
5. Predicted team pass rate based on current trajectory
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
    result = run_manager_insights_agent()
    print("=== MANAGER INSIGHTS AGENT ===")
    print(result)