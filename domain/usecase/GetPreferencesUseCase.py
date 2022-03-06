from data.repository.PreferencesRepository import PreferencesRepository


class GetPreferencesUseCase:

    def __init__(self, repository: PreferencesRepository):
        self.__repository = repository

    def get_preferences(self, device_id):
        return self.__repository.get_preferences(device_id)
