class Solution:
    def longestPalindrome(self, s: str) -> str:
        resIdx, resLen = 0, 0
        n = len(s)

        def expand(l, r):
            while l >= 0 and r < len(s) and s[l] ==s[r]:
                l -= 1
                r += 1
            return s[l+1:r] 
                
        res = ""
        for i in range(n):
            for cand in (expand(i, i), expand(i, i+1)):
                if len(cand) > len(res):
                    res = cand

        return res
        