import requests, os, re

baseURL = "https://adventofcode.com/"

headers = {"User-Agent": "github.com/Armandur/AdventOfCode by rasmus.pettersson.vik@gmail.com"}

class colors:
    black = "30m"
    red = "31m"
    brightred = "91m"
    green = "32m"
    brightgreen = "92m"
    yellow = "33m"
    brightyellow = "93m"
    blue = "34m"
    brightblue = "94m"
    magenta = "35m"
    brightmagenta = "95m"
    cyan = "36m"
    brightcyan = "96m"
    white = "37m"
    brightwhite = "97m"

    bluebg = "44m"
    cyanbg = "46m"
    redbg = "41m"
    greenbg = "42m"

    brightgreenbg = "102m"
    

    colors = [red, green, yellow, blue, magenta, cyan]
    brightColors = [brightred,  brightgreen, brightyellow, brightblue, brightmagenta, brightcyan]


def colorString(string, color):
	start = "\033["
	start += color
	reset = "\033[0m"
	return f"{start}{string}{reset}"
    

def getInput(year, day, cookie):
    fileName = f"{year}\{year}-{day}.txt"
    if os.path.isfile(fileName):
        with open(fileName, 'r') as file:
            return file.read().splitlines()

    request = requests.get(f"{baseURL}{year}/day/{day}/input", cookies={"session": cookie}, headers=headers)

    if request.status_code == 200:
        with open(fileName, 'w') as file:
            file.write(request.text)
        return request.text.splitlines()
    else:
        print(f"Error: {request.status_code}")

def postAnswer(year, day, level, answer, cookie):
    data = {"answer": answer, "level": level}
    request = requests.post(f"{baseURL}{year}/day/{day}/answer", data, cookies={"session": cookie}, headers=headers)

    for line in request.text.splitlines():
        if line.startswith("<article"):
            return re.sub('<[^<]+?>', '', line)