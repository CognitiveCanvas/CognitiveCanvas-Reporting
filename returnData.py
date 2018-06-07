from collections import defaultdict
from flask import Flask, render_template, request, jsonify, g, redirect, url_for, make_response
from time import gmtime, strftime

from selenium.common.exceptions import WebDriverException

from getDataFromMongo import DbData
from getDataFromSite import ScrapeMap
from getDummyData import DummyData
from getDataFromSite import ScrapeMap
from datetime import datetime, timedelta
from json import loads

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
    list_of_users = mongo.get_user_by_key_values("email", user_email.strip(";").split(";"))
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


@app.route("/users/<string:user_email>/nodes")
def get_nodes_by_user_id(user_email):
    list_of_maps = mongo.get_user_by_key_value("email", user_email, fields=["MapsCreated"])
    nodes_by_map = {}
    sum_of_nodes = 0
    for map in list_of_maps[0]["MapsCreated"]:
        # scraper = ScrapeMap("https://web:strate@webstrates.ucsd.edu/datateam/")
        nodes = mongo.get_nodes()  # scraper.get_nodes()
        nodes_by_map[map] = nodes
        sum_of_nodes += len(nodes)
    return return_json_data("success", "nodes", {"nodes": nodes_by_map, "total": sum_of_nodes})


@app.route("/users/<string:user_email>/nodes/frequency")
def get_node_frequency_by_user_id(user_email):
    list_of_maps = mongo.get_user_by_key_value("email", user_email, fields=["MapsCreated"])
    nodes_labels_by_map = defaultdict(int)
    for map in list_of_maps[0]["MapsCreated"]:
        # scraper = ScrapeMap("https://web:strate@webstrates.ucsd.edu/datateam/")
        nodes = mongo.get_nodes()  # scraper.get_nodes()
        for node in nodes:
            nodes_labels_by_map[node["label"]] += 1
    return return_json_data("success", "frequency", convert_frequency_to_list(nodes_labels_by_map))


@app.route("/nodes/frequency")
def get_node_frequency_for_all_users():
    list_of_users = mongo.get_users()
    nodes_labels_by_map = defaultdict(int)
    for user in list_of_users:
        for map in user["MapsCreated"]:
            # scraper = ScrapeMap("https://web:strate@webstrates.ucsd.edu/datateam/")
            nodes = mongo.get_nodes()  # scraper.get_nodes()
            for node in nodes:
                nodes_labels_by_map[node["label"]] += 1
    return return_json_data("success", "frequency", convert_frequency_to_list(nodes_labels_by_map))


@app.route("/users/<string:user_email>/edges/frequency")
def get_edge_frequency_by_user_id(user_email):
    list_of_maps = mongo.get_user_by_key_value("email", user_email, fields=["MapsCreated"])
    edges_labels_by_map = defaultdict(int)
    for map in list_of_maps[0]["MapsCreated"]:
        # scraper = ScrapeMap("https://web:strate@webstrates.ucsd.edu/datateam/")
        edges = mongo.get_edges()  # scraper.get_nodes()
        for edge in edges:
            edges_labels_by_map[edge["label"]] += 1
    return return_json_data("success", "frequency", convert_frequency_to_list(edges_labels_by_map))


@app.route("/edges/frequency")
def get_edge_frequency_for_all_users():
    list_of_users = mongo.get_users()
    edges_labels_by_map = defaultdict(int)
    for user in list_of_users:
        for map in user["MapsCreated"]:
            # scraper = ScrapeMap("https://web:strate@webstrates.ucsd.edu/datateam/")
            edges = mongo.get_edges()  # scraper.get_nodes()
            for edge in edges:
                edges_labels_by_map[edge["label"]] += 1
    return return_json_data("success", "frequency", convert_frequency_to_list(edges_labels_by_map))


@app.route("/users/<string:owner_email>/maps")
def get_map_data_by_owner_email(owner_email):
    list_of_maps = mongo.get_map_by_key_value("Owner", owner_email)
    title_filter = request.args.get("title") or request.form.get("title")
    id_filter = request.args.get("id") or request.form.get("id")
    list_of_maps = filter_map_by_date_range(list_of_maps)

    if not (title_filter or id_filter):
        return return_json_data("success", "maps", list_of_maps)
    if title_filter and not id_filter:
        return return_json_data("success", "maps", [i for i in list_of_maps if i['Title'] == title_filter])
    id_filter = int(id_filter)
    if id_filter and not title_filter:
        return return_json_data("success", "maps", [i for i in list_of_maps if i['MapWebstrateID'] == id_filter])
    return return_json_data("success", "maps", [i for i in list_of_maps if i['MapWebstrateID'] == id_filter and
                                                i['Title'] == title_filter])


@app.route("/users/<string:owner_email>/maps/timeline")
def get_map_timeline_by_owner_email(owner_email):
    list_of_maps = mongo.get_map_by_key_value("Owner", owner_email)
    type_filter = request.args.get("filter") or request.form.get("filter")
    filtered_list = defaultdict(int)

    if type_filter == "days":
        for i in list_of_maps:
            creation_date = datetime.fromtimestamp(i["Created Date"])
            print(creation_date.strftime("%Y-%m-%d"))
            today = datetime.today()
            ten_days_ago = today - timedelta(days=70)

            for day in (ten_days_ago + timedelta(n) for n in range(71)):
                if creation_date.date() == day.date():
                    filtered_list[day.strftime("%Y-%m-%d")] += 1

    return return_json_data("success", "maps", dict(filtered_list))


@app.route("/maps")
def get_map_data():
    list_of_maps = mongo.get_maps()
    list_of_maps = filter_map_by_date_range(list_of_maps)
    return return_json_data("success", "maps", list_of_maps)


@app.route("/maps/<string:map_id>")
def get_map_data_by_map_id(map_id):
    list_of_maps = mongo.get_map_by_key_value("MapWebstrateID", map_id)
    return return_json_data("success", "maps", list_of_maps)


@app.route("/maps/<string:map_id>/nodes")
def get_nodes_by_map_id(map_id):
    # scraper = ScrapeMap("https://web:strate@webstrates.ucsd.edu/datateam/")
    node_filter = request.args.get("filter") or request.form.get("filter")
    nodes = mongo.get_nodes()  # scraper.get_nodes()
    if node_filter:
        nodes = {i.get("id"): i.get(node_filter) for i in nodes}
    return return_json_data("success", "nodes", nodes)


@app.route("/maps/<string:map_id>/edges")
def get_edges_by_map_id(map_id):
    # try:
    #     scraper = ScrapeMap("https://web:strate@webstrates.ucsd.edu/datateam/")
    #     edges = scraper.get_edges()
    # except WebDriverException:
    edges = mongo.get_edges()
    edge_filter = request.args.get("filter") or request.form.get("filter")
    if edge_filter:
        edges = {i.get("id"): i.get(edge_filter) for i in edges}
    return return_json_data("success", "edges", edges)


def filter_map_by_date_range(list_of_maps):
    from_date = request.args.get("fromdate") or request.form.get("fromdate")
    to_date = request.args.get("todate") or request.form.get("todate") or datetime.today().timestamp()
    if from_date:
        list_of_maps = [i for i in list_of_maps if int(from_date) <= int(i["Created Date"]) <= int(to_date)]
    return list_of_maps


def return_json_data(status, dtype, payload):
    response = jsonify({"status": status, dtype: payload})
    response.headers.add('Access-Control-Allow-Origin', '*')
    return response


def convert_frequency_to_list(freq_dic):
    return [{"label": i, "frequency": j} for i, j in freq_dic.items()]
