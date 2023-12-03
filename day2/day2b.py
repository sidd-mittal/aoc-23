"""
need to basically find the max of each color per game
and multiply all numbers maxes together
"""

import re

def getValidGame(line):
    semiColon = line.index(":")
    line = line[semiColon + 2:]

    parts = re.split(",|;", line)

    # if a color doesn't exist, we want to multiply by 1 so it doesn't impact the result
    maxRed = 1
    maxGreen = 1
    maxBlue = 1

    for element in parts:
        parsed = element.split()
        num = int(parsed[0])
        
        if "red" in element:
            maxRed = max(maxRed, num)
        elif "green" in element:
            maxGreen = max(maxGreen, num)
        elif "blue" in element:
            maxBlue = max(maxBlue, num)
    
    powerOfSet = maxRed * maxGreen * maxBlue
    return powerOfSet

def main():
    totalSum = 0
    inputFile = "/Users/siddmittal/Desktop/advent-of-code/day2/input.txt"
    with open(inputFile, "r") as file:
        for line in file:
            line = line.strip()
            totalSum += getValidGame(line)
    
    print(totalSum)

if __name__ == "__main__":
    main()