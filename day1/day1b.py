"""
Your calculation isn't quite right. It looks like some of the 
digits are actually spelled out with letters: one, two, three,
 four, five, six, seven, eight, and nine also count as valid 
 "digits".

sixdddkcqjdnzzrgfourxjtwosevenhg9

this line should return 69 (six is first digit and 9 is last digit)

ndtwone562kzfhdrhgcjv4two

12

"""

def getSum(line):
    # this is the funniest thing i've ever done lmfao --> got inspo from the subreddit
    numbers = {
        "one": "o1e",
        "two": "t2o",
        "three": "thr3e", 
        "four": "fo4r",
        "five": "fi5e",
        "six": "s6x",
        "seven": "sev7n",
        "eight": "eig8t",
        "nine": "ni9e"
    }

    # pretty naive way --> replace all occurences of the string with the number equivalent
    # then proceed as usual 

    newLine = line
    for key, value in numbers.items():
        if key in line:
            newLine = newLine.replace(key, value)
    
    # find first digit
    for char in newLine:
        if char.isdigit():
            firstDigit = char
            break
    
    # find second digit
    for char in reversed(newLine):
        if char.isdigit():
            secondDigit = char
            break
    
    twoDigitNumber = int(firstDigit) * 10 + int(secondDigit)
    return twoDigitNumber


def main():
    totalSum = 0

    inputFile = "/Users/siddmittal/Desktop/advent-of-code/day1/input.txt"

    with open(inputFile, "r") as file:
        for line in file:
            print(line)
            sum = getSum(line)
            print(sum)
            totalSum += sum

    print("total: ", totalSum)
            
if __name__ == "__main__":
    main()