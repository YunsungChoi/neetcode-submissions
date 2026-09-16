class Solution:
    def partitionLabels(self, s: str) -> List[int]:

        dic = {}
        res = []
        count = 1
        
        for idx, char in enumerate(s):
            dic[char] = idx

        maxIdx = 0
        for idx, char in enumerate(s):
            maxIdx = max(dic[char], maxIdx)
            if idx == maxIdx:
                res.append(count)
                count = 0
            count += 1
        
        return res







    
        
        