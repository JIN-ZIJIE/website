from flask import Flask, render_template


# Create a Flask Instance
app = Flask(__name__)

# Create a route decorator
@app.route("/")

#ef hello_world():
#   return "<h1>Hello, World!</h1>"

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

# create custom error
# invalid url
@app.errorhandler(404)
def page_not_found(e):
    return render_template('404.html'),404

# internal server error
@app.errorhandler(500)
def page_not_found(e):
    return render_template('500.html'),500


