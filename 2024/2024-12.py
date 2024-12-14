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


def loadGardenMap(puzzleInput) -> list:
	gardenMap = list()
	for y, line in enumerate(puzzleInput):
		row = list()
		for x, column in enumerate(line):
			row.append(column)
		gardenMap.append(row)
	return gardenMap


def findRegions(position, gardenMap, visited) -> list:
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


def part1(puzzleInput):
	visited = set()

	global colors
	colors = randomizeColors()

	gardenMap = loadGardenMap(puzzleInput)

	# tregion = findRegions((0,0), gardenMap)

	# printMap(gardenMap, tregion[1])
	# print(countPerimeters(tregion))
		
	regions = list()
	for y, row in enumerate(gardenMap):
		for x, column in enumerate(row):
			result = findRegions((x, y), gardenMap, visited)
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
		
		# print(f"Region growing plant " + util.colorString(region[0], colors[region[0]]) +f", found at {region[1][0]}")
		# print(f"Perimeter length is {perimeterLength} U, area is {perimeterArea} U²")
		# print(f"Price of fencing is {fencingCost} ¤")
		# printMap(gardenMap, region[1])
		# print()
		count += fencingCost
	
	return count


def getPerimeters(region) -> list:
	perimeters = list()
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
				perimeters.append(newPos)
	return perimeters

def getSides(region, gardenMap=None):
	region = region[1]
	
	sortedX = sorted(region, key=lambda x: x[0])
	leftmost = sortedX[0]
	rightmost = sortedX[-1]

	sortedY = sorted(region, key=lambda x: x[1])
	topmost = sortedY[0]
	bottommost = sortedY[-1]

	#Scan up down
	startX = leftmost[0]
	startY = topmost[1]

	endX = rightmost[0]
	endY = bottommost[1]

	topEdges = list()
	bottomEdges = list()

	for y in range(startY, endY+1):
		for x in range(startX, endX+1):
			if (x, y) in region:
				scanUp = addTuple((x, y), (0, -1))
				scanDown = addTuple((x, y), (0, 1))
				
				if scanUp not in region:
					#Top edge
					topEdges.append((x, y))
				
				if scanDown not in region:
					#Bottom edge
					bottomEdges.append((x,y))

	# Sort found edges by x value
	topEdges = sorted(topEdges, key=lambda x: x[1]) 
	bottomEdges = sorted(bottomEdges, key=lambda x: x[1])

	sides = list()
	group = None

	while topEdges:
		if group is None or group[-1][1] != topEdges[0][1] or group[-1][0] != topEdges[0][0] - 1:
			if group:
				sides.append(group)
			group = [topEdges.pop(0)]
		else:
			group.append(topEdges.pop(0))

	if group:
		sides.append(group)
		

	group = None
	while bottomEdges:
		if group is None or group[-1][1] != bottomEdges[0][1] or group[-1][0] != bottomEdges[0][0] - 1:
			if group:
				sides.append(group)
			group = [bottomEdges.pop(0)]
		else:
			group.append(bottomEdges.pop(0))

	if group:
		sides.append(group)
		
	return (len(sides) * 2)
	

def part2(puzzleInput):
	global colors
	visited = set()

	gardenMap = loadGardenMap(puzzleInput)

	# tregion = findRegions((0, 0), gardenMap, visited)

	# printMap(gardenMap, tregion[1])
	# print()
	# printMap(gardenMap, getPerimeters(tregion))
	# print()
	# sides = scanRegion(tregion)
	# print(sides)

	regions = list()
	for y, row in enumerate(gardenMap):
		for x, column in enumerate(row):
			result = findRegions((x, y), gardenMap, visited)
			if result is not None:
				regions.append(result)

	#allRegions = [coord for _, coords in regions for coord in coords]
	#pprint(allRegions)
	#printMap(gardenMap, allRegions)
	count = 0

	for region in regions:
		numberOfSides = getSides(region, gardenMap)
		perimeterArea = len(region[1])
		fencingCost = numberOfSides * perimeterArea
		
		print(f"Region growing plant " + util.colorString(region[0], colors[region[0]]) +f", found at {region[1][0]}")
		print(f"Number of sides is {numberOfSides}, area is {perimeterArea} U²")
		print(f"Price of fencing is {fencingCost} ¤")
		printMap(gardenMap, region[1])
		print()
		count += fencingCost
	
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