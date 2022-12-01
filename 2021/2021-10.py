import util

from collections import deque

def checkLine(line):
	pairs = {
		'(' : ')',
		'[' : ']',
		'{' : '}',
		'<' : '>'
	}
	stack = deque()
	stack.append(line[0])
	# print(line)
	for symbol in line[1:]:
		try:
			if len(stack) == 0 and symbol not in pairs.values():
				stack.append(symbol)
			elif symbol != pairs[stack[-1]]:
				stack.append(symbol)
			else:
				stack.pop()
			string = ""
			for item in stack:
				string += item
		# print(string)
		except KeyError:
			wrongCloser = stack.pop()
			# print(f"Wrong closer: {wrongCloser}")
			return wrongCloser
			break
	if len(stack) == 0:
		return "Correct"
	else:
		return "Incomplete"

def completeLine(line):
	closers = ""
	pairs = {
		'(' : ')',
		'[' : ']',
		'{' : '}',
		'<' : '>'
	}

	stack = deque()
	stack.append(line[0])
	for symbol in line[1:]:
		if len(stack) == 0 and symbol not in pairs.values():
			stack.append(symbol)
		elif symbol != pairs[stack[-1]]:
			stack.append(symbol)
		else:
			stack.pop()

	while len(stack) != 0:
		closers+= pairs[stack.pop()]

	return closers

def calculateScore(string):
	score = 0
	points = {
		')' : 1,
		']' : 2,
		'}' : 3,
		'>' : 4
	}
	for ch in string:
		score = (score * 5) + points[ch]

	return score

def part1(input):
	count = 0
	lines = input

	wrongClosers = []

	for line in lines:
		stack = deque()
		stack.append(line[0])
		#print(line)
		result = checkLine(line)

		if result != "correct":
			wrongClosers.append(result)

	points = {
		')' : 3,
		']' : 57,
		'}' : 1197,
		'>' : 25137
	}

	for key in points.keys():
		count += wrongClosers.count(key) * points[key]

	return count

def part2(input):
	count = 0
	lines = input

	incompleteLines = []
	for line in lines:
		result = checkLine(line)
		if result == "Incomplete":
			incompleteLines.append(line)

	closingStrings = []
	for incompleteLine in incompleteLines:
		closingStrings.append(completeLine(incompleteLine))

	scores = []
	for string in closingStrings:
		scores.append(calculateScore(string))

	scores.sort()

	middle = int((len(scores)-1) / 2 + 0.5)
	count = scores[middle]

	return count


if __name__ == '__main__':
	input = util.getInput(2021, 10)
	test = []
	with open("test.txt", "r") as file:
		test = file.read().splitlines()

	print(f"Part one: {part1(input)}")
	#print(util.postAnswer(2021, 10, 1, part1(input)))

	print(f"Part two: {part2(input)}")
	#print(util.postAnswer(2021, 10, 2, part2(input)))