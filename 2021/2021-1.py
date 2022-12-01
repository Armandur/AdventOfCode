import util

def part1():
    input = util.getInput(2021, 1)
    #input = open("test.txt", 'r').read().splitlines()
    count = 0
    for i in range(1, len(input)):
        if int(input[i]) > int(input[i-1]):
            count += 1
    return count

def part2():
    input = util.getInput(2021, 1)
    #input = open("test.txt", 'r').read().splitlines()

    input = list(map(int, input))
    count = 0
    for i in range(0, len(input)-3):
        A = input[i:i+3]
        B = input[i+1:i+4]
        if sum(B) > sum(A):
            count += 1
    return count

if __name__ == '__main__':
    print(f"Part one: {part1()}")
    print(f"Part two: {part2()}")