T = 'Help'

import pickle

class TicTacToe:

	def __init__(self, size = 3):

		self.board = [[0 for j in range(size)] for i in range(size)]
		self.size = size
		#-1 is player 1's turn
		#1 is player 2's turn
		self.turn = -1
		self.winner = 0


	#Return false if space is taken, or invalid coord is given
	def setPiece(self, coord):
		x,y = coord
		if(not self.isValid(coord) or self.board[x][y] != 0):
			return False
		self.board[x][y] = self.turn
		self.turn *= -1
		return True

	def isValid(self, coord):
		x,y = coord
		return 0<=x<self.size and 0<=y<self.size


	#encode the game board (change -1 to X and ...) and winner
	def export(self):
		data = pickle.dumps(self.board)
		return data

	def updateBoard(self, data):
		results = pickle.loads(data)
		self.board = results


	def __str__(self):
		s = ''
		for i in range(self.size):
			for j in range(self.size):
				if self.board[i][j] == 1:
					s+='X'
				elif self.board[i][j] == -1:
					s+='O'
				else:
					s+='-'
			s+='\n'
		return s

	#return winner
	#if no winner, return 0
	def checkWinner(self):
		horizontal, vertical = True, True
		h_prev, v_prev = 0, 0
		d_prev, diagonal = 0, True
		rd_prev, rev_diagonal = 0, True

		self.winner = 0
		for i in range(self.size):
			h_prev = self.board[0][i]
			v_prev = self.board[i][0]
			for j in range(self.size):
				if horizontal and h_prev == self.board[i][j]:
					h_prev = self.board[i][j]

				else:
					horizontal = False
				if vertical and v_prev == self.board[j][i]:
					v_prev = self.board[j][i]
				else:
					vertical = False
			#check winner
			if vertical or horizontal:
				self.winner = self.turn * -1 #bc set piece changes turn
				break
			horizontal, vertical = True, True

		#check diagonals
		d_prev = self.board[0][0]
		rd_prev = self.board[self.size-1][0]
		for i in range(self.size):
			if diagonal and d_prev == self.board[i][i]:
				d_prev = self.board[i][i]
			else:
				diagonal = False
			if rev_diagonal and rd_prev == self.board[self.size-1-i][i]:
				rd_prev = self.board[self.size-1-i][i]
			else:
				rev_diagonal = False
		if diagonal or rev_diagonal:
			self.winner = self.turn * -1 #bc set piece changes turn

		#TODO: check draw

		return self.winner 


if __name__ == "__main__":
	g = TicTacToe()
	'''
	g.setPiece((0,0))
	g.setPiece((1,1))
	g.setPiece((1,0))
	g.setPiece((1,2))
	g.setPiece((2,0))
	'''
	g.setPiece((1,1))
	g.setPiece((0,0))
	g.setPiece((1,2))
	g.setPiece((1,0))
	g.setPiece((2,1))
	g.setPiece((2,0))
	
	'''
	g.setPiece((0,0))
	g.setPiece((1,0))
	g.setPiece((1,1))
	g.setPiece((2,0))
	g.setPiece((2,2))
	
	g.setPiece((2,0))
	g.setPiece((1,0))
	g.setPiece((1,1))
	g.setPiece((2,1))
	g.setPiece((0,2))
	'''
	c = g.checkWinner()
	print(g)
	