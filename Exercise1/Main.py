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
        self._graph: Graph = Graph(state_space_path=state_space_path, heuristics_path=heuristics_path)
        self._open: List[Tuple[City, int, List[City]]] = []
        self._closed: List[str] = []

    def breadth_first_search(self) -> Optional[Tuple[int, int, float, List[str], str]]:
        # <editor-fold desc="Initially set open list">
        initial_city: City = self._graph.get_graph()[self._graph.get_initial_state()]
        goal_city_names: List[str] = self._graph.get_goal_states()
        self._open = [(initial_city, 0, [])]
        # </editor-fold>
        while self._open:
            # <editor-fold desc="Gets next tuple from the open list and put it on closed">
            open_tuple: Tuple[City, int, List[City]] = self._open.pop(0)
            head: City = open_tuple[0]
            current_cost: int = open_tuple[1]
            predecessors: List[City] = open_tuple[2]
            self._closed.append(head.get_name())
            # </editor-fold>
            if head.get_name() in goal_city_names: #"Check whether goal state has been reached"
                # <editor-fold desc="Prepares return statement">
                states_visited: int = len(self._closed)
                path_length: int = len(predecessors) + 1
                path_cost: float = float(current_cost)
                predecessor_names: List[str] = []
                for predecessor_element in predecessors:
                    predecessor_names.append(predecessor_element.get_name())
                head_name: str = head.get_name()
                return states_visited, path_length, path_cost, predecessor_names, head_name
                # </editor-fold>
            for road in head.get_roads():
                # <editor-fold desc="Add new notes to the open list">
                if road.get_to() not in self._closed:
                    self._open.append(
                        (
                            self._graph.get_graph()[road.get_to()],
                            current_cost + road.get_cost(),
                            predecessors + [head]
                        )
                    )
                # </editor-fold>
        return None

    def uniform_cost_a_star_search(self, is_uniform_cost: bool) -> Optional[Tuple[int, int, float, List[str], str]]:
        # <editor-fold desc="Initially set open list">
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
        # </editor-fold>
        while self._open:
            # <editor-fold desc="Gets next tuple from the open list and put it on closed">
            open_tuple: Tuple[City, int, List[City]] = (
                just(self._open)
                .pipe(map(
                    lambda open_list: open_list.pop(0)
                ))
                .pipe(first())
                .run()
            )
            self._closed.append(open_tuple[0].get_name())
            # </editor-fold>
            # <editor-fold desc="Check whether goal state has been reached">
            found_goal_state: bool = (
                just(self._graph)
                .pipe(map(
                    lambda graph: graph.get_goal_states()
                ))
                .pipe(map(
                    lambda goal_state_names: open_tuple[0].get_name() in goal_state_names
                ))
                .pipe(first())
                .run()
            )
            # </editor-fold>
            if found_goal_state:
                # <editor-fold desc="Prepares return statement">
                states_visited: int = len(self._closed)
                path_length: int = len(open_tuple[2]) + 1
                path_cost: float = float(open_tuple[1])
                predecessor_names: List[str] = (
                    from_list(open_tuple[2])
                    .pipe(map(
                        lambda pred: pred.get_name()
                    ))
                    .pipe(to_list())
                    .run()
                )
                head_name: str = open_tuple[0].get_name()
                return states_visited, path_length, path_cost, predecessor_names, head_name
                # </editor-fold>
            # <editor-fold desc="Create preliminary open list and sort it">
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
            if is_uniform_cost:
                preliminary_open.sort(key=lambda x: x[1])
            else:
                preliminary_open.sort(key=lambda x: x[1] + x[0].get_heuristic_value())

            # </editor-fold>
            # <editor-fold desc="Add the preliminary open list to the open list">
            self._open = (
                just(self._open)
                .pipe(map(
                    lambda open_list: open_list + preliminary_open
                ))
                .pipe(first())
                .run()
            )
            # </editor-fold>
        return None

    def a_star_search_defined_start(self, initial_city_name: str) -> float:
        # <editor-fold desc="Initially set open list">
        self._open = (
            just(self._graph)
            .pipe(map(
                lambda graph_object: (graph_object.get_graph(), initial_city_name)
            ))
            .pipe(map(
                lambda graph_info: (graph_info[0][graph_info[1]], 0, [])
            ))
            .pipe(to_list())
            .run()
        )
        # </editor-fold>
        while self._open:
            # <editor-fold desc="Gets next tuple from the open list and put it on closed">
            open_tuple: Tuple[City, int, List[City]] = (
                just(self._open)
                .pipe(map(
                    lambda open_list: open_list.pop(0)
                ))
                .pipe(first())
                .run()
            )
            self._closed.append(open_tuple[0].get_name())
            # </editor-fold>
            # <editor-fold desc="Check whether goal state has been reached">
            found_goal_state: bool = (
                just(self._graph)
                .pipe(map(
                    lambda graph: graph.get_goal_states()
                ))
                .pipe(map(
                    lambda goal_state_names: open_tuple[0].get_name() in goal_state_names
                ))
                .pipe(first())
                .run()
            )
            # </editor-fold>
            if found_goal_state:
                # <editor-fold desc="Prepares return statement">
                return float(open_tuple[1])
                # </editor-fold>
            # <editor-fold desc="Create preliminary open list and sort it">
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
            # </editor-fold>
            # <editor-fold desc="Add the preliminary open list to the open list">
            self._open = (
                just(self._open)
                .pipe(map(
                    lambda open_list: open_list + preliminary_open
                ))
                .pipe(first())
                .run()
            )
            # </editor-fold>
        return 0

    def check_optimistic_consistent(self, is_optimistic: bool) -> Tuple[bool, List[Tuple[bool, str, str, float, float, float]]]:
        if not is_optimistic:
            success, success_List = main_node.check_optimistic_consistent(is_optimistic=True)
            if not success:
                return (False, [])

        graph_to_check: Dict[str, City] = self._graph.get_graph()
        output: bool = True
        output_list: List[Tuple[bool, str, str, float, float, float]] = []
        for city_name in graph_to_check:
            city: City = graph_to_check[city_name]
            true_cost: float = self.a_star_search_defined_start(initial_city_name=city_name)
            heuristic_cost: float = city.get_heuristic_value()
            for road in city.get_roads():
                successor_name: str = road.get_to()
                successor: City = graph_to_check[successor_name]
                heuristic_cost_successor: float = successor.get_heuristic_value()
                road_cost: int = road.get_cost()
                if is_optimistic:
                    if heuristic_cost <= true_cost:
                        output_list.append((True, city_name, "",heuristic_cost, true_cost, 0))
                    else:
                        output_list.append((False, city_name, "",heuristic_cost, true_cost, 0))
                        output = False
                    self.clean()
                else:
                    if heuristic_cost <= road_cost + heuristic_cost_successor:
                        output_list.append((True, city_name, successor_name, heuristic_cost, road_cost, heuristic_cost_successor))
                    else:
                        output_list.append((True, city_name, successor_name, heuristic_cost, road_cost, heuristic_cost_successor))
                        output = False
        return output, output_list

    def clean(self):
        self._open: List[Tuple[City, int, List[City]]] = []
        self._closed: List[str] = []


if __name__ == '__main__':
    main_node: Main = Main("istra.txt", "istra_pessimistic_heuristic.txt")
    # <editor-fold desc="BFS">
    print("Running bfs:")
    test = main_node.breadth_first_search()
    if test is None:
        print("Unable to find a bfs route:")
    else:
        states_visited, path_length, path_cost, predecessor_names, head_name = test
        print(
            "States visited = "
            + str(states_visited)
            + "\n"
            + "Found path of length "
            + str(path_length)
            + " with total cost "
            + str(path_cost)
            + ":"
        )
        for predecessor_name in predecessor_names:
            print(
                predecessor_name
                + " =>"
            )
        print(head_name)
        main_node.clean()
    # </editor-fold>
    # <editor-fold desc="UCS">
    print("\n" + "Running ucs:")
    test = main_node.uniform_cost_a_star_search(is_uniform_cost=True)
    if test is None:
        print("Unable to find a ucs route:")
    else:
        states_visited, path_length, path_cost, predecessor_names, head_name = test
        print(
            "States visited = "
            + str(states_visited)
            + "\n"
            + "Found path of length "
            + str(path_length)
            + " with total cost "
            + str(path_cost)
            + ":"
        )
        for predecessor_name in predecessor_names:
            print(
                predecessor_name
                + " =>"
            )
        print(head_name)
        main_node.clean()
    # </editor-fold>
    # <editor-fold desc="A-Star">
    print("\n" + "Running astar:")
    test = main_node.uniform_cost_a_star_search(is_uniform_cost=False)
    if test is None:
        print("Unable to find a astar route:")
    else:
        states_visited, path_length, path_cost, predecessor_names, head_name = test
        print(
            "States visited = "
            + str(states_visited)
            + "\n"
            + "Found path of length "
            + str(path_length)
            + " with total cost "
            + str(path_cost)
            + ":"
        )
        for predecessor_name in predecessor_names:
            print(
                predecessor_name
                + " =>"
            )
        print(head_name)
    main_node.clean()
    # </editor-fold>
    # <editor-fold desc="Optimistic check">
    print("\n" + "Running check optimistic:")
    success, success_List = main_node.check_optimistic_consistent(is_optimistic=True)
    for individual_success, city_name, p_1,heuristic_cost, true_cost, p_2 in success_List:
        if individual_success:
            print(
                "[COR] h("
                + city_name
                + ") <= h*: "
                + str(heuristic_cost)
                + " <= "
                + str(true_cost)
            )
        else:
            print("[ERR] h(" + city_name + ") > h*: " + str(heuristic_cost) + " > " + str(true_cost))
            optimistic = False
    print("Heuristic is " + ("" if success else "not") + " optimistic")
    main_node.clean()
    # </editor-fold>
    # <editor-fold desc="Consistency test">
    print("\n" + "Running check consistent:")
    success, success_List = main_node.check_optimistic_consistent(is_optimistic=False)
    for individual_success, city_name, successor_name, heuristic_cost, road_cost, heuristic_cost_successor in success_List:
        if individual_success:
            print(
                "[COR] h("
                + city_name
                + ") <= h("
                + successor_name
                + ") + c: "
                + str(heuristic_cost)
                + " <= "
                + str(road_cost)
                + " + "
                + str(heuristic_cost_successor)
            )
        else:
            print(
                "[ERR] h("
                + city_name
                + ") > h("
                + successor_name
                + ") + c: "
                + str(heuristic_cost)
                + " > "
                + str(road_cost)
                + " + "
                + str(heuristic_cost_successor)
            )
    print("Consistent is " + ("" if success else "not") + " optimistic")
    main_node.clean()
    print("")
    # </editor-fold>
