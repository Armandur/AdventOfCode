import util
import datetime
import sys
from math import lcm


def boldString(string):
	start = "\033[92m"
	end = "\033[0m"
	return f"{start}{string}{end}"


class Monkey:
    LeastCommonMultiple = 0

    def __init__(self, id):
        self.id = id
        self.items = []
        self.operator = ""
        self.arguments = [0, 0]
        self.testDivisble = [-1, -1, -1] # [Divisible by, True Monkey ID, False Monkey ID]
        self.inspections = 0

    def __str__(self, verbose=False):
        string = ""
        if verbose:
            string =  f"Monkey {self.id}\n"
            string += f"Starting items: {self.items}\n"
            string += f"Operation: new = {self.arguments[0]} {self.operator} {self.arguments[1]}\n"
            string += f"Test: divisible by {self.testDivisble[0]}\n"
            string += f"If true: throw to monkey {self.testDivisble[1]}\n"
            string += f"If false: throw to monkey {self.testDivisble[2]}"
            return string
        
        string += f"Monkey {self.id}, Inspections: {self.inspections} : {self.items}"
        return string

    def calculate(self, PANIC=False):
        if not self.items:
            return -1
        
        currentItem = self.items[0]
        worry = a = b = 0

        if self.arguments[0] == "old":
            a = currentItem
        else:
            a = self.arguments[0]

        if self.arguments[1] == "old":
            b = currentItem
        else:
            b = self.arguments[1]

        match self.operator:
            case '+':
                worry = a + b

            case '*':
                worry = a * b

            case other:
                # uh oh
                return -1
        self.inspections += 1

        return worry

    def getNextMonkey(self, worry):
        if worry % self.testDivisble[0] == 0:
            return (self.testDivisble[1], True)
        else:
            return (self.testDivisble[2], False)

# A pack of monkeys is called a barrel or a troop
class Barrel:
    def __init__(self, input):
        self.monkeys = []
        self.load(input)

    def __str__(self, verbose=False):
        string = ""
        if verbose:
            for monkey in self.monkeys:
                string += str(monkey)
                string += "\n"
            return string       

        string = "Monkeys: "
        for monkey in self.monkeys:
            string += str(monkey.id)
            string += " "
        return string

    def load(self, input):
        chunkLength = 7
        for i in range(0, len(input), chunkLength):
            chunk = input[i:i+chunkLength]
            
            if not chunk:
                break
            
            monkey = Monkey(int(chunk[0].split()[1][:-1]))
            
            items = chunk[1].split(': ')[1].split(', ')
            monkey.items = list(map(int, items))
            monkey.operator = chunk[2][::-1].split()[1] #Reverse the list, split it by space and take the second element
            monkey.arguments = chunk[2].split(' = ')[1].split(f" {monkey.operator} ")

            if monkey.arguments[0] != "old": monkey.arguments[0] = int(monkey.arguments[0])
            if monkey.arguments[1] != "old": monkey.arguments[1] = int(monkey.arguments[1])

            monkey.testDivisble[0] = int(chunk[3].split()[-1])
            monkey.testDivisble[1] = int(chunk[4].split()[-1])
            monkey.testDivisble[2] = int(chunk[5].split()[-1])

            self.monkeys.append(monkey)

        divisors = []
        for monkey in self.monkeys:
            divisors.append(monkey.testDivisble[0])
        
        Monkey.LeastCommonMultiple = lcm(*map(int, divisors))

    
    def doRounds(self, rounds, PANIC=False, verbose=False):
        for round in range(1, rounds+1):
            if verbose:
                print()
                print(f"Round {round}")
            for i in range(0, len(self.monkeys)):
                monkey = self.monkeys[i]
                if verbose:
                    print(f"Monkey {monkey.id}")

                for item in monkey.items.copy():
                    worry = 0
                    if PANIC:
                        worry = monkey.calculate() % Monkey.LeastCommonMultiple # 🧙
                    else:
                        worry = monkey.calculate() // 3

                    nextMonkey = monkey.getNextMonkey(worry)
                    item = self.monkeys[i].items.pop(0)

                    self.monkeys[nextMonkey[0]].items.append(worry)
                    if verbose:
                        print(f"Monkey looks at item [{boldString(item)}], you worry {boldString(worry)}")
                        print(f"Monkey throws item to monkey {boldString(nextMonkey[0])}, {nextMonkey[1]}")
                        print()
                if verbose:
                    print()


def part1(input):
    count = 0
    barrel = Barrel(input)
    print(barrel.__str__(True))
    barrel.doRounds(20)
    print(barrel.__str__(True))

    def getInspection(monkey):
        return monkey.inspections

    barrel.monkeys.sort(key=getInspection, reverse=True)

    count = barrel.monkeys[0].inspections * barrel.monkeys[1].inspections
    print(f"Monkeybusiness level is {boldString(count)}")

    return count


def part2(input):
    count = 0
    barrel = Barrel(input)
    print(barrel.__str__(True))
    barrel.doRounds(10000, PANIC=True)
    print(barrel.__str__(True))

    def getInspection(monkey):
        return monkey.inspections

    barrel.monkeys.sort(key=getInspection, reverse=True)

    count = barrel.monkeys[0].inspections * barrel.monkeys[1].inspections
    print(f"Monkeybusiness level is {boldString(count)}")
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