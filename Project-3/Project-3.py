import math

def circle_area(radius):
    return math.pi * radius**2

def calculate_expression(n):
    nn = int(str(n) * 2)
    nnn = int(str(n) * 3)
    return n + nn + nnn

def sum_of_list(lst):
    return sum(lst)

def multiply_elements(lst):
    result = 1
    for num in lst:
        result *= num
    return result

def find_minimum(lst):
    return min(lst)




radius = float(input("Введіть радіус кола: "))
print("Площа кола з радіусом", radius, ":", circle_area(radius))


n = int(input("Введіть ціле число n: "))
print("Результат обчислення виразу:", calculate_expression(n))


numbers = [1, 2, 3, 4, 5]
print("Сума всіх елементів у списку:", sum_of_list(numbers))


print("Добуток всіх елементів у списку:", multiply_elements(numbers))


print("Найменше число у списку:", find_minimum(numbers))
