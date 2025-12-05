import util
import datetime
import sys
from pprint import pprint


def part1(puzzleInput):
	count = 0
	
	return count


def part2(puzzleInput):
	count = 0
	
	return count


if __name__ == '__main__':
	if len(sys.argv) < 2:
		print("No cookie supplied in sys.argv[1]")
		exit()
	cookie = sys.argv[1]
	
	puzzleInput = util.getInput(2020, 1, cookie)
	test = []
	with open(f"{2020}/test.txt", "r") as file:
		test = file.read().splitlines()

	print(f"Part one: {part1(puzzleInput)}")
	#print(util.postAnswer(2020, 1, 1, part1(puzzleInput), cookie))

	print(f"Part two: {part2(puzzleInput)}")
	#print(util.postAnswer(2020, 2, 2, part2(puzzleInput), cookie))