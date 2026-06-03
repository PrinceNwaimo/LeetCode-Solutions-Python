import sys
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
    def add_neighbor(self, neighbor, weight=0):
        self.adjacent[neighbor] = weight
    def get_connections(self):
        return self.adjacent.keys()
    def getVertexID(self):
        return self.id
    def setVisited(self):
        self.visited = True
    def getDistance(self):
        return self.distance
    def getColor(self):
        return self.color    
    def setColor(self, color):
        self.color = color
    def setDistance(self, dist):
        self.distance = dist
    def setPrevious(self, prev):
        self.previous = prev
    def getPrevious(self):
        return self.previous
    def __str__(self):
        return str(self.id) + ' adjacent: ' + str([x.id for x in self.adjacent])   
class Graph:
    def __init__(self):
        self.vertDictionary = {}
        self.numVertices = 0
        return self.adjacent.keys() 
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
        self.vertDictionary[frm].add_neighbor(self.vertDictionary[to], cost)     
    def getWeight(self, neighbor):
        return self.adjacent[neighbor] 
    def getVertices(self):
        return self.vertDictionary.keys()
    def setPrevious(self, current):
        self.previous = current
    def getPrevious(self):
        return self.previous
    def __str__(self):
        return 'Vertices: ' + str(self.vertDictionary)
    
class GraphValidTree:
    def validTree(self, n, edges):
        """
        :type n: int
        :type edges: List[List[int]]
        :rtype: bool
        """
        if n == 1 and len(edges) == 0:
            return True
        elif self.check_input(n, edges) == False:
            return False
        elif n == 0 and len(edges) > 0:
            return False
        elif n == 1 and len(edges) >= 1:
            return False
        else:
            G = Graph()
            for entries in edges:
                G.addEdge(entries[0], entries[1], 1)
            results = []
            for vertex in G:
                if vertex.getColor() == "white":
                    results.append(self.check_validity(vertex))

            if len(results) > 1:
                return False
            else:
                return results[0]      
    def check_input(self, n, edges):
        vertices = []
        for entries in edges:
            vertices.append(entries[0])
            vertices.append(entries[1])
        if len(set(vertices)) != n:
            return False         
        else:
            return True
    def check_validity(self, start):
        stack = []
        start.setColor("gray")
        stack.append(start)
        while stack != []:
            curr_node = stack.pop()
            for nbr in curr_node.getConnections():
                if nbr.getColor() == "gray":
                    return False
                if nbr.getColor() == "white":
                    nbr.setColor("gray")
                    stack.append(nbr)
            curr_node.setColor("black")
            return True