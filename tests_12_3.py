import unittest
from unittest import runner




class RunnerTest(unittest.TestCase):
    is_frozen = False



class TournamentTest(unittest.TestCase):
    is_frozen = True




class RunnerTest(unittest.TestCase):
    is_frozen = False

    @unittest.skipIf(is_frozen, "Тесты в этом кейсе заморожены'")
    def test_challenge(self):
        pass

    def test_run(self):
        pass

    def test_walk(self):
        pass


# ...

# ...

class TournamentTest(unittest.TestCase):
    is_frozen = True

    @unittest.skipIf(is_frozen, "Тесты в этом кейсе заморожены'")
    def test_first_tournament(self):
        pass

    @unittest.skipIf(is_frozen, "Тесты в этом кейсе заморожены'")
    def test_second_tournament(self):
        pass

    @unittest.skipIf(is_frozen, "Тесты в этом кейсе заморожены'")
    def test_third_tournament(self):
        pass




if __name__ == "__main__":
    runner.run(test_12_3)

