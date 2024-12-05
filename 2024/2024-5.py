import util
import datetime
import sys
from pprint import pprint


def part1(puzzleInput):
	count = 0
	rules = []
	updates = []

	for lineNumber, line in enumerate(puzzleInput):
		if line != "":
			rules.append(line)
		else:
			updates = puzzleInput[lineNumber+1:]
			break

	beforeRules = {}
	afterRules = {}
	for rule in rules:
		r = [int(x) for x in rule.split('|')]
		if r[0] not in beforeRules:
			beforeRules[r[0]] = [r[1]]
		else:
			beforeRules[r[0]].append(r[1])
		
		if r[1] not in afterRules:
			afterRules[r[1]] = [r[0]]
		else:
			afterRules[r[1]].append(r[0])
	#print("Left")
	#pprint(afterRules)
	#print("Right")
	#pprint(beforeRules)
	#print()
	#pprint(updates)

	validRules = []

	for update in updates:
		upd = [int(x) for x in update.split(',')]
		print("Update "+util.colorString(upd, util.colors.green))
		afterValid = True
		beforeValid = True
		for page in upd:
			if page in afterRules.keys():
				print(util.colorString(page, util.colors.cyan) + " after " + str(afterRules[page]))
				for rule in afterRules[page]:
					if rule in upd:
						print("Rule: " + util.colorString(rule, util.colors.cyan) + " should come before Page: " + util.colorString(page, util.colors.green) + " checking...")
						pagePos = upd.index(page)
						rulePos = upd.index(rule)
						print(f"Page: {pagePos} > Rule: {rulePos}")
						if not pagePos > rulePos:
							print(util.colorString("Rule broken!", util.colors.red))
							afterValid = False
							break
			
				if afterValid == False:
					break
			
			if afterValid == False:
					break
			#if page in beforeRules.keys():
			#	print(util.colorString(page, util.colors.cyan) + " before " + str(beforeRules[page]))
		if afterValid:
			validRules.append(upd)
		print()

	pprint(validRules)
	for rule in validRules:
		print(rule[int(len(rule)/2)])
		count += rule[int(len(rule)/2)]
	
	return count


def part2(puzzleInput):
	count = 0
	
	return count


if __name__ == '__main__':
	cookie = sys.argv[1]
	today = datetime.datetime.now()
	puzzleInput = util.getInput(today.year, today.day, cookie)
	test = []
	with open(f"{today.year}/test.txt", "r") as file:
		test = file.read().splitlines()

	print(f"Part one: {part1(puzzleInput)}")
	print(util.postAnswer(today.year, today.day, 1, part1(puzzleInput), cookie))

	print(f"Part two: {part2(puzzleInput)}")
	#print(util.postAnswer(today.year, today.day, 2, part2(puzzleInput), cookie))