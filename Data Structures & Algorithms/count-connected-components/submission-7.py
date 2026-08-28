class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        path = defaultdict(list)
        visited = set()
        res = 0

        def dfs(node):

            if node not in visited:
                visited.add(node)

            for nei in path[node]:
                if nei in visited:
                    continue
                dfs(nei)



        for u, v in edges:
            path[u].append(v)
            path[v].append(u)

        for node in range(n):
            if node not in visited:
                dfs(node)
                res += 1
        
        return res