import random
import unittest
from Main import pullData, Game_Manager

__author__ = 'jensinamart'
class TestPullData(unittest.TestCase):


    def test_stars(self):
        pd = pullData()
        # randomWords = "blueberry homewards zero banana gravel hairless avenging highway circuitry agency".split()
        # word = randomWords[random.randint(0,9)]
        fileOpen = open("tryFile.txt", "r")
        foString = fileOpen.read().split()
        word = foString[random.randint(0,9)]
        wordCount = len(word)
        starCounter = 0
        starWord = ""
        while wordCount > starCounter: ##Determines the number of letters in the word and makes an * version
            starWord += "*"
            starCounter += 1
        self.assertEqual(pd.makeStars(word), starWord)


    def test_readFile(self):
        pd = pullData()
        array = []
        with open("tryFile.txt", "r") as file:
            for line in file:
                array.append(line.strip())
        self.assertEqual(len(array), len(pd.readFile()))
        for fl in pd.readFile():
            self.assertNotIn('',fl)


class TestGame(unittest.TestCase):
    def test_create(self):
        gm = Game_Manager()
        self.assertIsNotNone(gm)

    def testCheck(self):
         gmtrue = Game_Manager().checkWord("testword","testword")
         gmfalse = Game_Manager().checkWord("testword", "wrongword")
         self.assertTrue(gmtrue)
         self.assertFalse(gmfalse)