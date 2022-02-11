from dependency_injector import containers, providers

from data.datasource.PreferencesDataBase import PreferencesDataBase
from data.repository.PreferencesRepository import PreferencesRepository
from domain.usecase.GetPreferencesUseCase import GetPreferencesUseCase


class PreferencesApiContainer(containers.DeclarativeContainer):
    config = providers.Configuration()
    data_base = providers.Factory(PreferencesDataBase)
    repository = providers.Factory(PreferencesRepository, data_base)
    use_case = providers.Factory(GetPreferencesUseCase, repository)