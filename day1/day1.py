"""
The newly-improved calibration document consists of lines of text; each line originally 
contained a specific calibration value that the Elves now need to recover. On each line, 
the calibration value can be found by combining the first digit and the last digit (in that order) 
to form a single two-digit number.

1abc2
pqr3stu8vwx
a1b2c3d4e5f
treb7uchet

In this example, the calibration values of these four lines are 12, 38, 15, and 77. Adding these together produces 142.
"""

def getSum(line):
    # find the first digit
    for char in line: 
        if char.isdigit():
            firstDigit = char
            break
    
    # find the last digit
    for char in reversed(line):
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
            totalSum += getSum(line)
    
    print(totalSum)
            
if __name__ == "__main__":
    main()