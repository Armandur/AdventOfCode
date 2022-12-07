import util
import datetime
import sys
import copy


def part1(input):
    count = 0
    filesystem = []
    currentPath = []

    for line in input:
        if line[0] == '$': #Command
            command = line.split()[1:3]
            if command[0] == "cd":
                if command[1] == "..":
                    currentPath.pop()
                else:
                    currentPath.append(command[1])
                    traversePath = copy.deepcopy(currentPath)
                    
                    for position in filesystem:
                        if position.keys():
                            pass

                print(f"Current dir: {'/'.join(currentPath)}")

            elif command[0] == "ls":
                pass

        else: #Folder or file
            pass
    
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
	#print(util.postAnswer(today.year, today.day, 1, part1(input), cookie))

	print(f"Part two: {part2(input)}")
	#print(util.postAnswer(today.year, today.day, 2, part2(input), cookie))