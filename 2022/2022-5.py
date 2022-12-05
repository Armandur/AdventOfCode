import util
import datetime
import sys


def part1(input):
    count = 0

    stacks = []
    numStacksLine = 0
    
    #Get the row with the number of stacks
    for row, line in enumerate(input):
        if line == "":
            #print(f"Empty line at line {row}!")
            numStacksLine = row-1

    #Split the row and get the last number == number of stacks
    #Add that number of empty lists to the list.
    numStacks = int(input[numStacksLine].split()[-1])
    for i in range(0, numStacks):
        stacks.append([])

    start = input[:numStacksLine]
    start.reverse() #Reverse the list to start stacking boxes from the bottom up.
    delta = 4
    for row, line in enumerate(start):
        for position in range(0, numStacks):
            crate = line[position*4+1].strip()
            if crate != "":
                #print(f"Row: {row} Position: {position} - {line[position*4+1]}")
                stacks[position].append(crate)

    #Loop over instructions
    for line in input[numStacksLine+2:]:
        count = int(line.split()[1])
        origin = int(line.split()[3])-1 #Correct for index
        destination = int(line.split()[5])-1 #Correct for index
        #print(f"Moving {count} boxes, from {origin} to {destination}")
        for boxes in range(0, count):
            stacks[destination].append(stacks[origin].pop())

    #print(stacks)
    
    count = ""
    for stack in stacks:
        count += stack.pop()

    return count


def part2(input):
    count = 0

    stacks = []
    numStacksLine = 0
    
    #Get the row with the number of stacks
    for row, line in enumerate(input):
        if line == "":
            #print(f"Empty line at line {row}!")
            numStacksLine = row-1

    #Split the row and get the last number == number of stacks
    #Add that number of empty lists to the list.
    numStacks = int(input[numStacksLine].split()[-1])
    for i in range(0, numStacks):
        stacks.append([])

    start = input[:numStacksLine]
    start.reverse() #Reverse the list to start stacking boxes from the bottom up.
    delta = 4
    for row, line in enumerate(start):
        for position in range(0, numStacks):
            crate = line[position*4+1].strip()
            if crate != "":
                #print(f"Row: {row} Position: {position} - {line[position*4+1]}")
                stacks[position].append(crate)

    #Loop over instructions
    for line in input[numStacksLine+2:]:
        count = int(line.split()[1])
        origin = int(line.split()[3])-1 #Correct for index
        destination = int(line.split()[5])-1 #Correct for index
        #print(f"Moving {count} boxes, from {origin} to {destination}")

        #CrateMover 9001!
        lifted = []
        for boxes in range(0, count):
            lifted.append(stacks[origin].pop())
        
        lifted.reverse()
        for box in lifted:
            stacks[destination].append(box)
    
    #print(stacks)

    count = ""
    for stack in stacks:
        count += stack.pop()
        
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