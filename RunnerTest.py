import logging

import tests_12_4
import unittest


class RunnerTest(unittest.TestCase):
    logging.basicConfig(level=logging.INFO, filemode='w', filename='runner_tests.log', encoding='UTF-8',
                        format='%(asctime)s | %(levelname)s | %(message)s')

    def test_walk(self):

        try:
            a = tests_12_4.Runner('Azat', -6)
            for i in range(10):
                a.walk()
            self.assertEqual(a.distance, 50)
            logging.info('"test_walk" выполнен успешно')
        except:
            logging.warning('Неверная скорость для Runner', exc_info=True)

    def test_run(self):

        try:
            b = tests_12_4.Runner(video)
            for j in range(10):
                b.run()
            self.assertEqual(b.distance, 100)
            logging.info('"test_run" выполнен успешно')
        except:
            logging.warning('Неверный тип данных для объекта Runner', exc_info=True)

    def test_challenge(self):
        c = tests_12_4.Runner('Almaz')
        d = tests_12_4.Runner('Andrey')
        for i in range(10):
            c.walk()
        for j in range(10):
            d.run()
        self.assertNotEqual(c.distance, d.distance)


if __name__ == '__main__':
    unittest.main

    # first = Runner('Вося', -5)
    # second = Runner('Илья', 5)
    # third = Runner('Арсен', 10)
    #
    # t = Tournament(101, first, second)
    # print(t.start())
