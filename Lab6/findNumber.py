import random


def main():
    print("Guessing Game")
    numberToGuess = random.randint(1, 30)
    exitGame = False
    numberOfGuesses = 0

    file = open("GuessingSteps.txt", "w")
    file.write("Number to guess: " + str(numberToGuess) + "\n")
    file.write("User guesses\n")

    while not(exitGame):

        userInput = input("Enter one number: ")
        if not(userInput.isnumeric()) and userInput != "exit":
            msg = "Please enter a non decimal number\n"
            file.write(msg)
            print(msg)
        else:
            if userInput == "exit":
                file.write("Exit")
                exitGame = True
            else:
                numberOfGuesses += 1
                numberPicked = int(userInput)
                if numberToGuess == numberPicked:
                    msg = "Try #" + str(numberOfGuesses) + ": Number picked: " + str(numberPicked) + " - You guessed right!\n"
                    file.write(msg)
                    print(msg)
                    exitGame = True
                elif numberToGuess > numberPicked:
                    msg = "Try #" + str(numberOfGuesses) + ": Number picked: " + str(numberPicked) + " - The secret number is greater\n"
                    file.write(msg)
                    print(msg)
                else:
                    msg = "Try #" + str(numberOfGuesses) + ": Number picked: " + str(numberPicked) + " - The secret number is lower\n"
                    file.write(msg)
                    print(msg)

    file.close()
    print("Bye")


if __name__ == "__main__":
    main()
