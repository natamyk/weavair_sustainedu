from flask import Flask, render_template
from models.user_model import User
from utils.data_processing import load_data

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

if __name__ == '__main__':
    app.run(debug=True)
