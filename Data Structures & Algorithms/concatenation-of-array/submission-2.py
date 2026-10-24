class Solution:
    def getConcatenation(self, nums: List[int]) -> List[int]:
        n = len(nums)
        res = [0] * (2 * n)
        for ind, num in enumerate(nums):
            res[ind] = res[ind + n] = num
        
        return res
        

        