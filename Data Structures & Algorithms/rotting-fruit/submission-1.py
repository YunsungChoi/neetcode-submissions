class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        fresh = 0
        res = 0
        q = deque()
        dirs = [(1,0),(-1, 0),(0, 1),(0, -1)]

        for i in range(0, len(grid)):
            for j in range(0, len(grid[0])):
                if grid[i][j] == 1:
                    fresh += 1
                if grid[i][j] == 2:
                    q.append((i,j))
        
        while q and fresh > 0: #starting from rotten fruit
            for i in range(len(q)):
                row, col = q.popleft()
                for dr, dc in dirs:
                    nr, nc = row + dr, col + dc
                    if nr < 0 or nr >= len(grid) or nc < 0 or nc >=len(grid[0]):
                        continue
                    if grid[nr][nc] != 1:
                        continue
                    grid[nr][nc] = 2
                    fresh -= 1
                    q.append((nr, nc))
            res += 1
                    
        return res if fresh == 0 else -1



        

        