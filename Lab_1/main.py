print("СТРОКИ")

print("Задание №1")
str1 = "Цель работы: познакомиться с основными"
print("м" in str1)

print()

print("Задание №2")
str1 = "Цель работы: познакомиться с основными"
print(len(str1))

print()

print("Задание №3")
str1 = "Цель работы: познакомиться с основными"
print(str1.count("о"))

print("\nСПИСКИ")

print("Задание №1")
my_list = [1,2,3,4,5,6]
print(len(my_list))

print()

print("Задание №2")
my_list = [1,2,3,4,5,6]
my_list.append(2)
print(*my_list)

print()

print("Задание №3")
my_list = [1,2,3]
my_list.insert(0,12)
print(*my_list)

print()

print("Задание №4")
my_list = [1,2,3,10]
my_list.insert(1,12)
print(*my_list)



print("\nКортежи")

print("Задание №1")
my_tuple = (1,2,5,6)
print(len(my_tuple))

print()

print("Задание №4")
my_tuple = (1,2,5,6)
temp = (12,)
my_tuple = my_tuple[0:1] + temp + my_tuple[1:]
print(my_tuple)

print()

print("Задание №5")
my_tuple = (1,2,3,10)
my_tuple = my_tuple[0:2] + my_tuple[3:]
print(my_tuple)

print()

print("Задание №15")
my_tuple = (1,2,3,4,5,6,2,1,2,'a','b',2,5)
new_tuple = tuple()
new_tuple = (my_tuple[0], my_tuple[int((len(my_tuple))/2)],my_tuple[-1])

print(new_tuple)
