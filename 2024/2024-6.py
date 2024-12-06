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
		self.positions = []
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
		self.entities = []
		self.character = Character(Point(0, 0), "^", Terminal().red, Direction.north)

	def height(self):
		return len(self.map)

	def width(self):
		return len(self.map[0])
	
	def isBlocked(self, point):
		for entity in self.entities:
			if entity.position == point and entity.blocking:
				return True
		return False

	def load(self, data):
		height = len(data)
		width = len(data[0])
		groundCharacter = " "

		term = Terminal()

		for y in range(height):
			print(term.home + term.clear + f"Loading row {y}")
			row = [(Entity(Point(-1, -1), groundCharacter, Terminal().on_black, blocking=False))] * width
			self.map.append(row)

		obstacleCharacter = "#"
		guardCharacter = "^"
		for y, line in enumerate(data):
			print(term.home + term.clear + f"Loading entites, {len(self.entities)} loaded")
			for x, character in enumerate(line):
				if character == obstacleCharacter:
					self.entities.append(Entity(Point(x, y), obstacleCharacter, Terminal().yellow))
				if character == guardCharacter:
					self.character.position.shift((x, y))

	def saveMap(self):
		with open("2024-6-save.txt", "w") as savefile:
			for y in range(self.height()):
				line = ""
				for x in range(self.width()):
					writePos = Point(x, y)
					if writePos == self.character.position:
						line += self.character.character
					else:
						c = self.map[y][x].character
						if writePos in self.character.positions:
							c = "."
						for entity in self.entities:
							if entity.position == writePos:
								c = entity.character
						line += c
				savefile.write(line+"\n")

def part1(puzzleInput):
	input()
	count = 0

	puzzleMap = Map()
	puzzleMap.load(puzzleInput)

	os.system("mode 60,60")
	term = Terminal()

	def refreshMap(windowSize=30):
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
						for entity in puzzleMap.entities:
							if entity.position == writePos:
								c = entity.color + entity.character
						line += c
				printMap.append(line)
			for n, line in enumerate(printMap):
				print(term.move_xy(0, n) + line, end="")

	puzzleMap.character.positions.append(Point(puzzleMap.character.position.x, puzzleMap.character.position.y))
	while True:
		newPos = Point(puzzleMap.character.position.x, puzzleMap.character.position.y)
		newPos.shift(puzzleMap.character.direction.value)
		if (newPos.x < 0 or newPos.x > puzzleMap.width()) or (newPos.y < 0 or newPos.y > puzzleMap.height()):
			break

		if not puzzleMap.isBlocked(newPos):
			puzzleMap.character.position.move(newPos.x, newPos.y)
			if newPos not in puzzleMap.character.positions:
				puzzleMap.character.positions.append(newPos)
		else:
			puzzleMap.character.turn("right")

		count = len(puzzleMap.character.positions)
		
		if count > 5220:
			refreshMap(30)
			
		with term.hidden_cursor():
			print(term.move_xy(0, 31) + term.green + str(puzzleMap.character.position))
			print(term.move_xy(0, 32) + term.green + str(count-1))
		#time.sleep(0.05)
	#puzzleMap.saveMap()

	return count-1


def part2(puzzleInput):
	count = 0
	
	return count


if __name__ == '__main__':
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