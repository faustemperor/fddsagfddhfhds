import random

list1 = [random.randint(1, 100) for _ in range(10)]
list2 = [random.randint(1, 100) for _ in range(10)]
print("Список 1:", list1)
print("Список 2:", list2)
combined_list = list1 + list2
unique_combined_list = list(set(combined_list))
common_elements_list = list(set(list1) & set(list2))
unique_list1 = list(set(list1))
unique_list2 = list(set(list2))
min_max_list1 = [min(list1), max(list1)]
min_max_list2 = [min(list2), max(list2)]
print("Элементы обоих списков:", combined_list)
print("Элементы без повторений:", unique_combined_list)
print("Общие элементы:", common_elements_list)
print("Уникальные элементы списка 1:", unique_list1)
print("Уникальные элементы списка 2:", unique_list2)
print("Минимальное и максимальное значение списка 1:", min_max_list1)
print("Минимальное и максимальное значение списка 2:", min_max_list2)