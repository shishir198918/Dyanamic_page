from flask import Flask,render_template,request
import json

page=Flask(__name__, template_folder="templates") # (__name__) used for where to look for resources 
count=0

@page.route("/") 
def hello():
    global count
    count = count+1
    return "mango: " + str(count)


@page.route("/mul/<int:num1>/<int:num2>")
def multiply(num1,num2):
    #return f"multiple of {num1} and {num2} is {num1*num2}"
    return [num1,num2],201
@page.route("/url_para",methods=["POST","GET"])
def url_parameter():
    return (render_template("form.html")) #request is handle all data send by client 
                          # .args for argument 

@page.route("/url_p1/",methods=["GET","POST"])
def d1():
    if request.method=="GET":

        num1=request.args.get("marks",type=int)
        roll=request.args.get("rollno",type=str)
        return f"{num1},{roll}"
    elif request.method=="POST":
        data=request.get_json()
        #data={"cuisine":"INDIAN"}
        return f"cuisine {data['cuisine']}"    

@page.route("/show_data",methods=["GET"])
def show():
    if request.method=="GET":
        file=open("data/db.json","r")
        project_data=json.load(file)
        file.close()
        
        project=project_data[0]["title"]
        description=project_data[0]["description"]
        return render_template("index.html",Project=project,Description=description)

@page.route("/show1_data",methods=["GET"])
def show1():
    if request.method=="GET":
        file=open("data/db.json","r")
        project_data=json.load(file)
        file.close()
        return render_template("index.html",Project_data=project_data)

@page.route("/append" ,methods=["GET","POST"])
def append_data():
    if request.method=="GET":
        return render_template("fromtest.html")
    if request.method=="POST":
        input_data=request.form
        file=open("data/db.json","r+")
        db=file.read()
        file.seek(len(db)-1)
        file.write(','+json.dumps(input_data)+']')
        file.close()
        return input_data


