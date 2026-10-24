class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        count = 0
        for ind, num in enumerate(nums):
            if num == val:
                nums[ind] = 999
            else:
                count += 1
        
        nums.sort()
        return count
        