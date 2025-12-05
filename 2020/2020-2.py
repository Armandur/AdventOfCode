import util
import datetime
import sys
from pprint import pprint


def part1(puzzleInput):
	count = 0

	def checkPassword(password, char, minOccur, maxOccur):
		occurences = password.count(char)
		return occurences >= minOccur and occurences <= maxOccur

	for line in puzzleInput:
		policy, password = line.split(': ')
		rule, char = policy.split(' ')
		minOccur, maxOccur = map(int, rule.split('-'))
		#print(f"Password:\t{password}\nPolicy:\t{policy}\nChar:\t{char}\nMin:\t{minOccur}\nMax:\t{maxOccur}")

		if checkPassword(password, char, minOccur, maxOccur):
			print(f"{minOccur}-{maxOccur} {char}: {password} " + util.colorString("Valid password!", util.colors.green))
			count += 1
		else:
			print(f"{minOccur}-{maxOccur} {char}: {password} " + util.colorString("Invalid password!", util.colors.red))
			pass
	
	return count


def part2(puzzleInput):
	count = 0

	for line in puzzleInput:
		policy, password = line.split(': ')
		rule, char = policy.split(' ')
		firstPos, secondPos = map(int, rule.split('-'))

		firstMatch = password[firstPos - 1] == char
		secondMatch = password[secondPos - 1] == char

		if firstMatch ^ secondMatch:
			print(f"{firstPos}-{secondPos} {char}: {password} " + util.colorString("Valid password!", util.colors.green))
			count += 1
		else:
			print(f"{firstPos}-{secondPos} {char}: {password} " + util.colorString("Invalid password!", util.colors.red))
			pass

	return count


if __name__ == '__main__':
	if len(sys.argv) < 2:
		print("No cookie supplied in sys.argv[1]")
		exit()
	cookie = sys.argv[1]
	
	puzzleInput = util.getInput(2020, 2, cookie)
	test = []
	with open(f"{2020}/test.txt", "r") as file:
		test = file.read().splitlines()

	#print(f"Part one: {part1(puzzleInput)}")
	#print(util.postAnswer(2020, 2, 1, part1(puzzleInput), cookie))

	print(f"Part two: {part2(puzzleInput)}")
	print(util.postAnswer(2020, 2, 2, part2(puzzleInput), cookie))