import util

def part1(input):
    count = 0
    input = input[0].split(',')
    input = list(map(int, input))

    print(input)

    #iterate list and for every element check distance/fuel to current element and sum this,
    # add position and fuel to dict as position with the sum to move there

    positions = {} #position : fuel to change
    for currentposition in input:
        fuelsum = 0
        for position in input:
            fuelsum += abs(position - currentposition)
        positions[currentposition] = fuelsum

    positionLowestFuel = min(positions, key=positions.get)
    print(f"Position with lowest fuel cost: {positionLowestFuel}, fuel cost: {positions[positionLowestFuel]}")

    count = positions[positionLowestFuel]
    return count

def part2(input):
    count = 0
    input = input[0].split(',')
    input = list(map(int, input))

    #iterate list and for every element check distance/fuel to current element and sum this,
    # add position and fuel to dict as position with the sum to move there

    positions = {} #position : fuel to change
    for currentposition in range(0, max(input)): #We now have to consider all possible positions, not just those with crabs
        fuelsum = 0
        for position in input:
            fuelsum += int(abs(position-currentposition) * (1+abs(position-currentposition)) / 2)
        positions[currentposition] = fuelsum

    positionLowestFuel = min(positions, key=positions.get)
    print(f"Position with lowest fuel cost: {positionLowestFuel}, fuel cost: {positions[positionLowestFuel]}")

    count = positions[positionLowestFuel]
    return count

if __name__ == '__main__':
	input = util.getInput(2021, 7)
	test = []
	with open("test.txt", "r") as file:
		test = file.read().splitlines()

	#print(f"Part one: {part1(input)}")
	#print(util.postAnswer(2021, 7, 1, part1(input)))

	print(f"Part two: {part2(input)}")
	#print(util.postAnswer(2021, 7, 2, part2(input)))