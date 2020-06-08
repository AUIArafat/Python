class TicTacToe:
	def __init__(self):
		self.turn = 'X'
		self.the_board = {
			'top-L': ' ',
			'top-M': ' ',
			'top-R': ' ',
			'mid-L': ' ',
			'mid-M': ' ',
			'mid-R': ' ',
			'low-L': ' ',
			'low-M': ' ',
			'low-R': ' ',
		}
		self.board_array = ['','top-L', 'top-M', 'top-R', 'mid-L', 'mid-M','mid-R','low-L', 'low-M', 'low-R' ]
	def print_board(self):
		print(self.the_board['top-L'] + " |" + self.the_board['top-M'] + " |" + self.the_board['top-R'])
		print("--+--+--")
		print(self.the_board['mid-L'] + " |" + self.the_board['mid-M'] + " |" + self.the_board['mid-R'])
		print("--+--+--")
		print(self.the_board['low-L'] + " |" + self.the_board['low-M'] + " |" + self.the_board['low-R'])

	def check_the_winner(self):
		if self.the_board['top-L'] != ' ' and self.the_board['top-L'] == self.the_board['top-M'] and \
				self.the_board['top-M'] == self.the_board['top-R']:
			return True
		if self.the_board['top-L'] != ' ' and self.the_board['top-L'] == self.the_board['mid-M'] and \
				self.the_board['mid-M'] == self.the_board['low-R']:
			return True
		if self.the_board['top-R'] != ' ' and self.the_board['top-R'] == self.the_board['mid-R'] and \
				self.the_board['mid-R'] == self.the_board['low-R']:
			return True
		if self.the_board['mid-L'] != ' ' and self.the_board['mid-L'] == self.the_board['mid-M'] and \
				self.the_board['mid-M'] == self.the_board['mid-R']:
			return True
		if self.the_board['low-L'] != ' ' and self.the_board['low-L'] == self.the_board['low-M'] and \
				self.the_board['low-M'] == self.the_board['low-R']:
			return True
		if self.the_board['low-L'] != ' ' and self.the_board['low-L'] == self.the_board['mid-M'] and \
				self.the_board['mid-M'] == self.the_board['top-R']:
			return True
		if self.the_board['low-L'] != ' ' and self.the_board['low-L'] == self.the_board['mid-L'] and \
				self.the_board['mid-L'] == self.the_board['top-L']:
			return True

	def start_the_game(self):
		for i in range(9):
			print("Now turn for " + self.turn)
			print(
				"Please enter a value (1-9) where you want to turn")
			try:
				choice = input()
				move = self.board_array[int(choice)]
				if self.the_board[move] == ' ':
					self.the_board[move] = self.turn
				else:
					print('You have entered invalid value or entered a value which already placed')
			except ValueError as e:
				print(e)
			self.print_board()

			if self.check_the_winner():
				print("The winner is " + self.turn)
				return

			if self.turn == 'X':
				self.turn = 'O'
			else:
				self.turn = 'X'
		print("The game is drawn")


if __name__ == '__main__':
	TicTacToeOb = TicTacToe()
	TicTacToeOb.print_board()
	TicTacToeOb.start_the_game()
