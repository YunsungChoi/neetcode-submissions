class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        # right -> down -> left -> top 
        dirs = [(0, 1), (1, 0), (0, -1), (-1, 0)]
        d = 0
        m = len(matrix)
        n = len(matrix[0])
        res = []
        visited = set()
        r, c = 0, 0

        for _ in range(m * n):
            res.append(matrix[r][c])
            visited.add((r, c))
            nr, nc = r + dirs[d][0], c + dirs[d][1]
            if nr >= m or nr < 0 or nc >= n or nc < 0 or (nr, nc) in visited:
                d = (d+1) % 4
                nr, nc = r + dirs[d][0], c + dirs[d][1]
            r, c = nr, nc
        
        return res

        
        