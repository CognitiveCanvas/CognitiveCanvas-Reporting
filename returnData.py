from flask import Flask, render_template, request, jsonify, g, redirect, url_for
from time import gmtime, strftime
from getDataFromMongo import DbData
from getDummyData import DummyData
from getDataFromSite import *

app = Flask(__name__)
mongo = DummyData()
# mongo = DbData(app)


@app.errorhandler(404)
def page_not_found(error):
    print(error)
    return jsonify({"status": "failure", "message": "route does not exist"}), 404


@app.route("/")
def display_posts():
    return jsonify({"status": "success", "message": "system running since " + strftime("%Y-%m-%d %H:%M:%S", gmtime())})


@app.route("/users")
def get_user_data():
    list_of_users = mongo.get_users()
    return jsonify({"status": "success", "users": list_of_users})


@app.route("/users/<string:user_email>")
def get_user_data_by_user_email(user_email):
    list_of_users = mongo.get_user_by_key_value("email", user_email)
    return jsonify({"status": "success", "users": list_of_users})


@app.route("/users/type/<string:user_type>")
def get_user_data_by_user_type(user_type):
    list_of_users = mongo.get_user_by_key_value("Type", user_type)
    return jsonify({"status": "success", "users": list_of_users})


@app.route("/users/online")
def get_user_data_if_logged_in():
    list_of_users = mongo.get_user_by_key_value("isLogin", True)
    return jsonify({"status": "success", "users": list_of_users})


@app.route("/users/<string:user_email>/maps/created")
def get_maps_created_by_user_email(user_email):
    list_of_users = mongo.get_user_by_key_value("email", user_email, fields=["MapsCreated"])
    if len(list_of_users) == 0:
        return jsonify({"status": "success", "maps": []})
    list_of_maps = list_of_users[0]["MapsCreated"]
    return jsonify({"status": "success", "maps": list_of_maps})


@app.route("/users/<string:user_email>/maps/accessed")
def get_maps_accessed_by_user_email(user_email):
    list_of_users = mongo.get_user_by_key_value("email", user_email, fields=["MapsAccessed"])
    if len(list_of_users) == 0:
        return jsonify({"status": "success", "maps": []})
    list_of_maps = list_of_users[0]["MapsAccessed"]
    return jsonify({"status": "success", "maps": list_of_maps})


@app.route("/users/create")
def create_user():
    mongo.add_user({"name": request.args['name'], "id": request.args["id"]})
    return jsonify({"status": "success", "message": "user added successfully"})
