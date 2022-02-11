from domain.model.LightMode import LightMode
from domain.model.LightRange import LightRange


class LightPreferences:

    def __init__(self, mode: LightMode, range: LightRange):
        self.mode = mode
        self.range = range
