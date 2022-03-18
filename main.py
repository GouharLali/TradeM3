from flask import Blueprint, render_template, Flask, url_for, redirect
from flask_login import login_required, current_user
#from . import db
from flask import Flask, render_template, request
#import trademebot 
from TradeM3.trademebot import intents, predict_class, get_response
#from TradeM3 import trademebot
#tb = os.system("trademebot.py")
#print(intents)

main = Blueprint("main", __name__)

@main.route("/")
def index():
    return render_template("index.html")

@main.route("/profile")
@login_required
def profile():
    return render_template("profile.html", username = current_user.name)

@main.route("/trades_physical")
def trades_physical():
    return render_template("trades_physical.html")

@main.route("/trades_digital")
def trades_digital():
    return render_template("trades_digital.html")

@main.route("/trades_active")
def trades_active():
    return render_template("trades_active.html")

@main.route("/trades_old")
def trades_old():
    return render_template("trades_old.html")

@main.route("/HTMLTEST")
def HTMLTEST():
    return render_template("HTMLTEST.html")

@main.route("/game_data11")
def game_data11():
    return render_template("game_data11.html")

@main.route("/about")
def about():
    return render_template("about.html")

# @main.route("/chatbot")
# def chatbot():
#     return render_template("chatbot.html")


# @main.errorhandler(404)
# def page_not_found(error):
#     return render_template("page_not_found.html"), 404

# @main.errorhandler(500)
# def internal_server_error(error):
#     return render_template("internal_server_error.html"), 500

answer_list = []

@main.route("/chatbot", methods=["POST", "GET"])
def chatbot():
    global answer_list
    if request.method == "POST":
        message =  request.form["message"]
        ints = predict_class(message)
        response = get_response(ints, intents)
        answer_list.append(response)
        print(answer_list)
        if len(answer_list) > 5:
            answer_list.remove(answer_list[0])
        return render_template("chatbot.html", message=message, answer_list=answer_list)
    return render_template("chatbot.html", message="", answer_list=answer_list)
