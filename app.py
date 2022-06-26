from flask import Flask, render_template, request
from flask_mysqldb import MySQL
import random


# Create a Flask Instance
app = Flask(__name__)

# config db
app.config['MYSQL_HOST'] = 'localhost'
app.config['MYSQL_USER'] = 'root'
app.config['MYSQL_PASSWORD'] = '123456'
app.config['MYSQL_DB'] = '问题'

mysql = MySQL(app)
# app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql://root:******@localhost/问题'

# questions come here in a list
questions = ['汉朝时有一猛将，人称飞将，他是谁？',
            '刘邦的两个著名的文官是谁？',
            '黄巾起义是那几个人开始的？',
            '袁绍的三个儿子叫啥？',
            '庞统的字是啥？',
            '明太祖是谁？',
            '包青天真正的名字叫啥？',
            '隋文帝是谁？',
            '乾隆皇帝的名字是啥？',
            '中国最后一个皇帝是谁？']

# answers come here in a list
answers = ['飞将军李广',
            '萧何、张良',
            '张角、张宝、张梁',
            '袁谭、袁熙、袁尚',
            '士元',
            '朱元璋',
            '包拯',
            '杨坚',
            '爱新觉罗 • 弘历',
            '爱新觉罗 • 博仪',]

# the question number and answer corresponds
# the index of the entity in the list is represented
# in a variable and is generated with the random module

# questionprinted = 

# Create a route decorator
@app.route("/")
def index():
    return render_template('index.html')

# localhost:5000/question
@app.route('/question')

def question():
    # QNA = random.randint(0, 9)
    # return questions[QNA]
    # return answers[QNA]
    return render_template('qn.html')

# localhost:5000/about
@app.route('/about')

def about():
    return render_template('about.html')

@app.route('/500')
def fiveoo():
    return render_template('500.html')

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


