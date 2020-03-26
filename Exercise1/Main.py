# <editor-fold desc="Import RX">
from rx import just, from_list
from rx.operators import map, to_list, filter, flat_map, first
# </editor-fold>

from typing import *

#Jorge Build
from FERAICourse2020.Exercise1.City import City
from FERAICourse2020.Exercise1.Graph import Graph
#Markus Build
#from Exercise1.City import City
#from Exercise1.Graph import Graph



# noinspection DuplicatedCode
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
                print(
                    "Found path of length "
                    + str((len(predecessors) + 1))
                    + " with total cost "
                    + str(current_cost)
                    + ":"
                )
                for predecessor in predecessors:
                    print(predecessor.get_name() + " =>")
                print(head.get_name())
                return
            for road in head.get_roads():
                if road.get_to() not in self._closed:
                    self._open.append(
                        (
                            self._graph.get_graph()[road.get_to()],
                            current_cost + road.get_cost(),
                            predecessors + [head]
                        )
                    )
        print("No route found")
        return

    def uniform_cost_search(self):
        self._open = (
            just(
                self._graph
            )
            .pipe(map(
                lambda graph_object: (graph_object.get_graph(), graph_object.get_initial_state())
            ))
            .pipe(map(
                lambda graph_info: (graph_info[0][graph_info[1]], 0, [])
            ))
            .pipe(to_list())
            .run()
        )
        while self._open:
            open_tuple: Tuple[City, int, List[City]] = (
                just(self._open)
                .pipe(map(
                    lambda open_list: open_list.pop(0)
                ))
                .pipe(first())
                .run()
            )
            self._closed.append(open_tuple[0].get_name())
            found_goal_state: bool = (
                just(self._graph)
                .pipe(map(
                    lambda graph: (graph.get_graph(), graph.get_goal_state())
                ))
                .pipe(map(
                    lambda graph_info: graph_info[0][graph_info[1]]
                ))
                .pipe(map(
                    lambda goal_state: goal_state.get_name()
                ))
                .pipe(map(
                    lambda goal_state_name: goal_state_name == open_tuple[0].get_name()
                ))
                .pipe(first())
                .run()
            )
            if found_goal_state:
                print("States visited = " + str((len(self._closed))))
                print(
                    "Found path of length "
                    + str((len(open_tuple[2]) + 1))
                    + " with total cost "
                    + str(open_tuple[1])
                    + ":"
                )
                (
                    from_list(open_tuple[2])
                    .pipe(map(
                        lambda predecessor: predecessor.get_name()
                    ))
                    .subscribe(
                        on_next=lambda predecessor_name: print(predecessor_name + " =>")
                    )
                )
                print(open_tuple[0].get_name())
                return
            preliminary_open: List[Tuple[City, int, List[City]]] = []
            (
                just(open_tuple[0])
                .pipe(flat_map(
                    lambda current_city: current_city.get_roads()
                ))
                .pipe(map(
                    lambda road: (road.get_to(), road.get_cost())
                ))
                .pipe(filter(
                    lambda road_info: road_info[0] not in self._closed
                ))
                .subscribe(
                    on_next=lambda road_info: preliminary_open.append(
                        (
                            self._graph.get_graph()[road_info[0]],
                            open_tuple[1] + road_info[1],
                            open_tuple[2] + [open_tuple[0]]
                        )
                    )
                )
            )
            preliminary_open.sort(key=lambda x: x[1])
            self._open = (
                just(self._open)
                .pipe(map(
                    lambda open_list: open_list + preliminary_open
                ))
                .pipe(first())
                .run()
            )
        print("No route found")
        return

    def a_star_search(self):
        self._open = (
            just(self._graph)
            .pipe(map(
                lambda graph_object: (graph_object.get_graph(), graph_object.get_initial_state())
            ))
            .pipe(map(
                lambda graph_info: (graph_info[0][graph_info[1]], 0, [])
            ))
            .pipe(to_list())
            .run()
        )
        while self._open:
            open_tuple: Tuple[City, int, List[City]] = (
                just(self._open)
                .pipe(map(
                    lambda open_list: open_list.pop(0)
                ))
                .pipe(first())
                .run()
            )
            self._closed.append(open_tuple[0].get_name())
            found_goal_state: bool = (
                just(self._graph)
                .pipe(map(
                    lambda graph_object: (graph_object.get_graph(), graph_object.get_goal_state())
                ))
                .pipe(map(
                    lambda graph_info: graph_info[0][graph_info[1]]
                ))
                .pipe(map(
                    lambda goal_state: goal_state.get_name()
                ))
                .pipe(map(
                    lambda goal_state_name: goal_state_name == open_tuple[0].get_name()
                ))
                .pipe(first())
                .run()
            )
            if found_goal_state:
                print("States visited = " + str((len(self._closed))))
                print(
                    "Found path of length "
                    + str((len(open_tuple[2]) + 1))
                    + " with total cost "
                    + str(open_tuple[1])
                    + ":"
                )
                (
                    from_list(open_tuple[2])
                    .pipe(map(
                        lambda predecessor: predecessor.get_name()
                    ))
                    .subscribe(
                        on_next=lambda predecessor_name: print(predecessor_name + " =>")
                    )
                )
                print(open_tuple[0].get_name())
                return
            preliminary_open: List[Tuple[City, int, List[City]]] = []
            (
                just(open_tuple[0])
                .pipe(flat_map(
                    lambda current_city: current_city.get_roads()
                ))
                .pipe(map(
                    lambda road: (road.get_to(), road.get_cost())
                ))
                .pipe(filter(
                    lambda road_info: road_info[0] not in self._closed
                ))
                .subscribe(
                    on_next=lambda road_info: preliminary_open.append(
                        (
                            self._graph.get_graph()[road_info[0]],
                            open_tuple[1] + road_info[1],
                            open_tuple[2] + [open_tuple[0]]
                        )
                    )
                )
            )
            preliminary_open.sort(key=lambda x: x[1]+x[0].get_heuristic_value())
            self._open = (
                just(self._open)
                .pipe(map(
                    lambda open_list: open_list + preliminary_open
                ))
                .pipe(first())
                .run()
            )
        print("No route found")
        return

    def clean(self):
        self._open: List[Tuple[City, int, List[City]]] = []
        self._closed: List[str] = []
        print("")


if __name__ == '__main__':
    main_node: Main = Main("istra.txt", "istra_heuristic.txt")
    print("Breadth first search:")
    main_node.breadth_first_search()
    main_node.clean()
    print("Uniform cost search:")
    main_node.uniform_cost_search()
    main_node.clean()
    print("A* search:")
    main_node.a_star_search()
