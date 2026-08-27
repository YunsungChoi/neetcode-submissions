class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        states = [0] * n
        path = defaultdict(list)
        visited = set()

        for n1, n2 in edges:
            path[n1].append(n2)
            path[n2].append(n1)

        def dfs(node, parent):
            if node in visited:
                return False
            visited.add(node)
            for nei in path[node]:
                if nei == parent: continue
                if not dfs(nei, node): return False
            return True

        return dfs(0, -1) and len(visited) == n