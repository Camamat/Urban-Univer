grades = [[5, 3, 3, 5, 4], [2, 2, 2, 3], [4, 5, 5, 2], [4, 4, 3], [5, 5, 5, 4, 5]]
students = {'Johnny', 'Bilbo', 'Steve', 'Khendrik', 'Aaron'}
students = tuple(students)
number_of_lists = len(grades)# равно 5
dictionary = {}
n = 0
for x in grades[n]:
    x = sum(grades[n]) / len(grades[n])
    dictionary[students[n]] = x
    n = n + 1
    if n == number_of_lists + 1:
        break
print(dictionary)