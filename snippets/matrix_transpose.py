def main():
    rows = 3
    columns = 4

    matrix = [
        [i*columns+j for j in range(columns)]
        for i in range(rows)
    ]

    print_matrix(matrix)
    print()

    #as list comprehension:
    transpose = comprehension_transpose(matrix)
    print_matrix(transpose)
    print()

    #as list comprehension, getting rid of inner indexing:
    transpose = comprehension_transpose2(matrix)

    #nested for-loops
    transpose2 = transpose_matrix(matrix)
    print_matrix(transpose2)
    print()

    #zip() - function
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

def comprehension_transpose(m):
    return [
        [m[i][j] for i, _ in enumerate(m)]
        for j, _ in enumerate(m[0])
    ]

def comprehension_transpose2(m):
    """ suggestion from David Choweller
        - simplifying the inner loop
    """
    return [
        [row[col] for row in m]
        for col, _ in enumerate(m[0])
    ]

def zipped_transpose(m):
    transpose = [list(x) for x in zip(*m)]
    return transpose


if __name__ == '__main__':
    main()
