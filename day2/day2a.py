"""
Determine which games would have been possible if the bag 
had been loaded with only 12 red cubes, 13 green cubes, 
and 14 blue cubes. What is the sum of the IDs of those games?

eg. 

Game 4: 1 green, 3 red, 6 blue; 3 green, 6 red; 3 green, 15 blue, 14 red
Game 5: 6 red, 1 blue, 3 green; 2 blue, 1 red, 2 green

Game 4 is impossible since they take out 15 blue one time
Game 5 is possible

max: 
12 red cubes
13 green cubes
14 blue cubes
"""
import re

def getValidGame(line, gameNumber):
    semiColon = line.index(":")
    line = line[semiColon + 2:]

    parts = re.split(",|;", line)
    for element in parts:
        strippedElement = element.strip()
        parsed = strippedElement.split(" ")
        num = int(parsed[0])
        
        if "red" in element:
            if num > 12:
                return 0
        elif "green" in element:
            if num > 13:
                return 0
        elif "blue" in element:
            if num > 14:
                return 0
        else:
            return 0
            
    print(line)
    print(gameNumber)
    print("----------")
    return gameNumber            

def main():
    totalSum = 0
    gameNumber = 1
    inputFile = "/Users/siddmittal/Desktop/advent-of-code/day2/input.txt"
    with open(inputFile, "r") as file:
        for line in file:
            line = line.strip()
            totalSum += getValidGame(line, gameNumber)
            gameNumber += 1
    
    print(totalSum)

if __name__ == "__main__":
    main()