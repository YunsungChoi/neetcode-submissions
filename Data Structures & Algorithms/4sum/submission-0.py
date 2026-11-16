class Solution:
    def fourSum(self, nums: List[int], target: int) -> List[List[int]]:
        # 3sum + 1 extra for loop. then 4,5,6,7sum requires 4, 5,6, 7 loops
        # recursion!

        nums.sort()
        res, quad = [], []
        def kSum(k, start, target):
            if k != 2: #non-base case
                for i in range(start, len(nums) - k + 1): # at least k values for other loops
                    if i > start and nums[i] == nums[i-1]:
                        continue
                    quad.append(nums[i])
                    kSum(k-1, i+1, target - nums[i])
                    quad.pop()
                return

            #base case, two sum II
            l, r, = start, len(nums) - 1
            while l < r: #같으면 같은value를 보고있는걸테니까.
                if nums[l] + nums[r] < target:
                    l += 1
                elif nums[l] + nums[r] > target:
                    r -= 1
                else:
                    #found!
                    res.append(quad + [nums[l], nums[r]])
                    l += 1
                    while l < r and nums[l] == nums[l -1]:
                        l += 1

        kSum(4, 0, target)
        return res
