def find_deepest_result(graph):
    visited_lines = []
    deepness = 1
    while graph:
        root_vertex = graph.pop(0)

        path = [vertex for vertex in graph
                if comparator(root_vertex, vertex) and vertex not in visited_lines]

        if path:
            deepness += 1
            visited_lines = visited_lines + path
    return deepness


def comparator(word1, word2):
    return len([letter for letter in list(word1) if letter not in list(word2)]) == 1 and len(word1) - len(word2) == 1


def take_info(file):
    with open(file) as file:
        lines = [line.rstrip() for line in file.readlines()]
        lines.pop(0)
        lines = sorted(lines, key=lambda elem: len(elem), reverse=True)
        return lines


def out_info(deepness):
    with open('wchain.out', 'w') as file:
        file.write(deepness)


def main(file):
    graph = take_info(file)
    print(graph)
    deepness = str(find_deepest_result(graph))
    out_info(deepness)


if __name__ == '__main__':
    main('wchain.in')
