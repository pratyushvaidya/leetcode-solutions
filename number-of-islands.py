# 200. NUMBER OF ISLANDS

class Solution:
    """
    Given an m x n 2D binary grid grid which represents a map of '1's (land) and '0's (water), return the number of islands.

    An island is surrounded by water and is formed by connecting adjacent lands horizontally or vertically. You may assume all four edges of the grid are all surrounded by water.

    Example 1:
    Input: grid = [
      ["1","1","1","1","0"],
      ["1","1","0","1","0"],
      ["1","1","0","0","0"],
      ["0","0","0","0","0"]
    ]
    Output: 1
    
    Example 2:
    Input: grid = [
      ["1","1","0","0","0"],
      ["1","1","0","0","0"],
      ["0","0","1","0","0"],
      ["0","0","0","1","1"]
    ]
    Output: 3
    """
    def numIslands(self, grid: List[List[str]]) -> int:
        count = 2
        def checkNeighbouring(i, j):
            if i-1 >= 0 and grid[i-1][j] == '1':
                grid[i-1][j] = count
                checkNeighbouring(i-1,j)
            if i+1 < len(grid) and grid[i+1][j] == '1':
                grid[i+1][j] = count
                checkNeighbouring(i+1,j)
            if j-1 >= 0 and grid[i][j-1] == '1':
                grid[i][j-1] = count
                checkNeighbouring(i,j-1)
            if j+1 < len(grid[i]) and grid[i][j+1] == '1':
                grid[i][j+1] = count
                checkNeighbouring(i,j+1)

        for i in range(len(grid)):
            for j in range(len(grid[i])):
                if grid[i][j] == '1':
                    grid[i][j] = count
                    checkNeighbouring(i,j)
                    count+=1
        print(grid)
        return count-2
