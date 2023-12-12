numbers = [2, -93, -2, 8, None, -44, -1, -85, -14, 90, -22, -90, -100, -8, 38, -92, -45, 67, 53, 25]

# TODO заменить значение пропущенного элемента средним арифметическим
void = numbers.index(None)
first = (numbers[:void])
second = (numbers[void + 1:])
summ_first = sum(first)
summ_second = sum(second)

middle = (summ_first + summ_second) / len(numbers)
numbers[void] = middle
print("Измененный список:", numbers )
