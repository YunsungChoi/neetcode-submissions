class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        anagram_s = {}
        for char in s:
            anagram_s[char] = anagram_s.get(char, 0) + 1

        anagram_t= {}
        for char in t:
            anagram_t[char] = anagram_t.get(char, 0) + 1
            
        
        return anagram_s == anagram_t