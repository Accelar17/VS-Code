def swap_halves(arr):
    length = len(arr)
    midpoint = length // 2

    
    arr[midpoint:], arr[:midpoint] = arr[:midpoint], arr[midpoint:]

    return arr


array1 = [1, 2, 5, 6, 7, 8]
array2 = [6, 7, 8, 9, 1, 2]

print("Перший масив після обміну половин:", swap_halves(array1))
print("Другий масив після обміну половин:", swap_halves(array2))
