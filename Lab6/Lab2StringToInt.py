'''
  Luis Montes
'''

import sys


def str_to_int(strArgument):
    sumTotal = 0
    base = 10
    factor = 1
    digitsDict = {
        "0": 0, "1": 1, "2": 2, "3": 3,
        "4": 4, "5": 5, "6": 6, "7": 7,
        "8": 8, "9": 9
    }

    for digit in reversed(range(0, len(strArgument))):
        if digit == 0 and strArgument[digit] == "-":
            sumTotal = -1 * sumTotal
        else:
            try:
                sumTotal = sumTotal + digitsDict.get(strArgument[digit]) * factor
            except Exception as error:
                raise ValueError('String cannot be converted to Integer.')
            factor = factor * base
    return sumTotal


if len(sys.argv) > 1:
    userInput = sys.argv[1]
else:
    userInput = input("Please enter a number: ")

result = str_to_int(userInput)
print("Original value: " + userInput + ". Type: " + str(type(userInput)))
print("Converted value: " + str(result) + ". Type: " + str(type(result)))
