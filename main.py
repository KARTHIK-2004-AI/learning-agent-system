import json
from agents.learning_path_curator import run_learning_path_curator
from agents.study_plan_generator import run_study_plan_generator
from agents.assessment_agent import run_assessment_agent
from agents.manager_insights_agent import run_manager_insights_agent

def run_multi_agent_system(learner_id: str, role: str, goal: str, cert_id: str, current_score: int):
    
    print("\n" + "="*60)
    print("   ENTERPRISE LEARNING AGENT SYSTEM")
    print("="*60)
    print(f"   Learner  : {learner_id}")
    print(f"   Role     : {role}")
    print(f"   Target   : {cert_id}")
    print("="*60)

    # ── AGENT 1: Learning Path Curator ──────────────────────────
    print("\n[AGENT 1] Learning Path Curator is running...")
    print("-"*60)
    learning_path = run_learning_path_curator(role, goal)
    print(learning_path)

    # ── AGENT 2: Study Plan Generator ───────────────────────────
    print("\n[AGENT 2] Study Plan Generator is running...")
    print("-"*60)
    study_plan = run_study_plan_generator(learner_id)
    print(study_plan)

    # ── AGENT 3: Assessment Agent ────────────────────────────────
    print("\n[AGENT 3] Assessment Agent is running...")
    print("-"*60)
    assessment = run_assessment_agent(learner_id, cert_id, current_score)
    print(assessment)

    # ── AGENT 4: Manager Insights ────────────────────────────────
    print("\n[AGENT 4] Manager Insights Agent is running...")
    print("-"*60)
    insights = run_manager_insights_agent()
    print(insights)

    # ── FINAL SUMMARY ────────────────────────────────────────────
    print("\n" + "="*60)
    print("   SYSTEM SUMMARY")
    print("="*60)
    print(f"✅ Learning path curated for: {role}")
    print(f"✅ Study plan generated for:  {learner_id} targeting {cert_id}")
    print(f"✅ Assessment completed —  current score: {current_score}%")
    
    if current_score >= 75:
        print("🎉 VERDICT: Learner is READY for the exam!")
    elif current_score >= 60:
        print("⚠️  VERDICT: Learner is ALMOST READY — 1-2 more weeks recommended")
    else:
        print("📚 VERDICT: Learner NEEDS MORE PREP — follow the study plan")
    
    print("="*60)
    print("\n[SYSTEM] All agents completed successfully.\n")


if __name__ == "__main__":
    run_multi_agent_system(
        learner_id="L-1001",
        role="Cloud Engineer",
        goal="become proficient in Azure cloud development and deployment",
        cert_id="AZ-204",
        current_score=45
    )