class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        # i, j = 0, 0 
        # res = []
        # while i < len(word1) and j < len(word2):
        #     res.append(word1[i])
        #     res.append(word2[j])
        #     i += 1
        #     j += 1
        # res.append(word1[i:])
        # res.append(word2[j:])
        # return "".join(res)

        n, m = len(word1), len(word2)
        res = []

        for i in range(max(n, m)):
            if i < n:
                res.append(word1[i])
            if i < m:
                res.append(word2[i])
        return "".join(res)
        