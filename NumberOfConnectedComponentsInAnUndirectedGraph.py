import sys
from queue import Queue
   
class Vertex:
    def __init__(self, node):
        self.id = node
        self.adjacent = {}
        # Set distance to infinity for all nodes
        self.distance = sys.maxsize
        # Mark all nodes unvisited        
        self.visited = False
        # Mark all nodes color with white        
        self.color = 'white'      
        # Predecessor
        self.previous = None
        
    def getVertexID(self):
        return self.id
    def getConnections(self):
        return self.adjacent.keys()  
    def getWeight(self, neighbor):
        return self.adjacent[neighbor]
    def addNeighbor(self, neighbor, weight=0):
        self.adjacent[neighbor] = weight
    def getColor(self):
        return self.color
    def setPrevious(self, prev):
        self.previous = prev
    def setVisited(self):
        self.visited = True
    def __str__(self):
        return str(self.id) + ' adjacent: ' + str([x.id for x in self.adjacent])
    
                
class Graph:
    def __init__(self):
        self.vertDictionary = {}
        self.numVertices = 0
    def __iter__(self):
        return iter(self.vertDictionary.values())
    def addVertex(self, node):
        self.numVertices = self.numVertices + 1
        newVertex = Vertex(node)
        self.vertDictionary[node] = newVertex
        return newVertex
    def getVertex(self, n):
        if n in self.vertDictionary:
            return self.vertDictionary[n]
        else:
            return None
    def addEdge(self, frm, to, cost = 0):
        if frm not in self.vertDictionary:
            self.addVertex(frm)
        if to not in self.vertDictionary:
            self.addVertex(to)

        self.vertDictionary[frm].addNeighbor(self.vertDictionary[to], cost)
        self.vertDictionary[to].addNeighbor(self.vertDictionary[frm], cost)
    def getVertices(self):        
        return self.vertDictionary.keys()   
    def setPrevious(self, current, prev):
        self.vertDictionary[current].setPrevious(prev)
    def getPrevious(self, current):
        return self.vertDictionary[current].previous
    
class NumberOfConnectedComponentsInAnUndirectedGraph(object):
    # @param {integer} n
    # @param {integer[][]} edges
    # @return {integer}
    def countComponents(self, n, edges):
        """
        :type n: int
        :type edges: List[List[int]]
        :rtype: int
        """
        if n == 1 and edges == []:
            return 1
        else:
            graph = Graph()
            for entries in edges:
                graph.addEdge(entries[0], entries[1])
            count = 0   
            for vertex in graph:
                if vertex.getColor() == 'white':
                    count += 1
                    self.bfs(graph, vertex)
            return count
    def bfs(self, graph, start):
        start.setVisited()
        start.color = 'gray'
        queue = Queue()
        queue.put(start)
        while not queue.empty():
            current = queue.get()
            for neighbor in current.getConnections():
                if neighbor.getColor() == 'white':
                    neighbor.setVisited()
                    neighbor.color = 'gray'
                    queue.put(neighbor)
            current.color = 'black'
        if __name__ == "__main__":
            n= 5
            edges1 = [[0, 1], [1, 2], [3, 4]]  
            edges2 = [[0, 1], [1, 2], [2, 3], [3, 4]]
            solution = NumberOfConnectedComponentsInAnUndirectedGraph()
            
            print(solution.countComponents(n, edges1))
            print(solution.countComponents(n, edges2))  
            