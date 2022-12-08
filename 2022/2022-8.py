import util
import datetime
import sys

def boldString(string):
	start = "\033[92m"
	end = "\033[0m"
	return f"{start}{string}{end}"

class Tree:
    def __init__(self, height):
        self.height = int(height)
        self.visible = False
        self.scenicScore = 0

    def __str__(self):
        if not self.visible:
            return str(self.height)
        return boldString(self.height)

    def __repr__(self) -> str:
        return self.__str__()

class Forest:
    def __init__(self, trees=[]):
        self.trees = trees
        
        self.width = len(self.trees[0]) #Left-Right
        self.height = len(self.trees) #Up-Down
        
        self.__observe()

    def __str__(self, scenicScore=False):
        string = ""
        for row in self.trees:
            for tree in row:
                if scenicScore:
                    string += f"{str(tree.scenicScore)}"
                else:
                    string += f"{str(tree)}"

                string += " "
            string += "\n"
        return string

    def visibleTrees(self):
        count = 0
        for row in self.trees:
            for tree in row:
                if tree.visible:
                    count += 1
        return count

    def highestScenicScore(self):
        allScores = [tree.scenicScore for row in self.trees for tree in row]
        return max(allScores)

    def _calculateScenicScore(self, row, column):
        height = self.trees[row][column].height
        score = [0, 0, 0, 0] #Right, Left, Up, Down
        
        #Look right
        for num, tree in enumerate(self.trees[row][column+1:]):
            if tree.height < height:
                score[0] = num+1
                continue
            score[0] = num+1
            break

        #Look left
        for num, tree in enumerate(self.trees[row][column-1::-1]): # Witchcraft!
            if tree.height < height:
                score[1] = num+1
                continue
            score[1] = num+1
            break

        if column == 0: #Fix for 0 score on edge trees
            score[1] = 0

        #Look up
        for num, _row in enumerate(self.trees[row-1::-1]):
            tree = _row[column]
            if tree.height < height:
                score[2] = num+1
                continue
            score[2] = num+1
            break

        if row == 0: #Fix for 0 score on edge trees
            score[2] = 0

        #Look down
        for num, _row in enumerate(self.trees[row+1:]):
            tree = _row[column]
            if tree.height < height:
                score[3] = num+1
                continue
            score[3] = num+1
            break


        return score[0] * score[1] * score[2] * score[3]
    
    def __observe(self):
        for row in range(self.width):
            for col in range(self.height):
                self.trees[row][col].scenicScore = self._calculateScenicScore(row, col)

        for index in range(self.width):
            self.__checkRow(index, "right")
        
        for index in range(self.width):
            self.__checkRow(index, "left")

        for index in range(self.height):
            self.__checkRow(index, "down")

        for index in range(self.height):
            self.__checkRow(index, "up")

    def __checkRow(self, index, direction):
        maxHeight = -1

        if direction == "right": # 0-99
            for tree in self.trees[index]:
                if tree.height > maxHeight:
                    tree.visible = True
                    maxHeight = tree.height
            return

        if direction == "left": # 99-0
            for tree in self.trees[index][::-1]: # Reverse the line in place
                if tree.height > maxHeight:
                    tree.visible = True
                    maxHeight = tree.height
            return
            
        if direction == "down": # 0-99
            for row in self.trees:
                if row[index].height > maxHeight:
                    row[index].visible = True
                    maxHeight = row[index].height
            return

        if direction == "up": # 99-0
            for row in self.trees[::-1]: # Reverse the line in place
                if row[index].height > maxHeight:
                    row[index].visible = True
                    maxHeight = row[index].height
            return 

def loadForest(input):
    temp = []
    for line in input:
        tempRow = []
        for position in line:
            tempRow.append(Tree(position))
        temp.append(tempRow)
    
    return Forest(temp)


def part1(input):
    count = 0

    forest = loadForest(input)

    #print(forest)
    #print(f"\nVisible trees: {forest.visibleTrees()}")

    count = forest.visibleTrees()

    return count


def part2(input):
    count = 0
    
    forest = loadForest(input)
    
    #print(forest)
    #print(forest.__str__(scenicScore=True))
    
    count = forest.highestScenicScore()
    
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