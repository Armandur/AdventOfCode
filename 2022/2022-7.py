import util
import datetime
import sys
from anytree import Node, Walker, Resolver, ChildResolverError, AsciiStyle


def part1(input):
    count = 0
    filesystem = Node("ROOT", files=[])
    resolver = Resolver("name")
    currentPath = []
    #print(currentPath)
    #print(RenderTree(filesystem, style=AsciiStyle()))
    listing = False

    for line in input:
        currentPathString = f"/{'/'.join(currentPath)}"

        if line[0] == '$': #Command
            command = line.split()[1:3]
            if command[0] == "cd":
                listing = False

                if command[1] == "..":
                    currentPath.pop()
                    continue
                if command[1] == ''.join(currentPath):
                    # We are here already!
                    continue

                if command[1] == '/':
                    currentPath.append(filesystem.root.name)
                    continue

                try:
                    newPath = currentPath.copy()
                    newPath.append(f"{command[1]}")

                    newPath = f"/{'/'.join(newPath)}"
                    print(f"Going to {newPath}")

                    resolver.get(filesystem, newPath)
                except ChildResolverError:
                    print(f"Creating {newPath}")
                    
                    Node(command[1], parent=resolver.get(filesystem, currentPathString), files=[])
                    currentPath.append(command[1])
            elif command[0] == "ls":
                listing = not listing
                continue

        if line.split()[0] == "dir":
            continue
        
        
        node = resolver.get(filesystem, currentPathString)
        node.__dict__["files"].append((line.split()[1], line.split()[0]))


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

	print(f"Part one: {part1(test)}")
	#print(util.postAnswer(today.year, today.day, 1, part1(input), cookie))

	print(f"Part two: {part2(input)}")
	#print(util.postAnswer(today.year, today.day, 2, part2(input), cookie))