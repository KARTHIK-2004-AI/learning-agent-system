from flask import Flask, render_template, request, jsonify
from agents.learning_path_curator import run_learning_path_curator
from agents.study_plan_generator import run_study_plan_generator
from agents.assessment_agent import run_assessment_agent
from agents.manager_insights_agent import run_manager_insights_agent
from agents.engagement_agent import run_engagement_agent
import markdown

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/generate', methods=['POST'])
def generate():
    data = request.json
    learner_id = data.get('learner_id', 'L-1001')
    role = data.get('role', 'Cloud Engineer')
    goal = data.get('goal', '')
    cert_id = data.get('cert_id', 'AZ-204')
    current_score = int(data.get('current_score', 45))

    results = {}

    results['learning_path'] = markdown.markdown(
        run_learning_path_curator(role, goal)
    )
    results['study_plan'] = markdown.markdown(
        run_study_plan_generator(learner_id)
    )
    results['assessment'] = markdown.markdown(
        run_assessment_agent(learner_id, cert_id, current_score)
    )
    results['manager_insights'] = markdown.markdown(
        run_manager_insights_agent()
    )
    results['engagement'] = markdown.markdown(
        run_engagement_agent(learner_id)
    )

    return jsonify(results)

if __name__ == '__main__':
    app.run(debug=True)