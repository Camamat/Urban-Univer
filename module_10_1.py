from threading import Thread
import time
from datetime import datetime
from time import sleep

def wite_words(word_count, file_name):
    with open(f'{file_name}', 'w', encoding='utf8') as f:
        for i in range(1, word_count + 1):
            f.write(f'Какое-то слово №{i}' + '\n')
            time.sleep(0.1)
    print(f'Завершилась запись в файл {file_name}')

time_start = datetime.now()

wite_words(10, 'example1.txt')
wite_words(30, 'example2.txt')
wite_words(200, 'example3.txt')
wite_words(100, 'example4.txt')

time_end = datetime.now()
time_res = time_end - time_start
print(time_res)

time_start = datetime.now()

thr_first = Thread(target=wite_words, args=(10, 'example5.txt'))
thr_second = Thread(target=wite_words, args=(30, 'example6.txt'))
thr_third = Thread(target=wite_words, args=(200, 'example7.txt'))
thr_four = Thread(target=wite_words, args=(100, 'example8.txt'))

thr_first.start()
thr_second.start()
thr_third.start()
thr_four.start()

thr_first.join()
thr_second.join()
thr_third.join()
thr_four.join()

time_end = datetime.now()
time_res = time_end - time_start
print(time_res)