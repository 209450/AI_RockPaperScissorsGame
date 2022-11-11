import unittest

from AI.RockPaperScissorsClassifier import RockPaperScissorsClassifier


class TestRockPaperScissorsClassifier(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        cls.classifier = RockPaperScissorsClassifier()
        cls.classifier.load_model("rps.h5")

    def test_should_be_rock(self):
        img = self.classifier.load_image("photo examples/rock.jpg")
        self.assertEqual(self.classifier.predict(img), "rock")

    def test_should_be_paper(self):
        img = self.classifier.load_image("photo examples/paper.jpg")
        self.assertEqual(self.classifier.predict(img), "paper")

    def test_should_be_scissors(self):
        img = self.classifier.load_image("photo examples/scissors.jpg")
        self.assertEqual(self.classifier.predict(img), "scissors")


if __name__ == '__main__':
    unittest.main()


