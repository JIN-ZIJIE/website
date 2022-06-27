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
# questions = ['汉朝时有一猛将，人称飞将，他是谁？',
            # '刘邦的两个著名的文官是谁？',
            # '黄巾起义是那几个人开始的？',
            # '袁绍的三个儿子叫啥？',
            # '庞统的字是啥？',
            # '明太祖是谁？',
            # '包青天真正的名字叫啥？',
            # '隋文帝是谁？',
            # '乾隆皇帝的名字是啥？',
            # '中国最后一个皇帝是谁？']

# answers come here in a list
# answers = ['飞将军李广',
            # '萧何、张良',
            # '张角、张宝、张梁',
            # '袁谭、袁熙、袁尚',
            # '士元',
            # '朱元璋',
            # '包拯',
            # '杨坚',
            # '爱新觉罗 • 弘历',
            # '爱新觉罗 • 博仪',]

# the question number and answer corresponds
# the index of the entity in the list is represented
# in a variable and is generated with the random module

# Create a route decorator
@app.route("/")
def index():
    return render_template('index.html')

# localhost:5000/question
@app.route('/question')
def question():
    QNA = random.randint(1, 34)
    if QNA == 1:
        return render_template('qn1.html')
    if QNA == 2:
        return render_template('qn2.html')
    if QNA == 3:
        return render_template('qn3.html')
    if QNA == 4:
        return render_template('qn4.html')
    if QNA == 5:
        return render_template('qn5.html')
    if QNA == 6:
        return render_template('qn6.html')
    if QNA == 7:
        return render_template('qn7.html')
    if QNA == 8:
        return render_template('qn8.html')
    if QNA == 9:
        return render_template('qn9.html')
    if QNA == 10:
        return render_template('qn10.html')
    if QNA == 11:
        return render_template('qn11.html')
    if QNA == 12:
        return render_template('qn12.html')
    if QNA == 13:
        return render_template('qn13.html')
    if QNA == 14:
        return render_template('qn14.html')
    if QNA == 15:
        return render_template('qn15.html')
    if QNA == 16:
        return render_template('qn16.html')
    if QNA == 17:
        return render_template('qn17.html')
    if QNA == 18:
        return render_template('qn18.html')
    if QNA == 19:
        return render_template('qn19.html')
    if QNA == 20:
        return render_template('qn20.html')
    if QNA == 21:
        return render_template('qn21.html')
    if QNA == 22:
        return render_template('qn22.html')
    if QNA == 23:
        return render_template('qn23.html')
    if QNA == 24:
        return render_template('qn24.html')
    if QNA == 25:
        return render_template('qn25.html')
    if QNA == 26:
        return render_template('qn26.html')
    if QNA == 27:
        return render_template('qn27.html')
    if QNA == 28:
        return render_template('qn28.html')
    if QNA == 29:
        return render_template('qn29.html')
    if QNA == 30:
        return render_template('qn30.html')
    if QNA == 31:
        return render_template('qn31.html')
    if QNA == 32:
        return render_template('qn32.html')
    if QNA == 33:
        return render_template('qn33.html')
    if QNA == 34:
        return render_template('qn34.html')

# localhost:5000/about
@app.route('/about')
def about():
    return render_template('about.html')

# localhost:5000/database
@app.route('/datapwd123456')#, methods=['GET', 'POST']
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
