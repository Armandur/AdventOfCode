import util
import datetime
import sys


def part1(input):
    count = 0
    
    for line in input:
        #Turn lines into listed lists of ints 2-4,6-8 => [[2, 4], [6, 8]]
        pair = [list(map(int, line.split(',')[0].split('-'))), list(map(int, line.split(',')[1].split('-')))]

        #Turn into sets of the ranges
        pair[0] = set(range(pair[0][0], pair[0][1]+1))
        pair[1] = set(range(pair[1][0], pair[1][1]+1))

        #print(f"{pair[0]} - {pair[1]}")
        if (pair[0].issubset(pair[1]) or pair[1].issubset(pair[0])):
            count += 1

    return count


def part2(input):
    count = 0
    
    for line in input:
        #Turn lines into listed lists of ints 2-4,6-8 => [[2, 4], [6, 8]]
        pair = [list(map(int, line.split(',')[0].split('-'))), list(map(int, line.split(',')[1].split('-')))]

        #Turn into sets of the ranges
        pair[0] = set(range(pair[0][0], pair[0][1]+1))
        pair[1] = set(range(pair[1][0], pair[1][1]+1))

        for position in pair[0]:
            if position in pair[1]:
                count += 1
                break
    
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
	print(util.postAnswer(today.year, today.day, 2, part2(input), cookie))