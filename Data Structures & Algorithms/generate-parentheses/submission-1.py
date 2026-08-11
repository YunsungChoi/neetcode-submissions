class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        # only open '(' if open < n
        # only add ')' if closed < open
        #valid when open == close == n
        res = []
        path = []
        def backtrack(open, close):
            #base case
            if open == close == n:
                res.append("".join(path))
                return
            if open < n:
                path.append('(')
                backtrack(open + 1, close)
                path.pop()

            if close < open:
                path.append(')')
                backtrack(open, close +1)
                path.pop()
        backtrack(0, 0)
        return res
                
                

