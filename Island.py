'''
Given a 2d grid map of '1's (land) and '0's (water), count the number of islands. An island is surrounded by water and is formed
by connecting adjacent lands horizontally or vertically. You may assume all four edges of the grid are all surrounded by water.

//cute

Solution : 
The problem looks similar to graph. Here, we need to traverse whole graph in order to find number of islands.
Our goal is to visit entire matrix in one dfs call.
Upon traversing the graph we will search for land(i.e, 1), from here we will make a call to dfs function which will traverse in and around of
that particular index.
Increment count, once traversed and return the count value
'''

# Helper recursive function to check for availability of water around the island
    def dfs(self, grid, i, j):
        if i<0 or j<0 or i>=len(grid) or j>=len(grid[0]) or grid[i][j]!= '1':     # Checking for index out of range
            return
        grid[i][j]='0'                                                            # Mark as 0, once traversed
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
                if grid[i][j]=='1':                                               # If there is water, then make a call to dfs
                    self.dfs(grid,i,j)
                    islandCount+=1                                                # Increment counter value
        return islandCount
