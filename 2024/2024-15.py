import util
import datetime
import sys
from pprint import pprint
from blessed import Terminal
import time

Direction = {
	'^' : (0, -1),
	#northeast = (1, -1)
	'>' : (1, 0),
	#southeast = (1, 1)
	'v' : (0, 1),
	#southwest = (1, -1)
	'<' : (-1, 0)
	#northwest = (-1, -1)
}

def addTuple(a:tuple, b:tuple) -> tuple:
	return (a[0]+b[0], a[1]+b[1])

class Entity:
	def __init__(self, point: tuple, character: str, color: util.colors, blocking = False):
		self.position = point
		self.character = character
		self.color = color
		self.blocking = blocking

	def move(self, point : tuple):
		self.position = point

	def shift(self, delta : tuple):
		self.position = addTuple(self.position, delta)

class Lanternfish(Entity):
	def __init__(self, point: tuple, character: str, color: util.colors):
		self.position = point
		self.character = character
		self.color = color
		self.movements = list()
		self.positions = set()
		super().__init__(point, character, color)
	
	def loadMovements(self, data):
		self.movements = data

class Map:
	def __init__(self):
		self.map = []
		self.lanternFish = Lanternfish((0, 0), "@", Terminal().yellow)
		self.obstacles = set()
		self.walls = set()

	def height(self):
		return len(self.map)

	def width(self):
		return len(self.map[0])
	
	def __onMap(self,  point):
		return point[0] >= 0 and point[1] >= 0 and point[1] < self.height() and point[0] < self.width()
	
	def isBlocked(self, point):
		if self.__onMap(point):
			return self.map[point.y][point.x].blocking
		else:
			return None

	def load(self, data):
		height = len(data)
		width = len(data[0])
		groundCharacter = " "
		term = Terminal()
		for y in range(height):
			row = [(Entity((-1, -1), groundCharacter, Terminal().on_black, blocking=False))] * width
			self.map.append(row)

		boxCharacter = "O"
		wallCharacter = "#"
		fishCharacter = "@"
		boxes = 0
		walls = 0
		for y, line in enumerate(data):
			for x, character in enumerate(line):
				if character == boxCharacter:
					self.map[y][x] = Entity((x, y), boxCharacter, Terminal().red)
					boxes += 1

				if character == wallCharacter:
					self.map[y][x] = Entity((x, y), wallCharacter, Terminal().green, blocking=True)
					self.walls.add((x, y))
					walls += 1

				if character == fishCharacter:
					self.lanternFish.move((x, y))

		print(term.home + f"{boxes} boxes loaded. {walls} walls loaded.")

	def print(self, term, windowSize=30):
		startX = max(0, self.lanternFish.position[0] - windowSize*2 // 2)
		startY = max(0, self.lanternFish.position[1] - windowSize // 2)
		endX = min(self.width(), self.lanternFish.position[0] + windowSize*2 // 2)
		endY = min(self.height(), self.lanternFish.position[1] + windowSize // 2)

		with term.hidden_cursor():
			printMap = []
			for y in range(startY, endY):
				line = ""
				for x in range(startX, endX):
					writePos = (x, y)
					if writePos == self.lanternFish.position:
						line += self.lanternFish.color + self.lanternFish.character + " "
					else:
						c = self.map[y][x].color + self.map[y][x].character
						if writePos in self.lanternFish.positions:
							c = term.cyan + "."
						line += c + " "
				printMap.append(line)
			for n, line in enumerate(printMap):
				print(term.move_xy(0, n) + line, end="")

			nextMove = ""
			if self.lanternFish.movements:
				nextMove = self.lanternFish.movements[0]
			print(term.white + term.move_xy(0, len(printMap)+2) + f"Next Lanternfish move "+ term.yellow + f"{nextMove}" + term.white + f" , {len(self.lanternFish.movements)} left" , end="")
			print()

	def moveLanternfish(self):
		movement = self.lanternFish.movements.pop(0)
		newX, newY = addTuple(self.lanternFish.position, Direction[movement])
		if self.__onMap((newX, newY)):

			if not self.map[newY][newX].blocking:
				if self.map[newY][newX].character != "O":
					self.lanternFish.move((newX, newY))

				if self.map[newY][newX].character == "O":
					boxes = [(newX, newY)]
					newPosition = addTuple((newX, newY), Direction[movement])
					while self.map[newPosition[1]][newPosition[0]].character == "O":
						boxes.append(newPosition)
						newPosition = addTuple(newPosition, Direction[movement])
					
					if self.map[newPosition[1]][newPosition[0]].blocking == False:
						newBoxPositions = [addTuple(x, Direction[movement]) for x in boxes]
						for i, box in enumerate(boxes):
							self.map[newBoxPositions[i][1]][newBoxPositions[i][0]] = self.map[box[1]][box[0]]
							self.map[newBoxPositions[i][1]][newBoxPositions[i][0]].move(newBoxPositions[i])
						self.map[newY][newX] = Entity((-1, -1), " ", Terminal().on_black, blocking=False)
						self.lanternFish.move((newX, newY))
	def getBoxes(self):
		boxes = set()
		for y in range(self.height()):
			for x in range(self.width()):
				if self.map[y][x].character == "O":
					boxes.add((x, 100*y))
		return boxes



def part1(puzzleInput):
	count = 0
	warehouseData = puzzleInput[:puzzleInput.index("")]
	movementData = puzzleInput[puzzleInput.index("")+1:]

	warehouseMap = Map()
	warehouseMap.load(warehouseData)
	warehouseMap.lanternFish.loadMovements(list("".join(movementData)))
	term = Terminal()
	warehouseMap.print(term)

	while warehouseMap.lanternFish.movements:
		warehouseMap.moveLanternfish()
		warehouseMap.print(term)
	
	for box in warehouseMap.getBoxes():
		count += (box[1]+box[0])

	return count


def part2(puzzleInput):
	count = 0
	
	return count


if __name__ == '__main__':
	cookie = sys.argv[1]
	today = datetime.datetime.now()
	puzzleInput = util.getInput(today.year, 15, cookie)
	test = []
	with open(f"{today.year}/test.txt", "r") as file:
		test = file.read().splitlines()

	print(f"Part one: {part1(puzzleInput)}")
	#print(util.postAnswer(today.year, 15, 1, part1(puzzleInput), cookie))

	print(f"Part two: {part2(puzzleInput)}")
	#print(util.postAnswer(today.year, 15, 2, part2(puzzleInput), cookie))