import unittest
import moreOrLess


class TestClientServerMoreLess(unittest.TestCase):

    def setUp(self):
        self.more = moreOrLess

    def testyourChoice(self):
        text3, choice3 = self.more.yourChoice(0.2)
        text1, choice1 = self.more.yourChoice(1)
        text9, choice9 = self.more.yourChoice(9)
        textn, choicen = self.more.yourChoice('n')
        assert choice1 == 1 and choice3 == 0.2, "function yourChoice failed"
        assert int(choice9) == 100, "function yourChoice failed"
        assert choicen == 100, "function yourChoice failed"


    def testserverChoice(self):
        choice, text = self.more.serverChoice()
        assert choice >= -1 and choice <= 1, "serverChoice failed, wrong choice"

if __name__ == "__main__":
    unittest.main()