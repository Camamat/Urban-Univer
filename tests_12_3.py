import Test
import unittest

class RunnerTest(unittest.TestCase):

    is_frozen = False

    @unittest.skipIf(is_frozen == True, 'Тесты в этом кейсе заморожены')
    def test_walk(self):
        a = Test.Runner('Azat')
        for i in range(10):
            a.walk()
        self.assertEqual(a.distance, 50)

    @unittest.skipIf(is_frozen == True, 'Тесты в этом кейсе заморожены')
    def test_run(self):
        b = Test.Runner('Anton')
        for j in range(10):
            b.run()
        self.assertEqual(b.distance, 100)

    @unittest.skipIf(is_frozen == True, 'Тесты в этом кейсе заморожены')
    def test_challenge(self):
        c = Test.Runner('Almaz')
        d = Test.Runner('Andrey')
        for i in range(10):
            c.walk()
        for j in range(10):
            d.run()
        self.assertNotEqual(c.distance, d.distance)

if __name__ == '__main__':
    unittest.main

#    -_______________________________________________________________________________________________________-

import module_12
import unittest
import pprint

class TournamentTest(unittest.TestCase):

    is_frozen = True

    @classmethod
    def setUpClass(self):
        self.all_results = []

    def setUp(self):
        self.runner_1 = module_12.Runner('Усэйн', 10)
        self.runner_2 = module_12.Runner('Андрей', 9)
        self.runner_3 = module_12.Runner('Ник', 3)

    @unittest.skipIf(is_frozen == True, 'Тесты в этом кейсе заморожены')
    def test_turn1(self):
        turn_1 = module_12.Tournament(90, self.runner_1, self.runner_3)
        result = turn_1.start()
        self.assertTrue(result[max(result.keys())] == 'Ник')
        self.all_results.append(result)

    @unittest.skipIf(is_frozen == True, 'Тесты в этом кейсе заморожены')
    def test_turn2(self):
        turn_2 = module_12.Tournament(90, self.runner_2, self.runner_3)
        result = turn_2.start()
        self.assertTrue(result[max(result.keys())] == 'Ник')
        self.all_results.append(result)

    @unittest.skipIf(is_frozen == True, 'Тесты в этом кейсе заморожены')
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
