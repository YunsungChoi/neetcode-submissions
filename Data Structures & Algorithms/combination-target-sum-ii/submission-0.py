class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        res = []
        path = []

        candidates.sort()
        def dfs(start, total):
            if total == target:
                res.append(path.copy())
                return
            elif total > target:
                return
            else:
                for i in range(start, len(candidates)):
                    if i > start and candidates[i] == candidates[i-1]:
                        continue
                    else:
                        path.append(candidates[i])
                        dfs(i + 1, total + candidates[i])
                        path.pop()
        dfs(0, 0)
        return res
        