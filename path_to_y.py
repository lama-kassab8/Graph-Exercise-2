class Edge:
    def __init__(self, target):
        self.target= target

class Vertex:
    def __init__(self, label):
        self.label= label
        self.edges= []

class Graph:
    def __init__(self):
        self.vertices=[]

    def path_availability(self,label_x, label_y):
        start= None # this is the starting point (x)
        destination= None # this is the destination (y)

        for v in self.vertices: # loop in the list of vertices
            if v.label ==label_x: # if the label for the starting point given in the argument is found:
                start= v # make this vertex the starting point
            if v.label ==label_y: # if the label for the destination is given in the argument is found
                destination= v # make this vertex the destination

        if not start or not destination: # if the labels do not match any vertices, return not found
            return False
        
        visited= set() # create a list that only keeps the visited vertices without repetion

        def dfs(vertex): # use the dfs method to look for the destination
            if vertex in visited: # as we're going through the vertices, if the vertex we're at was visited before, do not append it to the visited list
                return False
            if vertex == destination:# if the vertex is the vertex we're trying to reach, return true to indicate it's found
                return True 
            visited.add(vertex) # if the vertex was not visited and not the destination, append it to the list of visited

            for edge in vertex.edges: # loop through all the edges
                if dfs(edge.target): # recusively call the dfs method on all the ougoing edges for all the adjacent vertices
                    return True # if the edge from start to destination is found, return True
            return False # if the edge is not found (as it does not lead to destination) return False
        return dfs(start) # recursively call this method to explore all the paths from start to the destination

# create vertices
a = Vertex("A")
b = Vertex("B")
c = Vertex("C")

# add edges: A → B, B → C
a.edges.append(Edge(b))
b.edges.append(Edge(c))

# create the graph
g = Graph()
g.vertices.extend([a, b, c])

# test 1: A to C (should be True, A → B → C)
print(g.path_availability("A", "C"))  # Expected: True

# test 2: C to A (should be False, no reverse edges)
print(g.path_availability("C", "A"))  # Expected: False    
