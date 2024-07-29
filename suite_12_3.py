import unittest
from tests_12_3 import RunnerTest, TournamentTest



suite_12_3 = unittest.TestSuite()
suite_12_3.addTests(unittest.TestLoader().loadTestsFromTestCase(RunnerTest))
suite_12_3.addTests(unittest.TestLoader().loadTestsFromTestCase(TournamentTest))
runner = unittest.TextTestRunner(verbosity=2)
runner.run(suite_12_3)

