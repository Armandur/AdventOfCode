import util
from statistics import mode
from collections import Counter, defaultdict


def load(input):
	template = input[0:input.index("")][0]
	rules = input[input.index("")+1:]

	temp = dict()
	for rule in rules:
		rule = rule.split(" -> ")
		temp[rule[0]] = rule[1]
	rules = temp
	#print(rules)
	return template, rules

def step2(polymer, rules, n):
	pairs = defaultdict(int)
	elements = defaultdict(int)

	for i, element in enumerate(polymer[:-1]):
		pairs[polymer[i:i+2]] += 1		#Add the pair as key and increase the occurence (NN += 1)
		elements[element] += 1			#Add the element as key and increase the occurence (N += 1)
	elements[polymer[-1]] += 1			#Add the last element in the polymer (B += 1)

	#print(pairs)
	#print(elements)

	for _ in range(n): # N = Steps to run
		for pair, count in list(pairs.items()):
			newElement = rules.get(pair, "")		#Get the element that corresponds to the pair (NN -> C)
			elements[newElement] += count			#Increase the count of the newElement in our polymer (C += 1)
			pairs[pair] -= count					#Decrease the old pair (We're going to insert in the middle so it removes [count] occurence of the current pair (NN-1)
			pairs[pair[0] + newElement] += count	#Increase the count of the first part of the pair with the new element after it (NC += 1)
			pairs[newElement + pair[1]] += count	#Increase the count of the second part of the pair with the new element before it (CN += 1)

	return elements


def step(polymer, rules):
	next = ""
	for i in range(len(polymer)):
		if i == len(polymer) -1:
			next += polymer[i]
			break
		#print(polymer[i]+polymer[i+1])
		if polymer[i]+polymer[i+1] in rules.keys():
			next += polymer[i]+rules[polymer[i]+polymer[i+1]]
	return next


def part1(input):
	count = 0
	template, rules = load(input)

	polymer = template
	for i in range(10):
		polymer = step(polymer, rules)
		print(i)

	mostCommon = polymer.count(mode(list(polymer)))
	cnt = Counter(polymer)
	leastCommon = min(cnt.values())
	print(mostCommon)
	print(leastCommon)

	count = mostCommon - leastCommon
	return count


def part2(input):
	count = 0
	template, rules = load(input)

	polymer = step2(template, rules, 40)
	print(f"Max: {max(polymer.values())}, Min: {min(polymer.values())}")
	count = max(polymer.values()) - min(polymer.values())
	return count


if __name__ == '__main__':
	input = util.getInput(2021, 14)
	test = []
	with open("test.txt", "r") as file:
		test = file.read().splitlines()

	#print(f"Part one: {part1(input)}")
	#print(util.postAnswer(2021, 14, 1, part1(input)))

	#print(f"Part two: {part2(input)}")
	#print(util.postAnswer(2021, 14, 2, part2(input)))