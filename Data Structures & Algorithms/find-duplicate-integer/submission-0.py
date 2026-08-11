class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        if len(nums) < 1:
            return 0
        empty_set = set()
        for i in range(len(nums)):
            if nums[i] in empty_set:
                return nums[i]
            empty_set.add(nums[i])
        return 0