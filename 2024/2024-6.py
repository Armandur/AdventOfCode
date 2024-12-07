import util
import datetime
import sys
from pprint import pprint
from blessed import Terminal
import os
import time
from enum import Enum

class Direction(Enum):
	north = (0, -1)
	#northeast = (1, -1)
	east = (1, 0)
	#southeast = (1, 1)
	south = (0, 1)
	#southwest = (1, -1)
	west = (-1, 0)
	#northwest = (-1, -1)
	

class Point:
	def __init__(self, x, y):
		self.x = x
		self.y = y

	def shift(self, direction):
		self.x += direction[0]
		self.y += direction[1]

	# x+ ->
	# y+
	# ||
	# \/

	def move(self, newX, newY):
		self.x = newX
		self.y = newY

	def __repr__(self):
		return f"({self.x}, {self.y})"
	
	def __eq__ (self, other):
		return (self.x, self.y) == (other.x, other.y)

class Entity:
	def __init__(self, point, character, color, blocking = True):
		self.position = point
		self.character = character
		self.color = color
		self.blocking = blocking

class Character(Entity):
	def __init__(self, point, character, color, direction):
		self.direction = direction
		self.directionPositions = list()
		self.positions = set()
		super().__init__(point, character, color)
	
	def turn(self, leftOrRight, degrees=90):
		directionList = list(Direction)
		index = directionList.index(self.direction)
		if leftOrRight == "left":
			if index == 0:
				self.direction = directionList[-1]
			else:
				self.direction = directionList[index-1]
		if leftOrRight == "right":
			if index == len(directionList)-1:
				self.direction = directionList[0]
			else:
				self.direction = directionList[index+1]
		if self.direction == Direction.north:
			self.character = "^"
		if self.direction == Direction.east:
			self.character = ">"
		if self.direction == Direction.south:
			self.character = "v"
		if self.direction == Direction.west:
			self.character = "<"

class Map:
	def __init__(self):
		self.map = []
		self.character = Character(Point(0, 0), "^", Terminal().red, Direction.north)
		self.obstacles = set()

	def height(self):
		return len(self.map)

	def width(self):
		return len(self.map[0])
	
	def isBlocked(self, point):
		if point.x >= 0 and point.y >= 0 and point.y < self.height() and point.x < self.width():
			return self.map[point.y][point.x].blocking

	def load(self, data):
		height = len(data)
		width = len(data[0])
		groundCharacter = " "
		term = Terminal()
		for y in range(height):
			row = [(Entity(Point(-1, -1), groundCharacter, Terminal().on_black, blocking=False))] * width
			self.map.append(row)

		obstacleCharacter = "#"
		guardCharacter = "^"
		obstacles = 0
		for y, line in enumerate(data):
			for x, character in enumerate(line):
				if character == obstacleCharacter:
					self.map[y][x] = Entity(Point(x, y), obstacleCharacter, Terminal().yellow)
					self.obstacles.add((x, y))
					obstacles += 1

				if character == guardCharacter:
					self.character.position.shift((x, y))
					self.character.directionPositions.append(((x, y), self.character.direction))
					self.character.positions.add((x, y))
		print(term.home + f"{obstacles} obstacles loaded")

	def saveMap(self):
		with open("2024/2024-6-save.txt", "w") as savefile:
			for y in range(self.height()):
				line = ""
				for x in range(self.width()):
					writePos = Point(x, y)
					if writePos == self.character.position:
						line += self.character.character
					else:
						c = self.map[y][x].character
						if writePos in self.character.directionPositions:
							c = "."
						line += c
				savefile.write(line+"\n")

puzzleMap = Map()

def refreshMap(term, windowSize=30):
		startX = max(0, puzzleMap.character.position.x - windowSize*2 // 2)
		startY = max(0, puzzleMap.character.position.y - windowSize // 2)
		endX = min(puzzleMap.width(), puzzleMap.character.position.x + windowSize*2 // 2)
		endY = min(puzzleMap.height(), puzzleMap.character.position.y + windowSize // 2)
		with term.hidden_cursor():
			printMap = []
			for y in range(startY, endY):
				line = ""
				for x in range(startX, endX):
					writePos = Point(x, y)
					if writePos == puzzleMap.character.position:
						line += puzzleMap.character.color + puzzleMap.character.character
					else:
						c = puzzleMap.map[y][x].color + puzzleMap.map[y][x].character
						if writePos in puzzleMap.character.positions:
							c = term.cyan + "."
						line += c
				printMap.append(line)
			for n, line in enumerate(printMap):
				print(term.move_xy(0, n) + line, end="")

def walkGuard(puzzleMap):
	newPos = (puzzleMap.character.position.x+puzzleMap.character.direction.value[0], puzzleMap.character.position.y+puzzleMap.character.direction.value[1])

	if (newPos[0] < 0 or newPos[0] >= puzzleMap.width()) or (newPos[1] < 0 or newPos[1] >= puzzleMap.height()):
		return "Exited!"
	
	if (newPos, puzzleMap.character.direction) in puzzleMap.character.directionPositions:
		return "Loopdeloop!"

	if not (newPos) in puzzleMap.obstacles:
		puzzleMap.character.position.move(newPos[0], newPos[1])
		if (newPos) not in puzzleMap.character.positions:
			puzzleMap.character.positions.add(newPos)
		if (newPos, puzzleMap.character.direction) not in puzzleMap.character.directionPositions:
			puzzleMap.character.directionPositions.append((newPos, puzzleMap.character.direction))
	else:
		puzzleMap.character.turn("right")
	return "Walking"

def part1(puzzleInput):
	term = Terminal()
	puzzleMap.load(puzzleInput)
	count = 0
	input()

	while True:
		status = walkGuard(puzzleMap)
		count = len(puzzleMap.character.positions)
		#if count > 5233:
		#if True:
		#	refreshMap(term, 15)
		
		if count % 100 == 0 or count > 5233:
		#if True:
			with term.hidden_cursor():
				print(term.move_xy(0, 31) + term.green + status)
				print(term.move_xy(0, 32) + term.green + str(puzzleMap.character.position))
				print(term.move_xy(0, 33) + term.green + str(count))
		if status == "Exited!" or status == "Loopdeloop!":
			break

	return count

#1753
def part2(puzzleInput):
	term = Terminal()
	originalRoute = list.copy(puzzleMap.character.directionPositions)
	count = 0
	index = 0

	placed = set()

	for point, _ in originalRoute:
		if point in placed:
			index += 1
			continue

		if index == 0:
			index += 1
			continue

		puzzleMap.character.positions.clear()
		puzzleMap.character.directionPositions.clear()
	
		puzzleMap.character.position.move(originalRoute[index-1][0][0], originalRoute[index-1][0][1])
		puzzleMap.character.direction = originalRoute[index-1][1]

		#puzzleMap.map[point[0]][point[1]] = Entity(point, "0", term.magenta)
		puzzleMap.obstacles.add(point)
		
		while True:
			#refreshMap(term, 15)
			status = walkGuard(puzzleMap)
			if status == "Loopdeloop!":
				count += 1
				print(term.move_xy(0, 38) + term.green + f"Loops: {count}")
				placed.add(point)
				puzzleMap.obstacles.remove(point)
				break
			if status == "Exited!":
				placed.add(point)
				puzzleMap.obstacles.remove(point)
				break
		index += 1
	return count


if __name__ == '__main__':
	os.system("mode 60,60")
	cookie = sys.argv[1]
	today = datetime.datetime.now()
	puzzleInput = util.getInput(today.year, today.day, cookie)
	test = []
	with open(f"{today.year}/test.txt", "r") as file:
		test = file.read().splitlines()

	print(f"Part one: {part1(puzzleInput)}")
	#print(util.postAnswer(today.year, today.day, 1, part1(puzzleInput), cookie))

	print(f"Part two: {part2(puzzleInput)}")
	#print(util.postAnswer(today.year, today.day, 2, part2(puzzleInput), cookie))