import os
import json
from openai import OpenAI
from dotenv import load_dotenv

load_dotenv()

# Load our knowledge base (this simulates Foundry IQ grounding)
def load_certifications():
    with open("data/certifications.json", "r") as f:
        return json.load(f)

# The agent function
def run_learning_path_curator(learner_role: str, learner_goal: str) -> str:
    client = OpenAI(
        base_url="https://models.inference.ai.azure.com",
        api_key=os.environ["GITHUB_TOKEN"],
    )

    # Load knowledge base
    cert_data = load_certifications()
    cert_context = json.dumps(cert_data, indent=2)

    # System prompt — this is the agent's "brain"
    system_prompt = f"""
You are a Learning Path Curator for an enterprise certification programme.
Your job is to recommend the most relevant certifications for a given role and goal.

You MUST only recommend certifications from the approved knowledge base below.
Always cite the certification ID when making recommendations.
Always mention prerequisites before advanced certifications.
Be specific and structured in your response.

APPROVED KNOWLEDGE BASE:
{cert_context}
"""

    # User message
    user_message = f"""
I am a {learner_role}.
My goal is: {learner_goal}

Please recommend a learning path for me with:
1. Which certification to start with and why
2. The full path to reach my goal
3. Estimated total study hours
4. Key skills I will gain
"""

    response = client.chat.completions.create(
        model=os.environ["MODEL_NAME"],
        messages=[
            {"role": "system", "content": system_prompt},
            {"role": "user", "content": user_message}
        ]
    )

    return response.choices[0].message.content


# Test it directly
if __name__ == "__main__":
    result = run_learning_path_curator(
        learner_role="Cloud Engineer",
        learner_goal="become proficient in Azure cloud development and deployment"
    )
    print("=== LEARNING PATH CURATOR AGENT ===")
    print(result)