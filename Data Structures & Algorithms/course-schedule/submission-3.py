class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        
        state = [0] * numCourses # 0: default, 1: figuringout, 2: confirmed that there's no cycle
        path = defaultdict(list)

        for course, pre in prerequisites:
            path[pre].append(course)
        
        def dfs(courseIndex):
            if state[courseIndex] == 1: return False
            if state[courseIndex] == 2: return True

            state[courseIndex] = 1
            for course in path[courseIndex]:
                if not dfs(course):
                    return False
            state[courseIndex] = 2
            return True

        
        for c in range(numCourses):
            if not dfs(c): return False
        return True