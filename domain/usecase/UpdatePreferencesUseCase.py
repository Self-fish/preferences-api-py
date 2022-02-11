from data.repository.PreferencesRepository import PreferencesRepository
from domain.model.LightPreferences import LightPreferences


class UpdatePreferencesUseCase:

    def __init__(self, repository):
        self.__repository: PreferencesRepository = repository

    def update_preference(self, light_preference, device_id):
        return self.__repository.update_preference(light_preference, device_id)
