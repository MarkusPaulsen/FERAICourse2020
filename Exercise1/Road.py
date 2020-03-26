class Road:
    def __init__(self, to: str, cost: int):
        self._to: str = to
        self._cost: int = cost

    def set_to(self, to: str):
        self._to = to

    def get_to(self) -> str:
        return self._to

    def set_cost(self, cost: int):
        self._cost = cost

    def get_cost(self) -> int:
        return self._cost
