from Road import *
from StateSpaceSearch import *
from Graph import *


class MainNode:
    def __init__(self, nameMain="Default", cost=999):
        self._nameMain: str = nameMain
        self.neighbours = []
        self._heuristic_val: int = cost

    def get_nameMain(self):
        return self._nameMain

    def set_nameMain(self, x):
        self._nameMain: str = x

    def get_heuristic_val(self):
        return self._heuristic_val

    def set_heuristic_val(self, x):
        self._heuristic_val: int = x

    def pop_neighbours(self):
        return self._neighbours.pop()

    def push_neighbours(self, x):
        self._neighbours.push(x)

    def clear_neighbours(self):
        return self._neighbours.clear()



if __name__ == '__main__':
    print("=========MAIN NODE=========")
    map = Graph()
    getGraph(map,'C:\\Users\\Jorge\\Documents\\Ingenieria informatica\\Tercero_Ig\\Segundo_Cuatri\\Artificial_Itelligence\\Labs\\Docs\\Lab1-Docs\\istra.txt',
             'C:\\Users\\Jorge\\Documents\\Ingenieria informatica\\Tercero_Ig\\Segundo_Cuatri\\Artificial_Itelligence\\Labs\\Docs\\Lab1-Docs\\istra_heuristic.txt')
    temp =map.graph["Umag"]
    print(
    breadthFirstSearch(map.get_initialState(),map.graph,map.get_goalState())
    )
    #print(temp.nameMain)
    #print(temp.get_heuristic_val())
    #for n in temp.neighbours:
    #    print(n.get_nameCity() + "--" + n.get_cost())

