import util

class Lanternfish:
	def __init__(self, timer):
		self.timer = timer

	def __str__(self):
		return str(self.timer)

	def __repr__(self):
		return self.__str__()

	def newDay(self):
		if self.timer == 0:
			self.timer = 6
		else:
			self.timer -= 1

def part1(input):
	count = 0
	input = input[0].split(',')
	input = list(map(int, input))

	school = []

	for value in input:
		school.append(Lanternfish(value))

	for i in range(0, 80):
		dailyFishes = []
		for fish in school:
			if fish.timer == 0:
				dailyFishes.append(Lanternfish(8))
			fish.newDay()
		school = school + dailyFishes

	count = (len(school))

	return count

def part2(input):
	count = 0
	input = input[0].split(',')
	input = list(map(int, input))

			 #0, 1, 2, 3, 4, 5, 6, 7, 8
	school = [0, 0, 0, 0, 0, 0, 0, 0, 0]
	count = len(input)

	for fish in input:
		school[fish] += 1

	for i in range(0, 256):
		temp = school[0] #Keep track of how many fish are spawning

		school[0] = school[1] #Move fishes of to next timer
		school[1] = school[2]
		school[2] = school[3]
		school[3] = school[4]
		school[4] = school[5]
		school[5] = school[6]
		school[6] = school[7]
		school[7] = school[8]

		school[6] += temp #Fish that have spawned are reset to 6
		school[8] = temp #This amount of new fishes added

		count += temp #Add amount of new fishes to count
	return count

if __name__ == '__main__':
	input = util.getInput(2021, 6)
	test = []
	with open("test.txt", "r") as file:
		test = file.read().splitlines()

	print(f"Part one: {part1(input)}")
	#print(util.postAnswer(2021, 6, 1, part1(input)))

	print(f"Part two: {part2(input)}")
	#print(util.postAnswer(2021, 6, 2, part2(input)))