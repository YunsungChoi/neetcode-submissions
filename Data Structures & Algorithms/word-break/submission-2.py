class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        
        memo = {}
        def findWord(i):
            if i == len(s): return True
            if i in memo: return memo[i]
            for w in wordDict:
                if s[i: i + len(w)] == w:
                    if findWord(i + len(w)):
                        memo[i] = True
                        return True
            memo[i] = False
            return False
        
        return findWord(0)



        
        