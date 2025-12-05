import util
import datetime
import sys
from pprint import pprint


def part1(puzzleInput):
	count = 0
	freshRanges = []
	for line in puzzleInput:
		if '-' in line:
			freshRanges.append(tuple(int(x) for x in line.split('-')))
		elif '' == line:
			pprint(freshRanges)
			continue
		else:
			ingredient = int(line)
			fresh = False
			for freshRange in freshRanges:
				if freshRange[0] <= ingredient <= freshRange[1]:
					fresh = True
					count += 1
					break
			if not fresh:
				print((util.colorString(f"{ingredient}", util.colors.brightred)))
			else:
				print((util.colorString(f"{ingredient}", util.colors.brightgreen)))
	
	return count


def part2(puzzleInput):
	count = 0
	freshRanges = []

	for line in puzzleInput:
		if '-' in line:
			freshRanges.append([int(x) for x in line.split('-')])
		elif '' == line:
			#pprint(freshRanges)
			freshRanges.sort()
			#pprint(freshRanges)
			break
	
	i = 0
	while True:
		if i >= len(freshRanges) - 1:
			break
		currentRange = freshRanges[i]
		nextRange = freshRanges[i + 1]
		if currentRange[1] >= nextRange[0] - 1:
			freshRanges[i] = [currentRange[0], max(currentRange[1], nextRange[1])]
			del freshRanges[i + 1]
		else:
			i += 1
	#pprint(freshRanges)

	for range in freshRanges:
		count += (range[1] - range[0] + 1)

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

	#print(f"Part two: {part2(test)}")
	print(util.postAnswer(today.year, today.day, 2, part2(puzzleInput), cookie))