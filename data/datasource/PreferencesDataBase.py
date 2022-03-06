import configparser
import certifi
from pymongo import MongoClient

from domain.model.LightPreferences import LightPreferences

CREDENTIALS_FILE = "db_connection.ini"
CREDENTIALS_SECTION = 'CREDENTIALS'
USER = 'user'
PASSWORD = 'password'
DATA_BASE_SECTION = 'DATABASE'
NAME = 'name'
DATA_BASE_NAME = "self-fish-db"
PREFERENCE_COLLECTION = "preference"


class PreferencesDataBase:

    def __connect_to_database(self):
        config = configparser.ConfigParser()
        config.read(CREDENTIALS_FILE)
        db_user = config[CREDENTIALS_SECTION][USER]
        db_password = config[CREDENTIALS_SECTION][PASSWORD]
        db_name = config[DATA_BASE_SECTION][NAME]
        return "mongodb+srv://" + db_user + ":" + db_password + "@cluster0.ryrnh.mongodb.net/" + \
               db_name + "?retryWrites=true&w=majority"

    def __get_database(self):
        client = MongoClient(self.__connect_to_database(), tlsCAFile=certifi.where())
        return client[DATA_BASE_NAME]

    def find_by_device_id(self, device_id):
        data_base = self.__get_database()
        collection = data_base[PREFERENCE_COLLECTION]
        items = collection.find()
        for item in items:
            if device_id == item["deviceId"]:
                return item
        return None

    def update_by_device_id(self, new_preferences: LightPreferences, device_id):
        data_base = self.__get_database()
        collection = data_base[PREFERENCE_COLLECTION]
        query = {"deviceId": device_id}
        values = {"$set": {"lightsPreferences": {"mode": new_preferences.mode.name,
                                                 "range": {"starting": new_preferences.range.starting,
                                                           "finishing": new_preferences.range.finishing}}}}
        collection.update_one(query, values)
        return self.find_by_device_id(device_id)

