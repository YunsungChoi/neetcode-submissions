class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        # 1. find entry point (row, col) -- just start at (0, 0)
        # 2. if found, check up, down, left and right for the next index
        # 3. if correct, do it again from that row, col for 2 for the next character of the word (index)
        # 4. if all wrong, return false, if right then 3

        dirs = [(1, 0),(-1, 0),(0, 1),(0, -1)]
        visited = set()

        def backTrack(row, col, index):
            if index == len(word):
                return True #성공
            if row < 0 or row >= len(board) or col < 0 or col >= len(board[0]):
                return False # 바운더리 바깥
            if (row, col) in visited or board[row][col] != word[index]:
                return False #이미 방문했거나 
            
            visited.add((row, col))
            for dr, dc in dirs:
                if backTrack(row + dr, col + dc, index +1):
                    return True
            visited.remove((row, col))
            return False
        
        for r in range(len(board)):
            for c in range(len(board[0])):
                if backTrack(r, c, 0):
                    return True
        return False




        