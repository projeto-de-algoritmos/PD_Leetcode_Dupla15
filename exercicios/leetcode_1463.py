# 1463. Cherry Pickup II

class Solution:
    def cherryPickup(self, grid):
        m = len(grid)
        n = len(grid[0])
        matrix = [[[0]*n for _ in range(n)] for __ in range(m)]

        for _ in range(m):
            array = []
            for _ in range(n):
                array.append(0)
            matrix.append(array)

        for row in list(range(m))[::-1]:
            for col1 in range(n):
                for col2 in range(n):
                    result = 0

                    result += grid[row][col1]
                    if col1 != col2:
                        result += grid[row][col2]

                    if row != m-1:
                        result += max(matrix[row+1][new_col1][new_col2]
                                      for new_col1 in [col1, col1+1, col1-1]
                                      for new_col2 in [col2, col2+1, col2-1]

                                      if 0 <= new_col1 < n and 0 <= new_col2 < n)

                    matrix[row][col1][col2] = result

        return matrix[0][0][n-1]


solve = Solution()
print(solve.cherryPickup([[3,1,1],[2,5,1],[1,5,5],[2,1,1]]))
