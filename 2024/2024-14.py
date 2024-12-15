import util
import datetime
import sys
from pprint import pprint
import random
import string
from math import prod

colors = {}

def randomizeColors() -> dict:
	global colors
	for character in string.ascii_uppercase + string.ascii_lowercase:
		colors.update({character : random.choice(util.colors.colors + util.colors.brightColors)})
	return colors

def printMap(bathroomMap : tuple, robots : list):
	for y in range(bathroomMap[1]):
		lineString = ""
		for x in range(bathroomMap[0]):
			robotSymbol = ""
			robotCount = 0
			for robot in robots:
				if (x, y) == robot.position:
					if robotSymbol == "":
						robotSymbol = util.colorString(str(robot), colors[str(robot)])
						robotCount += 1
					else:
						robotCount += 1
			if robotCount == 1:
				lineString += robotSymbol + " "
			if robotCount > 1:
				lineString += util.colorString(str(robotCount), util.colors.redbg) + " "
			if robotCount == 0:
				#lineString += "· "
				lineString += "  "
		print(lineString)

def addTuple(a:tuple, b:tuple) -> tuple:
	return (a[0]+b[0], a[1]+b[1])

class Robot:
	def __init__(self, symbol, position : tuple, velocity : tuple, mapSize=(11, 7)):
		self.position = position
		self.symbol = symbol
		self.position = position
		self.velocity = velocity
		self.mapSize = mapSize

	def move(self):
		self.position = addTuple(self.position, self.velocity)
		if self.position[0] < 0:
			newX = self.mapSize[0] + self.position[0]
			self.position = (newX, self.position[1])
		if self.position[1] < 0:
			newY = self.mapSize[1] + self.position[1]
			self.position = (self.position[0], newY)
		
		if self.position[0] >= self.mapSize[0]:
			newX = self.position[0] - self.mapSize[0]
			self.position = (newX, self.position[1])

		if self.position[1] >= self.mapSize[1]: 
			newY = self.position[1] - self.mapSize[1]
			self.position = (self.position[0], newY)

	def __str__(self):
		return str(self.symbol)
	
	def __repr__(self):
		return self.__str__()
	
def getQuadrant(position, mapSize):
	
	halfX = mapSize[0] // 2
	halfY = mapSize[1] // 2

	x, y = position

	topBottom = None
	leftRight = None
	if y < halfY:
		topBottom = 0
	elif y > halfY:
		topBottom = 1
	
	if x < halfX:
		leftRight = 0
	elif x > halfX:
		leftRight = 1

	if topBottom is None or leftRight is None:
		return None
	
	return (topBottom, leftRight)




def part1(puzzleInput, mapSize):
	count = 0
	robots = list()
	randomizeColors()

	for line in puzzleInput:
		position, velocity = line.split(" ")

		position = position[2:]
		velocity = velocity[2:]

		posX, posY = [int(x) for x in position.split(",")]
		velX, velY = [int(x) for x in velocity.split(",")]

		position = (posX, posY)
		velocity = (velX, velY)

		robots.append(Robot(random.choice(string.ascii_lowercase + string.ascii_uppercase), position, velocity, mapSize))
	

	#pprint(robots)
	#print("Initial state")
	#printMap(mapSize, robots)
	#print()
	counter1 = 0
	counter2 = 0
	for i in range(20000):
		if i >= 31:
			counter1 += 1

		if i >= 68:
			counter2 +=1

		for robot in robots:
			robot.move()
			
			if robot == robots[-1]:
				if counter1 == 103 or counter2 == 101:
					print(f"{i+1} seconds")
					printMap(mapSize, robots)
					print()
					if counter1 == 103:
						counter1 = 0
					if counter2 == 101:
						counter2 = 0

	robotsInQuadrants = {
		(0, 0) : 0,
		(1, 0) : 0,
		(0, 1) : 0,
		(1, 1) : 0
	}

	for robot in robots:
		quadrant = getQuadrant(robot.position, mapSize)
		if quadrant:
			robotsInQuadrants[quadrant] += 1

	#pprint(robotsInQuadrants)
	#print(prod(robotsInQuadrants.values()))
	count = prod(robotsInQuadrants.values())
	return count


def part2(puzzleInput):
	count = 0
	
	return count


if __name__ == '__main__':
	cookie = sys.argv[1]
	today = datetime.datetime.now()
	puzzleInput = util.getInput(today.year, 14, cookie)
	test = []
	with open(f"{today.year}/test.txt", "r") as file:
		test = file.read().splitlines()

	inputMapSize = (101, 103)
	testMapSize = (11, 7)

	print(f"Part one: {part1(puzzleInput, inputMapSize)}")
	#print(util.postAnswer(today.year, 14, 1, part1(puzzleInput), cookie))

	#print(f"Part two: {part2(puzzleInput)}")
	#print(util.postAnswer(today.year, 14, 2, part2(puzzleInput), cookie))