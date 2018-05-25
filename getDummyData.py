import json


class DummyData:
    def __init__(self):
        self.users_json = """[{
                                "email": "testuser1@ucsd.edu",
                                "FirstName": "Test",
                                "LastName": "User 1",
                                "Type": "student",
                                "isLogin": false,
                                "MapsCreated": ["datateam1", "datateam2", "datateam3"],
                                "MapsAccessed": ["datateam1", "datateam2", "datateam3", "datateam4", "datateam5"],
                                "MapsWithPermission": ["datateam1", "datateam2", "datateam3", "datateam4", "datateam5", "datateam6", "datateam7", "datateam8"]
                            }, {
                                "email": "testuser2@ucsd.edu",
                                "FirstName": "Test",
                                "LastName": "User 2",
                                "Type": "student",
                                "isLogin": false,
                                "MapsCreated": ["datateam4", "datateam5"],
                                "MapsAccessed": ["datateam3", "datateam4", "datateam5"],
                                "MapsWithPermission": ["datateam1", "datateam2", "datateam3", "datateam4", "datateam5"]
                            }, {
                                "email": "testuser3@ucsd.edu",
                                "FirstName": "Test",
                                "LastName": "User 3",
                                "Type": "student",
                                "isLogin": false,
                                "MapsCreated": ["datateam6", "datateam7", "datateam8"],
                                "MapsAccessed": ["datateam6", "datateam7", "datateam8"],
                                "MapsWithPermission": ["datateam6", "datateam7", "datateam8"]
                            }, {
                                "email": "testuser4@ucsd.edu",
                                "FirstName": "Test",
                                "LastName": "User 4",
                                "Type": "admin",
                                "isLogin": true,
                                "MapsCreated": [],
                                "MapsAccessed": ["datateam1", "datateam2", "datateam3", "datateam4", "datateam5", "datateam6", "datateam7", "datateam8"],
                                "MapsWithPermission": ["datateam1", "datateam2", "datateam3", "datateam4", "datateam5", "datateam6", "datateam7", "datateam8"]
                            }]"""

        self.map_json = """[{
                            "MapWebstrateID": "datateam1",
                            "Owner": "testuser1@ucsd.edu",
                            "Permission": ["testuser2@ucsd.edu", "testuser4@ucsd.edu"],
                            "Title": "Test Map 1",
                            "Created Date": 1527221822,
                            "Modified": 1527222822,
                            "Screen Shot": "testmap1.png",
                            "Versions": ["have", "no", "idea", "what", "this", "is"]
                        }, {
                            "MapWebstrateID": "datateam2",
                            "Owner": "testuser1@ucsd.edu",
                            "Permission": ["testuser2@ucsd.edu", "testuser4@ucsd.edu"],
                            "Title": "Test Map 2",
                            "Created Date": 1527223822,
                            "Modified": 1527224822,
                            "Screen Shot": "testmap1.png",
                            "Versions": ["have", "no", "idea", "what", "this", "is"]
                        }, {
                            "MapWebstrateID": "datateam3",
                            "Owner": "testuser2@ucsd.edu",
                            "Permission": ["testuser1@ucsd.edu", "testuser4@ucsd.edu"],
                            "Title": "Test Map 4",
                            "Created Date": 1527226822,
                            "Modified": 1527228822,
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
