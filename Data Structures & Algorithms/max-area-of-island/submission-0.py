class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        totalNum = 0
        visited = set()
        dirs = [(1, 0),(-1, 0),(0, 1),(0, -1)]

        def countIsland(row, col):
            
            if row < 0 or col < 0 or row >= len(grid) or col >= len(grid[0]):
                return 0

            if (row, col) in visited:
                return 0

            if grid[row][col] == 0:
                return 0
                
            localNum = 1
            visited.add((row, col))
            for dr, dc in dirs:
                localNum += countIsland(row + dr, col + dc)
            
            return localNum
                
        for r in range(len(grid)):
            for c in range(len(grid[0])):
                if grid[r][c] == 1 and (r, c) not in visited:
                    num = countIsland(r, c)
                    totalNum = max(totalNum, num)

        return totalNum
        