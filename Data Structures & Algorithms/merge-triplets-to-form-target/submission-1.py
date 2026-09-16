class Solution:
    def mergeTriplets(self, triplets: List[List[int]], target: List[int]) -> bool:

        found = set()
        for a, b, c in triplets:
            if a > target[0] or b > target[1] or c > target[2]:
                continue
            for idx, val in enumerate((a, b, c)):
                if val == target[idx]:
                    found.add(idx)
            
        return len(found) == 3

            
             



        