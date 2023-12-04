"""
Card 1: 41 48 83 86 17 | 83 86  6 31 17  9 48 53
Card 2: 13 32 20 16 61 | 61 30 68 82 17 32 24 19
Card 3:  1 21 53 59 44 | 69 82 63 72 16 21 14  1
Card 4: 41 92 73 84 69 | 59 84 76 51 58  5 54 83
Card 5: 87 83 26 28 32 | 88 30 70 12 93 22 82 36
Card 6: 31 18 13 56 72 | 74 77 10 23 35 67 36 11

Card 1 has four matching numbers, so you win one copy each of the next four cards: cards 2, 3, 4, and 5.

Your original card 2 has two matching numbers, so you win one copy each of cards 3 and 4.

Your copy of card 2 also wins one copy each of cards 3 and 4.

Your four instances of card 3 (one original and three copies) have two matching numbers, so you win four copies each of cards 4 and 5.

Your eight instances of card 4 (one original and seven copies) have one matching number, so you win eight copies of card 5.

Your fourteen instances of card 5 (one original and thirteen copies) have no matching numbers and win no more cards.

Your one instance of card 6 (one original) has no matching numbers and wins no more cards.
"""

from collections import defaultdict

scratchCards = defaultdict(int)

def getMatches(line):
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
    return size

def main():
    inputFile = "/Users/siddmittal/Desktop/advent-of-code/day4/input.txt"
    gameNumber = 1

    with open(inputFile, 'r') as file:
        for line in file:
            line = line.strip()
            index = line.index(":")
            line = line[index+2:]
            matches = getMatches(line)

            # add original card: 
            scratchCards[gameNumber] += 1
            currCards = scratchCards[gameNumber]
            for num in range(currCards):
                for i in range(1, matches + 1):
                    # add all copies
                    scratchCards[gameNumber + i] += 1
                
            gameNumber += 1
    
        totalMatches = 0

        for matches in scratchCards.values():
            totalMatches += matches

        print(totalMatches)

if __name__ == "__main__":
    main()