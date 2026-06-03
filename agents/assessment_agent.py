import os
import json
from openai import OpenAI
from dotenv import load_dotenv

load_dotenv()

def load_certification(cert_id: str) -> dict:
    with open("data/certifications.json", "r") as f:
        data = json.load(f)
    for cert in data["certifications"]:
        if cert["id"] == cert_id:
            return cert
    raise ValueError(f"Certification {cert_id} not found")

def run_assessment_agent(learner_id: str, cert_id: str, current_score: int) -> str:
    client = OpenAI(
        base_url="https://models.inference.ai.azure.com",
        api_key=os.environ["GITHUB_TOKEN"],
    )

    cert = load_certification(cert_id)

    system_prompt = """
You are an Assessment Agent for an enterprise certification programme.
Your job is to generate grounded practice questions and evaluate learner readiness.

Rules:
- Generate exactly 5 multiple choice questions
- Each question must relate to a specific skill from the certification
- Always cite which skill area each question tests
- After questions, provide a readiness verdict based on current score
- Format each question clearly with 4 options (A, B, C, D) and the correct answer
- Keep questions realistic and exam-style
"""

    user_message = f"""
Generate a practice assessment for:

LEARNER: {learner_id}
CERTIFICATION: {cert_id} — {cert['title']}
CURRENT PRACTICE SCORE: {current_score}%
SKILLS TO TEST: {', '.join(cert['skills'])}
DIFFICULTY: {cert['difficulty']}

Produce:
1. 5 multiple choice questions (with answers)
2. Which skill each question targets
3. Readiness verdict (Ready / Almost Ready / Needs More Prep)
4. Specific areas to focus on based on the skill gaps
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
    result = run_assessment_agent(
        learner_id="L-1001",
        cert_id="AZ-204",
        current_score=45
    )
    print("=== ASSESSMENT AGENT ===")
    print(result)