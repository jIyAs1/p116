# importing modules from flask library
from flask import Flask , render_template

# creating instance of class Flask, by providing __name__ keyword as argument
app = Flask(__name__)

# write the routes using decorator functions
# default route or 'URL'
@app.route("/")
def home():

    name = "Jiya" # write your name
    age = "15" # write your age

    return render_template('index.html' , name = name , age = age)

# define the route to father webpage
@app.route("/father")
def home():

    name = "Lalit" 
    age = "44"

    return render_template('index.html' , name = name , age = age)

# define the route to mother webpage
@app.route("/mother")
def home():

    name = "Riya" 
    age = "43"

    return render_template('index.html' , name = name , age = age)

# define the route to friends webpage
@app.route("/friend")
def home():

    name = "Sahiti" 
    age = "15"

    return render_template('index.html' , name = name , age = age)

# add other routes, if you want




# run the file
if __name__  ==  '__main__':
    app.run(debug=True)
