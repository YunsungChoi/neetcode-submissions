class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        phone = {
            "2": "abc",
            "3": "def",
            "4": "ghi",
            "5": "jkl",
            "6": "mno",
            "7": "pqrs",
            "8": "tuv",
            "9": "wxyz"    
        }

        if len(digits) < 1:
            return []
        
        res = []
        path = []

        def dfs(i):
            if len(path) == len(digits):
                res.append("".join(path))
                return
            for ch in phone[digits[i]]:
                path.append(ch)
                dfs(i+1)
                path.pop()
        
        dfs(0)
        return res
