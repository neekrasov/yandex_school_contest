import sys


def show_way(matrix, x_last, y_last, x, y):
    if matrix[x][y] != '.':
        return
    match x - x_last:
        case 1:
            matrix[x][y] = 'D'
        case -1:
            matrix[x][y] = 'U'
    match y - y_last:
        case 1:
            matrix[x][y] = 'R'
        case -1:
            matrix[x][y] = 'L'
    show_way(matrix, x, y, x - 1, y)
    show_way(matrix, x, y, x + 1, y)
    show_way(matrix, x, y, x, y + 1)
    show_way(matrix, x, y, x, y - 1)


def start():
    matrix, default_x, default_y = [], 0, 0
    for i in range(n):
        matrix.append([])
        for j, symbol in enumerate(input()):
            if symbol == 'S':
                default_x, default_y = i, j
            matrix[-1].append(symbol)
    show_way(matrix, default_x, default_y, default_x + 1, default_y)
    show_way(matrix, default_x, default_y, default_x - 1, default_y)
    show_way(matrix, default_x, default_y, default_x, default_y + 1)
    show_way(matrix, default_x, default_y, default_x, default_y - 1)
    for i in matrix:
        print(*i, sep="")


if __name__ == '__main__':
    sys.setrecursionlimit(10 ** 6)
    n, m = map(int, input().split())
    start()
