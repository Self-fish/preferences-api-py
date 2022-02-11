from data.datasource.PreferencesDataBase import PreferencesDataBase
from domain.model.LightPreferences import LightPreferences


class PreferencesRepository:

    def __init__(self, data_base: PreferencesDataBase):
        self.__data_base = data_base

    def get_preferences(self, device_id):
        return self.__data_base.find_by_device_id(device_id)

    def update_preference(self, light_preferences: LightPreferences, device_id):
        return self.__data_base.update_by_device_id(light_preferences, device_id)
