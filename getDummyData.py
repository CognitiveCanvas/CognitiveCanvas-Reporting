import json


class DummyData:
    def __init__(self):
        self.users_json = """[{
                                "email": "testuser1@ucsd.edu",
                                "FirstName": "Test",
                                "LastName": "User 1",
                                "Type": "student",
                                "isLogin": false,
                                "MapsCreated": [1, 2, 3],
                                "MapsAccessed": [1, 2, 3, 4, 5],
                                "MapsWithPermission": [1, 2, 3, 4, 5, 6, 7, 8]
                            }, {
                                "email": "testuser2@ucsd.edu",
                                "FirstName": "Test",
                                "LastName": "User 2",
                                "Type": "student",
                                "isLogin": false,
                                "MapsCreated": [4, 5],
                                "MapsAccessed": [3, 4, 5],
                                "MapsWithPermission": [1, 2, 3, 4, 5]
                            }, {
                                "email": "testuser3@ucsd.edu",
                                "FirstName": "Test",
                                "LastName": "User 3",
                                "Type": "student",
                                "isLogin": false,
                                "MapsCreated": [6, 7, 8],
                                "MapsAccessed": [6, 7, 8],
                                "MapsWithPermission": [6, 7, 8]
                            }, {
                                "email": "testuser4@ucsd.edu",
                                "FirstName": "Test",
                                "LastName": "User 4",
                                "Type": "admin",
                                "isLogin": true,
                                "MapsCreated": [],
                                "MapsAccessed": [1, 2, 3, 4, 5, 6, 7, 8],
                                "MapsWithPermission": [1, 2, 3, 4, 5, 6, 7, 8]
                            }]"""

        self.map_json = """[{
                            "MapWebstrateID": "1",
                            "Owner": "testuser1@ucsd.edu",
                            "Permission": ["testuser2@ucsd.edu", "testuser4@ucsd.edu"],
                            "Title": "Test Map 1",
                            "Created Date": 152547000,
                            "Modified": 1525474763,
                            "Screen Shot": "testmap1.png",
                            "Versions": ["have", "no", "idea", "what", "this", "is"]
                        }, {
                            "MapWebstrateID": "4",
                            "Owner": "testuser2@ucsd.edu",
                            "Permission": ["testuser1@ucsd.edu", "testuser4@ucsd.edu"],
                            "Title": "Test Map 4",
                            "Created Date": 152547000,
                            "Modified": 1525474763,
                            "Screen Shot": "testmap4.png",
                            "Versions": ["have", "no", "idea", "what", "this", "is"]
                        }]"""

        self.users = json.loads(self.users_json)
        self.maps = json.loads(self.map_json)

    def get_user_by_key_value(self, data_point, data_value, fields=None):
        data = [i for i in self.users if i[data_point] == data_value]
        if fields:
            return [{field:d[field] for field in fields} for d in data]
        return data

    def get_users(self):
        return self.users

    def get_map_by_key_value(self, data_point, data_value, fields=None):
        data = [i for i in self.maps if i[data_point] == data_value]
        if fields:
            return [{field:d[field] for field in fields} for d in data]
        return data

    def get_maps(self):
        return self.maps

    def add_user(self, user):
        self.users.append(user)
