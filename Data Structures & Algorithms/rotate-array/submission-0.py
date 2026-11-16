class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        d = deque(nums)
        for i in range(k):
            tmp = d.pop()
            d.appendleft(tmp)

        nums[:] = d