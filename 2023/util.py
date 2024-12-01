import requests, os, re

baseURL = "https://adventofcode.com/"

headers = {"User-Agent": "github.com/Armandur/AdventOfCode by rasmus.pettersson.vik@gmail.com"}

class colors:
	black = "30m"
	red = "31m"
	green = "32m"
	yellow = "33m"
	blue = "34m"
	magenta = "35m"
	cyan = "36m"
	white = "37m"

	colors = [red, green, yellow, blue, magenta, cyan]


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