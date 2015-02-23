#need convert str to list
#lc not AC
class Solution:
    # @param board, a 9x9 2D array
    # Solve the Sudoku by modifying the input board in-place.
    # Do not return any value.
    def solveSudoku(self, board):
        for i in xrange(9):
	        board[i] = list(board[i])
        res = []
        for i in xrange(9):
            for j in xrange(9):
                if board[i][j] == '.':
                    res.append(i * 9 + j)
        
        self.helper(board, res, 0)
        for i in range(9):
            board[i]=''.join(board[i])
    def helper(self, board, res,idx):
        if len(res) == idx:
            return True
        x = res[idx] / 9
        y = res[idx] % 9
        print idx
        for j in '123456789':
            if self.isValid(j,board, x, y):
                board[x][y] = str(j)
                if self.helper(board, res, idx + 1):
                    return True
            board[x][y] = '.'
        return False
    def isValid(self,j,board,x,y):
    	tmp = str(j)
        for i in range(9):
        	if board[i][y]==tmp: return False
        for i in range(9):
            if board[x][i]==tmp: return False
        for i in range(3):
            for j in range(3):
            	if board[(x/3)*3+i][(y/3)*3+j]==tmp: return False
        return True
                    
        
