import util
import os

def boldString(string):
	start = "\033[92m"
	end = "\033[0m"
	return f"{start}{string}{end}"

def clearConsole():
    command = 'clear'
    if os.name in ('nt', 'dos'):  # If Machine is running on Windows, use cls
        command = 'cls'
    os.system(command)


class Tile:
	def __init__(self, value):
		self.value = int(value)
		self.marked = False

	def __str__(self):
		string = ""
		if self.value < 10:
			string += " "

		string += str(self.value)

		if self.marked:
			return boldString(string)
		else:
			return string


class Board:
	def __init__(self):
		self.tiles = []

	# tiles[row][column]

	def markTiles(self, value):
		for row in self.tiles:
			for tile in row:
				if tile.value == value:
					tile.marked = True

	def checkRow(self, row):  # Check all the tiles in a row if they're marked
		count = 0
		for tile in self.tiles[row]:
			if tile.marked:
				count += 1
		if count == 5:
			return True
		return False

	def checkColumn(self, column):
		count = 0
		for row in self.tiles:
			if row[column].marked:
				count += 1
		if count == 5:
			return True
		return False

	def isBingo(self):
		for i in range(0, len(self.tiles)):
			for j in range(0, len(self.tiles[i])):
				if self.tiles[i][j].marked:
					if self.checkRow(i):
						return True
					if self.checkColumn(j):
						return True
		return False

	def sumUnmarked(self):
		sum = 0
		for row in self.tiles:
			for tile in row:
				if not tile.marked:
					sum += tile.value
		return sum

	def __str__(self):
		string = ""
		for row in self.tiles:
			for tile in row:
				string += str(tile)
				string += " "
			string += "\n"
		return string


def part1(input):
	numbers = []
	boards = []
	count = 0

	#Get the numbers to call
	numbers = input[0].split(",")
	numbers = list(map(int, numbers))
	input = input[2:] #Slice off the first number row for the bingo numbers

	tempBoard = Board()
	tempRow = []

	#Start of reading and creating the bingo-boards
	for line in input:
		for value in line.split():
			tempRow.append(Tile(value))

		if tempRow != []:
			tempBoard.tiles.append(tempRow.copy())
			tempRow = []

		if line == "" or line == input[-1]:
			boards.append(tempBoard)
			tempBoard=Board()

	#Start of the game
	for round, number in enumerate(numbers):
		clearConsole()
		for i, board in enumerate(boards):
			print(f"Round {round} - Number is: {number}!")
			print (f"Board #{i}")
			board.markTiles(number)
			print(board)

			if board.isBingo():
				count = board.sumUnmarked() * number
				print(f"Round {round} - Board #{i}\nB I N G O")
				print(count)
				unmarked = []
				for row in board.tiles:
					for tile in row:
						if not tile.marked:
							unmarked.append(tile.value)

				print(f"{'+'.join(list(map(str,unmarked)))}={sum(unmarked)}, {sum(unmarked)}*{number}={sum(unmarked)*number}")

				return count

	return count

def part2(input):
	numbers = []
	boards = []
	count = 0

	#Get the numbers to call
	numbers = input[0].split(",")
	numbers = list(map(int, numbers))
	input = input[2:] #Slice off the first number row for the bingo numbers

	tempBoard = Board()
	tempRow = []

	#Start of reading and creating the bingo-boards
	for line in input:
		for value in line.split():
			tempRow.append(Tile(value))

		if tempRow != []:
			tempBoard.tiles.append(tempRow.copy())
			tempRow = []

		if line == "" or line == input[-1]:
			boards.append(tempBoard)
			tempBoard=Board()

	#Start of the game

	originalBoards = boards.copy() #Copy the original boards just to check what index the last winning board has later
	bingoBoards = []
	for round, number in enumerate(numbers):
		clearConsole()
		for board in boards:
			board.markTiles(number)
			if board.isBingo():
				bingoBoards.append((board, number)) #make it a tuple with the number to be able to calculate the score

		for board in bingoBoards:
			if boards.count(board[0]) == 1: #Check if we haven't removed the board already
				boards.remove(board[0])

	count = bingoBoards[-1][0].sumUnmarked() * bingoBoards[-1][1]
	print(f"Last board to win is Board #{originalBoards.index(bingoBoards[-1][0])} with a score of {count}")
	return count

if __name__ == '__main__':
	test = []

	with open("test.txt", "r") as file:
		test = file.read().splitlines()

	#print(f"Part one: {part1(util.getInput(2021, 4))}")
	#print(f"Part one: {part1(test)}")

	#print(util.postAnswer(2021, 4, 1, part1()))

	print(f"Part two: {part2(util.getInput(2021, 4))}")
	#print(util.postAnswer(2021, 4, 2, part2(util.getInput(2021, 4))))