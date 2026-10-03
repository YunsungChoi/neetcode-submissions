class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        lowP = prices[0]
        res = 0
        for price in prices:
            lowP = min(lowP, price)
            res = max(res, price - lowP)
        return res


        