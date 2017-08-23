import unittest
from GuessValidator import isValidGuess
from GuessValidator import adj

class GuessValidator_Test(unittest.TestCase):

    def setUp(self):
        self.boggle = [['I','L','A','W'],['B','N','G','E'],['I','U','A','O'],['A','S','R','L']]
        self.row = len(self.boggle)
        self.col = len(self.boggle)
        self.verbose = False

    def test_adj(self):
        #Is neighbours of element [0,0] determined correctly in a 4x4 2D array (initialized into the setUp method)?
        self.assertItemsEqual(adj(0,0,self.row,self.col), [[0,1],[1,0],[1,1]])
        # Is neighbours of element [3,1] determined correctly in a 4x4 2D array (initialized into the setUp method)?
        self.assertItemsEqual(adj(3,1,self.row,self.col), [[2,0],[2,1],[2,2],[3,2],[3,0]])
        # Is neighbours of element [1,1] determined correctly in a 4x4 2D array (initialized into the setUp method)?
        self.assertItemsEqual(adj(1,1,self.row,self.col), [[0,0],[1,0],[2,0],[0,1],[0,2],[1,2],[2,1],[2,2]])
        # Is neighbours of element [1,2] determined correctly in a 4x4 2D array (initialized into the setUp method)?
        self.assertItemsEqual(adj(1,2,self.row,self.col), [[0,1],[0,2],[1,1],[2,1],[2,2],[0,3],[1,3],[2,3]])

    def test_isValidGuess(self):
        #Is given texts validated correctly according to initialized boggle array?
        self.assertTrue(isValidGuess(self.boggle, "BINGO", self.verbose))
        self.assertTrue(isValidGuess(self.boggle, "LINGO", self.verbose))
        self.assertTrue(isValidGuess(self.boggle, "ILNBIA", self.verbose))
        self.assertFalse(isValidGuess(self.boggle, "BUNGIE", self.verbose))
        self.assertFalse(isValidGuess(self.boggle, "BINS", self.verbose))
        self.assertFalse(isValidGuess(self.boggle, "SINUS", self.verbose))

    if __name__ == '__main__':
        unittest.main()