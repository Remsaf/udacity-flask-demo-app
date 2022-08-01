# from flask import Flask

# app = Flask(__name__)

# @app.route('/')
# def index():
#   return 'Hello world'



from flask import Flask
app = Flask(__name__)

@app.route('/')
def hello():
    return 'Hello World!'

# if __name__ == '__main__':
#     app.run(debug=True)

# initializing the app
# app = Flask(__name__) sets the name of your app to the name of your module ("app" if "app.py" is the name of your file).

# Using @app.route
# @app.route('/')
# def index():
#   ...
# In this case, @app.route is a Python decorator. Decorators take functions and returns another function, usually extending the input function with additional ("decorated") functionality. @app.route is a decorator that takes an input function index() as the callback that gets invoked when a request to route / comes in from a client.

# See: this primer on decorators from Real Python.



# Running the flask app: Terminal (option 1)
# Make sure you are in the directory that contains app.py
# We run a flask app defined at app.py by running this line of code on one line
# FLASK_APP=app.py FLASK_DEBUG=true flask run
# FLASK_APP must be set to the server file path with an equal sign in between. No spaces. FLASK_APP = app.py will not work.
# FLASK_DEBUG=true will enable debug mode which allows live reload
# flask run actually executes the flask server code in the app.py file
# Running the flask app: Python (option 2)
# Make sure you are in the directory that contains app.py
# Do not enter any of the flask code mentioned in option 1
# Simply include the following in your python file
# from flask import Flask

# # your program here
# # your program here


# #always include this at the bottom of your code
# if __name__ == '__main__':
#    app.run(host="0.0.0.0")
