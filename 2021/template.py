import util
import datetime
import sys


def part1(input):
	count = 0

	return count


def part2(input):
	count = 0

	return count


if __name__ == '__main__':
	cookie = sys.argv[1]
	today = datetime.datetime.now()
	input = util.getInput(today.year, today.day)
	test = []
	with open("test.txt", "r") as file:
		test = file.read().splitlines()

	print(f"Part one: {part1(input)}")
	#print(util.postAnswer(today.year, today.day, 1, part1(input)))

	print(f"Part two: {part2(input)}")
	#print(util.postAnswer(today.year, today.day, 2, part2(input)))