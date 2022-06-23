from flask import Flask, render_template,request
from flask_mysqldb import MySQL
import yaml

# Create a Flask Instance
app = Flask(__name__)

db = yaml.load(open('db.yaml'))
app.config['MYSQL_HOST'] = db['mysql_host']
app.config['MYSQL_USER'] = db['mysql_user']
app.config['MYSQL_PASSWORD'] = db['mysql_password']
app.config['MYSQL_DB'] =db['mysql_db']

mysql = MySQL(app)

# Create a route decorator
@app.route("/", methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        questiondb = request.form
        question = questiondb['question']
        sur = mysql.connection.cursor()
        cur.execute('INSERT INTO urser(问题) VALUES(%s)',(问题))
        mysql.connection.commit()
        cur.close()
        return '200'
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


