import util
import datetime
import sys
import time
import os
import copy

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
            return boldString("#")
        return "."

    def __repr__(self) -> str:
        return self.__str__()


class Rope:
    def __init__(self, x, y, length, board):
        # x = Column, 0 = left
        # y = Row, 0 = top

        self.sections = []
        for i in range(length):
            self.sections.append([x, y])
        self.length = length

        board[self.sections[::-1][0][1]][self.sections[::-1][0][0]].visited = True

    def _distance(self, node1, node2):
        return int(((node1[0] - node2[0])**2 + (node1[1] - node2[1])**2)**0.5)

    def _getDirection(self, ahead, behind):
        if ahead == behind:
            return [0, 0]

        leftRight = upDown = 0

        if ahead[0] > behind[0]:
            leftRight = 1
        elif ahead[0] < behind[0]:
            leftRight = -1
        else:
            leftRight = 0

        if ahead[1] > behind[1]:
            upDown = 1
        elif ahead[1] < behind[1]:
            upDown = -1
        else:
            upDown = 0

        return [leftRight, upDown]

    def move(self, direction, steps, board, display=False, speed=0.5):
        if not board.pathExists(self, direction, steps): # Need to extend the board if destination is out of bounds
            amount = steps
            board.extend(direction, amount)
            
            for section in self.sections:
                if direction == 'L': #X should increase by steps
                    section[0] += amount
                if direction == 'U': #Y should increase by steps
                    section[1] += amount

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
            head = self.sections[0]
            
            newX = head[0]+deltaX #New X-position of head
            newY = head[1]+deltaY #New Y-position of head
            
            self.sections[0] = [newX, newY] # Move the head
            
            for index, section in enumerate(self.sections[1:]): #Check and move next sections, skip the first
                current = section
                next = self.sections[index]
                distance = self._distance(current, next)
                if distance > 1: #We have a gap, need to follow with the sections!    
                    nextDirection = self._getDirection(next, current)
                    nextPos = [current[0]+nextDirection[0], current[1]+nextDirection[1]]
                    self.sections[index+1] = nextPos

            tail = self.sections[::-1][0]
            board.tiles[tail[1]][tail[0]].visited = True
            if display:
                clearConsole()
                print(board.__str__(self))
                time.sleep(speed)


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
        destination = [rope.sections[0][1], rope.sections[0][0]]
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
                if rope:
                    for id, section in enumerate(rope.sections):
                        if section == [_col, _row]:
                            char = str(id)
                            break
                if char == '0': char = 'H'
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
    
    board = Board(4, 4)
    rope = Rope(1, 1, 2, board)

    for line in input:
        rope.move(line.split()[0], int(line.split()[1]), board)

    tiles = [tile for row in board.tiles for tile in row]
    for tile in tiles:
        if tile.visited:
            count += 1

    return count


def part2(input):
    count = 0
    
    board = Board(4, 4)
    rope = Rope(1, 1, 10, board)

    for line in input:
        rope.move(line.split()[0], int(line.split()[1]), board)

    tiles = [tile for row in board.tiles for tile in row]
    for tile in tiles:
        if tile.visited:
            count += 1
    
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