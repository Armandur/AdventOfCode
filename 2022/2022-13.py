import util
import datetime
import sys
import json

def check(left, right, index):
    if index >= len(left) and index < len(right):
        return "Correct"
    elif index < len(left) and index >= len(right):
        return "Incorrect"
    elif index >= len(left) and index >= len(right):
        return "Next"


    if isinstance(left[index], int):
        
        if isinstance(right[index], int):

            if left[index] == right[index]:
                #Continuing
                return check(left, right, index+1)
            if left[index] < right[index]:
                return "Correct"
            else:
                return "Incorrect"

        if isinstance(right[index], int):
            result = check(left, list(right), index)
            if result == "Next":
                return check(left, right, index+1)
            else:
                return result

        if isinstance(right[index], list):
            result = check(list(left), right, index)
            if result == "Next":
                return check(left, right, index+1)
            else:
                return result
    

    result = check(left[index], right[index], 0)
    if result == "Next":
        return check(left, right, index+1)
    else:
        return result 

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
            
    indices = []
    for index, pair in enumerate(pairs[0:]):
        #print(pair)
        left = pair[0]
        right = pair[1]


        if check(left, right, 0) == "Correct":
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