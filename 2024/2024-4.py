import util
import datetime
import sys
from pprint import pprint
import time
import os

def part1(puzzleInput):
	count = 0

	#  Y  X ->
	#  |
	# \ /
	#   0123456789
	# 0 MMMSXXMASM
	# 1 MSAMXMSMSA
	# 2 AMXSXMAAMM
	# 3 MSAMASMSMX
	# 4 XMASAMXAMM
	# 5 XXAMMXXAMA
	# 6 SMSMSASXSS
	# 7 SAXAMASAAA
	# 8 MAMMMXMMMM
	# 9 MXMXAXMASX

	def printWordmap(wordMap, marked=list([]), color=util.colors.green):
		mapWidth = len(wordMap[0])
		mapHeight = len(wordMap)
		for y in range(0, mapHeight):
			line = ""
			for x in range(0, mapWidth):
				if marked and any((x, y) in sublist for sublist in marked):
					line += util.colorString(wordMap[y][x], color)
				else:
					line += wordMap[y][x]
			print(line)

	coordsXMAS = []

	def checkXMAS(wordMap, pos): #post (x, y)
		posX = pos[0]
		posY = pos[1]
		
		def onBoard(pos):
			x = pos[0]
			y = pos[1]
			if 0 <= x < len(wordMap[0]) and 0 <= y < len(wordMap):
				return True
			else:
				return False

		deltas = [
			[list(range(0, -4, -1)), list(range(0, -4, -1))], 	# UPLEFT
			[[0, 0, 0, 0], list(range(0, -4, -1))], 			# UP
			[list(range(0, 4)), list(range(0, -4, -1))],		# UPRIGHT
			[list(range(0, 4)), [0, 0, 0, 0]],					# RIGHT
			[list(range(0, 4)), list(range(0, 4))],				# DOWNRIGHT
			[[0, 0, 0, 0], list(range(0, 4))],					# DOWN
			[list(range(0, -4, -1)), list(range(0, 4))],		# DOWNLEFT
			[list(range(0, -4, -1)), [0, 0, 0, 0]]				# LEFT
		   ]
		
		for delta in deltas:
			XMAS = ""
			coords = []
			for i in range(4):
				x = posX+delta[0][i]
				y = posY+delta[1][i]
				if not onBoard((x, y)):
					XMAS = ""
					coords = []
					break
				XMAS += wordMap[y][x]
				coords.append((x, y))
			if XMAS == "XMAS":
				coordsXMAS.append(coords)
				#printWordmap(wordMap, coordsXMAS)
				#os.system("cls")

	mapWidth = len(puzzleInput[0])
	mapHeight = len(puzzleInput)
	for y in range(0, mapHeight):
		line = ""
		for x in range(0, mapWidth):
			if puzzleInput[y][x] == "X":
				sumOfXMASCoords = len(coordsXMAS)
				checkXMAS(puzzleInput, (x, y))
					
	#printWordmap(puzzleInput, coordsXMAS)
	count = len(list(map(list, {tuple(sublist) for sublist in coordsXMAS})))
	return count


def part2(puzzleInput):
	count = 0
	
	return count

if __name__ == '__main__':
	cookie = sys.argv[1]
	today = datetime.datetime.now()
	puzzleInput = util.getInput(today.year, 4, cookie)
	test = []
	with open(f"{today.year}/test.txt", "r") as file:
		test = file.read().splitlines()

	print(f"Part one: {part1(puzzleInput)}")
	print(util.postAnswer(today.year, 4, 1, part1(puzzleInput), cookie))

	print(f"Part two: {part2(puzzleInput)}")
	#print(util.postAnswer(today.year, today.day, 2, part2(puzzleInput), cookie))