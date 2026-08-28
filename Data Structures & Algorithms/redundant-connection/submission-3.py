class Solution:
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:

        path = defaultdict(list)
        res = []

        def dfs(node, parent):
            if node in visited:
                return True

            visited.add(node)
            for nei in path[node]:
                if nei == parent:
                    continue
                if dfs(nei, node):
                    return True
            return False


        for u, v in edges:
            path[u].append(v)
            path[v].append(u)
            visited = set()
            if dfs(u, -1):
                return [u,v]
        return []



            
                


        



        

        