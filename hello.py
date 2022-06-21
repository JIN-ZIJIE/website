from flask import Flask, render_template
from flask_sqlalchemy import SQLAlchemy


# Create a Flask Instance
app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql://root:123456@localhost/问题'

# Create a route decorator
@app.route("/")
def index():
    return render_template('index.html')

# localhost:5000/question
@app.route('/question')

def question():
    return render_template('question.html')

# localhost:5000/about
@app.route('/about')

def about():
    return render_template('about.html')

# localhost:5000/database
@app.route('/data')
def data():
    return render_template('data.html')

# create custom error
# invalid url
@app.errorhandler(404)
def page_not_found(e):
    return render_template('404.html'),404

# internal server error
@app.errorhandler(500)
def page_not_found(e):
    return render_template('500.html'),500


