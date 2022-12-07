import util
import datetime
import sys
from anytree import Resolver, ChildResolverError, AsciiStyle, RenderTree, PreOrderIter
from anytree import NodeMixin

def boldString(string):
	start = "\033[92m"
	end = "\033[0m"
	return f"{start}{string}{end}"

class Directory(NodeMixin):
    def __init__(self, name, files=[], parent=None, children=None):
        self.name = name
        self.files = files
        self.parent = parent
        if children:
            self.children = children
    
    
    def __repr__(self) -> str:
        string = self.name
        if self.files:
            string += boldString(f" {[file[0] for file in self.files]}")
        return string
    

    def _filesSize(self): #Get size of files in current dir
        return sum(file[1] for file in self.files)


    def getSize(self): #Get total size of this and child dirs
        size = 0
        for node in PreOrderIter(self):
            size += node._filesSize()
        return size


def loadFileSystem(input):
    filesystem = Directory("ROOT")
    resolver = Resolver("name")
    currentPath = []

    listing = False
    files = []

    for line in input:
        currentPathString = f"/{'/'.join(currentPath)}"

        if line[0] == '$': #Command
            if listing:
                listing = False
                resolver.get(filesystem, currentPathString).files = files
                files = []

            command = line.split()[1:3]
            if command[0] == "cd":
                if command[1] == "..":
                    currentPath.pop()
                    continue

                if command[1] == '/':
                    currentPath.append(filesystem.root.name)
                    continue

                try:
                    newPath = currentPath.copy()
                    newPath.append(f"{command[1]}")

                    newPath = f"/{'/'.join(newPath)}" #Create a path for the directory
                    #print(f"Going to {newPath}")

                    resolver.get(filesystem, newPath) #Try to access the path
                except ChildResolverError: #Path doesn't yet exist so we need to create
                    #print(f"Creating {newPath}")
                    
                    Directory(command[1], parent=resolver.get(filesystem, currentPathString))
                    currentPath.append(command[1]) #We are now in the new path
                    continue

            elif command[0] == "ls":
                listing = not listing
                #print(f"Listing files in dir = {listing}")

                continue

        elif line.split()[0] == "dir": #We handle directories above
                continue

        if listing:
            file = (line.split()[1], int(line.split()[0]))
            #print(f"File {file} in {currentPathString}")

            files.append(file)
            if line == input[-1]: #If we are at the last line we won't reset from expecting listing files by encountering a command
                resolver.get(filesystem, currentPathString).files = files

    return filesystem


def part1(input):
    count = 0
    filesystem = loadFileSystem(input)
    
    #print(RenderTree(filesystem, style=AsciiStyle()))

    totalStupidSize = 0
    for node in PreOrderIter(filesystem):
        if node.getSize() <= 100000:
            totalStupidSize += node.getSize()

    count = totalStupidSize

    return count


def part2(input):
    count = 0
    
    filesystem = loadFileSystem(input)
    
    totalDiskspace = 70000000
    requiredFreeDiskspace = 30000000
    usedDiskspace = filesystem.getSize()

    #print(RenderTree(filesystem, style=AsciiStyle()))
    
    def freeDiskspace(used=usedDiskspace, total=totalDiskspace):
        return total - used

    candidates = []
    for node in PreOrderIter(filesystem):
        if freeDiskspace() + node.getSize() > requiredFreeDiskspace:
            candidates.append(node.getSize())

    count = min(candidates)
    
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
	#print(util.postAnswer(today.year, today.day, 2, part2(input), cookie))