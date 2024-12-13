import util
import datetime
import sys
from pprint import pprint
import string
import random

colors = {}

def randomizeColors() -> dict:
	global colors
	for character in string.ascii_uppercase:
		colors.update({character : random.choice(util.colors.colors + util.colors.brightColors)})
	return colors

def printMap(gardenMap : list[list[int]], marked=list()):
	for y, row in enumerate(gardenMap):
		rowString = ""
		for x, column in enumerate(row):
			if (x, y) in marked:
				if (x, y) == marked[-1]:
					rowString += util.colorString(str(column), util.colors.redbg) + " "
				elif (x, y) == marked[0]:
					rowString += util.colorString(str(column), util.colors.greenbg) + " "
				else:
					rowString += util.colorString(str(column), util.colors.bluebg) + " "
			else:
				rowString += util.colorString(str(column), colors[column]) + " " 
		print(rowString)


def onMap(position : tuple, mapSize=140):
	x, y = position
	return (mapSize > x >= 0 and mapSize > y >= 0)


def addTuple(a:tuple, b:tuple) -> tuple:
	return (a[0]+b[0], a[1]+b[1])


def part1(puzzleInput):
	visited = set()

	def loadGardenMap(puzzleInput) -> list:
		gardenMap = list()
		for y, line in enumerate(puzzleInput):
			row = list()
			for x, column in enumerate(line):
				row.append(column)
			gardenMap.append(row)
		return gardenMap


	def findRegions(position, gardenMap) -> list:
		if position in visited:
			return None
		
		x, y = position

		plantLabel = gardenMap[y][x]

		region = (plantLabel, [])

		def traverse(position, plantLabel, region):
			#print(f"Searching region {plantLabel}\n")
			deltas = [
			(0, -1),
			(0, 1),
			(-1, 0),
			(1, 0)
			]

			x, y = position

			if position in visited:
				return
			
			if not onMap(position):
				return
			
			if gardenMap[y][x] != plantLabel:
				return

			region[1].append(position)
			visited.add(position)

			#printMap(gardenMap, list(visited))
			#print()
			
			for delta in deltas:
				newPosition = addTuple(position, delta)
				traverse(newPosition, plantLabel, region)

		traverse(position, plantLabel, region)

		if region:
			return region
		else:
			return None

	def countPerimeter(region) -> int:
		perimeterLength = 0
		deltas = [
			(0, -1),
			(0, 1),
			(-1, 0),
			(1, 0)
			]
		
		plantLabel = region[0]
		for position in region[1]:
			for delta in deltas:
				newPos = addTuple(position, delta)
				if newPos not in region[1]:
					perimeterLength += 1
		return perimeterLength

	global colors
	colors = randomizeColors()

	gardenMap = loadGardenMap(puzzleInput)

	# tregion = findRegions((0,0), gardenMap)

	# printMap(gardenMap, tregion[1])
	# print(countPerimeters(tregion))
		
	regions = list()
	for y, row in enumerate(gardenMap):
		for x, column in enumerate(row):
			result = findRegions((x, y), gardenMap)
			if result is not None:
				regions.append(result)

	#allRegions = [coord for _, coords in regions for coord in coords]
	#pprint(allRegions)
	#printMap(gardenMap, allRegions)
	count = 0

	for region in regions:
		perimeterLength = countPerimeter(region)
		perimeterArea = len(region[1])
		fencingCost = perimeterLength * perimeterArea
		
		print(f"Region growing plant " + util.colorString(region[0], colors[region[0]]) +f", found at {region[1][0]}")
		print(f"Perimeter length is {perimeterLength} U, area is {perimeterArea} U²")
		print(f"Price of fencing is {fencingCost} ¤")
		printMap(gardenMap, region[1])
		print()
		count += fencingCost
	
	return count


def part2(puzzleInput):
	count = 0
	
	return count


if __name__ == '__main__':
	cookie = sys.argv[1]
	today = datetime.datetime.now()
	puzzleInput = util.getInput(today.year, 12, cookie)
	test = []
	with open(f"{today.year}/test.txt", "r") as file:
		test = file.read().splitlines()

	print(f"Part one: {part1(puzzleInput)}")
	#print(util.postAnswer(today.year, 12, 1, part1(puzzleInput), cookie))

	print(f"Part two: {part2(puzzleInput)}")
	#print(util.postAnswer(today.year, 12, 2, part2(puzzleInput), cookie))