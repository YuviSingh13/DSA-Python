"""
# Bruteforce Approach
def countpaths(i, j, n, m) :
    if (i==n-1 and j == m-1) : return 1
    if (i >= n or j >= m) : return 0
    else return countpaths(i+1, j) + countpaths(i, j+1)

# Better Approach
using Dynamic Programming solution
"""


def uniquePaths(m: int, n: int) -> int:
    print()