class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        dirs = [(1,0),(-1,0),(0,1),(0,-1)]
        pacific = set()
        atlantic = set()

        ROW = len(heights)
        COL = len(heights[0])

        def dfs(row, col, visited):
            visited.add((row, col))
            for dr, dc in dirs:
                nr, nc = row + dr, col + dc
                if nr < 0 or nr >= ROW or nc < 0 or nc >=COL:
                    continue
                if (nr, nc) in visited:
                    continue
                if heights[nr][nc] >= heights[row][col]:
                    dfs(nr, nc, visited)

        for r in range(ROW): # left/right sides
            dfs(r, 0, pacific) #pacific
            dfs(r, COL-1, atlantic) #atlantic
        for c in range(COL): # up/down side
            dfs(0, c, pacific) #pacific
            dfs(ROW-1, c, atlantic) #atlantic

        res = []
        for row, col in pacific:
            if (row, col) in atlantic:
                res.append([row, col])
        return res




        