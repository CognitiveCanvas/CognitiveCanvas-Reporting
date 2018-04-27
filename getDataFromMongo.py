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

    def get_user_by_key_value(self, data_point, data_value):
        """
        Returns the records in the user table which match the given key value pair

        :param data_point: String
                           The data key which is to be looked up
        :param data_value: The corresponding value.
        :return: The records that correspond to the key value pair.
        """
        users = self.mongo.db.users.find({data_point: data_value})
        outdata = [i for i in users]
        for i in outdata:
            i.pop("_id")
        return outdata

    def add_user(self, user):
        self.mongo.db.users.insert(user)
