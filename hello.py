from flask import Flask, render_template


# Create a Flask Instance
app = Flask(__name__)

# Create a route decorator
@app.route("/")

#ef hello_world():
#   return "<h1>Hello, World!</h1>"

def hello_world():
    first_name = 'john'
    stuff = "this is bold text"

    favourite_pizza = ['pep', 'cheese', 'mush', 41]
    return render_template('index.html',
                           first_name=first_name, stuff=stuff,
                           favourite_pizza=favourite_pizza)


# localhost:5000/user/Jin
@app.route('/user/<name>')

def user(name):
    return render_template('user.html', user_name=name)

# create custom error

# invalid url
@app.errorhandler(404)
def page_not_found(e):
    return render_template('404.html'),404

# internaol server error
@app.errorhandler(500)
def page_not_found(e):
    return render_template('500.html'),500


