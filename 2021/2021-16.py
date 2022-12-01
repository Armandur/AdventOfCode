import util
import datetime
from collections import defaultdict

class Datorn:
	def __init__(self, _input):
		self.values = (bin(int(_input, 16))[2:]).zfill(4)
		self.versionSum = 0
		self.result = None

	def getBits(self, length):
		bits = "".join(self.values[:length])
		self.values = self.values[length:]
		return bits

	def run(self):
		version = int(self.getBits(3), 2) # Get the first three bits
		self.versionSum += version # Add to total sums
		pid = int(self.getBits(3, 2)) # Determine packet type

		if pid == 4: # Packet is a value:
			value = ""
			while True:
				bits = self.getBits(5)
				value += bits[1:] #Add all but first bit - first bit indicates if to keep going or not
				if bits[0] == '0': # Not a one so last "byte"
					break
				value = int(value, 2)
				return value
		else:


def part1(input):
	datorn = Datorn(input[0])

	return count


def part2(input):
	count = 0

	return count


if __name__ == '__main__':
	today = datetime.datetime.now()
	input = util.getInput(today.year, today.day)
	test = []
	with open("test.txt", "r") as file:
		test = file.read().splitlines()

	print(f"Part one: {part1(test)}")
	#print(util.postAnswer(today.year, today.day, 1, part1(input)))

	print(f"Part two: {part2(input)}")
	#print(util.postAnswer(today.year, today.day, 2, part2(input)))