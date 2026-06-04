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

## Screenshots

### Configure Learner & Run Agents
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

## Screenshots

### Configure Learner & Run Agents
<img width="1352" height="576" alt="image" src="https://github.com/user-attachments/assets/b1325af1-ce88-47b6-bdb3-59042f4130c3" />

### Learning Path & Study Plan
<img width="1157" height="471" alt="image" src="https://github.com/user-attachments/assets/36d4cfe6-9cec-4add-a45f-46926df70ba4" />

### Assessment Agent + Manager Insights
<img width="1164" height="470" alt="image" src="https://github.com/user-attachments/assets/114d3d2c-8ec1-490a-984d-fa5132094ecf" />



### Engagement Agent + Final Verdict
<img width="1165" height="595" alt="image" src="https://github.com/user-attachments/assets/a5f2dee2-474e-47f4-99f7-6a5ea878358b" />

---

## Agent Architecture

```
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
```

## Microsoft IQ Layers

| IQ Layer | How This System Uses It |
|---|---|
| **Foundry IQ** | Agents grounded in certifications knowledge base — only approved certifications recommended, no hallucination |
| **Fabric IQ** | Structured semantic data models learner profiles, roles, skill gaps, study hours, and pass thresholds |
| **Work IQ** | Engagement Agent reads work signals — meeting load, focus hours, preferred slots — to recommend realistic study windows |

---

## Foundry IQ Implementation

Real Foundry IQ connects to Azure Blob Storage, SharePoint, or OneLake.
In this implementation, `data/certifications.json` acts as the knowledge base.
Agents are instructed to ONLY recommend from this source and MUST cite
certification IDs — replicating Foundry IQ's grounded, citation-required
retrieval behaviour.

**To connect real Foundry IQ:**
1. Upload `certifications.json` to Azure Blob Storage
2. Index with Azure AI Search
3. Connect to Foundry Agent via knowledge base configuration
4. Replace JSON loader with Foundry IQ retrieval call

**What grounding prevents:**
- Agents cannot recommend certifications outside the knowledge base
- Prerequisites are enforced (AZ-900 before AZ-204)
- Every recommendation includes a cited certification ID
- Assessment questions map to approved skill areas only

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
│   ├── learning_path_curator.py    # Agent 1 — Foundry IQ grounding
│   ├── study_plan_generator.py     # Agent 2 — Fabric IQ planning
│   ├── assessment_agent.py         # Agent 3 — Foundry IQ assessment
│   ├── manager_insights_agent.py   # Agent 4 — Team risk analysis
│   └── engagement_agent.py         # Agent 5 — Work IQ scheduling
├── data/
│   ├── certifications.json         # Knowledge base (Foundry IQ)
│   ├── learner_profiles.json       # Synthetic learner data (Fabric IQ)
│   └── work_signals.json           # Work context data (Work IQ)
├── templates/
│   └── index.html                  # Flask web UI
├── app.py                          # Web application
├── main.py                         # Terminal orchestrator
├── requirements.txt
└── README.md

---

## How to Run

### Web Interface (Recommended)
```bash
git clone https://github.com/KARTHIK-2004-AI/learning-agent-system
cd learning-agent-system
python -m venv .venv
.venv\Scripts\activate        # Windows
source .venv/bin/activate     # Mac/Linux
pip install -r requirements.txt
```

Create `.env` file:
GITHUB_TOKEN=your_github_token_here
MODEL_NAME=gpt-4o

```bash
python app.py
# Open http://localhost:5000
```

### Terminal Mode
```bash
python main.py
```

### Individual Agents
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
- Flask — Web interface
- OpenAI SDK (Azure-compatible)
- GitHub Models — GPT-4o (Azure-hosted)
- Microsoft Foundry (target deployment platform)
