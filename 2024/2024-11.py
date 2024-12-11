import util
import datetime
import sys
from pprint import pprint
from functools import cache

def blink(stones : list[int]) -> list[int]:
	newStones = list()

	for stone in stones:
		if stone == 0:
			newStones.append(1)
			continue
		
		stoneString = str(stone)
		length = len(stoneString)
		if length % 2 == 0:
			newStone = [int(stoneString[:length//2]), int(stoneString[length//2:])]
			newStones += newStone
			continue

		newStones.append(stone * 2024)

	return newStones

def part1(puzzleInput):
	count = 0

	stones = list()
	stones = [int(i) for i in puzzleInput[0].split()]
	pprint(stones)

	for i in range(25):
		stones = blink(stones)

	pprint(len(stones))

	return count


stones = dict()

def blink2(stone):
	stoneString = str(stone)
	length = len(stoneString)

	if stone == 0:
		return (1, None)
	
	if length % 2 == 0:
		return (int(stoneString[:length//2]), int(stoneString[length//2:]))
	return (stone * 2024, None)


def calculate(stone, blinks):
	if (stone, blinks) in stones:
		return stones[(stone, blinks)]
	
	leftStone, rightStone = blink2(stone)

	if blinks == 1:
		if rightStone == None:
			return 1
		return 2
	else:
		amount = calculate(leftStone, blinks-1)
		if rightStone is not None:
			amount += calculate(rightStone, blinks-1)
		stones.update({(stone, blinks) : amount})
		return amount
	
def part2(puzzleInput):
	count = 0

	startingStones = [int(i) for i in puzzleInput[0].split()]
	pprint(startingStones)
	for stone in startingStones:
		count += calculate(stone, 75)
	
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