import util

class Point:
    def __init__(self, x ,y):
        self.x = x
        self.y = y

    def __str__(self):
        return f"({self.x}, {self.y})"

    def __repr__(self):
        return self.__str__()

    def __eq__(self, other):
        if self.x == other.x and self.y == other.y:
            return True
        return False

class Line:
    def __init__(self, a, b):
        self.a = a
        self.b = b

    def __str__(self):
        return f"{self.a} -> {self.b}"

    def __repr__(self):
        return self.__str__()

    def getLinePoints(self): #Return a list of all coordinates in the line
        points = []
        if self.getOrientation() == "dot":
            points.append(self.a)

        if self.getOrientation() == "right":
            for i in range(self.a.x, self.b.x+1):
                points.append(Point(i, self.a.y))

        if self.getOrientation() == "left":
            for i in range(self.a.x, self.b.x-1, -1):
                points.append(Point(i, self.a.y))

        if self.getOrientation() == "down":
            for i in range(self.a.y, self.b.y+1):
                points.append(Point(self.a.x, i))

        if self.getOrientation() == "up":
            for i in range(self.a.y, self.b.y-1, -1):
                points.append(Point(self.a.x, i))

        # And now for the diagonals

        if self.getOrientation() == "downright":
            distance = abs(self.a.x - self.b.x)
            for i in range(0, distance + 1):
                points.append(Point(self.a.x+i, self.a.y+i))

        if self.getOrientation() == "downleft":
            distance = abs(self.a.x - self.b.x)
            for i in range(0, distance + 1):
                points.append(Point(self.a.x - i, self.a.y + i))

        if self.getOrientation() == "upright":
            distance = abs(self.a.y - self.b.y)
            for i in range(0, distance + 1):
                points.append(Point(self.a.x+i, self.a.y-i))

        if self.getOrientation() == "upleft":
            distance = abs(self.a.y - self.b.y)
            for i in range(0, distance + 1):
                points.append(Point(self.a.x-i, self.a.y-i))

        return points


    def getOrientation(self):
        if self.a == self.b: # Just a dot:
            return "dot"
        if self.a.x == self.b.x: #Vertical
            if self.a.y < self.b.y:
                return "down"
            else:
                return "up"
        if self.a.y == self.b.y: #Horizontal
            if self.a.x < self.b.x:
                return "right"
            else:
                return "left"

        diagonalstring = ""
        if self.a.y < self.b.y:
            diagonalstring += "down"
        if self.a.y > self.b.y:
            diagonalstring += "up"
        if self.a.x < self.b.x:
            diagonalstring += "right"
        if self.a.x > self.b.x:
            diagonalstring += "left"
        return diagonalstring


def getLargest(lines, xy):
    largest = 0
    if xy == 'x':
        for line in lines:
            if line.a.x > largest:
                largest = line.a.x
            if line.b.x > largest:
                largest = line.b.x
    elif xy == 'y':
        for line in lines:
            if line.a.y > largest:
                largest = line.a.y
            if line.b.y > largest:
                largest = line.b.y
    return largest


def part1(input):
    count = 0
    lines = []

    for line in input:
        points = line.split(" -> ")

        tempPoints = []
        for point in points:
            point = point.split(',')
            point = list(map(int, point))
            tempPoints.append(Point(point[0], point[1]))
        lines.append(Line(tempPoints[0], tempPoints[1]))

    orthoLines = []
    for line in lines:
        #print(f"{line}, {line.getOrientation()}")
        if line.getOrientation() != "diagonal" and line.getOrientation() != "dot":
            orthoLines.append(line)

    print(f"Largest X: {getLargest(orthoLines, 'x')}\nLargest Y: {getLargest(orthoLines, 'y')}")

    oceanFloor = [[0 for col in range(getLargest(orthoLines, 'y')+2)] for row in range(getLargest(orthoLines, 'x')+2)]

    for line in orthoLines:
        for coordinate in line.getLinePoints():
            oceanFloor[coordinate.x][coordinate.y] += 1

    for row in oceanFloor:
        print(row)

    for row in oceanFloor:
        for col in row:
            if col >= 2:
              count += 1
    return count


def part2(input):
    count = 0
    lines = []

    for line in input:
        points = line.split(" -> ")

        tempPoints = []
        for point in points:
            point = point.split(',')
            point = list(map(int, point))
            tempPoints.append(Point(point[0], point[1]))
        lines.append(Line(tempPoints[0], tempPoints[1]))

    #for line in lines:
    #    print(f"{line}, {line.getOrientation()}, {line.getLinePoints()}")

    print(f"Largest X: {getLargest(lines, 'x')}\nLargest Y: {getLargest(lines, 'y')}")
    oceanFloor = [[0 for col in range(getLargest(lines, 'y')+2)] for row in range(getLargest(lines, 'x') + 2)]

    for line in lines:
        for coordinate in line.getLinePoints():
            oceanFloor[coordinate.x][coordinate.y] += 1

    for row in oceanFloor:
        for col in row:
            if col >= 2:
              count += 1
    return count


if __name__ == '__main__':
	input = util.getInput(2021, 5)
	test = []
	with open("test.txt", "r") as file:
		test = file.read().splitlines()

	#print(f"Part one: {part1(test)}")
	#print(util.postAnswer(2021, 5, 1, part1(input)))

	#print(f"Part two: {part2(input)}")
	print(util.postAnswer(2021, 5, 2, part2(input)))