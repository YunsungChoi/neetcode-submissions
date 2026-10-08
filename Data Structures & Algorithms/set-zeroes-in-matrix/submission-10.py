class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:

        zeroes = []
        for row in range(0, len(matrix)):
            for col in range(0, len(matrix[0])):
                if matrix[row][col] == 0:
                    zeroes.append((row, col))
        
        for r, c in zeroes:
            for i in range(0, len(matrix)):
                matrix[i][c] = 0
            for j in range(0, len(matrix[0])):
                matrix[r][j] = 0
                
                
                
        
        