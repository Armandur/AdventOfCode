import util
import datetime
import sys
from pprint import pprint
from math import sqrt, ceil
import random

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

def onMap(puzzleInput, position: tuple):
	height = len(puzzleInput)
	width = len(puzzleInput[0])
	x,y = position
	return (width > x >= 0 and height > y >= 0)

antennas = dict()
colors = dict()

def loadMap(puzzleInput):
	for y, line in enumerate(puzzleInput):
		for x, character in enumerate(line):
			if character == ".":
				continue
			if character not in antennas:
				antennas[character] = list()
			antennas[character].append((x, y))

	global colors
	if len(colors) != len(antennas.keys()):
		colors = dict()

	if not colors:
		for key in antennas.keys():
			colors.update({key : random.choice(util.colors.colors)})

def printMap(puzzleInput, antinodes):
	for y, line in enumerate(puzzleInput):
		printLine = ""
		for x, character in enumerate(line):
			if (x, y) in antinodes:
				if character != ".":
					color = colors[character]
					color = f"4{color[1:]}"
					printLine += f"{util.colorString(character, color)} "
				else:
					printLine += f"{util.colorString('#', util.colors.brightcyan)} "
				continue
			if character == ".":
				printLine += "· "
			else:
				printLine += f"{util.colorString(character, colors[character])} "
		print(printLine)

def part1(puzzleInput):
	count = 0

	loadMap(puzzleInput)
	antinodes = set()

	for frequency in antennas.keys():
		for antenna in antennas[frequency]:
			for secondAntenna in antennas[frequency]:
				if antenna == secondAntenna:
					continue
				delta = getDelta(antenna, secondAntenna)
				if onMap(puzzleInput, addTuple(secondAntenna, delta)):
					antinodes.add(addTuple(secondAntenna, delta))

				if onMap(puzzleInput, addTuple(antenna, negativeTuple(delta))):
					antinodes.add(addTuple(antenna, negativeTuple(delta)))

	printMap(puzzleInput, antinodes)
	count = len(antinodes)
				
	return count


def part2(puzzleInput):
	count = 0
	loadMap(puzzleInput)

	antinodes = set()
	
	for frequency in antennas.keys():
		for antenna in antennas[frequency]:
			for secondAntenna in antennas[frequency]:
				if antenna == secondAntenna:
					continue

				delta = getDelta(antenna, secondAntenna)
				nextPos = addTuple(antenna, delta)
				while onMap(puzzleInput, nextPos):
					antinodes.add(nextPos)
					nextPos = addTuple(nextPos, delta)

	printMap(puzzleInput, antinodes)
	count = len(antinodes)
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