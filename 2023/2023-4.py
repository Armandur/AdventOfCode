import util
import datetime
import sys
from pprint import pprint
import math

def part1(input):
	count = 0
	cards = []
	
	for line in input:
		card = []
		winningNumbers = []
		splitCard = line.split(" | ")[0].split(": ")[1].split(" ")
		
		while "" in splitCard:
			splitCard.remove("")
		
		for strNum in splitCard:
			card.append(int(strNum))

		splitWinners = line.split(" | ")[1].split(" ")
		while "" in splitWinners:
			splitWinners.remove("")

		for strWinners in splitWinners:
			winningNumbers.append(int(strWinners))

		#pprint(f"Card: {card} | Winners: {winningNumbers}")

		cards.append((card, winningNumbers))

	#pprint(cards)

	for card in cards:
		points = []
		numbers = card[0]
		winningNumbers = card[1]
		for number in numbers:
			if number in winningNumbers:
				points.append(number)

		count += int(math.pow(2,len(points)-1))
		
	return count


def part2(input):
	count = 0
	cards = []
	
	for line in input:
		card = []
		winningNumbers = []
		splitCard = line.split(" | ")[0].split(": ")[1].split(" ")
		
		while "" in splitCard:
			splitCard.remove("")
		
		for strNum in splitCard:
			card.append(int(strNum))

		splitWinners = line.split(" | ")[1].split(" ")
		while "" in splitWinners:
			splitWinners.remove("")

		for strWinners in splitWinners:
			winningNumbers.append(int(strWinners))

		#pprint(f"Card: {card} | Winners: {winningNumbers}")

		cards.append((card, winningNumbers))

	#pprint(cards)

	for card in cards:
		points = []
		numbers = card[0]
		winningNumbers = card[1]
		for number in numbers:
			if number in winningNumbers:
				points.append(number)

		count += int(math.pow(2,len(points)-1))
		
	return count


if __name__ == '__main__':
	cookie = sys.argv[1]
	today = datetime.datetime.now()
	input = util.getInput(today.year, today.day, cookie)
	test = []
	with open(f"{today.year}/test.txt", "r") as file:
		test = file.read().splitlines()

	print(f"Part one: {part1(input)}")
	print(util.postAnswer(today.year, today.day, 1, part1(input), cookie))

	print(f"Part two: {part2(input)}")
	#print(util.postAnswer(today.year, today.day, 2, part2(input), cookie))