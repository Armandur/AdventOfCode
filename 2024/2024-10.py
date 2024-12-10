import util
import datetime
import sys
from pprint import pprint
import time

colors = {
	0 : util.colors.brightgreen,
	1 : util.colors.brightblue,
	2 : util.colors.blue,
	3 : util.colors.brightcyan,
	4 : util.colors.cyan,
	5 : util.colors.yellow,
	6 : util.colors.brightmagenta,
	7 : util.colors.magenta,
	8 : util.colors.brightred,
	9 : util.colors.red
}

def printMap(topomap : list[list[int]], marked=list()):
	for y, row in enumerate(topomap):
		rowString = ""
		for x, column in enumerate(row):
			if (x, y) in marked:
				if (x, y) == marked[-1]:
					rowString += util.colorString(str(column), util.colors.redbg) + " "
				else:
					rowString += util.colorString(str(column), util.colors.bluebg) + " "
			else:
				rowString += util.colorString(str(column), colors[column]) + " " 
		print(rowString)

def onMap(position : tuple, mapSize : int):
	x, y = position
	return (mapSize > x >= 0 and mapSize > y >= 0)

def addTuple(a:tuple, b:tuple) -> tuple:
	return (a[0]+b[0], a[1]+b[1])

foundTrails = dict()

def traverse(position, path, map):
	if not path:
		path = [position]
	
	deltas = [
		(0, -1),
		(0, 1),
		(-1, 0),
		(1, 0)
	]

	for delta in deltas:
		newPos = addTuple(position, delta)
		currentHeight = map[position[1]][position[0]]

		if onMap(newPos, len(map[0])):
			newHeight = map[newPos[1]][newPos[0]]
			if newHeight - currentHeight == 1:
				path.append(newPos)
				if map[newPos[1]][newPos[0]] == 9:
					if (path[0], path[-1]) not in foundTrails.keys():
						foundTrails.update({(path[0], path[-1]) : path})
					path = path[:-1]
				else:
					traverse(newPos, path.copy(), map)
	path = []
	return

def part1(puzzleInput):
	print(f"")
	topographicalMap = list()
	trailheads = set()

	for y, line in enumerate(puzzleInput):
		row = list()
		for x, column in enumerate(line):
			row.append(int(column))
			if int(column) == 0:
				trailheads.add((x, y))
		topographicalMap.append(row)
	
	print()
	print(f"The reindeer gave us a topographical map, it is {len(puzzleInput)}x{len(puzzleInput[0])}:")
	printMap(topographicalMap)

	for trailhead in trailheads:
		traverse(trailhead, [], topographicalMap)

	#pprint(foundTrails)

	sortedKeys = list(foundTrails.keys())
	sortedKeys.sort()

	#for key in sortedKeys:	
		#print(f"Trail from {key[0]} to {key[1]}")
		#printMap(topographicalMap, foundTrails[key])
	
	count = len(sortedKeys)
	
	return count

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

	#print(f"Part one: {part1(puzzleInput)}")
	#print(util.postAnswer(today.year, today.day, 1, part1(puzzleInput), cookie))

	print(f"Part two: {part2(puzzleInput)}")
	#print(util.postAnswer(today.year, today.day, 2, part2(puzzleInput), cookie))