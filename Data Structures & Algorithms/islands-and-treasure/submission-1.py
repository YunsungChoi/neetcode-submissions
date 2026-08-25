class Solution:
    def islandsAndTreasure(self, grid: List[List[int]]) -> None:
        
        INF = 2147483647
        q = deque()
        dirs = [(1, 0),(-1, 0),(0, 1),(0, -1)]

        for row in range(0, len(grid)):
            for col in range(0, len(grid[0])):
                if grid[row][col] == 0:
                    q.append((row,col))
                    
        while q: #always start from 0(treasure)
            row, col = q.popleft()
            for dr, dc in dirs:
                nr, nc = row + dr, col + dc
                if nr < 0 or nr >= len(grid) or nc < 0 or nc >= len(grid[0]): #outofbound
                    continue
                if grid[nr][nc] != INF:
                    continue

                grid[nr][nc] = grid[row][col] +1
                q.append((nr, nc))
                    
                
        