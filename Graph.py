from MainNode import *
from StateSpaceSearch import *
from Road import *
class Graph:
    def __init__(self, initialState="def", goalState="def"):
        self.graph = {}
        self._initialState: str = initialState
        self._goalState: str = goalState

    def get_initialState(self):
        return self._initialState

    def set_initialState(self, x):
        self._initialState: str = x

    def get_goalState(self):
        return self._goalState

    def set_goalState(self, x):
        self._goalState: str = x

def getStasteSpace(path,map):

    print("=========Reading StasteSpace=========")
    f = open(path,encoding="utf8")
    lines = f.readlines()
    map.set_initialState(lines[1].strip("\n:"))
    map.set_goalState(lines[2].strip("\n:"))
    for line in lines:
        if (line.__contains__("#")):
            continue
        space_splitedLine = line.split(" ")
        nodeTemp = MainNode()
        nodeTemp.nameMain = space_splitedLine[0].strip("\n:")
        for i in space_splitedLine:
            if (i.__contains__(",")):
                comma_splitedLines = i.split(",")

                nodeTemp.neighbours.append(Road(comma_splitedLines[0],comma_splitedLines[1].strip()))

        map.graph[nodeTemp.nameMain]=nodeTemp
    f.close()

def getHeuristic(path,map):

    print("=========Reading Heuristic=========")
    f = open(path,encoding="utf8")
    lines = f.readlines()

    for line in lines:
        space_splitedLine = line.split(" ")
        temp=MainNode()

        temp.nameMain = space_splitedLine[0].strip("\n:")
        temp.cost = space_splitedLine[1]
        map.graph[temp.nameMain].set_heuristic_val(temp.cost)

    f.close()
def getGraph(graph,pathState, pathHeur):
    getStasteSpace(pathState,graph)
    getHeuristic(pathHeur,graph)