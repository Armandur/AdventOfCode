import util

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


def load(input):
	dots = input[0:input.index("")]
	instructions = input[input.index("")+1:]

	temp = set()
	for dot in dots:
		dot = dot.split(",")
		temp.add((int(dot[0]), int(dot[1])))
	dots = temp
	#print(dots)

	temp = list()
	for instruction in instructions:
		instruction = instruction.split("fold along ")
		instruction = instruction[1].split("=")
		temp.append((instruction[0], int(instruction[1])))
	instructions = temp
	#print(instructions)
	return dots, instructions


def printPaper(paper, mark, color):
	for row in paper:
		string = ""
		for ch in row:
			if ch == mark:
				string += colorString(ch, color)
			else:
				string += ch
		print(string)


def countDots(paper, dot):
	dots = 0
	for row in paper:
		for col in row:
			if col == dot:
				dots += 1
	return dots


def rotatePaper(paper): #Rotate 90 degrees counter clockwise
	p = list(map(list, zip(*paper)))
	p.reverse()
	return p


def foldX(paper, x):
	#Rotate paper 90 degres ccw and do foldY, flip three times to get back to original

	paper = rotatePaper(paper)
	paper = foldY(paper, x)

	#printPaper(paper, '#', color.green)

	paper = rotatePaper(paper)
	paper = rotatePaper(paper)
	paper.reverse()
	paper = rotatePaper(paper)
	return paper


def foldY(paper, y): #Return list[list] of paper with dots
	top = paper[:y]
	bottom = paper[y+1:]
	#diff = abs(len(top) - len(bottom)) #Check if we aren't folding in the middle
	diff = 0

	#print("Paper:")
	#printPaper(paper, '#', colors.green)

	#print("Top half:")
	#printPaper(top, '#', colors.green)

	#print("Bottom half:")
	#printPaper(bottom, '#', colors.green)

	if diff > 0:
		print(f"Padding {diff} lines")
		for i in range(diff):
			temp = []
			for j in range(len(top[0])):
				temp.append('.')
			if len(bottom) < len(top):
				bottom.append(temp)
			else:
				top.append(temp)

	bottom.reverse()

	foldedPaper = [['.' for row in range(len(top[0]))] for col in range(len(top))]

	#print(f"Top rows: {len(top)}, Bottom rows: {len(bottom)}, foldedPaper rows: {len(foldedPaper)}")

	for y in range(len(foldedPaper)):
		for x in range(len(foldedPaper[y])):
			if top[y][x] == '#':
				foldedPaper[y][x] = '#'
			elif bottom[y][x] == '#':
				foldedPaper[y][x] = '#'

	#for ch in range(len(foldedPaper[-1])):
	#	foldedPaper[-1][ch] = '.'

	return foldedPaper


def part1(input):
	count = 0
	dots, instructions = load(input)

	maxX = max(dots, key=lambda item:item[0])[0]
	maxY = max(dots, key=lambda item:item[1])[1]

	#print(f"Height: {maxY}")
	#print(f"Width: {maxX}")

	paper = [['.' for col in range(maxX+1)] for row in range(maxY+1)]

	for x, y in dots:
		paper[y][x] = '#'

	for direction, pos in instructions[0:1]:
		if direction == 'x':
			paper = foldX(paper, pos)
		elif direction == 'y':
			paper = foldY(paper, pos)

	#printPaper(paper, '#', colors.green)

	count = countDots(paper, '#')

	return count


def part2(input):
	count = 0
	count = 0
	dots, instructions = load(input)

	maxX = max(dots, key=lambda item:item[0])[0]
	maxY = max(dots, key=lambda item:item[1])[1]

	#print(f"Height: {maxY}")
	#print(f"Width: {maxX}")

	paper = [['.' for col in range(maxX+1)] for row in range(maxY+1)]

	for x, y in dots:
		paper[y][x] = '#'

	for direction, pos in instructions:
		if direction == 'x':
			paper = foldX(paper, pos)
		elif direction == 'y':
			paper = foldY(paper, pos)

	printPaper(paper, '#', colors.green)
	return count


if __name__ == '__main__':
	input = util.getInput(2021, 13)
	test = []
	with open("test.txt", "r") as file:
		test = file.read().splitlines()

	print(f"Part one: {part1(input)}")
	#print(util.postAnswer(2021, 13, 1, part1(input)))

	print(f"Part two: {part2(input)}")
	#print(util.postAnswer(2021, 13, 2, part2(input)))