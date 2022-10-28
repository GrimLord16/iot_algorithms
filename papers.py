from collections import defaultdict



class Graph:

    # Constructor
    def __init__(self):

        # default dictionary to store graph
        self.graph = defaultdict(list)

    # function to add an edge to graph
    def addEdge(self, u, v):
        self.graph[u].append(v)

    # A function used by DFS
    def DFSUtil(self, v, visited):

        # Mark the current node as visited
        # and print it
        stack = []
        visited.add(v)
        stack.append(v)

        # Recur for all the vertices
        # adjacent to this vertex
        for neighbour in self.graph[v]:
            if neighbour not in visited:
                self.DFSUtil(neighbour, visited)
        print(stack)
    # The function to do DFS traversal. It uses
    # recursive DFSUtil()
    def DFS(self, v):

        # Create a set to store visited vertices
        visited = set()

        # Call the recursive helper function
        # to print DFS traversal
        self.DFSUtil(v, visited)


def main():
 # Set to keep track of visited nodes of graph.
    print("Following is the Depth-First Search")
    g = Graph()
    g.addEdge("visa", "foreignpassport")
    g.addEdge("visa", "hotel")
    g.addEdge("visa", "bankstatement")
    g.addEdge("bankstatement", "nationalpassport")
    g.addEdge("hotel", "creditcard")
    g.addEdge("creditcard", "nationalpassport")
    g.addEdge("nationalpassport", "birthsertificate")
    g.addEdge("foreignpassport", "nationalpassport")
    g.addEdge("foreignpassport", "militarycertificate")
    g.addEdge("militarycertificate", "nationalpassport")
    g.DFS('visa')


if __name__ == '__main__':
    main()
