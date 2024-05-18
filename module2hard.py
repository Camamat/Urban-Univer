import random

n = [3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20]
number = random.choice(n)
print('Ваше число ', number)
list_ = []
for i in range(1, 21):
    for j in range((i + 1), 21):
            if number % (i + j) == 0:
                list_.extend([str(i) + str(j)])
            else:
                continue
print(list_)










