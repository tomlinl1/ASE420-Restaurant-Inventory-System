#!/usr/bin/python3


from flask import Flask, render_template # type: ignore

app = Flask(__name__)

@app.route("/")

def home():
    return render_template("index.html")

@app.route("/view")

def viewStock():
    return render_template("view-stock.html")

@app.route("/create")

def createStock():
    return render_template("create-stock.html")

@app.route("/add", methods=["POST"])
def add():
    return "This is how you will add your items"

@app.route("/delete", methods={"POST"})
def delete():
    return "This is where stuff will be deleted"

@app.route("/update", methods=["POST"])
def update():
    return "This is where things are updated"




