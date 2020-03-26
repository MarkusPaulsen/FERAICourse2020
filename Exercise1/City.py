from typing import *
#Jorge Build
from FERAICourse2020.Exercise1.Road import Road
#Markus Build
#from Exercise1.Road import Road

class City:
    def __init__(self, name: str, heuristic_value: int, roads: List[Road]):
        self._name: str = name
        self._heuristic_value: int = heuristic_value
        self._roads: List[Road] = roads

    def set_name(self, name_main: str):
        self._name: str = name_main

    def get_name(self) -> str:
        return self._name

    def set_heuristic_value(self, heuristic_value: int):
        self._heuristic_value = heuristic_value

    def get_heuristic_value(self) -> int:
        return self._heuristic_value

    def set_roads(self, roads: List[Road]):
        self._roads = roads

    def get_roads(self) -> List[Road]:
        return self._roads
