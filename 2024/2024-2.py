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
	def isSafe(report):
		deltas = []
		for i in range(len(report)):
			try:
				a = report[i]
				b = report[i+1]
				#print(f"{b} - {a} = {b - a}")
				deltas.append(b - a)
			except IndexError:
				continue
		deltaString = "["
		for index, delta in enumerate(deltas):
			if delta > 0:
				deltaString += util.colorString(delta, util.colors.green)
			elif delta < 0:
				deltaString += util.colorString(delta, util.colors.red)
			else:
				deltaString += util.colorString(delta, util.colors.yellow)
			if index < len(deltas)-1:
				deltaString += ", "
		deltaString += "]"
		print(util.colorString("Calculated Δ's: ", util.colors.cyan) + deltaString)
		return all(1 <= delta <= 3 for delta in deltas) or all(-3 <= delta <= -1 for delta in deltas)
	
	count = 0
	for linenumber, line in enumerate(input):
		report = [int(x) for x in line.split(" ")]
		print(f"Testing report {linenumber+1}\n" + util.colorString(report, util.colors.cyan))
		if isSafe(report):
			count += 1
			print(util.colorString("Safe! ", util.colors.green) + "Total safe reports: " +  util.colorString(count, util.colors.magenta))
		else:
			print()
			print(util.colorString("Not safe! ", util.colors.red) + util.colorString("Engaging dampener!", util.colors.yellow))
			broken = False
			for i in range(len(report)):
				testlist = report.copy()
				testlist.pop(i)
				if isSafe(testlist):
					count += 1
					print(util.colorString("Within tolerance! ", util.colors.green) + "Total safe reports: " +  util.colorString(count, util.colors.magenta))
					broken = True
					break
			if not broken:
				print(util.colorString("Above tolerance! ", util.colors.red) + "Total safe reports: " +  util.colorString(count, util.colors.magenta))
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