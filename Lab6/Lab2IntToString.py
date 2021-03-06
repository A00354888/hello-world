'''
  Luis Montes
'''

import sys


def int_to_str(intArgument):
    digitsDict = {
        0: "0", 1: "1", 2: "2", 3: "3",
        4: "4", 5: "5", 6: "6", 7: "7",
        8: "8", 9: "9"
    }
    dashChar = ""
    concatenatedStringNumber = ""

    try:
        if intArgument < 0:
            intArgument = intArgument * -1
            dashChar = "-"

        while int(intArgument / 10) != 0:
            digit = intArgument % 10
            intArgument = int(intArgument / 10)
            concatenatedStringNumber = digitsDict.get(digit) + concatenatedStringNumber

        concatenatedStringNumber = digitsDict.get(intArgument) + concatenatedStringNumber
    except Exception as error:
        raise ValueError('Integer cannot be converted to String.' + error)
    return dashChar + concatenatedStringNumber


def main(args):
    if len(args) > 1:
        userInput = args[1]
    else:
        userInput = input("Please enter a number: ")

    intUserInput = int(userInput)
    result = int_to_str(intUserInput)
    print("Original value: " + userInput + ". Type: " + str(type(intUserInput)))
    print("Converted value: " + result + ". Type: " + str(type(result)))


if __name__ == "__main__":
    main(sys.argv)