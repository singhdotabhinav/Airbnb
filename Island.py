'''
Given a 2d grid map of '1's (land) and '0's (water), count the number of islands. An island is surrounded by water and is formed
by connecting adjacent lands horizontally or vertically. You may assume all four edges of the grid are all surrounded by water.



Sol
'''


class Solution:
    # Helper recursive function to check for availability of water around the island
    def dfs(self, grid, i, j):
        if i<0 or j<0 or i>=len(grid) or j>=len(grid[0]) or grid[i][j]!= '1':     # Checking for index out of range
            return
        grid[i][j]='0'
        self.dfs(grid, i+1, j)                                                    # Check on right side of island 
        self.dfs(grid, i-1, j)                                                    # Check on left side of island
        self.dfs(grid, i, j+1)                                                    # Check on up side of island
        self.dfs(grid, i, j-1)                                                    # Check on down side of island
        
     
    # Main driver function
    def numIslands(self, grid: List[List[str]]) -> int:
        if not grid:                                                              # If no input then return
            return 0
        islandCount = 0                                                           # Initialize count of island to zero                                                                                        
        
        for i in range(len(grid)):                                                
            for j in range(len(grid[0])):
                if grid[i][j]=='1':
                    self.dfs(grid,i,j)
                    islandCount+=1
        return islandCount
