numbers = [2, -93, -2, 8, None, -44, -1, -85, -14, 90, -22, -90, -100, -8, 38, -92, -45, 67, 53, 25]

# TODO заменить значение пропущенного элемента средним арифметическим
first = (numbers[:4])
second = (numbers[5:])
summ_first = sum(first)
summ_second = sum(second)

middle = (summ_first + summ_second) / len(numbers)
numbers[4] = middle
print("Измененный список:", numbers )
