from flask import Flask, render_template, request, jsonify, g, redirect, url_for
from time import gmtime, strftime

app = Flask(__name__)


@app.errorhandler(404)
def page_not_found(error):
    print(error)
    return jsonify({"status": "failure", "message": "route does not exist"}), 404


@app.route("/")
def display_posts():
    return jsonify({"status": "success", "message": "system running since "+strftime("%Y-%m-%d %H:%M:%S", gmtime())})


@app.route("/user/<int:user_id>")
def get_user_data(user_id):
    return