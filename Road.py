
class Road:
    def __init__(self, nameCity, cost):
        self._nameMain: str = nameCity
        self._cost: int = cost


    def set_nameMain(self, x):
        self._nameMain: str = x

    def get_nameMain(self):
        return self._nameMain

    def set_cost(self, x):
        self._cost: str = x

    def get_cost(self):
        return self._cost