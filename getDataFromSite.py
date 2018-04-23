import requests
import json

json_url = "http://dpaste.com/1HFV0Q7.txt"


def get_action_data(userid=None, action_filter=None):
    in_data = json.loads(requests.get(json_url).text)
    if action_filter:
        in_data = [i for i in in_data if i["action"] == action_filter]
    if userid:
        return [i for i in in_data if i["userid"] == userid]
    return in_data

