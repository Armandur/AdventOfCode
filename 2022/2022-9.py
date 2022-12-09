import util
import datetime
import sys
import time
import os

def boldString(string):
	start = "\033[92m"
	end = "\033[0m"
	return f"{start}{string}{end}"

def clearConsole():
    command = 'clear'
    if os.name in ('nt', 'dos'):  # If Machine is running on Windows, use cls
        command = 'cls'
    os.system(command)


class Tile:
    def __init__(self):
        self.visited = False

    def __str__(self):
        if self.visited:
            return boldString(".")
        return "."

    def __repr__(self) -> str:
        return self.__str__()


class Rope:
    def __init__(self, x, y, board):
        # x = Column, 0 = left
        # y = Row, 0 = top
    
        self.head = [x, y]
        self.tail = [x, y]

        board[self.tail[1]][self.tail[0]].visited = True

    def _manhattanDistance(self):
        return abs(self.tail[0] - self.head[0]) + abs(self.tail[1] - self.head[1]) - 1


    def move(self, direction, steps, board):
        boardExtended = False
        if not board.pathExists(self, direction, steps):
            board.extend(direction, steps)
            #print(f"Board extended by {steps} in dir {direction}")
            if direction == 'L': #X should increase by steps
                self.head[0] += steps
                self.tail[0] += steps

            if direction == 'U': #Y should increase by steps
                self.head[1] += steps
                self.tail[1] += steps
        
        deltaX = deltaY = 0
        if direction == "R":
            deltaX = 1
        if direction == "L":
            deltaX = -1
        if direction == "D":
            deltaY = 1
        if direction == "U":
            deltaY = -1

        for step in range(steps):
            newX = self.head[0]+deltaX
            newY = self.head[1]+deltaY

            self.head = [newX, newY]
            board.tiles[newY][newX].visited = True
            
            if self._manhattanDistance() == 2:
                #Move tail
                pass
            continue #Below prints for each step, kind of fun!
            clearConsole()
            print(f"Board: {len(board.tiles)}, {len(board.tiles[0])}")
            print(f"Tail at: {self.tail}")
            print(f"Head at: {self.head}")
            print(f"Instruction: {direction} {steps}")
            print(board.__str__(self))



class Board:
    def __init__(self, row, col):
        self.tiles = []
        tempRow = []

        for _row in range(row):
            for _col in range(col):
                tempRow.append(Tile())
            self.tiles.append(tempRow)
            tempRow = []

    def pathExists(self, rope, direction, steps):
        destination = [rope.head[1], rope.head[0]]
        if direction == 'R':
            destination[1] += steps
        if direction == 'L':
            destination[1] -= steps
        if direction == 'D':
            destination[0] += steps
        if direction == 'U':
            destination[0] -= steps

        if min(destination) < 0 or max(destination) >= len(self.tiles) or max(destination) >= len(self.tiles[0]):
            return False
        return True


    def extend(self, direction, amount):
        width = len(self.tiles[0])
        
        if direction == 'R':
            for row in self.tiles:
                for tiles in range(amount):
                    row.append(Tile())

        if direction == 'L':
            for row in self.tiles:
                for tiles in range(amount):
                    row.insert(0, Tile())

        if direction == 'U':
            for tiles in range(amount):
                tempRow = []
                for i in range(width):
                    tempRow.append(Tile())
                self.tiles.insert(0, tempRow)

        if direction == 'D':
            for tiles in range(amount):
                tempRow = []
                for i in range(width):
                    tempRow.append(Tile())

                self.tiles.append(tempRow)



    def __str__(self, rope=False):
        string = ""
        for _row, row in enumerate(self.tiles):
            for _col, col in enumerate(row):
                char = str(col)
                if rope and rope.tail == [_col, _row]:
                    char = 'T'
                if rope and rope.head == [_col, _row]:
                    char = 'H'
                string += char
                string += " "
            string += "\n"
        return string

    def __repr__(self):
        return self.__str__()

    def __getitem__(self, key):
        return self.tiles[key]



def part1(input):
    count = 0
    
    board = Board(1, 1)
    rope = Rope(0, 0, board)

    print(board.__str__(rope))
    for line in input:
        clearConsole()
        print(f"Board: {len(board.tiles)}, {len(board.tiles[0])}")
        print(f"Tail at: {rope.tail}")
        print(f"Head at: {rope.head}")
        print(f"Instruction: {line}")
        print(board.__str__(rope))

        rope.move(line.split()[0], int(line.split()[1]), board)
        time.sleep(1)

    clearConsole()
    print(f"Board: {len(board.tiles)}, {len(board.tiles[0])}")
    print(f"Tail at: {rope.tail}")
    print(f"Head at: {rope.head}")
    print(f"Instruction: {line}")
    print(board.__str__(rope))

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