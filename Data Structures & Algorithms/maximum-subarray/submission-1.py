class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        localS, totalS = 0, nums[0]
        if len(nums) == 1:
            return nums[-1]

        for num in nums:
            if localS < 0: localS = 0
            localS += num
            totalS = max(totalS, localS)

        return totalS