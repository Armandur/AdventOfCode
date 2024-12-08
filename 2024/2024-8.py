import util
import datetime
import sys
from pprint import pprint
from math import sqrt, ceil
import random

def part1(puzzleInput):
	count = 0
	antennas = dict()
	for y, line in enumerate(puzzleInput):
		for x, character in enumerate(line):
			if character == ".":
				continue
			if character not in antennas:
				antennas[character] = list()
			antennas[character].append((x, y))

	def getDelta(a:tuple, b:tuple) -> int:
		return (b[0]-a[0], b[1]-a[1])

	def distance(a:tuple, b:tuple) -> int:
		aX, aY = a
		bX, bY = b
		return ceil(sqrt((bX - aX)**2 + (bY - aY)**2))
	
	def halfTupleCeil(tup: tuple) -> tuple:
		return (ceil(tup[0]/2), ceil(tup[1]/2))
	
	def negativeTuple(tup: tuple) -> tuple:
		return tuple([y*-1 for y in tup])
	
	def addTuple(a:tuple, b:tuple) -> tuple:
		return (a[0]+b[0], a[1]+b[1])

	def onMap(position: tuple):
		height = len(puzzleInput)-1
		width = len(puzzleInput[0])-1
		x,y = position
		return (width >= x >= 0 and height >= y >= 0)
	
	colors = dict()
	for key in antennas.keys():
		colors.update({key : random.choice(util.colors.colors)})

	antinodes = set()
	
	def printMap():
		for y, line in enumerate(puzzleInput):
			printLine = ""
			for x, character in enumerate(line):
				if (x, y) in antinodes:
					printLine += "# "
					continue
				if character == ".":
					printLine += "· "
				else:
					printLine += f"{util.colorString(character, colors[character])} "
			print(printLine)
	


	pprint(antennas)
	for frequency in antennas.keys():
		for index, antenna in enumerate(antennas[frequency]):
			for secondAntenna in antennas[frequency][index+1:]:
				pprint(f"{frequency} : First: {antenna}, Second: {secondAntenna}")
				delta = getDelta(antenna, secondAntenna)
				if onMap(addTuple(secondAntenna, delta)):
					antinodes.add(addTuple(secondAntenna, delta))

				if onMap(addTuple(antenna, negativeTuple(delta))):
					antinodes.add(addTuple(antenna, negativeTuple(delta)))

	printMap()

	count = len(antinodes)
				
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

	print(f"Part one: {part1(puzzleInput)}")
	#print(util.postAnswer(today.year, today.day, 1, part1(puzzleInput), cookie))

	print(f"Part two: {part2(puzzleInput)}")
	#print(util.postAnswer(today.year, today.day, 2, part2(puzzleInput), cookie))