import util
import datetime
import sys

wins = { 
    'A' : 'Y',
    'B' : 'Z',
    'C' : 'X'
}

draws = {
    'A' : 'X',
    'B' : 'Y',
    'C' : 'Z'
}

losses = {
    'A' : 'Z',
    'B' : 'X',
    'C' : 'Y'
}

points = {
    'A' : 1,
    'X' : 1,
    'B' : 2,
    'Y' : 2,
    'C' : 3,
    'Z' : 3
}

def part1(input):
    count = 0

    for line in input:
        opponent = line.split()[0]
        me = line.split()[1]

        if(wins[opponent] == me):
            #print("I win!")
            count += points[me] + 6

        elif draws[opponent] == me:
            #print("Draw!")
            count += points[me] + 3
        else:
            #print("I lose!")
            count += points[me] + 0

    
    return count


def part2(input):
    count = 0

    outcome = {
        'X': "Loose",
        'Y': "Draw",
        'Z': "Win"
    }

    for line in input:
        opponent = line.split()[0]
        me = line.split()[1]
        
        if outcome[me] == "Loose":
            count += points[losses[opponent]] + 0

        elif outcome[me] == "Draw":
            count += points[draws[opponent]] + 3

        elif outcome[me] == "Win":
            count += points[wins[opponent]] + 6


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