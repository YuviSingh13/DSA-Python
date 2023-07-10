# Bruteforce Approach

def markRow(matrix, n, m, i):
    for j in range(m):
        if matrix[i][j] != 0:
            matrix[i][j] = -1


def markCol(matrix, n, m, j):
    for i in range(n):
        if matrix[i][j] != 0:
            matrix[i][j] = -1


def zeroMatrix(matrix, n, m):
    for i in range(n):
        for j in range(m):
            if matrix[i][j] == 0:
                markRow(matrix, n, m, i)
                markCol(matrix, n, m, j)

    for i in range(n):
        for j in range(m):
            if matrix[i][j] == -1:
                matrix[i][j] = 0

    return matrix


if __name__ == "__main__":
    # matrix = [[1, 1, 1], [1, 0, 1], [1, 1, 1]]
    matrix = [[0, 1, 2, 0], [3, 4, 5, 2], [1, 3, 1, 5]]
    n = len(matrix)
    m = len(matrix[0])
    ans = zeroMatrix(matrix, n, m)

    print("The Final matrix is:", ans)


# Better Approach

def zeroMatrix(matrix, n, m):
    row = [0] * n  # row array
    col = [0] * m  # col array

    # Traverse the matrix:
    for i in range(n):
        for j in range(m):
            if matrix[i][j] == 0:
                # mark ith index of row wih 1:
                row[i] = 1

                # mark jth index of col wih 1:
                col[j] = 1

    # Finally, mark all (i, j) as 0
    # if row[i] or col[j] is marked with 1.
    for i in range(n):
        for j in range(m):
            if row[i] or col[j]:
                matrix[i][j] = 0

    return matrix


if __name__ == "__main__":
    matrix = [[1, 1, 1], [1, 0, 1], [1, 1, 1]]
    n = len(matrix)
    m = len(matrix[0])
    ans = zeroMatrix(matrix, n, m)

    print("The Final matrix is:")
    for row in ans:
        for ele in row:
            print(ele, end=" ")
        print()


# Optimal Approach

def zeroMatrix(matrix, n, m):

    col0 = 1

    # Traverse the matrix:
    for i in range(n):
        for j in range(m):
            if matrix[i][j] == 0:
                matrix[i][0] = 0

                if j != 0:
                    matrix[0][j] = 0
                else:
                    col0 = 0

    for i in range(1, n):
        for j in range(1, m):
            if matrix[i][0] == 0 or matrix[0][j] == 0:
                matrix[i][j] = 0

    if matrix[0][0] == 0:
        for j in range(m):
            matrix[0][j] = 0
    if col0 == 0:
        for i in range(n):
            matrix[i][0] = 0

    return matrix


if __name__ == "__main__":
    matrix = [[1, 1, 1], [1, 0, 1], [1, 1, 1]]
    n = len(matrix)
    m = len(matrix[0])
    ans = zeroMatrix(matrix, n, m)

    print("The Final matrix is:")
    for row in ans:
        for ele in row:
            print(ele, end=" ")
        print()