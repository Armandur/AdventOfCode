import util
import datetime
import sys
from collections import namedtuple
from copy import deepcopy


Position = namedtuple("Position", "x y")


class offset:
	up = (-1, 0)
	down = (1, 0)

	left = (0, -1)
	right = (0, 1)

	upleft = (-1, -1)
	upright = (-1, 1)

	downleft = (1, -1)
	downright = (1, 1)


class Tile:
    lowerDelta = 96

    def __init__(self, height, x, y):
        self.height = ord(height)-Tile.lowerDelta
        self.visited = False
        self.type = None # Start, # End
        self.position = Position(x, y)

    def __lt__(self, tile):
        return self.height < tile.height

    def __str__(self):
        string = chr(self.height+Tile.lowerDelta)

        if self.type:
            if self.type == "Start":
                string = 'S'
            elif self.type == "End":
                string = 'E'

        # Blue Green Yellow Red Magenta
        if self.height > 21:
            string = util.colorString(string, util.colors.magenta)
        elif self.height > 16:
            string = util.colorString(string, util.colors.red)
        elif self.height > 11:
            string = util.colorString(string, util.colors.yellow)
        elif self.height > 5:
            string = util.colorString(string, util.colors.green)
        else:
            string = util.colorString(string, util.colors.blue)

        if self.visited:
            string = util.colorString(chr(self.height+Tile.lowerDelta), util.colors.black)

        return string


class Board:
    def __init__(self, input=None):
        self.tiles = []
        self.start = None
        self.end = None
        if input:
            self.loadTiles(input)


    def loadTiles(self, input):
        for y, line in enumerate(input):
            tempLine = []
            for x, char in enumerate(line):
                if char == 'S':
                    tempTile = Tile('a', x, y)
                    tempTile.type = "Start"
                    tempLine.append(tempTile)
                    self.start = tempTile
                    continue
                
                if char == 'E':
                    tempTile = Tile('z', x, y)
                    tempTile.type = "End"
                    tempLine.append(tempTile)
                    self.end = tempTile
                    continue

                tempLine.append(Tile(char, x, y))
            self.tiles.append(tempLine)


    def __str__(self):
        string = ""
        for row in self.tiles:
            for tile in row:
                string += str(tile)
                if tile.height < 10 or tile.type == "Start" or tile.type == "End":
                    string += ''
                string += ''
            string += '\n'
        return string


    def calculateEffort(self, a, b):
        if b.height <= a.height + 1:
            return True
        return False


    def getAdjacents(self, tile, orthogonal=True):
        adjacents = []
        offsets = [offset.up, offset.down, offset.left, offset.right, offset.downleft, offset.downright, offset.upleft, offset.upright]

        if orthogonal:
            offsets = offsets[0:4]

        for o in offsets:
            try:
                if tile.position.x + o[0] < 0 or tile.position.y + o[1] < 0:
                    continue
                self.tiles[tile.position.y + o[0]][tile.position.x + o[1]]
                adjacents.append(self.tiles[tile.position.y + o[1]][tile.position.x + o[0]])
            except IndexError:
                pass

        return adjacents


    def findPath(self, a=None, b=None):
        a = self.start
        b = self.end

        pathIndex = 0
        
        if a and b:
            a = a
            b = b

        paths = [[self.start]]
        
        visited = [paths[0][0].position]

        while pathIndex < len(paths):
            currentPath = paths[pathIndex]
            lastTile = currentPath[-1]
            adjacentTiles = self.getAdjacents(lastTile)

            for tile in adjacentTiles:
                if b.position == tile.position:
                    currentPath.append(b)
                    return currentPath
            
            for tile in adjacentTiles:
                if self.calculateEffort(lastTile, tile):
                    if tile.position not in visited:
                        newPath = currentPath[:]
                        newPath.append(tile)
                        paths.append(newPath)
                        visited.append(tile.position)
            pathIndex +=1
        return []


def part1(input):
    count = 0
    board = Board(input)
    #print(board)

    network = board.findPath()

    for row in board.tiles:
        string = ""
        for tile in row:
            string += str(tile)
        print(string)

    for tile in network:
        board.tiles[tile.position.y][tile.position.x].visited=True

    for row in board.tiles:
        string = ""
        for tile in row:
            string += str(tile)
        print(string)

    count = len(network)

    return count


def part2(input):
	count = 0
	
	return count


if __name__ == '__main__':
    cookie = sys.argv[1]
    today = datetime.datetime.now()
    input = util.getInput(today.year, 12, cookie)
    test = []
    with open(f"{today.year}/test.txt", "r") as file:
        test = file.read().splitlines()
        
    print(f"Part one: {part1(input)}")
    #print(util.postAnswer(today.year, 12, 1, part1(input), cookie))
    
    print(f"Part two: {part2(input)}")
	#print(util.postAnswer(today.year, today.day, 2, part2(input), cookie))