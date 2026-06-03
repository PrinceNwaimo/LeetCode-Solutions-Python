class NumberOfIslands:
# @param {boolean[][]} grid a boolean 2D matrix
    # @return {int} an integer
    def numIslands(self, grid):
        if not grid:            
            return 0   
        row = len(grid)
        col = len(grid[0])
        used = [[False for j in range(col)] for i in range(row)]
        count = 0
        for i in range(row):
            for j in range(col):
                if grid[i][j] == '1' and used[i][j] == False:
                    self.dfs(grid, used, i, j)
                    count += 1  
        return count
    def dfs(self, grid, used,row, col, i, j):
        if grid[i][j] == '0' or used[i][j] == True:
            return
        used[i][j] = True
        if i != 0:
            self.dfs(grid, used, row, col, i - 1, j)
        if i != row - 1:
            self.dfs(grid, used, row, col, i + 1, j)
        if j != 0:
            self.dfs(grid, used, row, col, i, j - 1)
        if j != col - 1:
            self.dfs(grid, used, row, col, i, j + 1)