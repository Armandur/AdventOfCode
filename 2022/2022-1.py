import util
import datetime
import sys


def part1(input):
	count = 0

	elves = []

	sum = 0
	for line in input:
		if line != "":
			sum += int(line)
		else:
			elves.append(sum)
			sum = 0

	if input[-1] != "":
		elves.append(int(input[-1]))

	count = max(elves)

	return count


def part2(input):
	count = 0

	elves = []

	_sum = 0
	for line in input:
		if line != "":
			_sum += int(line)
		else:
			elves.append(_sum)
			_sum = 0

	if input[-1] != "":
		elves.append(int(input[-1]))

	elves.sort(reverse=True)

	count = sum(elves[0:3])

	return count


if __name__ == '__main__':
	cookie = sys.argv[1]
	today = datetime.datetime.now()
	input = util.getInput(today.year, today.day, cookie)
	test = []
	with open("2022/test.txt", "r") as file:
		test = file.read().splitlines()

	print(f"Part one: {part1(input)}")
	#print(util.postAnswer(today.year, today.day, 1, part1(input), cookie))

	print(f"Part two: {part2(input)}")
	#print(util.postAnswer(today.year, today.day, 2, part2(input), cookie))