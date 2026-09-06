class Solution:
    def maxProduct(self, nums: List[int]) -> int:

        if len(nums) == 1:
            return nums[0]

        curMin, curMax = 1, 1
        res = 0
        for num in nums:
            curMax, curMin = max(curMax * num, curMin * num, num), min(curMax * num, curMin * num, num)
            res = max(res, curMax)

        return res
        