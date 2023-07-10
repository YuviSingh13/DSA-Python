from typing import List


def rotate(matrix: List[List[int]]) -> None:
    print("Initial : ", matrix)
    for i in range(len(matrix)):
        for j in range(i):
            matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]
    print("Rotated : ",matrix)

    n = len(matrix[0])
    for i in range(len(matrix)):
        for j in range(n//2):
            matrix[i][j], matrix[i][n-j-1] = matrix[i][n-j-1], matrix[i][j]
    print("After reverse : ", matrix)
    return matrix


matrix = [[1,2,3],[4,5,6],[7,8,9]]
rotate(matrix)