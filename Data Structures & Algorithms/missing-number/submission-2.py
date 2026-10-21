class Solution:
    def missingNumber(self, nums: List[int]) -> int:

        # res = 0
        # for i in range(len(nums) + 1):
        #     if res not in nums:
        #         return res
        #     else:
        #         res += 1
        n = len(nums)
        xorr = n
        for i in range(n):
            xorr = xorr ^ i ^ nums[i]
        return xorr