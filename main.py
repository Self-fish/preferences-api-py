import sys
import logging
from flask import Flask
from flask_restful import Api

from PreferencesApiContainer import PreferencesApiContainer
from framework.controller.PreferencesController import PreferencesController

app = Flask(__name__)
api = Api(app)

api.add_resource(PreferencesController, '/preferences')  # add endpoints

if __name__ == '__main__':
    preferences_container = PreferencesApiContainer()
    preferences_container.wire(modules=[sys.modules[__name__]])
    app.run(host='0.0.0.0', port=8081)
    log = logging.getLogger('werkzeug')
    log.disabled = True

