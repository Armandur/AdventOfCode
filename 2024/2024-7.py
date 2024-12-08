import util
import datetime
import sys
from pprint import pprint


Operators = {
	"+": lambda a, b: a+b,
	"*": lambda a, b: a*b,
	"||": lambda a, b: int(str(a)+str(b))
}

def part1(puzzleInput):
	count = 0

	for line in puzzleInput:
		eq = line.split(":")

		def solve(target, parts):
			def rekursionshelvetet(i, rest):
				if rest > target:
					return 0
				
				if i == len(parts):
					if rest == target:
						return target
					else:
						return 0
				
				for operator in Operators:
					if operator == "||":
						continue

					res = rekursionshelvetet(i+1, Operators[operator](rest, parts[i]))

					if res:
						return res	
				return 0
			return rekursionshelvetet(1, parts[0])
		
		result =  solve(int(eq[0]), [int(x) for x in eq[1].split()])
		if result:
			count += result
	
	return count


def part2(puzzleInput):
	count = 0

	for line in puzzleInput:
		eq = line.split(":")

		def solve(target, parts):
			def rekursionshelvetet(i, rest):
				if rest > target:
					return 0
				
				if i == len(parts):
					if rest == target:
						return target
					else:
						return 0
				
				for operator in Operators:
					res = rekursionshelvetet(i+1, Operators[operator](rest, parts[i]))
					
					if res:
						return res	
				return 0
			return rekursionshelvetet(1, parts[0])
		
		result =  solve(int(eq[0]), [int(x) for x in eq[1].split()])
		if result:
			count += result
	
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