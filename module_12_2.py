import module_12
import unittest
import pprint

class TournamentTest(unittest.TestCase):
    @classmethod
    def setUpClass(self):
        self.all_results = []

    def setUp(self):
        self.runner_1 = module_12.Runner('Усэйн', 10)
        self.runner_2 = module_12.Runner('Андрей', 9)
        self.runner_3 = module_12.Runner('Ник', 3)


    def test_turn1(self):
        turn_1 = module_12.Tournament(90, self.runner_1, self.runner_3)
        result = turn_1.start()
        self.assertTrue(result[max(result.keys())] == 'Ник')
        self.all_results.append(result)


    def test_turn2(self):
        turn_2 = module_12.Tournament(90, self.runner_2, self.runner_3)
        result = turn_2.start()
        self.assertTrue(result[max(result.keys())] == 'Ник')
        self.all_results.append(result)

    def test_turn3(self):
        turn_3 = module_12.Tournament(90, self.runner_1, self.runner_2, self.runner_3)
        result = turn_3.start()
        self.assertTrue(result[max(result.keys())] == 'Ник')
        self.all_results.append(result)

    @classmethod
    def tearDownClass(cls):
        for result in cls.all_results:
            print(result)

if __name__ == '__main__':
    unittest.main
