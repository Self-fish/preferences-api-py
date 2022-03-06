from flask import request
from flask_restful import reqparse, Resource
from dependency_injector.wiring import inject, Provide
import json

from PreferencesApiContainer import PreferencesApiContainer
from domain.model.LightMode import LightMode
from domain.model.LightPreferences import LightPreferences
from domain.model.LightRange import LightRange
from domain.usecase.GetPreferencesUseCase import GetPreferencesUseCase
from domain.usecase.UpdatePreferencesUseCase import UpdatePreferencesUseCase


class PreferencesController(Resource):

    @inject
    def __init__(self, get_use_case: GetPreferencesUseCase = Provide[PreferencesApiContainer.get_use_case],
                 update_use_case: UpdatePreferencesUseCase = Provide[PreferencesApiContainer.update_use_case]):
        self.__get_use_case = get_use_case
        self.__update_use_case = update_use_case

    def get(self):
        parser = reqparse.RequestParser()
        parser.add_argument('deviceId', required=True)
        args = parser.parse_args()
        preference: dict = self.__get_use_case.get_preferences(args['deviceId'])
        preference.pop("_id", None)
        preference.pop("_class", None)
        return json.loads(json.dumps(preference))

    def put(self):
        body = request.json
        light_preference = LightPreferences(LightMode[body["lightsPreferences"]["mode"]],
                                            LightRange(body["lightsPreferences"]["range"]["starting"],
                                                       body["lightsPreferences"]["range"]["finishing"]))
        preference: dict = self.__update_use_case.update_preference(light_preference, body["deviceId"])
        preference.pop("_id", None)
        preference.pop("_class", None)
        return json.loads(json.dumps(preference))

