def is_prime(func):
    def wrapper(a, b, c):
        result = func(a, b, c)
        lis = []
        for i in range(1, result + 1):
            j = result / i
            if j.is_integer():
                lis.append(j)
        if len(lis) == 2:
            return 'Простое'
        else:
            return 'Составное'

    return wrapper


@is_prime
def sum_three(a, b, c):
    print(a + b + c)
    return a + b + c

result = sum_three(2, 3, 6)
print(result)