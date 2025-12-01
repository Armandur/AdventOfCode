import util
import datetime
import sys
from pprint import pprint


def part1(puzzleInput):
	count = 0
	
	dial = 50

	def turnDial(direction, steps):
		nonlocal dial
		if steps > 99:
			steps = steps % 100
			#print(util.colorString(f"Steps reduced to {steps}", util.colors.brightyellow))

		if direction == "R":
			if dial + steps > 99:
				dial += steps - 100
			else:
				dial += steps
		elif direction == "L":
			if dial - steps < 0:
				dial -= steps - 100
			else:
				dial -= steps
		
	#print(util.colorString(dial, util.colors.brightred))
	for line in puzzleInput:
		turnDial(line[0], int(line[1:]))
		if dial == 0:
			#print(util.colorString(dial, util.colors.brightgreen))
			count += 1
		else:
			#pprint(dial)
			pass

	return count


def part2(puzzleInput):
	count = 0
	
	dial = 50

	def turnDial(direction, steps):
		nonlocal dial
		nonlocal count

		previousDial = dial

		# Om vi vrider flera varv kan vi spara antalet varv baserat på hundratalet
		# och sedan använda tio- och entalen för vidare stegning
		if steps > 99:
			count += (steps // 100)
			steps = steps % 100

		if direction == "R":
			dial = dial + steps
		elif direction == "L":
			dial = dial - steps
		
		# Vi har vridit ratten förbi 0 eller 99, wrappa runt
		if dial >= 100 or dial <= 0:
			dial = dial % 100

			# Kolla om vi rört på oss och att vi inte började på 0 och alltså kommit tillbaka till 0
			if dial != previousDial and previousDial != 0:
				count += 1
				
	print(util.colorString(dial, util.colors.brightred))
	for line in puzzleInput:
		print(util.colorString(f"{line[0]} : {int(line[1:])}", util.colors.brightyellow))
		turnDial(line[0], int(line[1:]))
		if dial == 0:
			print(util.colorString(dial, util.colors.brightgreen) + f"\t:\t{count}")
		else:
			print( f"{dial}\t:\t{count}")
			pass

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
	#print(util.postAnswer(today.year, today.day, 1, part1(puzzleInput), cookie))

	#print(f"Part two: {part2(puzzleInput)}")
	print(util.postAnswer(today.year, today.day, 2, part2(puzzleInput), cookie))