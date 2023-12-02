import util
import datetime
import sys
from pprint import pprint


def part1(input):
	count = 0
	games = []
	
	#save only the max number of cubes shown in each game?

	for line in input:
		cubes = {}
		id = int(line.split(':')[0].split(' ')[1])
		rounds = line.split(": ")[1].split('; ')
		#print(rounds) # ['3 blue, 4 red', '1 red, 2 green, 6 blue', '2 green']
		for round in rounds:
			pairs = round.split(', ')
			#print(pairs) # ['3 blue', '4 red']
			for pair in pairs:
				amount = int(pair.split(' ')[0])
				color = pair.split(' ')[1]
				if color in cubes and amount > cubes[color]:
					cubes[color] = amount
				elif color not in cubes:
					cubes[color] = amount
		games.append((id, cubes))
	pprint(games)
	
	check = \
	{
		"red": 12,
		"green": 13,
		"blue": 14
	}

	for game in games:
		red = False
		green = False
		blue = False
		for color in check.keys():
			if color in game[1] and game[1][color] <= check[color]:
				if color == "red": red = True
				if color == "green": green = True
				if color == "blue": blue = True
		if red and green and blue:
			count += game[0]
	
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