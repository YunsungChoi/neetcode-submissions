class Solution:
    def minWindow(self, s: str, t: str) -> str:
        if len(t) > len(s):
            return ""

    
        countT = Counter(t)
        need = len(countT)
        have = 0
        dic = defaultdict(int)
        res, resLen = [-1,-1], float("inf")
        l = 0

        for idx, char in enumerate(s):
            dic[char] = 1 + dic.get(char, 0)
            if char in countT and dic[char] == countT[char]:
                have += 1
            while have == need:
                if (idx - l + 1) < resLen:
                    res = [l, idx+1]
                    resLen = idx - l + 1

                dic[s[l]] -= 1
                if s[l] in countT and dic[s[l]] < countT[s[l]]:
                    have -= 1
                l += 1
        l, r = res
        return s[l: r] if resLen != float("inf") else ""



        