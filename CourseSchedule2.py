from queue import Queue
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
        self.predecessor = None
        self.indegree = 0
        
    def addNeighbor(self, neighbor, weight=0):
        self.adjacent[neighbor] = weight   
    def getConnections(self):
        return self.adjacent.keys()
    def getVertexID(self):
        return self.id
    def getWeight(self, neighbor):
        return self.adjacent[neighbor]
    def setDistance(self, dist):
        self.distance = dist    
    def getDistance(self):
        return self.distance
    def setColor(self, color):
        self.color = color
    def getColor(self):
        return self.color
    def setPrevious(self, prev):
        self.predecessor = prev
    def getPrevious(self):
        return self.predecessor
    def setIndegree(self, indegree):
        self.indegree = indegree 
    def getIndegree(self):
        return self.indegree
    def setVisited(self):
        self.visited = True
    def getVisited(self):
        return self.visited 
    def __str__(self):
        return str(self.id) + ' adjacent: ' + str([x.id for x in self.adjacent])
class DirectedGraph:
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
    def getVertices(self):
            return self.vertDictionary.keys()
    def setPrevious(self, current):
            self.previous = current
    def getPrevious(self):
            return self.previous
    def __str__(self):
            return 'Vertices: ' + str(self.vertDictionary)
        
class CourseSchdeule2:
    def __init__(self):
        self.has_cycle = False
    def findOrder(self, numCourses, prerequisites):
        """
        :type numCourses: int
        :type prerequisites: List[List[int]]
        :rtype: List[int]
        """
        if prerequisites == [] and numCourses > 0:
            return [entries for entries in range(numCourses)]
        elif prerequisites == [] and numCourses == 0:
            return []
        else:            
            G = DirectedGraph()
            for entries in prerequisites:
                G.addEdge(entries[1], entries[0], 1)
            return self.topsort(G)
    def topsort(self, G):
          if G.getVertices() == []:
            return []
          else:
            topological_list = []
            topological_queue = Queue()
            nodes = G.getVertices()
            for node in G:
                if node.getIndegree() == 0:
                    topological_queue.put(node)      
            while topological_queue.empty() == False:
                current_node = topological_queue.get()
                topological_list.append(current_node.getVertexID())
                for neighbor in current_node.getConnections():
                    neighbor.setIndegree(neighbor.getIndegree() - 1)
                    if neighbor.getIndegree() == 0:
                        topological_queue.put(neighbor)
            if len(topological_list) != len(nodes):
                      self.has_cycle = True
            return topological_list
if __name__ == "__main__":
    numCourses = 4
    prerequisites = [[1,0],[2,0],[3,1],[3,2]]
    print(CourseSchdeule2().findOrder(numCourses, prerequisites))   
    print(CourseSchdeule2().findOrder(2, [[1,0]]))
    print(CourseSchdeule2().findOrder(3, [[1,0]]))   
    print(CourseSchdeule2().findOrder(4, [[1,0],[2,0],[3,1],[3,2]]))                   