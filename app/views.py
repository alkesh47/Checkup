__author__ = 'Alkesh'
from app import app
from flask import render_template,request

@app.route('/')
def my_form():
    if request.method == "POST":
        return ("Submission Succesful! Here's your .ical file")
    return render_template("healthjss.html")

@app.route('/submit', methods = ["GET", "POST"])
def my_form_post():
    text = request.form['smoking2']
    return render_template("Submission Successful!")