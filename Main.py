__author__ = 'jensinamart'
__author__ = 'Jen Mart'

import random
import unittest


class Game_Manager:

    # randomWords = "blueberry homewards zero banana gravel hairless avenging highway circuitry agency".split()
    # word = randomWords[random.randint(0,9)]
    #RandomWords consists of the same words in the tryFile.txt
    #I left this bit of code incase of troubles using the file attachment

    def __init__(self):
        self.pullData = pullData()

    def HangMan(self):
        word = self.pullData.readFile()
        print word
        winState = self.pullData.makeStars(word)

        turns = 0
        wrongLetters = ""
        rightLetters = ""
        hangManWord = "H A N G M A N ".split()
        failState = ""
        wordCount = len(word)
        starCounter = 0
        while turns != 7:
            print failState
            print winState
            print "Guess a letter"
            playerInput = raw_input()
            if len(playerInput) != 1: #Confirms only a single character has been used.
                print("please enter only a single character")
            else:
                playerInput.lower() #lowers the case of the character to avoid confusion
                counterThing = 0
                #If player enters a character already used, the system informs them.
                checkRight = self.checkWord(playerInput, rightLetters)
                checkLeft = self.checkWord(playerInput, wrongLetters)

                if (checkRight) or (checkLeft):
                    print "You've already guessed that"
                    print "\n"
                else:
                    wrdChk = self.checkWord(playerInput, word)
                    if (wrdChk):
                        print "correct!"
                        print "\n"
                        rightLetters += playerInput
                        currentLetter = playerInput
                        #If a player guesses correctly, the system adds the correct letter
                        # were it's corresponding astrisk is located
                        while wordCount != counterThing:
                            if currentLetter in word[counterThing]:
                                winState = winState[:counterThing] + currentLetter + winState[counterThing + 1:]
                                counterThing += 1
                            else:
                                counterThing += 1
                    else:
                        print "incorrect!"
                        print "\n"
                        wrongLetters += playerInput + " "
                        failState += hangManWord[turns]
                        turns += 1
                    if turns == 7:
                        print failState
                        print "you lose! The answer was " + word
                        break
                    if winState == word:
                        print "you win! The answer was " + winState
                        break
                if len(wrongLetters) > 0:
                    print "Incorrect letters used: " +  wrongLetters


    def checkWord(self, input, peram):
        if input in peram:
            return True
        else:
            return False



class pullData:


    def readFile(self):
        # randomWords = "blueberry homewards zero banana gravel hairless avenging highway circuitry agency".split()
        # word = randomWords[random.randint(0,9)]
        fileOpen = open("tryFile.txt", "r")
        foString = fileOpen.read().split()
        word = foString[random.randint(0,9)]
        return word

    def makeStars(self, word):
        wordCount = len(word)
        starCounter = 0
        starWord = ""
        while wordCount > starCounter: ##Determines the number of letters in the word and makes an * version
            starWord += "*"
            starCounter += 1
        return starWord

def startGame():
    h = Game_Manager()
    h.HangMan()

startGame()





