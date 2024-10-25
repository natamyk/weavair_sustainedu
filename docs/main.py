from flask import Flask
from user_profile import UserProfile
from content_management import ContentManagement
from ai_engine import AIEngine

app = Flask(__name__)

@app.route('/')
def index():
    return "Welcome to the AI-Driven Adaptive Learning Platform!"

@app.route('/generate_user_profile/<user_id>')
def generate_user_profile(user_id):
    profile = UserProfile(user_id)
    return profile.create_profile()

@app.route('/generate_content/<topic>')
def generate_content(topic):
    content = ContentManagement()
    return content.create_content(topic)

@app.route('/recommend_learning_path/<user_id>')
def recommend_learning_path(user_id):
    ai_engine = AIEngine(user_id)
    return ai_engine.recommend_learning_path()

if __name__ == '__main__':
    app.run(debug=True)
