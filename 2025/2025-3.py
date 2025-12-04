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

	def printPositions(line, positions):
		lineString = ""
		for x, value in enumerate(line):
			if x in positions.values():
				lineString += util.colorString(value, util.colors.green)
			else:
				lineString += value
		print(lineString)

	for line in puzzleInput:
		positions = {
			0 : len(line)-12,
			1 : len(line)-11,
			2 : len(line)-10,
			3 : len(line)-9,
			4 : len(line)-8,
			5 : len(line)-7,
			6 : len(line)-6,
			7 : len(line)-5,
			8 : len(line)-4,
			9 : len(line)-3,
			10 : len(line)-2,
			11 : len(line)-1,
		}

		# Börja med alla positioner längst till höger och flytta sedan en efter en till vänster,
		# börjande med den vänstraste och flytta inte förbi någon position

		for x in positions.keys():
			#print(line[positions[x]])
			if x == 0:
				maxValue = -1
				maxPosition = -1
				for y in range(positions[x], -1, -1):
					if int(line[y]) >= maxValue: # Måste vara >= och inte bara > för att komma längst till vänster
						maxValue = int(line[y])
						maxPosition = y
				positions[x] = maxPosition
			else:
				maxValue = -1
				maxPosition = -1
				for y in range(positions[x], positions[x-1], -1):
					if int(line[y]) >= maxValue:
						maxValue = int(line[y])
						maxPosition = y
				positions[x] = maxPosition
		printPositions(line, positions)
		count += int(''.join([line[positions[i]] for i in range(12)]))
		print()
	return count


if __name__ == '__main__':
	if len(sys.argv) < 2:
		print("No cookie supplied in sys.argv[1]")
		exit()
	cookie = sys.argv[1]
	today = datetime.datetime.now()
	puzzleInput = util.getInput(today.year, 3, cookie)
	test = []
	with open(f"{today.year}/test.txt", "r") as file:
		test = file.read().splitlines()

	#print(f"Part one: {part1(puzzleInput)}")
	#print(util.postAnswer(today.year, 3, 1, part1(puzzleInput), cookie))

	print(f"Part two: {part2(puzzleInput)}")
	print(util.postAnswer(today.year, 3, 2, part2(puzzleInput), cookie))