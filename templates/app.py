from flask import Flask , render_template , request 

app = Flask(__name__)


todolist = [] 




@app.route("/" , method=["GET" , "POST"]) 

def home():

    if request.method=="POST":
        task= request.form["task"]

        # now we will make a dictionary 
        # storing the data in the dictionary 
        tododict = {
             "tasktitle": "task",
             "Status": False
        } 

        todolist.append(tododict);  

        return render_template("home.html", todolist=todolist)
    
app.run(debug = True) 










    




    
