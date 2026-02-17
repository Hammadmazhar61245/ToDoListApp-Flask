from flask import Flask , render_template

app = Flask(__name__)

@app.route("/")
def home():
    return render_template("home.html")

@app.route("/display")
def display():
    return render_template("display.html") 


    
