from typing import List


def searchMatrix(matrix: List[List[int]], target: int) -> bool:
    n = len(matrix)
    m = len(matrix[0])

    low = 0
    high = (n*m)-1

    while low <= high:
        mid = (low+ (high-low)//2)
        if matrix[mid//m][mid%m] == target:
            return True
        if matrix[mid//m][mid%m] < target:
            low = mid + 1
        else:
            high = mid - 1
    return False

