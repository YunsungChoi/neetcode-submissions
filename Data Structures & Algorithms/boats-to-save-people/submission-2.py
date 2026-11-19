class Solution:
    def numRescueBoats(self, people: List[int], limit: int) -> int:
        people.sort()
        res = 0
        l = 0
        r = len(people) - 1

        while l <= r: # 조건문 확인! at most 2 people in one boat at the same time.
            remain = limit - people[r]
            r -= 1
            res += 1
            if l <= r and remain >= people[l]:
                l += 1
        return res
        