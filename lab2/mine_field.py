def is_valid(x, y, row, column):
    if row > x >= 0 and column > y >= 0:
        return True

    return False


def is_safe(mat, visited, x, y):
    if mat[x][y] == 0 or visited[x][y]:
        return False

    return True


def spot_mines_and_convert_neighbours(mat, row, column):
    row_num = [-1, -1, 0, 1, 1, 1, 0, -1]
    col_num = [0, -1, -1, -1, 0, 1, 1, 1]
    for i in range(row):
        for j in range(column):

            if mat[i][j] == 0:
                for k in range(8):
                    if is_valid(i + row_num[k], j + col_num[k], row, column):
                        mat[i + row_num[k]][j + col_num[k]] = -1

    for i in range(row):
        for j in range(column):
            if mat[i][j] == -1:
                mat[i][j] = 0


def find_shortest_path_util(mat, visited, i, j, dist, column, row, row_num, col_num):

    global min_dist

    if j == column - 1:
        if min_dist != 0:
            min_dist = min(dist, min_dist)
            return min_dist
        else:
            min_dist = dist
            return min_dist

    if min_dist != 0:
        if dist > min_dist:
            return

    visited[i][j] = True

    for k in range(4):
        if is_valid(i + row_num[k], j + col_num[k], row, column) and is_safe(mat, visited, i + row_num[k],
                                                                             j + col_num[k]):
            find_shortest_path_util(mat, visited, i + row_num[k], j + col_num[k], dist + 1, column, row,
                                    row_num, col_num)

    visited[i][j] = False


def find_shortest_path(mat):
    global min_dist
    min_dist = 0

    row_num = [-1, 0, 0, 1]
    col_num = [0, -1, 1, 0]
    row = len(mat)
    column = len(mat[0])

    visited = [[False for _ in range(column)] for _ in range(row)]

    spot_mines_and_convert_neighbours(mat, row, column)

    for i in range(row):
        if mat[i][0] == 1:
            find_shortest_path_util(mat, visited, i, 0, 0, column, row, row_num, col_num)
            if min_dist == column - 1:
                break

    if min_dist != 0:
        print("Length of shortest safe route is", min_dist)
    else:
        print("Destination not reachable from given source")


def main():
    mat = [
        [1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
        [1, 0, 1, 1, 1, 1, 1, 1, 1, 1],
        [1, 1, 1, 0, 1, 1, 1, 1, 1, 1],
        [1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
        [1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
        [1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
        [1, 0, 1, 1, 1, 0, 1, 1, 0, 1],
        [1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
        [1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
        [0, 1, 1, 1, 1, 0, 1, 1, 1, 1],
        [1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
        [1, 1, 1, 0, 1, 1, 1, 1, 1, 1]]

    find_shortest_path(mat)

    for i in range(len(mat)):
        print(mat[i])


if __name__ == "__main__":
    main()
