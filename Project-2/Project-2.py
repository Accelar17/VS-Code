
print("Перші 10 натуральних чисел (while):")
n = 1
while n <= 10:
    print(n, end=" ")
    n += 1
print()


print("Перші 10 натуральних чисел (for):")
for i in range(1, 11):
    print(i, end=" ")
print()


num = int(input("Введіть число: "))
sum_of_numbers = sum(range(1, num + 1))
print("Сума чисел від 1 до", num, ":", sum_of_numbers)


numbers_list = [3, 7, 12, 15, 21]
print("Числа зі списку:")
for number in numbers_list:
    print(number, end=" ")
print()


num = int(input("Введіть число для обчислення факторіала: "))
factorial = 1
for i in range(1, num + 1):
    factorial *= i
print("Факторіал числа", num, ":", factorial)


decimal_number = int(input("Введіть десяткове число: "))
binary_number = bin(decimal_number)
print("Двійкове представлення числа", decimal_number, ":", binary_number)
