#!/usr/bin/python3


from flask import Flask, render_template

app = Flask(__name__)

@app.route("/")

def home():
    return "Welcome to Antonio's Pizza Pub Inventory System."

@app.route("/add", methods=["POST"])
def add():
    return "This is how you will add your items"



