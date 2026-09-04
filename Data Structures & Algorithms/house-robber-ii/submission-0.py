class Solution:
    def rob(self, nums: List[int]) -> int:
        def helper(nums):
            r1, r2 = 0, 0
            for num in nums:
                temp = max(num+r1, r2)
                r1 = r2
                r2 = temp
            return r2
        return max(nums[0], helper(nums[1:]), helper(nums[:-1]))
        
        