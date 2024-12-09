import util
import datetime
import sys
from pprint import pprint

def part1(puzzleInput):
	puzzleInput = puzzleInput[0]

	index = 0
	state = "file" #file/freespace

	diskMap = list()
	id = 0

	while index < len(puzzleInput):
		if state == "file":
			diskMap.append([id, int(puzzleInput[index])])
			id += 1

		if state == "freespace":
			diskMap.append([".", int(puzzleInput[index])])

		index += 1

		if state == "file":
			state = "freespace"
		elif state == "freespace":
			state = "file"

	diskmapstring = ""
	for block in diskMap:
		diskmapstring += str(block[0]) * block[1]

	#print(diskmapstring)

	while True:
		lastElement = diskMap[-1]
		blocks = [id[0] for id in diskMap]
		if "." not in blocks:
			break

		firstEmptySpaceIndex = blocks.index(".")
		firstEmptySpace = diskMap[firstEmptySpaceIndex]

		if lastElement[0] == ".":
			diskMap.pop(-1)
			continue

		if lastElement[1] <= firstEmptySpace[1]:
			diskMap.insert(firstEmptySpaceIndex, lastElement)
			firstEmptySpace[1] -= lastElement[1]
			if firstEmptySpace[1] == 0:
				diskMap.pop(firstEmptySpaceIndex+1)
			diskMap.pop(-1)

		elif lastElement[1] > firstEmptySpace[1]:
			diskMap.insert(firstEmptySpaceIndex, [lastElement[0], firstEmptySpace[1]])
			lastElement[1] -= firstEmptySpace[1]
			diskMap.pop(firstEmptySpaceIndex + 1)
		
		# diskmapstring = ""
		# for block in diskMap:
		# 	diskmapstring += str(block[0]) * block[1]
		# print(diskmapstring)

	diskmapstring = ""
	for block in diskMap:
		diskmapstring += str(block[0]) * block[1]
	
	#print(diskmapstring)
	#pprint(diskMap)
	count = 0
	id = 0
	for block in diskMap:
		if block[0] == ".":
			continue
		for n in range(id, block[1]+id):
			count += block[0] * n
		id = id + block[1]

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
	#print(util.postAnswer(today.year, today.day, 1, part1(puzzleInput), cookie))

	print(f"Part two: {part2(puzzleInput)}")
	#print(util.postAnswer(today.year, today.day, 2, part2(puzzleInput), cookie))