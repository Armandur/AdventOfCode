import util
import datetime
import sys


def part1(input):
	count = 0
	numbers = []

	for line in input:
		digits = ""
		for character in line:
			if character.isdigit():
				digits += character
		numbers.append(int(f"{digits[0]}{digits[-1]}"))

	count = sum(numbers)

	return count

def part2(input):
	count = 0
	numbers = []
	textnumbers = [("one", 1), ("two", 2), ("three", 3), ("four", 4), ("five", 5), ("six", 6), ("seven", 7), ("eight", 8), ("nine", 9)]

	for line in input:
		search = []

		for number in textnumbers:
			_lfind = line.find(number[0])
			_rfind = line.rfind(number[0])

			if _lfind != -1:
				search.append((number[1], _lfind))
			if _rfind != -1:
				search.append((number[1], _rfind))

		for character in enumerate(line):
			if character[1].isdigit():
				search.append((int(character[1]), character[0]))

		search.sort(key=lambda x: x[1])
		firstNumber = search[0][0]
		lastNumber = search[-1][0]
		numbers.append(int(f"{firstNumber}{lastNumber}"))
		#print(search)

	#print(numbers)

	count = sum(numbers)

	return count


if __name__ == '__main__':
	cookie = sys.argv[1]
	today = datetime.datetime.now()
	input = util.getInput(today.year, today.day, cookie)
	test = []
	with open(f"{today.year}/test.txt", "r") as file:
		test = file.read().splitlines()

	print(f"Part one: {part1(input)}")
	#print(util.postAnswer(today.year, today.day, 1, part1(input), cookie))

	print(f"Part two: {part2(input)}")
	#print(util.postAnswer(today.year, today.day, 2, part2(input), cookie))