import util
import datetime
import sys
from pprint import pprint
import math
from collections import Counter

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
	
	for id, line in enumerate(input):
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

		#pprint(f"Card {id+1}: {card} | Winners: {winningNumbers}")

		cards.append((id+1, card, winningNumbers))

	#pprint(cards)

	cardsTotal = len(cards)
	cardEval = {}
	for card in cards:
		cardEval[card[0]] = {"amount": 1, "wins": 0}
	
	for card in cards:
		currentCardID = card[0]
		winningNumbers = list(set(card[1]) & set(card[2]))
		# How many cards does this card win?
		if winningNumbers:
			cardEval[currentCardID]["wins"] = len(winningNumbers)

	for card in cardEval:
		for wins in range(cardEval[card]["wins"]):
			#Add the amount of this card to the next range(wins)-cards
			cardEval[card+wins+1]["amount"] += cardEval[card]["amount"]

	pprint(cardEval)

	for card in cardEval:
		count += cardEval[card]["amount"]

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
	print(util.postAnswer(today.year, today.day, 2, part2(input), cookie))