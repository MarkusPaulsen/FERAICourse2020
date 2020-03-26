from typing import *
from Exercise1.City import City
from Exercise1.Graph import Graph


class Main:
    def __init__(self, state_space_path: str, heuristics_path: str):
        self._graph = Graph(state_space_path=state_space_path, heuristics_path=heuristics_path)
        self._open: List[Tuple[City, int, List[City]]] = []
        self._closed: List[str] = []

    def breadth_first_search(self):
        initial_city: City = self._graph.get_graph()[self._graph.get_initial_state()]
        goal_city: City = self._graph.get_graph()[self._graph.get_goal_state()]
        self._open = [(initial_city, 0, [])]
        while self._open:
            open_tuple: Tuple[City, int, List[City]] = self._open.pop(0)
            head: City = open_tuple[0]
            current_cost: int = open_tuple[1]
            predecessors: List[City] = open_tuple[2]
            self._closed.append(head.get_name())
            if head.get_name() == goal_city.get_name():
                print("States visited = " + str((len(self._closed))))
                print("Found path of length " + str((len(predecessors) + 1)))
                print("with total cost " + str(current_cost) + ":")
                for predecessor in predecessors:
                    print(predecessor.get_name() + " =>")
                print(head.get_name())
                return
            for road in head.get_roads():
                if road.get_to() not in self._closed:
                    self._open.append(
                        (self._graph.get_graph()[road.get_to()], current_cost + road.get_cost(), predecessors + [head])
                    )
        print("No route found")
        return


if __name__ == '__main__':
    main_node: Main = Main("istra.txt", "istra_heuristic.txt")
    main_node.breadth_first_search()
