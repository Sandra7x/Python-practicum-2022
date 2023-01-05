from flask import Blueprint, redirect, url_for, render_template


views = Blueprint(__name__, "views")

@views.route("/")
def index():
    return redirect(url_for("welcome"))

@views.route("welcome")
def welcome():
    return render_template("index.html")

@views.route("welcome/home")
def welcome_home():
    return render_template("welcome_home.html")

@views.route("welcome/back")
def welcome_back():
    return render_template("welcome_back.html")