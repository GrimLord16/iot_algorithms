from collections import defaultdict


def covert_input_into_arrays():
    with open("governin.txt", 'r') as reader:
        data = [tuple(line.split()) for line in reader]
    return data



def find_the_first_one(data):
    temp1 = []
    temp2 = []
    for edge in data:
        temp1.append(edge[0])
        temp2.append(edge[1])
    x = str(list[0](set(temp1) - set(temp2)))
    x = x.replace("['", "")
    x = x.replace("']", "")
    return x


class Graph:

    def __init__(self):
        self.graph = defaultdict(list)

    def add_edge(self, my_tuple):
        first, second = my_tuple
        self.graph[first].append(second)

    def dfs_util(self, v, visited):

        stack = []
        visited.add(v)
        stack.append(v)

        for neighbour in self.graph[v]:
            if neighbour not in visited:
                self.dfs_util(neighbour, visited)
        x = str(stack)
        x = x.replace("['", "")
        x = x.replace("']", "")
        print(x)

    def dfs(self, v):

        visited = set()
        self.dfs_util(v, visited)

    def fillout(self, array):

        for edge in array:
            self.add_edge(edge)


def main():
    graph = Graph()
    data = covert_input_into_arrays()
    graph.fillout(data)
    source = find_the_first_one(data)
    graph.dfs(source)

    # print(stack)
    # output(stack)


if __name__ == '__main__':
    main()
