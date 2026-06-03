# Enterprise Learning Agent System
> Multi-agent AI system for enterprise certification programme management
> Built for: Microsoft Foundry Reasoning Agents Challenge

---

## What This System Does

This system helps organisations manage internal certification programmes
using a chain of specialised AI agents. Each agent has one job, and
together they form a complete reasoning pipeline — from learning path
recommendation to team-level risk analysis.

---

## Agent Architecture
User Input
│
▼
[Agent 1] Learning Path Curator
│  Recommends certifications grounded in approved knowledge base
│
▼
[Agent 2] Study Plan Generator
│  Builds week-by-week schedule based on learner capacity
│
▼
[Agent 3] Assessment Agent
│  Generates grounded practice questions + readiness verdict
│
▼
[Agent 4] Manager Insights Agent
│  Analyses entire team — surfaces risk, predicts pass rates
│
▼
[Agent 5] Engagement Agent
│  Recommends study windows based on real work patterns
│
▼
System Summary + Verdict

---

## Microsoft IQ Layers

| IQ Layer | How This System Uses It |
|---|---|
| **Foundry IQ** | Agents are grounded in a certifications knowledge base. Only approved certifications are recommended — no hallucination |
| **Fabric IQ** | Structured semantic data models learner profiles, roles, skill gaps, study hours, and pass thresholds |
| **Work IQ** | Engagement Agent reads work signals — meeting load, focus hours, preferred slots — to recommend realistic study windows |

---

## Agent Responsibilities

### Agent 1 — Learning Path Curator
- Maps learner role and goal to relevant certifications
- Respects prerequisites (AZ-900 before AZ-204)
- Only recommends from approved knowledge base
- Cites certification IDs in every recommendation

### Agent 2 — Study Plan Generator
- Reads learner profile (hours available, weeks until exam, current score)
- Generates week-by-week schedule that fits real constraints
- Front-loads foundations, advances difficulty progressively
- Flags if timeline is too tight to realistically pass

### Agent 3 — Assessment Agent
- Generates 5 exam-style questions grounded in certification skills
- Cites which skill area each question tests
- Produces readiness verdict (Ready / Almost Ready / Needs More Prep)
- Identifies specific skill gaps with actionable recommendations

### Agent 4 — Manager Insights Agent
- Analyses all learners simultaneously
- Identifies at-risk learners and explains why
- Performs capacity analysis (hours available vs hours needed)
- Predicts team pass rate based on current trajectory
- Recommends top 3 manager actions

### Agent 5 — Engagement Agent
- Reads work signals (meeting hours, focus hours, preferred slots)
- Recommends specific study windows avoiding peak work days
- Generates personalised reminder messages per learner
- Flags capacity-constrained learners

---

## Reasoning Patterns Used

| Pattern | Where Used |
|---|---|
| Planner–Executor | Curator plans the path, Generator executes the schedule |
| Grounded Retrieval | All agents read from structured data before responding |
| Critic / Verifier | Assessment Agent scores readiness against pass threshold |
| Role Specialisation | Each agent has a single clear responsibility |
| Team-level Reasoning | Manager Agent reasons across all learners simultaneously |

---

## Project Structure
learning-agent-system/
├── agents/
│   ├── learning_path_curator.py    # Agent 1
│   ├── study_plan_generator.py     # Agent 2
│   ├── assessment_agent.py         # Agent 3
│   ├── manager_insights_agent.py   # Agent 4
│   └── engagement_agent.py         # Agent 5
├── data/
│   ├── certifications.json         # Knowledge base (Foundry IQ simulation)
│   ├── learner_profiles.json       # Synthetic learner data (Fabric IQ)
│   └── work_signals.json           # Work context data (Work IQ simulation)
├── main.py                         # Orchestrator — runs all agents in sequence
├── .env                            # API credentials (not committed)
├── .gitignore
└── README.md

---

## How to Run

### 1. Clone the repository
```bash
git clone https://github.com/YOUR_USERNAME/learning-agent-system
cd learning-agent-system
```

### 2. Create virtual environment
```bash
python -m venv .venv

# Mac/Linux
source .venv/bin/activate

# Windows
.venv\Scripts\activate
```

### 3. Install dependencies
```bash
pip install openai python-dotenv
```

### 4. Set up credentials
Create a `.env` file:
GITHUB_TOKEN=your_github_token_here
MODEL_NAME=gpt-4o

### 5. Run the full system
```bash
python main.py
```

### 6. Run individual agents
```bash
python agents/learning_path_curator.py
python agents/study_plan_generator.py
python agents/assessment_agent.py
python agents/manager_insights_agent.py
python agents/engagement_agent.py
```

---

## Synthetic Data Notice

> All data in this project is synthetic and fictional.
> No real employee names, emails, or personal information is used.
> Learner IDs (L-1001), Employee IDs (EMP-001), and all profiles
> are fabricated for demonstration purposes only.

---

## Azure Foundry Deployment Note

This system is designed for Microsoft Foundry deployment.
It currently runs on GitHub Models (GPT-4o via Azure-hosted inference)
due to Azure subscription constraints during development.

The architecture is fully compatible with:
- Azure AI Foundry Agent Service
- Foundry IQ knowledge base integration
- Azure AI Search for grounded retrieval
- Hosted Agents deployment pattern

---

## Responsible AI

- All outputs are clearly labelled as AI-generated
- No PII or real employee data is used anywhere
- Agents are grounded in approved data — no free-text hallucination
- Manager insights avoid exposing individual sensitive details
- Human oversight recommended before acting on agent verdicts

---

## Built With

- Python 3.11
- OpenAI SDK (Azure-compatible)
- GitHub Models — GPT-4o
- Microsoft Foundry (target deployment platform)