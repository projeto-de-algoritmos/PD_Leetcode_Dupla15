# 63. Unique Paths II

class Solution(object):
    def uniquePathsWithObstacles(self, grid):
        m = len(grid)
        n = len(grid[0])

        if grid[0][0] == 1:
            return 0

        grid[0][0] = 1

        for i in range(1,m):
            grid[i][0] = int(grid[i][0] == 0 and grid[i-1][0] == 1)

        for j in range(1, n):
            grid[0][j] = int(grid[0][j] == 0 and grid[0][j-1] == 1)

        for i in range(1,m):
            for j in range(1,n):
                if grid[i][j] == 0:
                    grid[i][j] = grid[i-1][j] + grid[i][j-1]
                else:
                    grid[i][j] = 0
   
        return grid[m-1][n-1]

solve = Solution()
print(solve.uniquePathsWithObstacles([[0,0,0],[0,1,0],[0,0,0]]))
