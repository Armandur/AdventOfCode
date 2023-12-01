import util
import datetime
import sys


def part1(input):
	count = 0
	numbers = []

	for line in input:
		digits = ""
		for character in line:
			try:
				if character.isdigit():
					digits += character
			except:
				pass

		numbers.append(int(f"{digits[0]}{digits[-1]}"))

	count = sum(numbers)

	return count

def part2(input):
	count = 0
	numbers = []
	textnumbers = [("one", 1), ("two", 2), ("three", 3), ("four", 4), ("five", 5), ("six", 6), ("seven", 7), ("eight", 8), ("nine", 9)]

	for line in input:
		leftsearch = []
		rightsearch = []
		for number in textnumbers:
			lposition = line.find(number[0])
			rposition = line.rfind(number[0])

			if lposition != -1:
				leftsearch.append((number[1], lposition))
			
			if rposition != -1:
				rightsearch.append((number[1], rposition))

		#print(leftsearch)
		#print(rightsearch)

		numsearch = []
		for num in range(1,9):
			numpos = line.find(str(num))
			if numpos != -1:
				numsearch.append((num, numpos))
		#print(numsearch)

		if len(leftsearch) == 1 and len(rightsearch) == 1 and len(numsearch) == 0:
			numbers.append(leftsearch[0][0])
			continue

		if len(leftsearch) == 0 and len(numsearch) == 1:
			numbers.append(numsearch[0][0])
			continue

		if len(leftsearch) == 0 and len(numsearch) > 1:
			print(numsearch)
			continue

		firstNumber = leftsearch[0]
		lastNumber = rightsearch[0]

		for number in leftsearch:
			if number[1] < firstNumber[1]:
				firstNumber = number

		for number in rightsearch:
			if number[1] > lastNumber[1]:
				lastNumber = number

		for number in numsearch:
			if number[1] < firstNumber[1]:
				firstNumber = number
			if number[1] > lastNumber[1]:
				lastNumber = number

		print(f"{firstNumber[0]}{lastNumber[0]}")
		numbers.append(int(f"{firstNumber[0]}{lastNumber[0]}"))

	count = sum(numbers)

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