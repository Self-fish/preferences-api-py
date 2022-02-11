from data.datasource.PreferencesDataBase import PreferencesDataBase


class PreferencesRepository:

    def __init__(self, data_base: PreferencesDataBase):
        self.__data_base = data_base

    def get_preferences(self, device_id):
        return self.__data_base.find_by_device_id(device_id)