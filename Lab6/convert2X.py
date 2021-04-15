'''
  A00354888 - Luis Eduardo Montes Siordia
'''

import sys


def decimalToHexadecimal(number):
    hexDict = {
        0: "0",
        1: "1",
        2: "2",
        3: "3",
        4: "4",
        5: "5",
        6: "6",
        7: "7",
        8: "8",
        9: "9",
        10: "A",
        11: "B",
        12: "C",
        13: "D",
        14: "E",
        15: "F",
    }
    hexadecimalNumber = ""
    while number >= 16:
        hexadecimalNumber = hexDict[number % 16] + hexadecimalNumber
        number = int(number / 16)
    hexadecimalNumber = hexDict[number] + hexadecimalNumber
    return hexadecimalNumber


def decimalToBinary(number):
    binaryNumber = ""
    while number >= 2:
        binaryNumber = str(int(number % 2)) + binaryNumber
        number = int(number / 2)
    binaryNumber = str(number) + binaryNumber
    return binaryNumber

def main(args):
    if len(args) > 1:
        userInput = args[1]
    else:
        userInput = input("Please enter a number: ")

    while not(userInput.isnumeric()):
        userInput = input("Please enter a non decimal number: ")

    userNumber = int(userInput)
    hexadecimalNumber = decimalToHexadecimal(userNumber)
    binaryNumber = decimalToBinary(userNumber)
    print("\nDecimal Number: " + userInput)
    print("Binary Number: " + binaryNumber)
    print("Hexadecimal Number: " + hexadecimalNumber + "\n")


if __name__ == "__main__":
    main(sys.argv)
