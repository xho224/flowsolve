#Path generating library
import os
#Website framework library Flask import here
from flask import Flask, render_template, request, url_for, session, abort, redirect, flash

#Set up flask app instance
app = Flask(__name__)

#Python app root
app_root = os.path.dirname(os.path.abspath(__file__))


#Use root as route. When visit root, function homgepage is called
@app.route('/')
def homepage():
    #return a template
    return render_template("main.html")

#Set the secret key.  keep this really secret:
app.secret_key = '???'

#Test and run (always at the end)
if __name__ == "__main__":
    app.run(debug=True)