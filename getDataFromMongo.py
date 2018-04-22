from flask_pymongo import PyMongo


class DbData:
    def __init__(self, app):
        app.config['MONGO_DBNAME'] = 'testdb'
        self.mongo = PyMongo(app)

    def get_user_by_id(self, data_point, data_value):
        users = self.mongo.db.users.find({data_point: data_value})
        outdata = [i for i in users]
        for i in outdata:
            i.pop("_id")
        return outdata

    def add_user(self, user):
        self.mongo.db.users.insert(user)