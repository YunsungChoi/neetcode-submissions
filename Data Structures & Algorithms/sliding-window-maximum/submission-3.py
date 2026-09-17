class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        
        heap = []
        res = []

        for idx, num in enumerate(nums):
            heapq.heappush(heap, (-num, idx))
            if idx >= k-1:
                while heap[0][1] <= idx-k:
                    heapq.heappop(heap)
                res.append(-heap[0][0])
        return res


           


            


        