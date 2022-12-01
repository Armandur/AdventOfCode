import util
import random

class colors:
	black = "30m"
	red = "31m"
	green = "32m"
	yellow = "33m"
	blue = "34m"
	magenta = "35m"
	cyan = "36m"
	white = "37m"

	colors = [red, green, yellow, blue, magenta, cyan]

def colorString(string, color):
	start = "\033["
	start += color
	reset = "\033[0m"
	return f"{start}{string}{reset}"


def isLowest(x, y, cave):
	offsets = []
	location = getLocation(x, y, cave)
	if location == "middle":
		offsets = [[-1, 0], [1, 0], [0, -1], [0, 1]]

	elif location == "topleft":
		offsets = [[1, 0], [0, 1]]

	elif location == "topright":
		offsets = [[1, 0], [0, -1]]

	elif location == "bottomright":
		offsets = [[-1, 0], [0, -1]]

	elif location == "left":
		offsets = [[1, 0], [0, 1], [0, -1]]

	elif location == "top":
		offsets = [[1, 0], [-1, 0], [0, 1]]

	elif location == "bottom":
		offsets = [[-1, 0], [0, 1], [0, -1]]

	elif location == "right":
		offsets = [[1, 0], [-1, 0], [0, -1]]

	lowest = True
	for offset in offsets:
		oX = x + offset[0]
		oY = y + offset[1]

		oCave = cave[oX][oY]
		current = cave[x][y]

		if oCave <= current:
			lowest = False
			break

	return lowest


def getLocation(x, y, cave):
	if 0 < x < len(cave)-1 and 0 < y < len(cave[0])-1:
		return "middle"

	elif x == y == 0:
		return "topleft"
	elif x == 0 and y == len(cave[0])-1:
		return "topright"

	elif x == len(cave)-1 and y == 0:
		return "bottomleft"
	elif x == len(cave)-1 and y == len(cave[0])-1:
		return "bottomright"

	elif x == 0 and y < len(cave[0])-1:
		return "left"
	elif y == 0 and x < len(cave)-1:
		return "top"

	elif x == len(cave)-1:
		return "bottom"
	elif y == len(cave[0])-1:
		return "right"


def fillBasin(basinPoints, x, y, cave):
	location = getLocation(x, y, cave)
	offsets = []
	if location == "middle":
		offsets = [[-1, 0], [1, 0], [0, -1], [0, 1]]

	elif location == "topleft":
		offsets = [[1, 0], [0, 1]]

	elif location == "topright":
		offsets = [[1, 0], [0, -1]]

	elif location == "bottomright":
		offsets = [[-1, 0], [0, -1]]

	elif location == "left":
		offsets = [[1, 0], [0, 1], [0, -1]]

	elif location == "top":
		offsets = [[1, 0], [-1, 0], [0, 1]]

	elif location == "bottom":
		offsets = [[-1, 0], [0, 1], [0, -1]]

	elif location == "right":
		offsets = [[1, 0], [-1, 0], [0, -1]]

	if cave[x][y] != 9:
		if [x, y] not in basinPoints:
			basinPoints.append([x, y])
		else:
			return
		for offset in offsets:
			fillBasin(basinPoints, x+offset[0], y+offset[1], cave)
	else:
		return


def part1(input):
	count = 0
	cave = []
	for line in input:
		line = list(map(int, line))
		cave.append(line)

	height = len(cave)
	width = len(cave[0])

	for x in range(0, height):
		row = ""
		for y in range(0, width):
			if isLowest(x, y, cave):
				row += colorString(str(cave[x][y]), colors.green)
				count += cave[x][y]+1
			else:
				row += str(cave[x][y])
		print(row)

	return count

def part2(input):
	count = 0
	cave = []
	for line in input:
		line = list(map(int, line))
		cave.append(line)

	height = len(cave)
	width = len(cave[0])

	lowestPoints = []
	basins = []

	for x in range(0, height):
		row = ""
		for y in range(0, width):
			if isLowest(x, y, cave):
				lowestPoints.append([x, y])

	for points in lowestPoints:
		basinPoints = []
		fillBasin(basinPoints, points[0], points[1], cave)
		basins.append((basinPoints, random.choice(colors.colors)))

	for x in range(0, height):
		row = ""
		for y in range(0, width):
			if [x, y] in lowestPoints:
				row += colorString(cave[x][y], colors.white)
			else:
				inBasin = False
				for basin in basins:
					if [x, y] in basin[0]:
						row += colorString(cave[x][y], basin[1])
						inBasin = True
				if not inBasin:
					row += str(cave[x][y])
		print(row)

	basins.sort(key = lambda x: len(x[0]), reverse=True)

	count = len(basins[0][0]) * len(basins[1][0]) * len(basins[2][0])

	return count

if __name__ == '__main__':
	input = util.getInput(2021, 9)
	test = []
	with open("test.txt", "r") as file:
		test = file.read().splitlines()

	#print(f"Part one: {part1(input)}")
	#print(util.postAnswer(2021, 9, 1, part1(input)))

	#print(f"Part two: {part2(input)}")
	#print(util.postAnswer(2021, 9, 2, part2(input)))