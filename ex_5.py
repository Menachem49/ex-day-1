numbers = [10, 20, 30, 40, 50]
print(numbers, numbers[1] , numbers[-1], numbers[2])

names = ["Avi", "Meni", "Dan", "Gad"]
print(len(names))
print(numbers[1], numbers[-1])
names[1] = "Gelad"
print(names)

greades = [10, 20, 30, 40, 50]
greades.append(100)
greades.insert(0, 90)
greades[2] = 85
print(greades)

numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
del numbers[1]
del numbers[-1]
del numbers[2]
# print(numbers)

products = ["Apple" "pear", "banana", "milk"]
t = "milk" in products
print(t)
f = "pp" in products
print(f)

numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
for num in numbers:
    print(num)

numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
for num in numbers:
    if num % 2 == 0:
        print(num)

numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
sum = 0
for num in numbers:
    sum += num
print(sum)

numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
max_num = numbers[0]
for num in numbers:
    if num > max_num:
        max_num = num
print(max_num)

names = ["Avi", "Meni", "Dan", "Gad"]
name = input(":")
for n in  names:
    if n == name:
        print("Found")
        break
else:
    print("Not found")


numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
number = int(input(":"))
indexes = [index for index, num in enumerate(numbers) if num == number]
print(indexes)

numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
count = 0
for num in numbers:
    if num > 50:
        count+= 1
print(count)

numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
new_ = [num for num in numbers if num % 2 ==0]
print(new_)


names = ["Avi", "Meni", "Dan", "Gad", "Itay"]
for i, name in enumerate(names, 1):
    print(i, name)

numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
print(numbers[:3])
print(numbers[-3])
print(numbers[2:6])

names = ["Noa", "Ori", "Maya", "Itay", "Tamar", "Daniel", "Yael", "Omer", "Shira", "Yonatan"]
print(names[::2])
print(names[1::2])
print(names[::-2])

numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20]
new_1 = numbers[10]
new_1 = numbers[:10]
new_1 = numbers[5: 14]

numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20]
new_1 = numbers[len(numbers) / 2]
new_1 = numbers[:len(numbers) / 2]

numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
new_1 = [num * 2 for num in numbers]
new_2 = [num ** 2 for num in numbers]
new_3 = [num for num in numbers if num % 2 == 0]
new_4 = [num for num in numbers if num > 5]

grades = [55, 90, 67, 100, 45, 82, 73, 30]
new_1 = [graed for graed in grades if graed >= 60]
new_2 = [graed for graed in grades if graed < 60]
new_3 = [graed + 5 for graed in grades]

names = ["Moshe", "David", "Dana", "Noa", "Michael", "Avi"]
new_1 = [name for name in names if len(name) > 4]
new_2 = [name.upper() for name in names]
new_3 = [name for name in names if name.startswith("D")]

numbers = [12, 7, 25, 30, 9, 44, 18, 3]
new_1 = [num for num in numbers if num % 3 == 0 and num > 10]

numbers = [int(input(":")) for _ in range(10)]
sum_ = 0
big = numbers[0]
min_ = numbers[0]
for num in numbers:
    sum_ += num
    if num > big: big= num
    if num < min_: min_ = num
print(min_, big, sum_)

names = ["Avi", "Meni", "Dan", "Gad", "Itay"]
name = input()
for name_ in names:
    if name == name_:
        del names[names.index(name)]
        break
else:
    print("Name not found")

numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
new_1 = [num for num in numbers if num % 2 == 0]
new_1 = [num for num in numbers if num % 2 != 0]
new_1 = [num for num in numbers if num > 20]

numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
num = int(input())
index = []
for i, num_ in enumerate(numbers):
    if num == num_:
        index.append(i)
if not index:
    print ("Number not found")
else:
    print(index, len(index))


numbers_1 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
numbers_2 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
numbers_1 += numbers_2
print(numbers_1)
print(numbers_1[:5])
print(numbers_1[-5:])
print(numbers_1[::-1])

numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
num = int(input())
for n in numbers:
    if num == n:
        print("number elredy exsist")
        break
else:
    numbers.append(num)
print(numbers)


grades = [85, 72, 90, 55, 100, 63, 48, 77]
while True:
    print("""
===== Grades Management =====

1. Show all grades
2. Add a grade
3. Search for a grade
4. Remove a grade
5. Show passing grades
6. Show failing grades
7. Show highest and lowest grade
8. Show average grade
9. Show first 3 grades
10. Show grades in reverse
0. Exit
""")
    choose = int(input())
    if choose  == 1:
        print(grades)
    elif choose == 2:
        grade = float(input())
        grades.append(grade)
    elif choose == 3:
        grade = float(input())
        index = []
        for i, gr in enumerate(grades):
            if grade == gr:
                index.append(i)
        print(index, len(index))
    elif choose == 4:
        grade = float(input())
        for i, gr in enumerate(grades):
            if grade == gr:
                del grades[i]
                print("delete")
                break
        else:print("not found")
    elif choose == 5:
        print([g for g in grades if g >= 60])
    elif choose == 6:
        print([g for g in grades if g < 60])
    elif choose == 7:
        max_ = grades[0]
        min_ = grades[0]
        for g in grades:
            if g > max_: max_ = g
            elif g < min_: min_ = g
        print(max_, min_)
    elif choose == 8:
        sum = 0
        for g in grades:
            sum += g
        print(sum / len(grades))
    elif choose == 9:
        print(grades[:3])
    elif choose == 10:
        print(grades[::-1])
    elif choose == 11:
        break
    else:
        continue

        