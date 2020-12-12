def main():
    rows = 3
    columns = 4

    matrix = [[i*columns+j for j in range(columns)] for i in range(rows)]
    print_matrix(matrix)

    transpose = [[matrix[i][j] for i, _ in enumerate(matrix)] for j, _ in enumerate(matrix[0])]
    print_matrix(transpose)


def print_matrix(m):
    for row in m:
        print(row)


if __name__ == '__main__':
    main()
