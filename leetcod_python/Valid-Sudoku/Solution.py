class Solution:
    # @param board, a 9x9 2D array
    # @return a boolean
    def isValidSudoku(self, board):
        for i in xrange(9):
            d = set()
            for j in xrange(9):
                if board[i][j] != '.' and board[i][j] in d:
                    return False
                elif board[i][j] != '.':
                    d.add(board[i][j])
        for i in xrange(9):
            d = set()
            for j in xrange(9):
                if board[j][i] != '.' and board[j][i] in d:
                    return False
                elif board[j][i] != '.':
                    d.add(board[j][i])
        for m in xrange(0, 9, 3):
            for n in xrange(0, 9, 3):
                d = set()
                for i in xrange(m, m + 3):
                    for j in xrange(n, n + 3):
                        if board[i][j] != '.' and board[i][j] in d:
                            return False
                        elif board[i][j] != '.':
                            d.add(board[i][j])
        return True
