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
		coords = []
		XMAS = ""

		# UP
		for y in range(pos[1], pos[1]-len("XMAS"), -1):
			if y < 0:
				break
			# print(wordMap[y][pos[0]])
			XMAS += wordMap[y][pos[0]]
			coords.append(((pos[0], y)))
		if XMAS == "XMAS":
			coordsXMAS.append(coords)
		coords = []
		XMAS = ""

		# DOWN
		try:
			for y in range(pos[1], pos[1]+len("XMAS")):
				if y > len(wordMap):
					break
				# print(wordMap[y][pos[0]])
				XMAS += wordMap[y][pos[0]]
				coords.append((pos[0], y))
			if XMAS == "XMAS":
				coordsXMAS.append(coords)
		except IndexError:
			pass
		coords = []
		XMAS = ""

		# LEFT
		for x in range(pos[0], pos[0]-len("XMAS"), -1):
			if x < 0:
				break
			# print(wordMap[pos[1]][x])
			XMAS += wordMap[pos[1]][x]
			coords.append((x, pos[1]))
		if XMAS == "XMAS":
			coordsXMAS.append(coords) 
		coords = []
		XMAS = ""
		
		# RIGHT
		try: 
			for x in range(pos[0], pos[0]+len("XMAS")):
				if x > len(wordMap[0]):
					break
				# print(wordMap[pos[1]][x])
				XMAS += wordMap[pos[1]][x]
				coords.append((x, pos[1]))
			if XMAS == "XMAS":
				coordsXMAS.append(coords)
		except IndexError:
			pass
		coords = []
		XMAS = ""

		# UPLEFT
		try:
			for step, y in enumerate(range(pos[1], pos[1]-len("XMAS"), -1)):
				x = pos[0]-step
				if x < 0 or y < 0:
					break
				XMAS += wordMap[y][x]
				coords.append((x, y))

				# printWordmap(wordMap, [[(x, y)]], util.colors.red)
				# print("UPLEFT")
				# print(util.colorString(f"({x}, {y})", util.colors.cyan))
				# time.sleep(0.3)
				# os.system("cls")					
				if XMAS == "XMAS":
					coordsXMAS.append(coords)
		except IndexError:
			pass
		coords = []
		XMAS = ""

		# UPRIGHT
		try:
			for step, y in enumerate(range(pos[1], pos[1]-len("XMAS"), -1)):
				x = pos[0]+step
				if x > len(wordMap[0]) or y < 0:
					break
				XMAS += wordMap[y][x]
				coords.append((x, y))

				# printWordmap(wordMap, [[(x, y)]], util.colors.red)
				# print("UPRIGHT")
				# print(util.colorString(f"({x}, {y})", util.colors.cyan))
				# time.sleep(0.3)
				# os.system("cls")
			if XMAS == "XMAS":
				coordsXMAS.append(coords)
		except IndexError:
			pass
		coords = []
		XMAS = ""

		# DOWNLEFT
		try:
			for step, y in enumerate(range(pos[1], pos[1]+len("XMAS"))):
				x = pos[0]-step
				if x > len(wordMap[0] or y > len(wordMap)):
					break
				XMAS += wordMap[y][x]
				coords.append((x, y))
				
				# printWordmap(wordMap, [[(x, y)]], util.colors.red)
				# print("DOWNLEFT")
				# print(util.colorString(f"({x}, {y})", util.colors.cyan))
				# time.sleep(0.3)
				# os.system("cls")
			if XMAS == "XMAS":
				coordsXMAS.append(coords)
		except IndexError:
			pass
		coords = []
		XMAS = ""

		# DOWNRIGHT
		try:
			for step, y in enumerate(range(pos[1], pos[1]+len("XMAS"))):
				x = pos[0]+step
				if x > len(wordMap[0] or y > len(wordMap)):
					break
				XMAS += wordMap[y][x]
				coords.append((x, y))
				
				# printWordmap(wordMap, [[(x, y)]], util.colors.red)
				# print("DOWNRIGHT")
				# print(util.colorString(f"({x}, {y})", util.colors.cyan))
				# time.sleep(0.3)
				# os.system("cls")
				if XMAS == "XMAS":
					coordsXMAS.append(coords)
		except IndexError:
			pass
		coords = []
		XMAS = ""

	mapWidth = len(puzzleInput[0])
	mapHeight = len(puzzleInput)
	for y in range(0, mapHeight):
		line = ""
		for x in range(0, mapWidth):
			#printWordmap(input, [[(x, y)]], util.colors.red)
			#time.sleep(0.2)
			#os.system("cls")
			if puzzleInput[y][x] == "X":
				sumOfXMASCoords = len(coordsXMAS)
				checkXMAS(puzzleInput, (x, y))
				#if len(coordsXMAS) > sumOfXMASCoords:
					#printWordmap(puzzleInput, coordsXMAS)
					#print()
					#print(len(coordsXMAS))
					#input()
					#os.system("cls")
					
	#printWordmap(input, coordsXMAS)
	count = len(list(map(list, {tuple(sublist) for sublist in coordsXMAS})))
	return count


def part2(input):
	count = 0
	
	return count

if __name__ == '__main__':
	cookie = sys.argv[1]
	today = datetime.datetime.now()
	puzzleInput = util.getInput(today.year, today.day, cookie)
	test = []
	with open(f"{today.year}/test.txt", "r") as file:
		test = file.read().splitlines()

	print(f"Part one: {part1(test)}")
	#print(util.postAnswer(today.year, today.day, 1, part1(input), cookie))

	print(f"Part two: {part2(puzzleInput)}")
	#print(util.postAnswer(today.year, today.day, 2, part2(input), cookie))