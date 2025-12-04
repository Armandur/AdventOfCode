import util
import datetime
import sys
from pprint import pprint


def part1(puzzleInput):
	count = 0
	puzzleInput = puzzleInput[0].split(',')
	for _range in puzzleInput:
		start, end = map(int, _range.split('-'))
		print (f"Range:\t{start}-{end}")
		for i in range(start, end + 1):
			firstHalf = str(i)[:len(str(i))//2]
			secondHalf = str(i)[(len(str(i))+1)//2:]
			#pprint (f"  Number: {i}, First half: {firstHalf}, Second half: {secondHalf}")
			if firstHalf == secondHalf and len(str(i)) % 2 == 0:
				print (f"\tMatch: {util.colorString(firstHalf, util.colors.green)} {util.colorString(secondHalf, util.colors.green)}")
				count += i
		print()

	return count

def part2(puzzleInput):
	count = 0
	puzzleInput = puzzleInput[0].split(',')
	for _range in puzzleInput:
		start, end = map(int, _range.split('-'))
		print("----------------")
		print (f"Range:\t{start}-{end}")
		print("----------------")
		for i in range(start, end + 1):
			halfLen = len(str(i)) // 2
			for j in range(1, halfLen+1):
				if len(str(i)) % j != 0:
					continue
				substr = str(i)[:j]
				#print(f"Comparing {str(i)[:j]}\tin\t{str(i)}")
				if substr * (len(str(i)) // j) == str(i):
					count += i
					print(util.colorString("***", util.colors.green))
					print (f"Match:\t{util.colorString(substr, util.colors.green)} repeated {len(str(i)) // j} times to form {str(i)}")
					print(util.colorString("***", util.colors.green))
					print()
					break
				
		print()
	
	return count


if __name__ == '__main__':
	if len(sys.argv) < 2:
		print("No cookie supplied in sys.argv[1]")
		exit()
	cookie = sys.argv[1]
	today = datetime.datetime.now()
	puzzleInput = util.getInput(today.year, 2, cookie)
	test = []
	with open(f"{today.year}/test.txt", "r") as file:
		test = file.read().splitlines()

	#print(f"Part one: {part1(puzzleInput)}")
	#print(util.postAnswer(today.year, 2, 1, part1(puzzleInput), cookie))

	#print(f"Part two: {part2(puzzleInput)}")
	#print(util.postAnswer(today.year, 2, 2, part2(puzzleInput), cookie))