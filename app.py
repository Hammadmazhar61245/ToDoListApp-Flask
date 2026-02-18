from flask import Flask , render_template, request 

app = Flask(__name__)

todolist=[] 

@app.route("/" , methods=["POST" , "GET"])



def home():
    tododict = {} 
    if request.method=="POST":
        tasktitle = request.form["task"] 
        taskdescription = request.form["description"]
        tasktime = request.form["tasktime"]
        taskstatus = request.form["status"]
        

        tododict = {
            "TaskTitle": tasktitle,
            "TaskDescription": taskdescription, 
            "TaskTime":tasktime, 
            "TaskStatus": taskstatus
        }   

        todolist.append(tododict)
        

    return render_template("home.html", todolist=todolist)

if __name__ == "__main__": 
    app.run(debug =True ) 






