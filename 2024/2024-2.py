import util
import datetime
import sys
from pprint import pprint


def part1(input):
	count = 0

	for line in input:
		previousValue = 0
		previousDelta = ""
		safe = True
		delta = ""

		for index, value in enumerate([int(x) for x in line.split(" ")]):
			if index >= 1:
				if value < previousValue:
					delta = "decr"
				if value > previousValue:
					delta = "incr"
				if value == previousValue:
					delta = "stab"

				print(f"[{index}] : {value} : Δ {delta} - {abs(value - previousValue)}")
				
				if previousDelta and previousDelta != delta:
					print("Change in Δ, Unsafe!")
					safe = False
					break
				
				if abs(value - previousValue) > 3:
					print("To steep Δ, Unsafe!")
					safe = False
					break

				previousDelta = delta
			previousValue = value
		if safe : count += 1
		print()

	return count


def part2(input):
	count = 0
	
	return count


if __name__ == '__main__':
	cookie = sys.argv[1]
	today = datetime.datetime.now()
	input = util.getInput(today.year, today.day, cookie)
	test = []
	with open(f"{today.year}/test.txt", "r") as file:
		test = file.read().splitlines()

	print(f"Part one: {part1(input)}")
	print(util.postAnswer(today.year, today.day, 1, part1(input), cookie))

	print(f"Part two: {part2(input)}")
	#print(util.postAnswer(today.year, today.day, 2, part2(input), cookie))