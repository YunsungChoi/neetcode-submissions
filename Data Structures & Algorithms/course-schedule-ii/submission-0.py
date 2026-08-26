class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:

        path = defaultdict(list)
        states = [0] * numCourses # 0: default, 1: figuringout, 2: confirmed that there's no cycle
        res = []

        #create lists of linked nodes
        for course, pre in prerequisites:
            path[pre].append(course)

        def dfs(pre):
            if states[pre] == 1: return False
            if states[pre] == 2: return True

            states[pre] = 1
            for c in path[pre]:
                if not dfs(c):
                    return False
            states[pre] = 2
            res.append(pre)
            return True
        
        for c in range(numCourses):
            if not dfs(c): return []
        
        return res[::-1]
            
            


        