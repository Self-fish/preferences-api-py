import configparser
import certifi
from pymongo import MongoClient


class PreferencesDataBase:

    def __connect_to_database(self):
        config = configparser.ConfigParser()
        config.read("db_connection.ini")
        db_user = config['CREDENTIALS']['user']
        db_password = config['CREDENTIALS']['password']
        db_name = config['DATABASE']['name']
        return "mongodb+srv://" + db_user + ":" + db_password + "@cluster0.ryrnh.mongodb.net/" + \
               db_name + "?retryWrites=true&w=majority"

    def __get_database(self):
        client = MongoClient(self.__connect_to_database(), tlsCAFile=certifi.where())
        db = client.test
        print(db)
        return client["self-fish-db"]

    def find_by_device_id(self, device_id):
        data_base = self.__get_database()
        collection = data_base["preference"]
        items = collection.find()
        for item in items:
            if device_id == item["deviceId"]:
                return item
        return None

