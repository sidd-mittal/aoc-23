"""
- almost working
- not done yet
main bug: 
jheightwovtone8fourtcsbhhntkq3nine1nine

11, one
34, 1
6, two
29, 3
15, four
2, eight
14, 8
30, nine
{11: 'one', 34: '1', 6: 'two', 29: '3', 15: 'four', 2: 'eight', 14: '8', 30: 'nine'}
81
"""


def getSum(line):
    numbers = {
        "one": "1",
        "two": "2",
        "three": "3", 
        "four": "4",
        "five": "5",
        "six": "6",
        "seven": "7",
        "eight": "8",
        "nine": "9"
    }

    parsed = {}

    for key, value in numbers.items():
        if key in line:
            index = line.index(key)
            parsed[index] = key
            print(f"{index}, {key}")
        
        if value in line:
            index = line.index(value)
            parsed[index] = value
            print(f"{index}, {value}")
    
    print(parsed)

    maxIndex = max(parsed.keys())
    minIndex = min(parsed.keys())

    firstDigit = parsed[minIndex]
    secondDigit = parsed[maxIndex]

    firstDigit = numbers.get(firstDigit, firstDigit)
    secondDigit = numbers.get(secondDigit, secondDigit)

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

    print(totalSum)
            
if __name__ == "__main__":
    main()