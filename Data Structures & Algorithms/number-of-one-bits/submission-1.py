class Solution:
    def hammingWeight(self, n: int) -> int:
        count = 0
        num = str(bin(n))
        for n in num:
            if n == "1":
                count += 1
        return count