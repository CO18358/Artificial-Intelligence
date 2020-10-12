#import library to calculate time
import time
import random

class Graph:

    #initialization
    def __init__(self, graph = None, dir = True):
        self.graph = graph or {}
        self.dir = dir
        if not dir:
            self.make_undir_graph()

    #undirected graph
    def make_undir_graph(self):
        for i in list(self.graph.keys()):
            for (j, weight) in self.graph[i].items():
                self.graph.setdefault(j, {})[i] = weight

    #make edge
    def make_edge(self, vrt_1, vrt_2, weight = 1):
        self.graph.setdefault(vrt_1, {})[vrt_2] = weight
        if not self.dir:
            self.graph.setdefault(vrt_2, {})[vrt_1] = weight

    #get adjacent nodes
    def get(self, vrt_1, vrt_2 = None):
        adj_vrt = self.graph.setdefault(vrt_1, {})
        if vrt_2 is None:
            return adj_vrt
        else:
            return adj_vrt.get(vrt_2)

    #return vertices in graph
    def fetch_vertices(self):
        s1 = set([k1 for k1 in self.graph.keys()])
        s2 = set([k2 for v in self.graph.values() for k2, v2 in v.items()])
        vrts = s1.union(s2)
        return list(vrts)
    
class Vertex:

    #initialization
    def __init__(self, name, root):
        self.name = name
        self.root = root
        self.src_dist = 0
        self.tgr_dist = 0
        self.cost = 0

    #compare 2 vertices
    def __eq__(self, other):
        return self.name == other.name

    #sort vertices
    def __lt__(self, other):
        return self.cost < other.cost

    #PRINT VERTEX_COST
    def __repr__(self):
        return '({0})'.format(self.cost)

def bfs(graph, heuristics, source, target):
    
    #visited and unvisted nodes list
    visited = []
    unvisited = []
    src = Vertex(source, None)
    trg = Vertex(target, None)

    # source -> unvisted list
    unvisited.append(src)
    print(unvisited)

    while len(unvisited) > 0:
        
        #sort unvisited list
        unvisited.sort()
        print(unvisited)

        #get lowest cost vertex
        low_heur_vrt = unvisited.pop(0)

        #source -> visited list
        visited.append(low_heur_vrt)

        #check if its target
        if low_heur_vrt == trg:
            
            # path of source to target
            path = []

            while low_heur_vrt != src:
                path.append(low_heur_vrt.name + ': ' + str(low_heur_vrt.src_dist))
                low_heur_vrt = low_heur_vrt.root
            path.append(src.name + ': ' + str(src.src_dist))
            return path[::-1]

        adjacent = graph.get(low_heur_vrt.name)

        for key, value in adjacent.items():
            
            #create neighbor vertex
            ngbr = Vertex(key, low_heur_vrt)

            if (ngbr in visited):
                continue
            ngbr.src_dist = low_heur_vrt.src_dist + graph.get(low_heur_vrt.name, ngbr.name)
            ngbr.tgr_dist = heuristics.get(ngbr.name)
            ngbr.cost = ngbr.tgr_dist
            
            #check neighbor cost and if unvisited
            if add_to_unvisit(unvisited, ngbr) == True:
                unvisited.append(ngbr)
                
    return None #if No path

#Check if neighbor can be added to unvisited
def add_to_unvisit(unvisited, neighbour):
    for vertex in unvisited:
        if neighbour == vertex and neighbour.cost >= vertex.cost:
            return False
    return True 

#driver code
print("Best First Search Algortihm")
graph = Graph()
#add edges
graph.make_edge('A','G',25)
graph.make_edge('A','I',43)
graph.make_edge('A','L',56)
graph.make_edge('B','C',39)
graph.make_edge('B','F',38)
graph.make_edge('B','J',34)
graph.make_edge('B','K',87)
graph.make_edge('C','H',79)
graph.make_edge('C','I',79)
graph.make_edge('C','K',23)
graph.make_edge('D','G',71)
graph.make_edge('D','J',56)
graph.make_edge('D','K',58)
graph.make_edge('D','L',55)
graph.make_edge('D','M',68)
graph.make_edge('E','H',88)
graph.make_edge('E','K',59)
graph.make_edge('E','M',49)
graph.make_edge('F','G',26)
graph.make_edge('F','I',29)
graph.make_edge('F','J',30)
graph.make_edge('G','J',96)
graph.make_edge('H','J',92)
graph.make_edge('H','K',84)
graph.make_edge('J','K',83)
graph.make_edge('J','L',88)
graph.make_edge('K','M',66)
graph.make_undir_graph()
#heuristics
heuristics = {
    'A': random.randint(1, 100),
    'B': random.randint(1, 100),
    'C': random.randint(1, 100),
    'E': random.randint(1, 100),
    'D': random.randint(1, 100),
    'G': random.randint(1, 100),
    'F': random.randint(1, 100),
    'H': random.randint(1, 100),
    'I': random.randint(1, 100),
    'J': random.randint(1, 100),
    'K': random.randint(1, 100),
    'L': random.randint(1, 100),
    'M': random.randint(1, 100),
}
src = input("Enter the Source Vertex: ")
trg = input("Enter the Target Vertex: ")
#INITAL TIME
start = time.time()
route = bfs(graph, heuristics, src, trg)
print('The route from Source to Target Node is: {0}'.format(route))
print()
#FINAL TIME
end = time.time()
print("Program Execution Time: ", end-start, " seconds")
