import util
import datetime
import sys
import json

def part1(input):
    count = 0
    pairs = []
    pair = []
    for line in input:
        if line == "":
            continue
        pair.append(json.loads(line))
        if len(pair) == 2:
            pairs.append(pair)
            pair = []
    
    #for pair in pairs:
    #    print(pair[0])
    #    print(pair[1])
    #    print()

    def check(left, right):
        if isinstance(left, list):
            if isinstance(right, list):
                return check(list(left), list(right))
            if isinstance(left[0], int):
                if isinstance(right[0], int):
                    return left < right 
            
    indices = []
    for index, pair in enumerate(pairs[0:]):
        #print(pair)
        left = pair[0]
        right = pair[1]


        if check(left, right):
            indices.append(index)

    print(indices)


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

	print(f"Part one: {part1(test)}")
	#print(util.postAnswer(today.year, today.day, 1, part1(input), cookie))

	print(f"Part two: {part2(input)}")
	#print(util.postAnswer(today.year, today.day, 2, part2(input), cookie))