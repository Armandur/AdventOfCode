import util
import datetime
import sys


lowerDelta = 96
upperDelta = 38


def part1(input):
	count = 0

	for line in input:
		container1 = line[:len(line)//2]
		container2 = line[len(line)//2:]
		
		container1 = [*container1]
		container2 = [*container2]

		common = list(set(container1) & set(container2))[0]
		
		priority = 0
		if common.islower():
			priority = ord(common)-lowerDelta
		else:
			priority = ord(common)-upperDelta
		
		#print(f"{common} - {priority}")
		count += priority
		
	return count


def part2(input):
	count = 0

	group = []
	for num, line in enumerate(input):
		if num % 3 == 2: #Third line in group
			group.append(line)

			common = list(set(group[0]) & set(group[1]) & set(group[2]))[0]
			
			priority = 0
			if common.islower():
				priority = ord(common)-lowerDelta
			else:
				priority = ord(common)-upperDelta
		
			#print(f"{common} - {priority}")
			count += priority		

			group = []
		else:
			group.append(line)	

	return count


if __name__ == '__main__':
	cookie = sys.argv[1]
	today = datetime.datetime.now()
	input = util.getInput(today.year, today.day, cookie)
	test = []
	with open(f"{today.year}/test.txt", "r") as file:
		test = file.read().splitlines()

	print(f"Part one: {part1(input)}")
	#print(util.postAnswer(today.year, today.day, 1, part1(input), cookie))

	print(f"Part two: {part2(input)}")
	#print(util.postAnswer(today.year, today.day, 2, part2(input), cookie))