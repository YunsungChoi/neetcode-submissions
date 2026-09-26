class Solution:
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:

        # DFS
        # path = defaultdict(list)
        # res = []

        # def dfs(node, parent):
        #     if node in visited:
        #         return True

        #     visited.add(node)
        #     for nei in path[node]:
        #         if nei == parent:
        #             continue
        #         if dfs(nei, node):
        #             return True
        #     return False


        # for u, v in edges:
        #     path[u].append(v)
        #     path[v].append(u)
        #     visited = set()
        #     if dfs(u, -1):
        #         return [u,v]
        # return []

        ##### NEW! Union Find ##### Path Compression / Union by Rank #####

        N = len(edges)
        par = [i for i in range(N + 1)] #ith node -> parent ( 1  through n)
        rank = [1] * (N + 1)

        def find(n):
            #recursively is a bit nicer
            if n != par[n]:
                par[n] = find(par[n])
            return par[n]

        def union(n1, n2):
            p1, p2 = find(n1), find(n2)
            if p1 == p2:
                return False

            if rank[p1] > rank[p2]:
                par[p2] = p1
                rank[p1] += rank[p2]
            else:
                par[p1] = p2
                rank[p2] += rank[p1]
            return True

        for n1, n2 in edges:
            if not union(n1, n2):
                return [n1, n2]







            
                


        



        

        