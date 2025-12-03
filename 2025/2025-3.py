import util
import datetime
import sys
from pprint import pprint


def part1(puzzleInput):
	count = 0
	for line in puzzleInput:
		joltages = []
		for x, joltage in enumerate(line):
			#print(f"Checking joltage {joltage} at index {x}")
			
			mappedJoltage = [int(y) for y in line[x+1:]]
			if mappedJoltage == []:
				continue
			#print(f"Mapped joltage list: {mappedJoltage}")

			maxSecondBatteryJoltage = max(mappedJoltage)
			#print()
			#print(f"Max second battery joltage: {maxSecondBatteryJoltage}")
			
			combinedJoltage = joltage + str(maxSecondBatteryJoltage)
			joltages.append(int(combinedJoltage))

			#print(f"Combined joltage: {int(combinedJoltage)}")
			#print()
		print(f"Max joltage combination {util.colorString(str(max(joltages)), util.colors.green)}")
		print()
		count += max(joltages)
	
	return count


def part2(puzzleInput):
	count = 0
	
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
	print(util.postAnswer(today.year, today.day, 1, part1(puzzleInput), cookie))

	#print(f"Part two: {part2(puzzleInput)}")
	#print(util.postAnswer(today.year, today.day, 2, part2(puzzleInput), cookie))