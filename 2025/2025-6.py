import util
import datetime
import sys
from pprint import pprint
from copy import deepcopy


def part1(puzzleInput):
	count = 0
	
	problems = []

	for element in puzzleInput[0].split():
		problems.append([int(element)])

	for line in puzzleInput[1:]:
		for i, element in enumerate(line.split()):
			if element == '*' or element == '+':
				problems[i].append(element)
			else:
				problems[i].append(int(element))
	
	for problem in problems:
		if problem[-1] == '*':
			result = 1
			for item in problem[:-1]:
				result *= item
			count += result
		elif problem[-1] == '+':
			result = 0
			for item in problem[:-1]:
				result += item
			count += result

	return count


def part2(puzzleInput):
	count = 0

	problems = []
	i = len(puzzleInput[0]) - 1
	numbers = []
	while i >= 0:
		number = ""
		for j in range(0, len(puzzleInput)):
			if puzzleInput[j][i] == ' ':
				continue
			else:
				number += puzzleInput[j][i]

		#print(number)

		if number[-1] == '*' or number[-1] == '+':	
			numbers.append(int(number[:-1]))
			numbers.append(number[-1])
			number = ""
			i -= 1
			problems.append(deepcopy(numbers))
			numbers = []
		else:
			numbers.append(int(number))
		i -= 1
	pprint(problems)

	for problem in problems:
		if problem[-1] == '*':
			result = 1
			for item in problem[:-1]:
				result *= item
			count += result
		elif problem[-1] == '+':
			result = 0
			for item in problem[:-1]:
				result += item
			count += result

	return count


if __name__ == '__main__':
	if len(sys.argv) < 2:
		print("No cookie supplied in sys.argv[1]")
		exit()
	cookie = sys.argv[1]
	today = datetime.datetime.now()
	puzzleInput = util.getInput(today.year, today.day, cookie)
	test = []
	with open(f"{today.year}/test.txt", "r") as file:
		test = file.read().splitlines()

	#print(f"Part one: {part1(puzzleInput)}")
	#print(util.postAnswer(today.year, today.day, 1, part1(puzzleInput), cookie))

	#print(f"Part two: {part2(test)}")
	print(util.postAnswer(today.year, today.day, 2, part2(puzzleInput), cookie))