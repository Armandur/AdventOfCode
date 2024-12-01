import util
import datetime
import sys
from pprint import pprint


def part1(input):
	count = 0

	left = []
	right = []

	for line in input:
		left.append([int(x) for x in line.split("   ")][0])
		right.append([int(x) for x in line.split("   ")][1])
	left.sort()
	right.sort()

	for index, x in enumerate(left):
		pprint(f"{left[index]} {right[index]} : {abs(left[index] - right[index])}")
		count += abs(left[index] - right[index])
	return count


def part2(input):
	count = 0
	
	left = []
	right = []

	for line in input:
		left.append([int(x) for x in line.split("   ")][0])
		right.append([int(x) for x in line.split("   ")][1])
	
	for x in left:
		pprint(f"{x} : {right.count(x)}")
		count += x * right.count(x)

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