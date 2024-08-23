import Test
import unittest

class RunnerTest(unittest.TestCase):

    def test_walk(self):
        a = Test.Runner('Azat')
        for i in range(10):
            a.walk()
        self.assertEqual(a.distance, 50)

    def test_run(self):
        b = Test.Runner('Anton')
        for j in range(10):
            b.run()
        self.assertEqual(b.distance, 100)

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