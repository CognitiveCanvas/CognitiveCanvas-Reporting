from flask import Flask, render_template, request, jsonify, g, redirect, url_for
from time import gmtime, strftime
from getDataFromMongo import DbData
from getDataFromSite import *


app = Flask(__name__)
mongo = DbData(app)

@app.errorhandler(404)
def page_not_found(error):
    print(error)
    return jsonify({"status": "failure", "message": "route does not exist"}), 404


@app.route("/")
def display_posts():
    return jsonify({"status": "success", "message": "system running since "+strftime("%Y-%m-%d %H:%M:%S", gmtime())})


@app.route("/user/<int:user_id>")
def get_user_data_by_user_id(user_id):
    list_of_users = mongo.get_user_by_key_value("id", user_id)
    return jsonify({"status": "success", "users": list_of_users})


@app.route("/user/<int:user_id>/actions")
def get_user_action_data_by_user_id(user_id):
    action_filter = request.args.get("filter", None) or request.form.get("filter",None)
    list_of_users = get_action_data(user_id, action_filter)
    return jsonify({"status": "success", "users": list_of_users})


@app.route("/users/create")
def create_user():
    mongo.add_user({"name": request.args['name'], "id": request.args["id"]})
    return jsonify({"status": "success", "message" : "user added successfully"})


