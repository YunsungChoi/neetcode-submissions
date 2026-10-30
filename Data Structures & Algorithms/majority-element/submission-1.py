class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        n = len(nums)
        map = {}
        for num in nums:
            map[num] = map.get(num, 0) + 1
        
        
        for key in map:
            if map[key] >= n/2:
                return key
        