from flask_pymongo import PyMongo


class DbData:
    """
    This class provides an object which can be used to connect to the System Database.


    The object of this class provides an interface to the Backend MongoDB Database.
    It is used to retrieve the data from the DB by the FLASK RESTAPI layer to
    provide an interface for the reports frontend.

    Takes the main Flask app as a parameter.

    """

    def __init__(self, app):
        """
        The initialization method for the DbData object. Remember to use the correct DB NAME.

        :param app: The Flask Object
        """
        app.config['MONGO_DBNAME'] = 'testdb'
        self.mongo = PyMongo(app)

    def get_user_by_key_value(self, data_point, data_value, fields=None):
        """
        Returns the records in the user table which match the given key value pair

        :param data_point: String
                           The data key which is to be looked up
        :param data_value: The corresponding value.
        :param fields: (Optional) The fields which need to be returned.
        :return: The records that correspond to the key value pair.
        """
        if fields:
            return self.__cleanse_data(self.mongo.db.users.find({data_point: data_value}, {i: 1 for i in fields}))
        return self.__cleanse_data(self.mongo.db.users.find({data_point: data_value}))

    def get_user_by_key_values(self, data_point, data_values, fields=None):
        find_data = {data_point: {"$in": data_values}}
        if fields:
            return self.__cleanse_data(self.mongo.db.users.find(find_data, {i: 1 for i in fields}))
        return self.__cleanse_data(self.mongo.db.users.find(find_data))

    def get_users(self):
        """

        TODO

        :return:
        """
        return self.__cleanse_data(self.mongo.db.users.find())

    def get_map_by_key_value(self, data_point, data_value, fields=None):
        """
        Returns the records in the user table which match the given key value pair

        :param data_point: String
                           The data key which is to be looked up
        :param data_value: The corresponding value.
        :param fields: (Optional) The fields which need to be returned.
        :return: The records that correspond to the key value pair.
        """
        if fields:
            return self.__cleanse_data(self.mongo.db.map.find({data_point: data_value}, {i: 1 for i in fields}))
        return self.__cleanse_data(self.mongo.db.map.find({data_point: data_value}))

    def get_map_by_key_values(self, data_point, data_values, fields=None):
        find_data = {data_point: {"$in": data_values}}
        if fields:
            return self.__cleanse_data(self.mongo.db.map.find(find_data, {i: 1 for i in fields}))
        return self.__cleanse_data(self.mongo.db.map.find(find_data))

    def get_maps(self):
        return self.__cleanse_data(self.mongo.db.map.find())

    def add_user(self, user):
        self.mongo.db.users.insert(user)

    @staticmethod
    def __cleanse_data(data):
        outdata = [i for i in data]
        for i in outdata:
            i.pop("_id")
        return outdata
