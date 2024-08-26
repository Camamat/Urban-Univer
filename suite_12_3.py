import unittest
import tests_12_3
import module_12_2

TestST = unittest.TestSuite()
TestST.addTest(unittest.TestLoader().loadTestsFromTestCase(Test_Runner.RunnerTest))
TestST.addTest(unittest.TestLoader().loadTestsFromTestCase(module_12_2.TournamentTest))

runner = unittest.TextTestRunner(verbosity=2)
runner.run(TestST)