def main():
    rows = 3
    columns = 4

    matrix = [[i*columns+j for j in range(columns)] for i in range(rows)]
    print_matrix(matrix)
    print()

    #as list comprehension:
    transpose = [[matrix[i][j] for i, _ in enumerate(matrix)] for j, _ in enumerate(matrix[0])]
    print_matrix(transpose)
    print()

    transpose2 = transpose_matrix(matrix)
    print_matrix(transpose2)
    print()

    transpose3 = zipped_transpose(matrix)
    print_matrix(transpose3)


def print_matrix(m):
    for row in m:
        print(row)


def transpose_matrix(m):
    rows = len(m)
    cols = len(m[0])
    transpose = [[0 for _ in range(rows)] for _ in range(cols)]
    for i in range(rows):
        for j in range(cols):
            transpose[j][i] = m[i][j]
    return transpose


def zipped_transpose(m):
    transpose = [list(x) for x in zip(*m)]
    return transpose


if __name__ == '__main__':
    main()
