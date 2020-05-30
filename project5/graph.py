from stack_array import *  # Needed for Depth First Search
from queue_array import *  # Needed for Breadth First Search


class Vertex:
    '''Add additional helper methods if necessary.'''

    def __init__(self, key):
        '''Add other attributes as necessary'''
        self.id = key
        self.adjacent_to = []
        self.color = 'black'  # Initialize color to black


class Graph:
    '''Add additional helper methods if necessary.'''

    def __init__(self, filename):
        '''Reads in the specification of a graph and creates a graph using an adjacency list representation.  
           You may assume the graph is not empty and is a correct specification.  E.g. each edge is 
           represented by a pair of vertices.  Note that the graph is not directed so each edge specified 
           in the input file should appear on the adjacency list of each vertex of the two vertices associated 
           with the edge.'''
        self.adjacency_list = {}
        self.graph = self.create_graph(filename)

    def create_graph(self, filename):
        try:
            graph_file = open(filename, 'r')
            for edges in graph_file:
                (v1, v2) = edges.split()
                self.add_vertex(v1)
                self.add_vertex(v2)
                self.add_edge(v1, v2)
            graph_file.close()
        except FileNotFoundError as exception:
            print(exception)
            exit(-1)

    def add_vertex(self, key):
        '''Add vertex to graph, only if the vertex is not already in the graph.'''
        if key not in self.adjacency_list:
            self.adjacency_list[key] = Vertex(key)

    def get_vertex(self, key):
        '''Return the Vertex object associated with the id. If id is not in the graph, return None'''
        if key in self.get_vertices():
            return self.adjacency_list[key]
        else:
            return None

    def add_edge(self, v1, v2):
        '''v1 and v2 are vertex id's. As this is an undirected graph, add an 
           edge from v1 to v2 and an edge from v2 to v1.  You can assume that
           v1 and v2 are already in the graph'''
        self.adjacency_list[v1].adjacent_to.append(v2)
        self.adjacency_list[v2].adjacent_to.append(v1)

    def get_vertices(self):
        '''Returns a list of id's representing the vertices in the graph, in ascending order'''
        vertices = []
        for vertex in self.adjacency_list:
            vertices.append(self.adjacency_list[vertex].id)
        return sorted(vertices)

    def conn_components(self):
        '''Returns a list of lists.  For example, if there are three connected components 
           then you will return a list of three lists.  Each sub list will contain the 
           vertices (in ascending order) in the connected component represented by that list.
           The overall list will also be in ascending order based on the first item of each sublist.
           This method MUST use Depth First Search logic!'''
        res = []
        visited = []
        vertices = self.get_vertices()
        stack = Stack(len(vertices))
        for vertex in vertices:
            temp = []
            if vertex not in visited:
                stack.push(vertex)
            while stack.is_empty() is not True:
                vertex = stack.pop()
                if vertex not in visited:
                    temp.append(vertex)
                    visited.append(vertex)
                    for current_vertex in self.get_vertex(vertex).adjacent_to:
                        if current_vertex not in visited and current_vertex not in temp:
                            stack.push(current_vertex)
            if len(temp) > 0:
                res.append(sorted(temp))
        return sorted(res, key = lambda res: res[0])

    def is_bipartite(self):
        '''Returns True if the graph is bicolorable and False otherwise.
           This method MUST use Breadth First Search logic!'''
        graphs = self.conn_components()
        for graph in graphs:
            visited = []
            queue = Queue(len(graph))
            queue.enqueue(graph[0])
            while queue.is_empty() is not True:
                vertex = queue.dequeue()
                if vertex not in visited:
                    vertex1_color = self.get_vertex(vertex).color
                    visited.append(vertex)
                    for current_vertex in self.get_vertex(vertex).adjacent_to:
                        if vertex1_color == 'black':
                            self.get_vertex(current_vertex).color = 'red'
                        vertex2_color = self.get_vertex(current_vertex).color
                        if vertex1_color == vertex2_color:
                            return False
                        if current_vertex not in visited:
                            queue.enqueue(current_vertex)
        return True
