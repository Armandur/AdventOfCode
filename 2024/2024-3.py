import util
import datetime
import sys
import os
from pprint import pprint
import time


def highLightPosition(line, start, end, color):
	ws1 = line[:end] +  "\033[0m" + line[end:]
	ws2 = ws1[:start] + "\033[" + color + ws1[start:]
	return ws2

def part1(input):
	count = 0
	for line in input:
		index = line.find("mul(")
		positions = []
		factors = []
		while index != -1:
			# print(f"mul( found at index {index}")
			positions.append(index)
			index = line.find("mul(", index+len("mul("))
			# print(highLightPosition(line, index+len("mul("), len(line), util.colors.yellow))
			# time.sleep(0.2)
			# os.system("cls")
		#pprint(positions)
		#time.sleep(2)
		for position in positions:
			# mul(1,1)
			# mul(123,123)
			print(f"Checking position {position}")
			# print(highLightPosition(line, position, position+len("mul("), util.colors.cyan))
			#time.sleep(0.2)
			# os.system("cls")
			# print(highLightPosition(line, position+len("mul(")+3, position+len("mul(")+8, util.colors.yellow))
			# time.sleep(0.2)
			# os.system("cls")
			endParenthesis = line.find(")", position+len("mul(")+3, position+len("mul(")+8)
			if endParenthesis != -1:
				#print(highLightPosition(highLightPosition(line, position, position+1, util.colors.cyan), endParenthesis+9, endParenthesis+10, util.colors.magenta))
				#print(line[position+len("mul(")+3:position+len("mul(")+7])
				#print(line[position:endParenthesis+1])
				#os.system("cls")
				
				operation = line[position+len("mul("):endParenthesis]
				try:
					if len(operation.split(',')) > 1:
						if " " not in operation.split(',')[0] and " " not in operation.split(',')[1]:
							factors.append([int(x) for x in operation.split(',')])
							print(highLightPosition(line, position, endParenthesis+1, util.colors.green))
				except ValueError:
					pass
				#time.sleep(1)
				#os.system("cls")
		for operation in factors:
			count += operation[0]*operation[1]
		print(f"Found, valid factors {factors}")
		print(f"Sum of products: {count}")
		print()
		time.sleep(2)
		os.system("cls")
	return count


def part2(input):
	count = 0
	program = []
	for line in input:
		index = line.find("mul(")
		positions = []
		operations = []
		while index != -1:
			positions.append(index)
			index = line.find("mul(", index+len("mul("))
		for position in positions:
			endParenthesis = line.find(")", position+len("mul(")+3, position+len("mul(")+8)
			if endParenthesis != -1:				
				operation = line[position+len("mul("):endParenthesis]
				try:
					if len(operation.split(',')) > 1:
						if " " not in operation.split(',')[0] and " " not in operation.split(',')[1]:
							operations.append((position, [int(x) for x in operation.split(',')]))
				except ValueError:
					pass

		# Part 2 All mul() operations found, search for all do() and don't()
		index = line.find("do()")
		while index != -1:
			operations.append((index, ("do()")))
			index = line.find("do()", index+len("do()"))
		
		index = line.find("don't()")
		while index != -1:
			operations.append((index, ("don't()")))
			index = line.find("don't()", index+len("don't()"))
		program.append(operations)

	for line in program:
		line.sort(key=lambda x: x[0])
	
	do = True
	for line in program:
		for operation in line:
			if operation[1] == "do()":
				do = True
			elif operation[1] == "don't()":
				do = False
			else:
				if do:
					count += operation[1][0] * operation[1][1]
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