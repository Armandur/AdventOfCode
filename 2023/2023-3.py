import util
import datetime
import sys
from pprint import pprint
import collections
import math

# Moved to global to be able to be used in part2()
schematic = []
partnumbersAdjacentToGears = []

def printSchematic(schematic):
	for line in schematic:
		printline = ""
		for char in line:
			if type(char) == int:
				printline += util.colorString(char, util.colors.green)
			elif char == '.':
				printline += char
			elif char == '*':
				printline += util.colorString(char, util.colors.yellow)
			else:
				printline += util.colorString(char, util.colors.red)
		print(printline)

def part1(input):
	count = 0

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
	#printSchematic(schematic)

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
					
					# For part2, attach the surrounding coordinates to the partnumber and add to a list
					# surroundingCoords = [] Only seems to be at most one * in contact
					surroundingCoords = ()
					for y_ in yRange:
						for x_ in xRange: # Only add if char at x_, y_ is a *
							if schematic[y_][x_] == "*":
								# surroundingCoords.append((x_, y_)) Only seems to be one * in contact
								surroundingCoords = (x_, y_) 

					if surroundingCoords:
						partnumbersAdjacentToGears.append((currentNumber, surroundingCoords))
					break
					## End for part 2

			if symbolFound:
				break

	count = sum(parts)

	return count


def part2(input):
	count = 0
	#printSchematic(schematic)
	#pprint(partnumbersAdjacentToGears)
	#print()

	adjacentGears = list(list(zip(*partnumbersAdjacentToGears))[1])
	#pprint(adjacentGears)

	 # Count all the occurences of a gear-coordinate,
	 # if a coordinate is counted twice it is adjacent to two part number
	counter = collections.Counter(adjacentGears)

	doubleAdjacentGearCoords = []

	for coordinate in counter:
		if counter[coordinate] == 2:
			doubleAdjacentGearCoords.append(coordinate)

	#print()
	#pprint(doubleAdjacentGearCoords)
	pairs = {}
	for part in partnumbersAdjacentToGears[:]:
		if part[1] in doubleAdjacentGearCoords:
			if part[1] not in pairs.keys():
				pairs[part[1]] = [part[0]]
			else:
				pairs[part[1]].append(part[0])
	#print()
	
	#pprint(pairs)

	#print()

	for pair in pairs:
		#print(math.prod(pairs[pair]))
		count += math.prod(pairs[pair])
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