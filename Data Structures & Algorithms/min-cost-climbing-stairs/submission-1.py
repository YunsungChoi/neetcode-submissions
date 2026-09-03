class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        memo = {}
        n = len(cost)

        def f(i):
            if i >= n: return 0
            if i in memo: return memo[i]

            total = cost[i] + min(f(i+1), f(i+2))
            memo[i] = total
            return total

        return min(f(0), f(1))


        