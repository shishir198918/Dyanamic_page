from flask import Flask,render_template,request,make_response
import json
import db 


page=Flask(__name__, template_folder="templates")

def Isempty(text):
    if text.strip()=="":
        return True
    return False


@page.route("/input/form" ,methods=["GET","POST"])
def form_data():
    if request.method=="GET":
        return render_template("fromtest.html")
    if request.method=="POST":
        text=request.form
        image=request.files["image"].read()
        if Isempty(text["title"] and text["description"]):
            print("khali sa khali hai")
        #db.insert_data("portfolio",text["title"],text["description"],image)
        print(text)
        return render_template("fromtest.html")

@page.route("/image/<int:id>")
def image(id):
    response=make_response()
    response.set_data(db.image_data('portfolio',id).tobytes())
    return response

@page.route("/")
@page.route("/profile")
def projects():
    project_data=db.json_data('portfolio')
    return render_template("index.html",Project_data=project_data) 

@page.route("/project",methods=["GET","PUT"])
def update():
    if request.method=="GET":
        project_data=db.json_data('portfolio')
        return render_template("selection.html",project_data=project_data)
    if request.method=="POST":
        update_data=request.form
        return update_data


 