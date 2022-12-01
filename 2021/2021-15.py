import util
import networkx as nx
import matplotlib.pyplot as plt

def writeText(text):
	return plt.annotate(text, xy=(10,10), xycoords="figure pixels")

def drawMap(cave, pos=None, marked=[], text=""):
	plt.clf()
	colors = []
	for node in cave.nodes:
		if node in marked:
				colors.append("red")
		else:
			colors.append("green")

	labels = nx.get_edge_attributes(cave, 'weight')
	text = writeText(text)
	nx.draw(cave, pos=pos, node_color=colors, with_labels=False, width=2, node_size=300, font_size=8)
	nx.draw_networkx_edge_labels(cave, pos=pos, edge_labels=labels, label_pos=0.3)
	plt.draw()

def part1(input):
	count = 0
	weights = []
	for line in input:
		tempLine = []
		for ch in line:
			tempLine.append((int(ch)))
		weights.append(tempLine.copy())

	Cave = nx.DiGraph()

	for i in range(len(weights)):
		for j in range(len(weights)):
			Cave.add_node((i, j))

	pos = {(x, y): (y, -x) for x, y in Cave.nodes()}

	for x, row in enumerate(weights):
		for y, col in enumerate(row):
			fr = (x, y)
			to = (x, y+1)
			if to[0] > len(weights)-1 or to[1] > len(weights[x])-1:
				continue
			Cave.add_weighted_edges_from([(to, fr, weights[x][y])])
			Cave.add_weighted_edges_from([(fr, to, weights[x][y+1])])

			fr = (x, y)
			to = (x+1, y)
			if to[0] > len(weights)-1:
				continue
			Cave.add_weighted_edges_from([(to, fr, weights[x][y])])
			Cave.add_weighted_edges_from([(fr, to, weights[x+1][y])])
	# The above doesn't get the last column...
	# bruteforce it!
	for x, row in enumerate(weights):
		y = len(weights)-1
		fr = (x, y)
		to = (x+1, y)
		if to[0] > len(weights)-1:
			continue
		Cave.add_weighted_edges_from([(to, fr, weights[x][y])])
		Cave.add_weighted_edges_from([(fr, to, weights[x + 1][y])])


	start = (0, 0)
	end = (len(weights)-1, len(weights[0])-1)
	#end = (25, 19)

	length, path = nx.bidirectional_dijkstra(Cave, start, end)
	print(path)

	if False:
		plt.ion()
		drawMap(Cave, pos, path, f"Length: {length}")
		plt.pause(1000)
	count = length
	return count


def part2(input):
	count = 0
	weights = []
	for line in input:
		tempLine = []
		for ch in line:
			tempLine.append((int(ch)))
		weights.append(tempLine.copy())

	weightsX = []
	size = (len(weights)*5, len(weights[0])*5)


	for x in range(len(weights)):
		tempLine = []
		i = 0
		for y in range(size[1]):
			if y % len(weights) == 0:
				i += 1

			value = weights[x % len(weights)][y % len(weights[0])]+i-1
			diff = value - 9
			if value > 9:
				value = diff

			tempLine.append(value)
		weightsX.append(tempLine)

	i = 0
	weightsX5 = []
	for y in range(size[0]):
		row = []

		if y % len(weights) == 0:
			i += 1

		for ch in weightsX[y%len(weightsX)]:
			value = ch+i-1
			diff = value - 9

			if value > 9:
				value = diff

			row.append(value)
		weightsX5.append(row)

	if False: #Print
		j = 0
		for line in weightsX5:
			string = ""
			i = 0
			for ch in line:
				string += str(ch)
				i += 1
				if i == 10:
					string += " "
					i = 0
			if j == 10:
				print()
				j = 0
			print(string)
			j += 1

	weights = weightsX5

	Cave = nx.DiGraph()

	for i in range(len(weights)):
		for j in range(len(weights)):
			Cave.add_node((i, j))

	pos = {(x, y): (y, -x) for x, y in Cave.nodes()}

	for x, row in enumerate(weights):
		for y, col in enumerate(row):
			fr = (x, y)
			to = (x, y+1)
			if to[0] > len(weights)-1 or to[1] > len(weights[x])-1:
				continue
			Cave.add_weighted_edges_from([(to, fr, weights[x][y])])
			Cave.add_weighted_edges_from([(fr, to, weights[x][y+1])])

			fr = (x, y)
			to = (x+1, y)
			if to[0] > len(weights)-1:
				continue
			Cave.add_weighted_edges_from([(to, fr, weights[x][y])])
			Cave.add_weighted_edges_from([(fr, to, weights[x+1][y])])
	# The above doesn't get the last column...
	# bruteforce it!
	for x, row in enumerate(weights):
		y = len(weights)-1
		fr = (x, y)
		to = (x+1, y)
		if to[0] > len(weights)-1:
			continue
		Cave.add_weighted_edges_from([(to, fr, weights[x][y])])
		Cave.add_weighted_edges_from([(fr, to, weights[x + 1][y])])


	start = (0, 0)
	end = (len(weights)-1, len(weights[0])-1)
	print(end)
	#end = (25, 19)

	length, path = nx.bidirectional_dijkstra(Cave, start, end)
	#print(path)

	if False:
		plt.ion()
		drawMap(Cave, pos, path, f"Length: {length}")
		plt.pause(1000)

	count = length
	return count


if __name__ == '__main__':
	input = util.getInput(2021, 15)
	test = []
	with open("test.txt", "r") as file:
		test = file.read().splitlines()

	#print(f"Part one: {part1(input)}")
	#print(util.postAnswer(2021, 15, 1, part1(input)))

	#print(f"Part two: {part2(input)}")
	#print(util.postAnswer(2021, 15, 2, part2(input)))