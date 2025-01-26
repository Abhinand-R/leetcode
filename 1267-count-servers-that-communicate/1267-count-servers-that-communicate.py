class Solution:
    def countServers(self, grid: List[List[int]]) -> int:
        res=0
        rc=[0]*len(grid)
        cc=[0]*len(grid[0])
        for r in range(len(grid)):
            for c in range(len(grid[0])):
                if grid[r][c]==1:
                    rc[r]+=1
                    cc[c]+=1
        for r in range(len(grid)):
            for c in range(len(grid[0])):
                if grid[r][c] and (rc[r]>1 or cc[c]>1):
                    res+=1
        return res