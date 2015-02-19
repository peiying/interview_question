class Solution:
    # @param board, a list of lists of 1 length string
    # @param word, a string
    # @return a boolean
    def exist(self, board, word):
       for i in range(len(board)):
           for j in range(len(board[0])):
               if board[i][j] == word[0]:
                   if self.helper(board, word[1:], i, j):
                       return True
       return False
    def helper(self, board, word, i, j):
        if len(word) == 0:
            return True
        if i - 1 >= 0 and board[i - 1][j] == word[0]:
            c = board[i][j]
            board[i][j] = '#'
            if self.helper(board, word[1:], i - 1, j):
                return True
            board[i][j] = c
        if j + 1 < len(board[0]) and board[i][j + 1] == word[0]:
            c = board[i][j]
            board[i][j] = '#'
            if self.helper(board, word[1:], i, j + 1):
                return True
            board[i][j] = c
        if i + 1 < len(board) and board[i + 1][j] == word[0]:
            c = board[i][j]
            board[i][j] = '#'
            if self.helper(board, word[1:], i + 1, j):
                return True
            board[i][j] = c
        if j - 1 >= 0 and board[i][j - 1] == word[0]:
            c = board[i][j]
            board[i][j] = '#'
            if self.helper(board, word[1:], i, j - 1):
                return True
            board[i][j] = c
        return False
            
        
        
