import util
import copy

def part1():
	input = util.getInput(2021, 3)
	count = 0
	data = [[0, 0],	# [Zeroes, Ones]
			[0, 0],
			[0, 0],
			[0, 0],
			[0, 0],
			[0, 0],
			[0, 0],
			[0, 0],
			[0, 0],
			[0, 0],
			[0, 0],
			[0, 0]]

	for line in input:
		for i, bit in enumerate(line):
			if bit == '0':
				data[i][0] += 1
			else:
				data[i][1] += 1

	gamma = ""
	epsilon = ""

	for point in data:
		if point[0] > point[1]:
			gamma += '0'
			epsilon += '1'
		else:
			gamma += '1'
			epsilon += '0'

	gamma = int(gamma, 2)
	epsilon = int(epsilon, 2)

	count = gamma * epsilon

	return count


def getBits(position, data, mode):
	ones = 0
	zeroes = 0
	for line in data:
		if line[position] == '0':
			zeroes += 1
		elif line[position] == '1':
			ones += 1

	if mode == "most":
		if ones > zeroes:
			return 1
		elif ones < zeroes:
			return 0
		elif ones == zeroes:
			return 1

	elif mode == "least":
		if ones < zeroes:
			return 1
		elif ones > zeroes:
			return 0
		elif ones == zeroes:
			return 0

def part2():
	input = util.getInput(2021, 3)
	#input = ""
	#with open("test.txt") as file:
	#	input = file.read().splitlines()

	oxygen = copy.deepcopy(input)
	co2 = copy.deepcopy(input)

	count = 0

	for i in range(0, len(oxygen[0])): # step through all positions
		templist = []
		#check most common bit in position
		if getBits(i, oxygen, "most") == 0:
			#most common bit is zero, only keep items with zero in position i
			for line in oxygen:
				if line[i] != '0': #if bit in position i is not equal to 0
					templist.append(line)
		else:
			for line in oxygen:
				if line[i] != '1':
					templist.append(line)

		for item in templist:
			oxygen.remove(item)

		if len(oxygen) == 1:
			break


	for i in range(0, len(co2[0])):
		templist = []

		if getBits(i, co2, "least") == 0:
			for line in co2:
				if line[i] != '0':
					templist.append(line)

		else:
			for line in co2:
				if line[i] != '1':
					templist.append(line)

		for item in templist:
			co2.remove(item)

		if len(co2) == 1:
			break


	print(oxygen)
	print(co2)

	oxygen = int(oxygen[0], 2)
	co2 = int(co2[0], 2)

	count = oxygen * co2
	return count


if __name__ == '__main__':
	#print(f"Part one: {part1()}")
	#print(util.postAnswer(2021, 3, 1, part1()))

	print(f"Part two: {part2()}")
	#print(util.postAnswer(2021, 3, 2, part2()))
