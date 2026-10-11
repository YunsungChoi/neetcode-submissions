class Solution:
    def isHappy(self, n: int) -> bool:
        visited = set()

        while n not in visited:
            visited.add(n)
            n = self.sumOfSquares(n)
            if n == 1: return True
        return False

    def sumOfSquares(self, n):
        output = 0
        while n:
            digit = n % 10 #1의자리 먼저 계산시작
            digit = digit ** 2
            output += digit #1의자리 제곱 계산후 저장 
            n = n // 10 #1의자리 제외 나머지 n에 업데이트
        return output
        