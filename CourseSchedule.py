class Vertex:
    def __init__(self, key):
        self.id = key
        self.adjacent = {}
        self.indegree = 0
        self.outdegree = 0
        self.predecessor = None
        self.visit_time = 0
        self.finish_time = 0
        self.color = "white"
    def add_neighbor(self, nbr, weight=0):
        self.adjacent[nbr] = weight
    def get_neighbors(self):
        return self.adjacent.keys()
    def get_id(self):
        return self.id
    def get_weight(self, nbr):
        return self.adjacent[nbr]
    def get_indegree(self):
        return self.indegree  
    def set_indegree(self, indegree):
        self.indegree = indegree
    def get_outdegree(self):
        return self.outdegree
    def set_outdegree(self, outdegree):
        self.outdegree = outdegree
    def get_predecessor(self):
        return self.predecessor
    def set_predecessor(self, predecessor):
        self.predecessor = predecessor
    def get_visit_time(self):
        return self.visit_time
    def set_visit_time(self, visit_time):
        self.visit_time = visit_time
    def get_finish_time(self):
        return self.finish_time
    def set_finish_time(self, finish_time):
        self.finish_time = finish_time
    def get_color(self):
        return self.color
    def set_color(self, color):
        self.color = color
    def __str__(self):
        return str(self.id) + ' adjacent: ' + str([x.id for x in self.adjacent])
    
class Graph:
    def __init__(self):
        self.vertex_dict = {}
        self.no_vertices = 0
        self.no_edges = 0
    def add_vertex(self, vert_key):
        new_vertex_obj = Vertex(vert_key)
        self.vertex_dict[vert_key] = new_vertex_obj
        self.no_vertices += 1
    def get_vertex(self, vert_key):
        if vert_key in self.vertex_dict:
            return self.vertex_dict[vert_key]
        else:
            return None 
    def add_edge(self, from_vert, to_vert, weight=0):
        if from_vert not in self.vertex_dict:
            self.add_vertex(from_vert)
        if to_vert not in self.vertex_dict:
            self.add_vertex(to_vert)
        self.vertex_dict[from_vert].add_neighbor(self.vertex_dict[to_vert], weight)
        self.no_edges += 1
    def get_edges(self):
        edges = []
        for vertex in self.vertex_dict.values():
            for neighbor in vertex.get_neighbors():
                edges.append((vertex.get_id(), neighbor.get_id()))
        return edges
    def get_vertices(self):
        return self.vertex_dict.keys()
    def __iter__(self):
        return iter(self.vertex_dict.values())
    
class DFS:
    def __init__(self, graph):
        self.graph = graph
        self.has_cycle = False
        
    def dfs(self):
        for vertex in self.graph:
            if vertex.get_color() == 'white':
                self.dfs_visit(vertex)
    def dfs_visit(self, vertex):
        vertex.set_color('gray')
        for neighbor in vertex.get_neighbors():
            if neighbor.get_color() == 'white':
                self.dfs_visit(neighbor)
            elif neighbor.get_color() == 'gray':
                self.has_cycle = True
        vertex.set_color('black')
class CourseSchedule(object):
    # @param {integer} numCourses
    # @param {integer[][]} prerequisites
    # @return {boolean}
    def canFinish(self, numCourses, prerequisites):
        """
        :type numCourses: int
        :type prerequisites: List[List[int]]
        :rtype: bool
        """
        if not prerequisites:
            return True
        else:
            graph = Graph()
            for entries in prerequisites:
                graph.add_edge(entries[1], entries[0])
            dfs = DFS(graph)
            dfs.dfs()
            if dfs.has_cycle:
                return False
            else:
                return True
if __name__ == "__main__":
    solution = CourseSchedule()
    print(solution.canFinish(2, [[1,0]]))
    print(solution.canFinish(2, [[1,0], [0,1]]))
    
        
                           
