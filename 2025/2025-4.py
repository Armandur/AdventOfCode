import util
import datetime
import sys
from pprint import pprint


def part1(puzzleInput):
	count = 0

	paperCoords = []

	def checkRoll(printingDepartment, pos): #pos = (x, y)
		posX = pos[0]
		posY = pos[1]

		def onBoard(pos):
			x = pos[0]
			y = pos[1]
			if 0 <= x < len(printingDepartment[0]) and 0 <= y < len(printingDepartment):
				return True
			else:
				return False
		deltas = [
			(-1, -1), # Top left
			(0, -1),  # Top
			(1, -1),  # Top right
			(-1, 0), # Left
			(1, 0),   # Right
			(-1, 1),  # Bottom left 
			(0, 1),   # Bottom
			(1, 1)   # Bottom right
		]

		adjacentRolls = 0
		for delta in deltas:
			x = posX+delta[0]
			y = posY+delta[1]
			if onBoard((x, y)) and printingDepartment[y][x] == "@":
				adjacentRolls += 1
		if adjacentRolls < 4:
			if (posX, posY) not in paperCoords:
				paperCoords.append((posX, posY))


	mapWidth = len(puzzleInput[0])
	mapHeight = len(puzzleInput)

	for y in range(0, mapHeight):
		for x in range(0, mapWidth):
			if puzzleInput[y][x] == "@":
				checkRoll(puzzleInput, (x, y))

	def printDepartmentMap(printingDepartment, marked=list([]), color=util.colors.green):
		mapWidth = len(printingDepartment[0])
		mapHeight = len(printingDepartment)
		for y in range(0, mapHeight):
			line = ""
			for x in range(0, mapWidth):
				if marked and any((x, y) in sublist for sublist in marked):
					line += util.colorString(printingDepartment[y][x], color)
				else:
					line += printingDepartment[y][x]
			print(line)

	printDepartmentMap(puzzleInput, [paperCoords], util.colors.green)
	count = len(paperCoords)
	return count


def part2(puzzleInput):
	count = 0
	
	return count


if __name__ == '__main__':
	if len(sys.argv) < 2:
		print("No cookie supplied in sys.argv[1]")
		exit()
	cookie = sys.argv[1]
	today = datetime.datetime.now()
	puzzleInput = util.getInput(today.year, today.day, cookie)
	test = []
	with open(f"{today.year}/test.txt", "r") as file:
		test = file.read().splitlines()

	#print(f"Part one: {part1(puzzleInput)}")
	print(util.postAnswer(today.year, today.day, 1, part1(puzzleInput), cookie))

	#print(f"Part two: {part2(puzzleInput)}")
	#print(util.postAnswer(today.year, today.day, 2, part2(puzzleInput), cookie))