def getPoints(line):
    games = line.split("|")

    winningNums = set()
    ownedNums = set()

    for i, game in enumerate(games):
        game = game.strip()
        nums = game.split()

        if i == 0:
            for num in nums:
                winningNums.add(int(num))
        else:
            for num in nums:
                ownedNums.add(int(num))

    commonSet = winningNums.intersection(ownedNums)
    size = len(commonSet)
    if size == 0:
        return 0
    else:
        return 2 ** (size-1)

def main():
    inputFile = "/Users/siddmittal/Desktop/advent-of-code/day4/input.txt"
    totalPoints = 0

    with open(inputFile, 'r') as file:
        for line in file:
            line = line.strip()
            index = line.index(":")
            line = line[index+2:]
            totalPoints += getPoints(line)
    
    print(totalPoints)

if __name__ == "__main__":
    main()