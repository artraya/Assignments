# Name: Alexandro Artraya do Carmo-Devine
# Student Number: 1036681

# This file is provided to you as a starting point for the "word_game.py" program of Assignment 1
# of CSP1150/CSP5110 in Semester 1, 2016.  It mainly provides you with a suitable list of words.
# Please use this file as the basis for your assignment work.  You are not required to reference it.

# Import the random module to allow us to select the word list and password at random.
import random

# This function receives two words as parameters should return the number of matching letters between them.
# See the assignment brief for details of this function's requirements.
def compareWords(guess, pickedPassword):
    count = 0
    for i,l in enumerate(guess):
        if l == pickedPassword[i]:
            count += 1
    return count

# Create a list of 100 words that are similar enough to work well for this game.
candidateWords = ['AETHER', 'BADGED', 'BALDER', 'BANDED', 'BANTER', 'BARBER', 'BASHER', 'BATHED', 'BATHER', 'BEAMED', 'BEANED', 'BEAVER', 'BECKET', 'BEDDER', 'BEDELL', 'BEDRID', 'BEEPER', 'BEGGAR', 'BEGGED', 'BELIES', 'BELLES', 'BENDED', 'BENDEE', 'BETTER', 'BLAMER', 'BLOWER', 'BOBBER', 'BOLDER', 'BOLTER', 'BOMBER', 'BOOKER', 'BOPPER', 'BORDER', 'BOSKER', 'BOTHER', 'BOWYER', 'BRACER', 'BUDGER', 'BUMPER', 'BUSHER', 'BUSIER', 'CEILER', 'DEADEN', 'DEAFER', 'DEARER', 'DELVER', 'DENSER', 'DEXTER', 'EVADER', 'GELDED', 'GELDER', 'HEARER', 'HEIFER', 'HERDER', 'HIDDEN', 'JESTER', 'JUDDER', 'KIDDED', 'KIDDER', 'LEANER', 'LEAPER', 'LEASER', 'LEVIED', 'LEVIER', 'LEVIES', 'LIDDED', 'MADDER', 'MEANER', 'MENDER', 'MINDER', 'NEATER', 'NEEDED', 'NESTER', 'PENNER', 'PERTER', 'PEWTER', 'PODDED', 'PONDER', 'RADDED', 'REALER', 'REAVER', 'REEDED', 'REIVER', 'RELIER', 'RENDER', 'SEARER', 'SEDGES', 'SEEDED', 'SEISER', 'SETTER', 'SIDDUR', 'TEENER', 'TEMPER', 'TENDER', 'TERMER', 'VENDER', 'WEDDER', 'WEEDED', 'WELDED', 'YONDER']


# Sets up game properties for initial play through and replay
def gameProperties():
    global wordList, password, guessesRemaining, Won, guessHistory
    wordList = random.sample(candidateWords, 8)
    password = random.choice(wordList)
    guessesRemaining = 4
    Won = False
    guessHistory = []
    return wordList, password, guessesRemaining, Won, guessHistory


# Loops through wordList from gameProperties and arranges with index + 1
def wordListNum(wordList):
    for i,l in enumerate(wordList):
        if i in guessHistory:
            print(" {}) {}  [{}/6 correct]".format(i+1, l, compareWords(l, password)))
        else:
            print(" {}) {}".format(i+1, l))
    print("")


# Exception handler for userInput while playing game
def userInputCheck():
    validRange = [0, 1, 2, 3, 4, 5, 6, 7, 8]
    try:
        global userInput
        userInput = int(input("Enter your guess (1 - 8): "))-1
    except:
        print("Opps, you entered a non-numeric character. Try again!")
        userInputCheck()
    else:
        if userInput in validRange and userInput not in guessHistory:
            return guessHistory.append(userInput)
        else:
            if userInput in guessHistory:
                print("Already selected this word")
                userInputCheck()
            elif userInput not in validRange:
                print("Woah! That no. is beyond the playing field. Try again!")
                userInputCheck()
            else:
                print("You fucked up somewhere...try again")
                userInputCheck()


# Exception handler for replayPrompt after game finishes
def replayPromptCheck():
    validRange = [0, 1]
    try:
        global replayInput
        replayInput = int(input("\nWould you like to play again?\nYes: 1 | No: 0\n"))
    except:
        print("Opps, you entered a non-numeric character. Try again!")
        replayPromptCheck()
    else:
        if replayInput in validRange:
            return replayInput
        else:
            print("Woah! That no. is beyond the playing field. Try again!")
            replayPromptCheck()


# Initial welcome for players and replay
def welcome():
    print("Welcome to Guess-The-Word-Game.\nPassword is one of these words:\n")


# Game domain where everything is initilised
def gameStart():
    replay = True
    while replay == True:
        welcome()
        gameProperties()
        guessesRemaining = 4
        Won = False
        while guessesRemaining > 0 and Won == False:
            wordListNum(wordList)
            print("\nGuesses remaining:", guessesRemaining)
            userInputCheck()
            guessesRemaining -= 1

            if wordList[userInput] == password:
                print("\nPassword correct")
                Won = True

            elif wordList[userInput] != password:
                print("\nLetters correct", compareWords(wordList[userInput], password), "/ 6\n")

        if Won == True:
            print("\nCongratulations, you win!")

        else:
            print("\nSorry, you lose")

        replayPromptCheck()
        if replayInput == 1:
            replay = True
        elif replayInput == 0:
            replay = False

    print("\nYou have finished Word-Game. Thanks for playing!")

gameStart()

