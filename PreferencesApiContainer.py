from dependency_injector import containers, providers

from data.datasource.PreferencesDataBase import PreferencesDataBase
from data.repository.PreferencesRepository import PreferencesRepository
from domain.usecase.GetPreferencesUseCase import GetPreferencesUseCase
from domain.usecase.UpdatePreferencesUseCase import UpdatePreferencesUseCase


class PreferencesApiContainer(containers.DeclarativeContainer):
    config = providers.Configuration()
    data_base = providers.Factory(PreferencesDataBase)
    repository = providers.Factory(PreferencesRepository, data_base)
    get_use_case = providers.Factory(GetPreferencesUseCase, repository)
    update_use_case = providers.Factory(UpdatePreferencesUseCase, repository)
