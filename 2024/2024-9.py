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

	#diskmapstring = ""
	#for block in diskMap:
	#	diskmapstring += str(block[0]) * block[1]

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
	position = 0
	for block in diskMap:
		if block[0] == ".":
			position += block[1]
			continue
		for n in range(position, block[1]+position):
			count += block[0] * n
		position += block[1]

	return count

def part2(puzzleInput):
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
		#	if int(puzzleInput[index]) > 0: # WTF, add freespace blocks even if space is 0 ???
			diskMap.append([".", int(puzzleInput[index])])

		index += 1

		if state == "file":
			state = "freespace"
		elif state == "freespace":
			state = "file"

	#diskmapstring = ""
	#for block in diskMap:
	#	diskmapstring += str(block[0]) * block[1]
	#print(diskmapstring)

	index = len(diskMap)-1
	#pprint(diskMap[index])

	def getFirstEmptyIndex(size):
		for index, i in enumerate(diskMap):
			if i[0] == "." and i[1] >= size:
				return index
		return -1

	while index != 0:
		current = diskMap[index]

		if diskMap[index][0] == ".":
			index -= 1
			continue
		
		#diskmapstring = ""
		#for block in diskMap:
		#	diskmapstring += str(block[0]) * block[1]
		#print(diskmapstring)

		searchSize = diskMap[index][1]
		firstEmptySpaceIndex = getFirstEmptyIndex(searchSize)

		if firstEmptySpaceIndex > index or firstEmptySpaceIndex == -1:
			index -= 1
			continue

		firstEmptySpace = diskMap[firstEmptySpaceIndex]
		
		if diskMap[index][1] < firstEmptySpace[1]:
			diskMap.insert(firstEmptySpaceIndex, diskMap.pop(index))
			insertedElement = diskMap[firstEmptySpaceIndex]
			firstEmptySpace[1] -= insertedElement[1]
			diskMap.insert(index+1, [".", insertedElement[1]])
			index -= 1
			continue

		if diskMap[index][1] == firstEmptySpace[1]:
			diskMap.insert(firstEmptySpaceIndex, diskMap.pop(index))
			diskMap.insert(index, diskMap.pop(firstEmptySpaceIndex+1))
			index -= 1
			continue

		index -= 1

	diskmapstring = ""
	for block in diskMap:
		diskmapstring += str(block[0]) * block[1]
	print(diskmapstring)

	count = 0
	position = 0
	for block in diskMap:
		if block[0] == ".":
			position += block[1] # Increase the position by the amount of free space (stored as a number in block[1])
			continue
		for n in range(position, block[1]+position):
			count += block[0] * n
		position += block[1]
	return count


if __name__ == '__main__':
	cookie = sys.argv[1]
	today = datetime.datetime.now()
	puzzleInput = util.getInput(today.year, today.day, cookie)
	test = []
	with open(f"{today.year}/test.txt", "r") as file:
		test = file.read().splitlines()

	print(f"Part one: {part1(test)}")
	#print(util.postAnswer(today.year, today.day, 1, part1(puzzleInput), cookie))

	print(f"Part two: {part2(puzzleInput)}")
	#print(util.postAnswer(today.year, today.day, 2, part2(puzzleInput), cookie))