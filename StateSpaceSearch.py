from MainNode import *
from Graph import *
def breadthFirstSearch(sO,succ,goal):
    iO = MainNode()
    iO.set_nameMain(sO)
    visited=[]
    nonVisited=[iO]
    while nonVisited:
        node = nonVisited.pop(0)

        if not visited.__contains__(node):
            visited.append(node)

            proxy = succ[node.get_nameMain()].neighbours
            for city in proxy:
                nonVisited.append(city)
    return visited

