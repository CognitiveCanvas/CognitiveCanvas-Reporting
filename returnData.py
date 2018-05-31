from collections import defaultdict
from flask import Flask, render_template, request, jsonify, g, redirect, url_for, make_response
from time import gmtime, strftime
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


@app.route("/users/<string:owner_email>/maps")
def get_map_data_by_owner_email(owner_email):
    list_of_maps = mongo.get_map_by_key_value("Owner", owner_email)
    title_filter = request.args.get("title") or request.form.get("title")
    id_filter = request.args.get("id") or request.form.get("id")
    from_date = request.args.get("fromdate") or request.form.get("fromdate")
    to_date = request.args.get("todate") or request.form.get("todate") or datetime.today().timestamp()

    if from_date:
        list_of_maps = [i for i in list_of_maps if from_date <= i["Created Date"] <= to_date]

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


@app.route("/maps/<string:map_id>")
def get_map_data_by_map_id(map_id):
    list_of_maps = mongo.get_map_by_key_value("MapWebstrateID", map_id)
    return return_json_data("success", "maps", list_of_maps)


@app.route("/maps/<string:map_id>/nodes")
def get_nodes_by_map_id(map_id):
    # scraper = ScrapeMap("https://web:strate@webstrates.ucsd.edu/datateam/")
    # node_filter = request.args.get("filter") or request.form.get("filter")
    # nodes = scraper.get_nodes()
    # if node_filter:
    #     nodes = {i.get("id"): i.get(node_filter) for i in nodes}
    return return_json_data("success", "nodes", loads('''[
        {
            "color": "blue",
            "creation_time": 1527188610,
            "id": "H1yuhFEyQ_1527188610581",
            "label": null,
            "locationX": "2214.17",
            "locationY": "1275.52",
            "shape": "circle",
            "size": "66.375"
        },
        {
            "color": "red",
            "creation_time": 1527188641,
            "id": "By8FhYNJm_1527188641813",
            "label": "Node Name",
            "locationX": "2486",
            "locationY": "1144",
            "shape": "circle",
            "size": "48.89"
        },
        {
            "color": "black",
            "creation_time": 1527188652,
            "id": "By8FhYNJm_1527188652520",
            "label": "OKOK",
            "locationX": "2370.85",
            "locationY": "1432.51",
            "shape": "circle",
            "size": "65.065"
        }
    ]'''))


@app.route("/maps/<string:map_id>/edges")
def get_edges_by_map_id(map_id):
    # scraper = ScrapeMap("https://web:strate@webstrates.ucsd.edu/datateam/")
    # edge_filter = request.args.get("filter") or request.form.get("filter")
    # edges = scraper.get_edges()
    # if edge_filter:
    #     edges = {i.get("id"): i.get(edge_filter) for i in edges}
    return return_json_data("success", "edges", loads(    '''[
    {
      "creation_time": 1527188849, 
      "id": "By8FhYNJm_1527188849601", 
      "label": "Name me please", 
      "locationX1": "2370.85", 
      "locationX2": "2486", 
      "locationY1": "1432.51", 
      "locationY2": "1144", 
      "source_id": "By8FhYNJm_1527188652520", 
      "target_id": "By8FhYNJm_1527188641813"
    }
  ]'''))



def return_json_data(status, dtype, payload):
    response = jsonify({"status": status, dtype: payload})
    response.headers.add('Access-Control-Allow-Origin', '*')
    return response
