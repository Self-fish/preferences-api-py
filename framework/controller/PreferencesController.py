from flask_restful import reqparse, Resource
from dependency_injector.wiring import inject, Provide
import json

from PreferencesApiContainer import PreferencesApiContainer
from domain.usecase.GetPreferencesUseCase import GetPreferencesUseCase


class PreferencesController(Resource):

    @inject
    def __init__(self, use_case: GetPreferencesUseCase = Provide[PreferencesApiContainer.use_case]):
        self.__use_case = use_case

    def get(self):
        parser = reqparse.RequestParser()
        parser.add_argument('deviceId', required=True)  # add args
        args = parser.parse_args()
        preference: dict = self.__use_case.get_preferences(args['deviceId'])
        preference.pop("_id", None)
        preference.pop("_class", None)
        return json.loads(json.dumps(preference))
