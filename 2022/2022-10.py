import util
import datetime
import sys

def boldString(string):
	start = "\033[92m"
	end = "\033[0m"
	return f"{start}{string}{end}"

class CPU:
    def __init__(self, input, speed=2):
        self.X = 1
        self.cycle = 0

        self.operations = []
        self.loadOperations(input)
        
        self.currentOperation = None
        self.operationRunning = False
        self.operationSpeed = speed-1
        self.operationTimeLeft = 0

    def loadOperations(self, input):
        for line in input:
            operation = ["", None]
            operation[0] = line.split()[0]
            if len(line.split()) == 2:
                operation[1] = int(line.split()[1])
            self.operations.insert(0, operation)

    def runProgram(self, cycles, program):
        result = None
        if program == "Signalstrength":
            interestingCycles = [20, 60, 100, 140, 180, 220]
            result = []
            for cycle in range(1, cycles+1):
                if cycle in interestingCycles:
                    result.append((cycle)*self.X)
                self.tick()

            return sum(result)
        if program == "Display":
            display = []
            displayWidth = 40
            cursorPosition = 0

            line = []
            for cycle in range(1, cycles+1):
                if cursorPosition >= self.X -1 and cursorPosition <= self.X +1:
                    line.append(boldString("#"))
                else:
                    line.append(".")
                self.tick()
                cursorPosition += 1
                if cursorPosition == displayWidth:
                    display.append(line)
                    line = []
                    cursorPosition = 0
            
            return display

    def tick(self):
        self.cycle += 1
        if not self.currentOperation:
            self.currentOperation = self.operations.pop()
        
        #print()
        #print(f"Cycle {self.cycle}")
        #print(f"Operation {self.currentOperation}")
        #print(f"X register: {self.X}")

        if self.currentOperation[0] == "noop":
            if self.operations:
                self.currentOperation = self.operations.pop()
            return
        
        if self.currentOperation[0] == "addx":
            if not self.operationRunning:
                self.operationTimeLeft = self.operationSpeed
                self.operationRunning = True
            
            if self.operationRunning and self.operationTimeLeft > 0:
                self.operationTimeLeft -= 1
                return

            if self.operationTimeLeft == 0 and self.operationRunning:
                self.X += self.currentOperation[1]
                if self.operations:
                    self.currentOperation = self.operations.pop()
                self.operationRunning = False               
        return


def part1(input):
    count = 0
    cpu = CPU(input)
    
    count = cpu.runProgram(220, "Signalstrength")
    
    return count


def part2(input):
    count = 0
    cpu = CPU(input)
    
    output = cpu.runProgram(240, "Display")
    for line in output:
        print(''.join(line))
        
    return


if __name__ == '__main__':
    cookie = sys.argv[1]
    today = datetime.datetime.now()
    input = util.getInput(today.year, today.day, cookie)
    test = []
    with open(f"{today.year}/test.txt", "r") as file:
        test = file.read().splitlines()
        
    print(f"Part one: {part1(input)}")
	#print(util.postAnswer(today.year, today.day, 1, part1(input), cookie)
    print(f"Part two: {part2(input)}")
	#print(util.postAnswer(today.year, today.day, 2, part2(input), cookie))