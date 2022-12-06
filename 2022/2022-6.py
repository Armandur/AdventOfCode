import util
import datetime
import sys


def part1(input):
    count = 0

    packetSize = 4
    for position in range(0, len(input[0])):
        chunk = input[0][position:position+packetSize]
        #print(f"{set(chunk)} Position = {position+packetSize}")
        if len(set(chunk)) == packetSize:
            count = position+packetSize
            break
    
    return count


def part2(input):
    count = 0
    
    packetSize = 14
    for position in range(0, len(input[0])):
        chunk = input[0][position:position+packetSize]
        #print(f"{set(chunk)} Position = {position+packetSize}")
        if len(set(chunk)) == packetSize:
            count = position+packetSize
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
	#print(util.postAnswer(today.year, today.day, 2, part2(input), cookie))