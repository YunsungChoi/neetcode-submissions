class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        totalNum = 0
        visited = set()

        def visitAll(row, col):
             #현재 row, col 은 1이니까 일단 visited에 더하고
            dirs = [(1, 0), (-1, 0), (0, 1), (0, -1)]
            if row < 0 or col < 0 or row >= len(grid) or col >= len(grid[0]):
                return

            if (row, col) in visited:
                return
            
            if grid[row][col] == "1":
                visited.add((row, col))
                for dr, dc in dirs:
                    visitAll(row + dr, col + dc)
        



        for r in range(0, len(grid)):
            for c in range(0, len(grid[0])):
                if (r, c) not in visited and grid[r][c] == "1":
                    totalNum += 1
                    visitAll(r, c)
        
        return totalNum
            
