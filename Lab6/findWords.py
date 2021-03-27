import sys
import os.path
from os import path

def countWordsInText(text):    
    wordDict = {}    
    for wordInText in text.split():
        wordDict[wordInText] = int(wordDict.get(wordInText, 0)) + 1    
    return wordDict

def createUserWordList():
    userInput = "Y"
    wordList = []
    while userInput.upper() == "Y"  :
        wordList.append(input("Please enter a word, the program will count the number of occurrences in the file: "))
        userInput = input("Do you wish to enter other word? (Y/N): ")
    return wordList

def askForFilePath(argFilePath):
    filePath = ""
    if path.exists(argFilePath):
        filePath = argFilePath
    else:
        fileNotFound = True
        while fileNotFound:
            userFilePath = input("File does not exist. Enter file name: ")
            if path.exists(userFilePath):
                filePath = userFilePath
                fileNotFound = False
    return filePath

def readTextFile(filePath):
    file = open(filePath, "r")
    return file.read()

if len(sys.argv) == 3:
    filePath = sys.argv[1]
    wordList = sys.argv[2].split(",")       
    if not(len(wordList) > 0) :
        wordList = createUserWordList()
else:   
    filePath = input("Enter file name: ")
    wordList = createUserWordList()

filePath = askForFilePath(filePath)
text = readTextFile(filePath)
returnDict = countWordsInText(text)

for word in wordList:
    print("Number of occurrences in text for word: '" + word + "' is: " + str(returnDict.get(word, 0)))
