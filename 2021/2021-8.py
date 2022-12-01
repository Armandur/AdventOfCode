import util

def identifyMapping(signals):
	codes = { 0: "", 1: "", 2: "", 3: "", 4: "", 5: "", 6: "", 7: "", 8: "" }

	signals = list(map(lambda x: "".join(sorted(x)), signals))

	lengthsix = []
	lengthfive = []
	for element in signals:
		element = "".join(sorted(element))

		#We can already know what codes are 1, 4, 7,8 due to len() being unique
		if len(element) == 2:
			codes[1] = element
		if len(element) == 4:
			codes[4] = element
		if len(element) == 3:
			codes[7] = element
		if len(element) == 7:
			codes[8] = element

		if len(element) == 6:
			lengthsix.append(element)

		if len(element) == 5:
			lengthfive.append(element)

	for element in lengthsix[:]:
		if all(ch in list(element) for ch in list(codes[4])): # Only #9 contains all codes from #4
			codes[9] = element
			lengthsix.remove(element)

		# #0 has all chars from #1 but is missing one from four (=3)
		if sum(ch in list(element) for ch in list(codes[1])) == 2 \
		and sum(ch in list(codes[4]) for ch in list(element)) == 3:
			codes[0] = element
			lengthsix.remove(element)

	codes[6] = lengthsix[0] # #6 is the last remaining element with len() == 6

	for element in lengthfive[:]:
		# Of the lengthfives only #5 has all but one of #6
		if sum(ch in list(element) for ch in list(codes[6])) == 5:
			codes[5] = element
			lengthfive.remove(element)

	# Of the remaining lengthfives only #3 has both elements of #1
	for element in lengthfive[:]:
		if sum(ch in list(element) for ch in list(codes[1])) == 2:
			codes[3] = element
			lengthfive.remove(element)

	# Last of lengthfive is then #2
	codes[2] = lengthfive[0]

	#Invert hte dict and return it
	codes = {v: k for k, v in codes.items()}
	return codes


def part1(input):
	count = 0
	for line in input:
		formatted = line.split(" | ")[1].split(" ")
		values = [2, 4, 3, 7]  #Number of segments for 1, 4, 7, 8
		for value in formatted:
			if len(value) in values:
				count += 1
	return count

def part2(input):
	count = 0
	for line in input:
		signals = line.split(" | ")[0].split(" ")
		mapping = identifyMapping(signals)

		output = line.split(" | ")[1].split(" ")
		output = list(map(lambda x: "".join(sorted(x)), output))

		code = ""
		for value in output:
			code += str(mapping[value])

		count += int(code)

	return count

if __name__ == '__main__':
	input = util.getInput(2021, 8)
	test = []
	with open("test.txt", "r") as file:
		test = file.read().splitlines()

	#print(f"Part one: {part1(input)}")
	#print(util.postAnswer(2021, 8, 1, part1(input)))

	#print(f"Part two: {part2(input)}")
	print(util.postAnswer(2021, 8, 2, part2(input)))