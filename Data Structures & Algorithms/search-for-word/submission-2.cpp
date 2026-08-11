class Solution {
private:
    vector<vector<int>> visit;

    bool helper(vector<vector<char>>& board, string word, int row, int col, int id) {
        if (id == word.size()) {
            return true;
        }

        if (row == -1 || col == -1 || row == board.size() || col == board[0].size() || board[row][col] != word[id] || visit[row][col] == 1) {
            return false;
        }

        visit[row][col] = 1;
        bool res = helper(board, word, row - 1, col, id + 1) || helper(board, word, row + 1, col, id + 1) || helper(board, word, row, col - 1, id + 1) || helper(board, word, row, col + 1, id + 1);
        visit[row][col] = 0;

        return res;
    }

public:
    bool exist(vector<vector<char>>& board, string word) {
        visit = vector<vector<int>>(board.size(), vector<int>(board[0].size(), 0));
        
        for (int r = 0; r < board.size(); r++) {
            for (int c = 0; c < board[0].size(); c++) {
                if (helper(board, word, r, c, 0)) {
                    return true;
                }
            }
        }

        return false;
    }
};
