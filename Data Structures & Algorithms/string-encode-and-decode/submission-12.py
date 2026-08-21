class Solution:

    def encode(self, strs: List[str]) -> str:
        encodedS = ""
        for s in strs:
            encodedS += s + 'Q'

        return encodedS

    def decode(self, s: str) -> List[str]:
        res = []
        word = ""

        for char in s:
            if (char == 'Q'):
                res.append(word)
                word = ""
            else:
                word += char
        
        return res
