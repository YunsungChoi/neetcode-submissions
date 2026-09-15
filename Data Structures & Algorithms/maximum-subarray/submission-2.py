class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        localS, totalS = 0, nums[0]

        for num in nums:
            if localS < 0: localS = 0
            localS += num
            totalS = max(totalS, localS)

        return totalS