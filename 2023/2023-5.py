import util
import datetime
import sys
from pprint import pprint


def part1(input):
	count = 0
	input = "\n".join(input)

	#seeds = list(map(int, input[0].split(": ")[1].split(" ")))
	#print(seeds)
	farmingMaps = {
		"seed-to-soil map:" : [],
		"soil-to-fertilizer map:" : [],
		"water-to-light map:" : [],
		"light-to-temperature map:" : [],
		"temperature-to-humidity map:" : [],
		"humidity-to-location map:" : []
	}

	seeds = list(map(int, input.split("\n")[0].split(": ")[1].split(" ")))
	preInput = input.split("\n")[2:]

	print(seeds)
	#pprint(preInput)
	#pprint(list(farmingMaps.keys()))
	
	# Get indexes of keys in dict farmingMaps in preInput
	# iterate from the index until element = '', add index-1 to end of range

	for key in list(farmingMaps.keys()):
		i = preInput.index(key)
		farmingMaps[key].append(i+1)
		
		while preInput[i] != '':
			if preInput[i] == preInput[-1]:
				i += 1
				break
			i += 1
		
		farmingMaps[key].append(i)
		#print(farmingMaps[key])

	for key in farmingMaps.keys():
		start = farmingMaps[key][0]
		end = farmingMaps[key][1]
		farmingMaps[key] = []
		for element in preInput[start:end]:
			farmingMaps[key].append(list(map(int, element.split(" "))))

	pprint(farmingMaps)

	return count

def part2(input):
	count = 0
	
	return count


if __name__ == '__main__':
	cookie = sys.argv[1]
	today = datetime.datetime.now()
	input = util.getInput(today.year, 5, cookie)
	test = []
	with open(f"{today.year}/test.txt", "r") as file:
		test = file.read().splitlines()

	print(f"Part one: {part1(test)}")
	#print(util.postAnswer(today.year, 5, 1, part1(input), cookie))

	print(f"Part two: {part2(input)}")
	#print(util.postAnswer(today.year, 5, 2, part2(input), cookie))