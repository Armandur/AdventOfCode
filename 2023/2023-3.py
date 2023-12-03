import util
import datetime
import sys
from pprint import pprint

def printSchematic(schematic):
	for line in schematic:
		printline = ""
		for char in line:
			if type(char) == int:
				printline += util.colorString(char, util.colors.green)
			elif char == '.':
				printline += char
			else:
				printline += util.colorString(char, util.colors.red)
		print(printline)

def part1(input):
	count = 0
	schematic = []
    
	#Add input to 2d array
	for line in input:
		row = []
		row.append('.')
		for char in line:
			if char.isdigit():
				row.append(int(char))
			else:
				row.append(char)
		row.append('.')
		schematic.append(row)

	
	# pad array with one . around edges
	schematic.insert(0, list("." * (len(schematic[0]))))
	schematic.insert(len(schematic), list("." * (len(schematic[0]))))
	printSchematic(schematic)

	# get all numbers, and coordinates of numbers and add to list?
	numbers = [] # (467, (1, 2))

	for y in range(1, len(schematic)-1): # -1, we don't need padded sides
		number = ""
		coordinates = (0,0)
		for x in range(1, len(schematic[0])-1): # -1, we don't need padded sides
			
			if len(number) >= 0 and type(schematic[y][x]) == int: # Either starting or continuing on a number
				if len(number) == 0: # Beginning number, we should note the coords
					coordinates = (x, y)
				
				number += str(schematic[y][x])
				
				if type(schematic[y][x+1]) != int: # We are at the end of the number, push to numbers [] and reset.
					numbers.append((int(number), coordinates))
					number = ""
					coordinates = (0, 0)
	#pprint(numbers)

	# Iterate over the found numbers, and "drive around" the coordinates, padding the array should have helped here

	parts = []
	for number in numbers:
		currentNumber = number[0]
		x = number[1][0]
		y = number[1][1]

		#....
		#.22.
		#....
		# rows to check is len(currentNumber)+2
		# cols is alwways three (y-1, y, y+1)
		# coords is always first number so first row to check is x-1
		# range is therefore x-1 to x+(len(str(currentNumber))+1)
		xRange = range(x-1, x+len(str(currentNumber))+1)
		yRange = range(y-1, y+2)
		
		#print(f"{currentNumber}, {x},{y}")
		
		symbolFound = False
		
		# Searching around the number
		for searchY in yRange:
			for searchX in xRange:
				current = schematic[searchY][searchX]
				if type(current) != int and current != '.':
					symbolFound = True
					parts.append(currentNumber)
					break

			if symbolFound:
				break

	count = sum(parts)

	return count


def part2(input):
	count = 0

	return count


if __name__ == '__main__':
	cookie = sys.argv[1]
	today = datetime.datetime.now()
	input = util.getInput(today.year, today.day, cookie)
	test = []
	with open(f"{today.year}/test.txt", "r") as file:
		test = file.read().splitlines()

	print(f"Part one: {part1(input)}")
	print(util.postAnswer(today.year, today.day, 1, part1(input), cookie))

	print(f"Part two: {part2(input)}")
	#print(util.postAnswer(today.year, today.day, 2, part2(input), cookie))