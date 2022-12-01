import util

def move(sub, command, level=1): #sub = [Horizontal, depth, (aim)]
	command = command.split()
	command[1] = int(command[1])

	if level==1:
		if command[0] == "forward":
			sub[0] += command[1]
		elif command[0] == "down":
			sub[1] += command[1]
		elif command[0] == "up":
			sub[1] -= command[1]

	if level==2:
		if command[0] == "forward":
			sub[0] += command[1]
			sub[1] += sub[2] * command[1]

		elif command[0] == "down":
			sub[2] += command[1]

		elif command[0] == "up":
			sub[2] -= command[1]

def part1():
	input = util.getInput(2021, 2)
	pos = [0, 0] # Horizontal, depth

	for line in input:
		move(pos, line)

	return pos[0] * pos[1]


def part2():
	input = util.getInput(2021, 2)
	pos = [0, 0, 0] # Horizontal, depth, aim

	for line in input:
		move(pos, line, 2)

	return pos[0] * pos[1]

if __name__ == '__main__':
	print(f"Part one: {part1()}")
	#print(util.postAnswer(2021,2,1,part1()))
	print(f"Part two: {part2()}")
	#print(util.postAnswer(2021,2,2,part2()))