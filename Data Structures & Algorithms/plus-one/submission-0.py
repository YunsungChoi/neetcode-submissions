class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:

        val = "".join(str(x) for x in digits)
        result = int(val) + 1
        res = []

        for char in str(result):
            res.append(char)

        return res

        