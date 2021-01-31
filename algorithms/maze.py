"""
Given an nxm grid, how many different ways can you reach the end?
You can only move right and down.

For these solutions n = 0 and m = 0 represents a 1x1 grid square.
"""

def countMazePathsRecursive(n = 0, m = 0):
    if n < 0 or m < 0:
        raise "cannot go below 0"
    elif n == 0 and m == 0:
        return 0
    elif n == 0 or m == 0:
        return 1
    return countMazePathsRecursive(n-1, m) + countMazePathsRecursive(n, m-1)

def countMazePathsMemo(n = 0, m = 0, memo = []):
    if not memo:
        memo = [[0 for j in range(m+1)] for i in range(n+1)]
    
    if n < 0 or m < 0:
        raise "cannot go below 0"
    elif n == 0 and m == 0:
        return 0
    elif n == 0 or m == 0:
        return 1

    if not memo[n][m]:
        memo[n][m] = countMazePathsMemo(n-1, m, memo) + countMazePathsMemo(n, m-1, memo)
    return memo[n][m]

def countMazePathsDP(n = 0, m = 0):
    if n < 0 or m < 0:
        raise "cannot go below 0"
    elif n == 0 and m == 0:
        return 0
    elif n == 0 or m == 0:
        return 1

    grid = [[0 for j in range(m+1)] for i in range(n+1)]

    for i in range(n+1):
        for j in range(m+1):
            if i == 0 and j == 0:
                grid[i][j] = 2
            elif i == 0 or j == 0:
                grid[i][j] = 1
            else:
                grid[i][j] = grid[i-1][j] + grid[i][j-1]

    return grid[n][m]

# (4,4) represents a 5x5 grid
print(countMazePathsRecursive(4,4))
print(countMazePathsMemo(4,4))
print(countMazePathsDP(4,4))