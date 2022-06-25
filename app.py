from typing import Any
from flask import Flask, render_template,request
from flask_mysqldb import MySQL


# Create a Flask Instance
app = Flask(__name__)

# config db
app.config['MYSQL_HOST'] = 'localhost'
app.config['MYSQL_USER'] = 'root'
app.config['MYSQL_PASSWORD'] = '123456'
app.config['MYSQL_DB'] = '问题'

mysql = MySQL(app)
# app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql://root:******@localhost/问题'

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
@app.route('/datapwd123456', methods=['GET', 'POST'])
def data():
    # if request.method == 'POST':
        # qna = request.form
        # question = qna['question']
        # answer = qna['answer']
        # cur = mysql.connection.cursor()
        # cur.execute('INSERT INTO qna(question, answer) VALUES(%s, %s)',(question, answer))
        # mysql.connection.commit()
        # cur.close()
        # return 'Success'
    return render_template('betterdata.html')

# localhost:5000/thanks
@app.route('/credits')

def credits():
    return render_template('thanks.html')

# create custom error
# invalid url
@app.errorhandler(404)
def page_not_found(e):
    return render_template('404.html'),404

# internal server error
@app.errorhandler(500)
def page_not_found(e):
    return render_template('500.html'),500


