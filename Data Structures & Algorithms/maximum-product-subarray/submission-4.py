class Solution:
    def maxProduct(self, nums: List[int]) -> int:

        if len(nums) == 1:
            return nums[0]

        curMin, curMax = 1, 1
        # res = 0 - 답이 0이상이라는 가정이 있을경우는 맞지만 더 안전하게 구현하려면
        res = nums[0] 
        for num in nums:
            curMax, curMin = max(curMax * num, curMin * num, num), min(curMax * num, curMin * num, num)
            res = max(res, curMax)

        return res
        