from flask import Flask,render_template,request,make_response
import json
import db 


page=Flask(__name__, template_folder="templates")

@page.route("/form" ,methods=["GET","POST"])
def form_data():
    if request.method=="GET":
        return render_template("fromtest.html")
    if request.method=="POST":
        text=request.form
        image=request.files["image"].read()
        db.insert_data("portfolio",text["title"],text["description"],image)
        return render_template("fromtest.html")

@page.route("/image/<int:id>")
def image(id):
        

@page.route("/profile")
def projects()    