import util

class offset:
	up = (-1, 0)
	down = (1, 0)

	left = (0, -1)
	right = (0, 1)

	upleft = (-1, -1)
	upright = (-1, 1)

	downleft = (1, -1)
	downright = (1, 1)

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

def clearConsole():
    command = 'clear'
    if os.name in ('nt', 'dos'):  # If Machine is running on Windows, use cls
        command = 'cls'
    os.system(command)


def getAdjacents(x, y, cave):
	adjacents = []
	offsets = [offset.up, offset.down, offset.left, offset.right, offset.downleft, offset.downright, offset.upleft, offset.upright]

	for o in offsets:
		try:
			if x+o[0] < 0 or y+o[1] < 0:
				continue
			cave[x+o[0]][y+o[1]]
			adjacents.append((x + o[0], y + o[1]))
		except IndexError:
			pass

	return adjacents


def step(cave):
	flashing = []
	flashed = set()
	#First increase all cells with 1

	for x in range(len(cave)):
		for y in range(len(cave[0])):
			cave[x][y] += 1
			if cave[x][y] > 9:
				flashing.append((x, y))

	while len(flashing) > 0:
		flashed.update(flashing)
		x, y = flashing.pop(0)

		for coordinate in getAdjacents(x, y, cave):
			x1, y1 = coordinate
			cave[x1][y1] += 1
			if cave[x1][y1] > 9 and (x1, y1) not in flashed:
				flashing.append(coordinate)

	for x in range(len(cave)):
		for y in range(len(cave[0])):
			if cave[x][y] > 9:
				cave[x][y] = 0

	return flashed


def printCavern(cave, mark,color):
	for i in range(len(cave)):
		row = ""
		for j in range(len(cave[0])):
			if cave[i][j] < 10:
				row += "  "
			else:
				row += " "
			if (i, j) in mark:
				row += colorString(cave[i][j], color)
			else:
				row += str(cave[i][j])
		print(row)


def part1(input):
	count = 0
	cavern = []

	for line in input:
		line = list(map(int, line))
		cavern.append(line)

	for i in range(100):
		print(i+1)
		flashed = step(cavern)
		count += len(flashed)
		printCavern(cavern, flashed, colors.green)

	return count


def part2(input):
	count = 0
	cavern = []

	for line in input:
		line = list(map(int, line))
		cavern.append(line)

	i = 1
	while i:
		print(i)
		flashed = step(cavern)
		printCavern(cavern, flashed, colors.green)
		if len(flashed) == len(cavern[0])**2:
			break
		i += 1

	count = i
	return count


if __name__ == '__main__':
	input = util.getInput(2021, 11)
	test = []
	with open("test.txt", "r") as file:
		test = file.read().splitlines()

	#print(f"Part one: {part1(input)}")
	#print(util.postAnswer(2021, 11, 1, part1(input)))

	#print(f"Part two: {part2(input)}")
	#print(util.postAnswer(2021, 11, 2, part2(input)))