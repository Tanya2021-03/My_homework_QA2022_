#Зформуйте строку, яка містить певну інформацію про символ в відомому слові. Наприклад "The [номер символу] symbol in [тут слово] is '[символ з відповідним порядковим номером]'". Слово та номер отримайте за допомогою input() або скористайтеся константою. Наприклад (слово - "Python" а номер символу 3) - "The 3 symbol in "Python" is 't' ".

my_list = input()
print("Задание № 1:")
print(f"The 3 symbol in {my_list} is - '{my_list[2]}'")


#Вести з консолі строку зі слів (або скористайтеся константою). Напишіть код, який визначить кількість слів, в цих даних.
my_list = input()
result = len(my_list.split())
print("Задание № 2:")
print(f"The sentence has {str(result)} words.")


#Існує ліст з різними даними, наприклад lst1 = ['1', '2', 3, True, 'False', 5, '6', 7, 8, 'Python', 9, 0, 'Lorem Ipsum']. Напишіть механізм, який сформує новий list (наприклад lst2), який би містив всі числові змінні, які є в lst1. Майте на увазі, що данні в lst1 не є статичними можуть змінюватись від запуску до запуску.
my_list1 = input()
my_list2 = my_list1
print("Задание № 3:")
print(my_list2)
