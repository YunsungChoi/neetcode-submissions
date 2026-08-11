class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        heap = [(x*x + y*y, x, y) for x, y in points] # based on origin(0,0) therefore x*x and y*y
        heapq.heapify(heap)

        res = []
        for _ in range(k):
            dist, x, y = heapq.heappop(heap)
            res.append([x, y])
        
        return res


        