import util
import networkx as nx
import matplotlib.pyplot as plt

typeColors = {
	"start": "lightgreen",
	"end": "green",
	"small": "lightblue",
	"big": "lightgrey"
}

def writeText(text):
	return plt.annotate(text, xy=(10,10), xycoords="figure pixels")


def drawMap(Cave, pos, text):
	plt.clf()
	colors = []
	for node in Cave.nodes:
		if Cave.nodes[node]["sub"] == True:
			colors.append("yellow")
		else:
			colors.append(typeColors[Cave.nodes[node]["type"]])

	text = writeText(text)
	nx.draw(Cave, pos=pos, node_color=colors, with_labels=True)
	plt.draw()


def traverse(paths, cave, node, end, extraChance, visited=[]):
	visited.append(node)
	if node == end:
		paths.append(visited)
		paths.sort(key=len)
		return

	for nb in cave.neighbors(node):
		type = cave.nodes[nb]["type"]

		if type == "small":
			if nb in visited:
				if extraChance: 		#	We get an extra chance!
					traverse(paths, cave, nb, end, False, visited.copy()) # Recurse with no extra chance
			else:
				traverse(paths, cave, nb, end, extraChance, visited.copy())

		elif type == "big" or nb not in visited:
			traverse(paths, cave, nb, end, extraChance, visited.copy())


def part1(input):
	count = 0
	Cave = nx.MultiGraph()

	for line in input:
		line = line.split('-')
		type = ""

		for cave in line:
			type = "small"
			if cave.isupper():
				type = "big"
			if cave == "start":
				type = "start"
			if cave == "end":
				type = "end"

			Cave.add_node(cave, type=type, sub=False)

	for line in input:
		line = line.split('-')
		Cave.add_edge(line[0], line[1])

	plt.ion()
	pos = nx.spring_layout(Cave)

	paths = []
	traverse(paths, Cave, "start", "end", False)

	draw = True
	if draw == False:
		return len(paths)

	submarine = "start"
	Cave.nodes[submarine]["sub"] = True
	drawMap(Cave, pos, "Yellow Submarine standing by...")

	plt.pause(2)
	_time = 0.001
	for path in paths:
		submarine = "start"
		Cave.nodes[submarine]["sub"] = True
		text = f"Paths = {len(paths)}, #{paths.index(path) + 1}: {path}"
		drawMap(Cave, pos, text)
		plt.pause(_time)

		for node in path:
			Cave.nodes[submarine]["sub"] = False
			submarine = node
			Cave.nodes[submarine]["sub"] = True

			drawMap(Cave, pos, text)
			plt.pause(_time)

		Cave.nodes[submarine]["sub"] = False

	count = len(paths)
	return count


def part2(input):
	count = 0
	Cave = nx.MultiGraph()

	for line in input:
		line = line.split('-')
		type = ""

		for cave in line:
			type = "small"
			if cave.isupper():
				type = "big"
			if cave == "start":
				type = "start"
			if cave == "end":
				type = "end"

			Cave.add_node(cave, type=type, sub=False)

	for line in input:
		line = line.split('-')
		Cave.add_edge(line[0], line[1])

	plt.ion()
	pos = nx.spring_layout(Cave)

	paths = []
	traverse(paths, Cave, "start", "end", True)

	draw = True
	if draw == False:
		return len(paths)

	submarine = "start"
	Cave.nodes[submarine]["sub"] = True
	drawMap(Cave, pos, "Yellow Submarine standing by...")
	plt.pause(3)

	_time = 0.1
	for path in paths:
		submarine = "start"
		Cave.nodes[submarine]["sub"] = True
		text = f"Paths = {len(paths)}, #{paths.index(path) + 1}: {path}"
		drawMap(Cave, pos, text)
		plt.pause(_time)

		for node in path:
			Cave.nodes[submarine]["sub"] = False
			submarine = node
			Cave.nodes[submarine]["sub"] = True

			drawMap(Cave, pos, text)
			plt.pause(_time)

		Cave.nodes[submarine]["sub"] = False

	count = len(paths)
	return count

if __name__ == '__main__':
	input = util.getInput(2021, 12)
	test = []
	with open("test.txt", "r") as file:
		test = file.read().splitlines()

	#print(f"Part one: {part1(test)}")
	#print(util.postAnswer(2021,12, 1, part1(input)))

	print(f"Part two: {part2(test)}")
	#print(util.postAnswer(2021, 12, 2, part2(input)))