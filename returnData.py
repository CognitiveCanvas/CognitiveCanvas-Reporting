from flask import Flask, render_template, request, jsonify, g, redirect, url_for, make_response
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
    return return_json_data("failure", "message", "route does not exist"), 404


@app.route("/")
def display_posts():
    return return_json_data("success", "message", "system running since " + strftime("%Y-%m-%d %H:%M:%S", gmtime()))


@app.route("/users")
def get_user_data():
    list_of_users = mongo.get_users()
    return return_json_data("success", "users", list_of_users)


@app.route("/users/<string:user_email>")
def get_user_data_by_user_email(user_email):
    list_of_users = mongo.get_user_by_key_value("email", user_email)
    return return_json_data("success", "users", list_of_users)


@app.route("/users/type/<string:user_type>")
def get_user_data_by_user_type(user_type):
    list_of_users = mongo.get_user_by_key_value("Type", user_type)
    return return_json_data("success", "users", list_of_users)


@app.route("/users/online")
def get_user_data_if_logged_in():
    list_of_users = mongo.get_user_by_key_value("isLogin", True)
    return return_json_data("success", "users", list_of_users)


@app.route("/users/<string:user_email>/maps/created")
def get_maps_created_by_user_email(user_email):
    list_of_users = mongo.get_user_by_key_value("email", user_email, fields=["MapsCreated"])
    if len(list_of_users) == 0:
        return return_json_data("success", "maps", [])
    list_of_maps = list_of_users[0]["MapsCreated"]
    return return_json_data("success", "maps", list_of_maps)


@app.route("/users/<string:user_email>/maps/accessed")
def get_maps_accessed_by_user_email(user_email):
    list_of_users = mongo.get_user_by_key_value("email", user_email, fields=["MapsAccessed"])
    if len(list_of_users) == 0:
        return return_json_data({"status", "maps", []})
    list_of_maps = list_of_users[0]["MapsAccessed"]
    return return_json_data("success", "maps", list_of_maps)


@app.route("/maps")
def get_map_data():
    list_of_maps = mongo.get_maps()
    return return_json_data("success", "maps", list_of_maps)


@app.route("/maps/<string:owner_email>")
def get_map_data_by_owner_email(owner_email):
    list_of_maps = mongo.get_map_by_key_value("Owner", owner_email)
    title_filter = request.args.get("title") or request.form.get("title")
    if not title_filter:
        return return_json_data("success", "maps", list_of_maps)
    return return_json_data("success", "maps", [i for i in list_of_maps if i['Title'] == title_filter])


@app.route("/maps/<int:map_id>")
def get_map_data_by_map_id(map_id):
    list_of_maps = mongo.get_map_by_key_value("MapWebstrateID", map_id)
    return return_json_data("success", "maps", list_of_maps)


@app.route("/users/create")
def create_user():
    mongo.add_user({"name": request.args['name'], "id": request.args["id"]})
    return return_json_data("success", "message", "user added successfully")


def return_json_data(status, dtype, payload):
    response = jsonify({"status": status, dtype: payload})
    response.headers.add('Access-Control-Allow-Origin', '*')
    return response
