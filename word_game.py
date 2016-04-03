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
exceptionListNum = ["Woah! That no. is beyond the playing field. Try again!", "Can you even count?!", "Sorry, can't hold all these numbers", "Errrrrgh, you're bad at this!", "You may want to try that again!", "You must be one of those slow learners. It's okay, try again!", "I don't think I could generate enough error messages to keep up with you!", "Hmm, did you try numbers", "One, two, three.....I can't hold all thee"]
exceptionListAlpha = ["Opps, you entered a non-numeric character. Try again!", "Remember to use a numeric character, otherwise you're hurting me!", "Errrrrrrrrrror, can you read?!", "Go on, try again!", "I'm running out of errors... try again!", "In case you didn't go to school, there exists such a thing called numbers... try again"]

# Sets up game properties for initial play through and replay
def gameProperties():
    global difficultyInput, wordList, password, guessesRemaining, Won, guessHistory
    difficultyPromptCheck()
    # userDifficulty = int(input("Select Difficulty"))
    if difficultyInput == 0:
        wordList = random.sample(candidateWords, 6)
        guessesRemaining = 6

    elif difficultyInput == 1:
        wordList = random.sample(candidateWords, 8)
        guessesRemaining = 4

    else:
        if difficultyInput == 2:
            wordList = random.sample(candidateWords, 10)
            guessesRemaining = 4

    password = random.choice(wordList)
    Won = False
    guessHistory = []
    return difficultyInput, wordList, password, guessesRemaining, Won, guessHistory


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
    if difficultyInput == 1:
        validRange = [0, 1, 2, 3, 4, 5, 6, 7, 8]
    elif difficultyInput == 0:
        validRange = [0, 1, 2, 3, 4, 5, 6]
    else:
        validRange = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    try:
        global userInput
        userInput = int(input("Enter your guess: "))-1
    except:
        print(random.choice(exceptionListAlpha))
        userInputCheck()
    else:
        if userInput in validRange and userInput not in guessHistory:
            return guessHistory.append(userInput)
        else:
            if userInput in guessHistory:
                print("Already selected this word")
                userInputCheck()
            elif userInput not in validRange:
                print(random.choice(exceptionListNum))
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
        print(random.choice(exceptionListAlpha))
        replayPromptCheck()
    else:
        if replayInput in validRange:
            return replayInput
        else:
            print(random.choice(exceptionListNum))
            replayPromptCheck()

def difficultyPromptCheck():
    validRange = [0, 1, 2]
    try:
        global difficultyInput
        difficultyInput = int(input("\nBefore we start, select your desired difficulty!\nEasy: 1\nMedium: 2\nHard: 3\n"))-1
    except:
        print(random.choice(exceptionListAlpha))
        difficultyPromptCheck()
    else:
        if difficultyInput in validRange:
            return difficultyInput
        else:
            print(random.choice(exceptionListNum))
            difficultyPromptCheck()

# Initial welcome for players and replay
def welcome():
    print("Welcome to Guess-The-Word-Game.\nPassword is one of these words:\n")


# Game domain where everything is initilised
def gameStart():
    replay = True
    while replay == True:
        global guessesRemaining
        gameProperties()
        welcome()
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

