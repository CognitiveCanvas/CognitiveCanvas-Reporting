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

        self.nodes_json = """[
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
                        ]"""

        self.edges_json = """[
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
                          ]"""

        self.users = json.loads(self.users_json)
        self.maps = json.loads(self.map_json)
        self.nodes = json.loads(self.nodes_json)
        self.edges = json.loads(self.edges_json)

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

    def get_nodes(self):
        return self.nodes

    def get_edges(self):
        return self.edges

    def add_user(self, user):
        self.users.append(user)
