import requests, os

baseURL = "https://adventofcode.com/"

def getInput(year, day, cookie):
    fileName = f"{year}-{day}.txt"
    if os.path.isfile(fileName):
        with open(fileName, 'r') as file:
            return file.read().splitlines()

    request = requests.get(f"{baseURL}{year}/day/{day}/input", cookies={"session": cookie})

    if request.status_code == 200:
        with open(fileName, 'w') as file:
            file.write(request.text)
        return request.text.splitlines()

def postAnswer(year, day, level, answer, cookie):
    data = {"answer": answer, "level": level}
    request = requests.post(f"{baseURL}{year}/day/{day}/answer", data, cookies={"session": cookie})

    for line in request.text.splitlines():
        if line.startswith("<article"):
            return line