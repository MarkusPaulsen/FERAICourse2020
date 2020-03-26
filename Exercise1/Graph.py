from typing import *
from Exercise1.City import City
from Exercise1.Road import Road


class Graph:
    def __init__(self, state_space_path: str, heuristics_path: str):
        self._graph: Dict[str, City] = {}
        self._initial_state: str = ""
        self._goal_state: str = ""
        self._initialise_graph(state_space_path=state_space_path, heuristics_path=heuristics_path)

    def get_graph(self) -> Dict[str, City]:
        return self._graph

    def set_graph(self, graph: Dict[str, City]):
        self._graph = graph

    def add_graph_entry(self, name: str, heuristic_value: int, roads: List[Road]):
        self._graph[name] = City(name=name, heuristic_value=heuristic_value, roads=roads)

    def get_initial_state(self) -> str:
        return self._initial_state

    def set_initial_state(self, initial_state: str):
        self._initial_state = initial_state

    def get_goal_state(self) -> str:
        return self._goal_state

    def set_goal_state(self, goal_state: str):
        self._goal_state = goal_state

    def _initialise_graph(self, state_space_path: str, heuristics_path: str):
        state_space_file = open(state_space_path, encoding="utf8")
        heuristics_file = open(heuristics_path, encoding="utf8")

        state_space_lines: List[str] = state_space_file.readlines()
        heuristics_lines: List[str] = heuristics_file.readlines()

        heuristics_dict: Dict[str, int] = {}
        for heuristics_line in heuristics_lines:
            splitted_heuristics_line: List[str] = heuristics_line.split(": ")
            heuristics_dict[splitted_heuristics_line[0]] = int((splitted_heuristics_line[1]).strip("\n"))

        self.set_initial_state(state_space_lines[1].strip("\n:"))
        self.set_goal_state(state_space_lines[2].strip("\n:"))

        for state_space_line in state_space_lines:
            if state_space_line.__contains__("#") or not state_space_line.__contains__(":"):
                continue
            space_splited_line: List[str] = state_space_line.split(" ")
            name: str = space_splited_line[0].strip(":")
            roads: List[Road] = []
            heuristic_value = heuristics_dict[name]
            for road_nr in range(1, len(space_splited_line)):
                road_splitted: List[str] = space_splited_line[road_nr].split(",")
                road_to: str = road_splitted[0]
                road_cost: int = int(road_splitted[1])
                roads.append(Road(road_to, road_cost))
            self.add_graph_entry(name=name, heuristic_value=heuristic_value, roads=roads)

        state_space_file.close()
        heuristics_file.close()
