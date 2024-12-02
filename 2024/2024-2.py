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

		print(util.colorString(line, util.colors.cyan))
		for index, value in enumerate([int(x) for x in line.split(" ")]):
			if index >= 1:
				if value < previousValue:
					delta = "decr"
				if value > previousValue:
					delta = "incr"
				if value == previousValue:
					delta = "stab"
				
				if previousDelta and previousDelta != delta:
					print("Change in Δ, Unsafe!")
					safe = False
					break
				
				if abs(value - previousValue) > 3:
					print("To steep Δ, Unsafe!")
					safe = False
					break
				previousDelta = delta
			print(f"[{index}] : {value} : Δ {delta} - {abs(value - previousValue)}")
			previousValue = value
		if safe : count += 1
		print()

	return count


def part2(input):
	count = 0

	def checkReport(lineNumber, line):
		previousValue = 0
		previousDelta = ""
		delta = ""
		
		print(f"Report {lineNumber+1}\n" + util.colorString(line, util.colors.cyan))
		report = line
		for index, value in enumerate(report):
			if not index:
				print(f"[{index}] : {value} :\tΔ {delta}\t- {abs(value - previousValue)}")
			
			if index >= 1:
				if value < previousValue:
					delta = "decr"
				if value > previousValue:
					delta = "incr"
				if value == previousValue:
					delta = "stab"
				
				print(f"[{index}] : {value} :\tΔ {delta}\t- {abs(value - previousValue)}")
				
				if (delta == "stab"):
					print(util.colorString(f"No Δ, Error!", util.colors.red))
					return ("Error", index)
				
				if (previousDelta and previousDelta != delta):
					print(util.colorString(f"Change in Δ, Error!", util.colors.red))
					return ("Error", index)
				
				if abs(value - previousValue) > 3:
					print(util.colorString(f"To steep Δ, Error!", util.colors.red))
					return ("Error", index)
				previousDelta = delta
			previousValue = value
		return ("Safe", -1)

	for lineNumber, line in enumerate(input):
		line = [int(x) for x in line.split(" ")]
		errors = 0
		result = checkReport(lineNumber, line)
		
		if result[0] == "Error":
			errors +=1
			newReport = line.copy()
			newReport.pop(result[1])

			print(util.colorString(f"Error in report, removing value {line[result[1]]} at [{result[1]}]", util.colors.red))
			print(util.colorString(f"Dampened report: {newReport}, running again...", util.colors.yellow))
			result = checkReport(lineNumber, newReport)
			if result[0] == "Safe":
				print(util.colorString(f"Report {lineNumber+1} within tolerances!", util.colors.green))
				count += 1
			else:
				print(util.colorString(f"Report {lineNumber+1} above tolerances!", util.colors.red))
		else:
			print(util.colorString(f"Report {lineNumber+1} within tolerances!", util.colors.green))
			count +=1
		print(util.colorString("---------------------", util.colors.magenta))
		print("Total safe reports: " + util.colorString(count, util.colors.magenta))
		print()
	return count


if __name__ == '__main__':
	cookie = sys.argv[1]
	today = datetime.datetime.now()
	input = util.getInput(today.year, today.day, cookie)
	test = []
	with open(f"{today.year}/test.txt", "r") as file:
		test = file.read().splitlines()

	#print(f"Part one: {part1(test)}")
	#print(util.postAnswer(today.year, today.day, 1, part1(input), cookie))

	print(f"Part two: {part2(input)}")
	#print(util.postAnswer(today.year, today.day, 2, part2(input), cookie))