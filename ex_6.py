numbers = (10, 20, 30, 40, 50)
print(numbers[0], numbers[-1])
print(len(numbers))
print(numbers[2])

names = ("Avi", "Meni", "Dan", "Gad", "Itay")
for name in names:
    print (name)
print("Avi" in names)
print(len(names))

numbers = (10, 20, 30, 40, 50)
print(numbers[:3])
print(numbers[::-1])

product = ("apple", 2.9, 550, "food")
print(product[0])
print(product[1])
print(product[2])
print(product[3])

numbers = (10, 20, 30, 40, 50)
sum_ = 0
max_ = numbers[0]
count_event = 0
for num in numbers:
    sum_ += num
    if num > max_: max_ =num
    if num % 2 == 0: count_event += 1
print (sum_, max_, count_event)

products = ("Laptop", "Mouse", "Keyboard", "Screen", "Printer")
new_1 = products[:3]
new_2 = products[-2:]
new_1 += new_2
print(new_1)

student = {    "name": "David",    "age": 22,    "grade": 95}
print(student["name"])
student["age"] = 23
student["city"] = "Tel Aviv"
print(student)

student = {"name": "David", "age": 22, "grade": 95, "city": "Tel Aviv"}
print(student["name"])
print(student["age"])
print(student["grade"])
print(student["city"])

car = {"brand": "Toyota", "model": "Cmery", "year": 2018, "price": 70000}
car["price"] = 68000
car["year"] = 2019
car["color"] = "White"
print(car)

salaries = {    "David": 12000,    "Moshe": 15000,    "Dana": 13500}
for key , value in salaries.items():
    print(f"{key}: {value}")
salaries["Moshe"] += 15000
salaries["Avi"] = 35000
print(salaries)

products = {"apple": 2.9, "milk":6.9, "banana":1.9}
product = input()
print(products.get(product,"product not foud"))

grades = {    "David": 90,    "Moshe": 75,    "Dana": 100,    "Noa": 55,    "Avi": 82}
for name, grade in grades.items():
    print(f"Student: {name} | Grade: {grade}")

grades = {    "David": 90,    "Moshe": 75,    "Dana": 100,    "Noa": 55,    "Avi": 82}
print ({k : v for k, v in grades.items() if v > 80 })
sum_ = 0
for grade in grades.values():
    sum_ += grade
print(sum_ / len(grades))
g = 0
name_ = ""
for name, grade in grades.items():
    if grade > g: 
        g = grade
        name_ = name
print(name_)
count = 0
print([count:=count +1 for grade in grades.values() if grade < 60][0])

products = {"apple": 2.9, "milk":6.9, "banana":1.9}
product = input()
price = float(input())
products[product] = price
print(products)

students = [    {"name": "David", "age": 20, "grade": 90},    {"name": "Moshe", "age": 22, "grade": 75},    {"name": "Dana", "age": 21, "grade": 100},    {"name": "Noa", "age": 19, "grade": 55},    {"name": "Avi", "age": 23, "grade": 82}]
big = 0
name = ''
for student in students:
    print(student["name"])
    print(student["grade"])
    print(student["name"] if student["grade"] >= 80 else '',end='\n' if student["grade"] >= 80 else '' )
    if student["grade"] > big:
        big = student["grade"]
        name = student["name"]

students.append({"name": "Meni", "age": 26, "grade": 100})
students[0]["grade"] = 10
index = None
name_ = input()
for i , item in enumerate(students):
    if item["name"]  == name_:
        index = i
students.pop(index)
print(students)

classroom = {    "Class A": ["David", "Moshe", "Dana"],    "Class B": ["Noa", "Avi", "Michael"],    "Class C": ["Daniel", "Shir", "Yossi"]}
for class_ in classroom:
    print(class_)
print(classroom["Class A"])
classroom["Class B"].append("Meni")
classroom["Class C"].remove("Shir")
print(len(classroom["Class A"]), len(classroom["Class B"]), len(classroom["Class C"]))

products = {    "Laptop": {        "price": 4500,        "stock": 10    },    "Mouse": {        "price": 80,        "stock": 50    },    "Keyboard": {        "price": 150,        "stock": 20    }}
for pro in products:
    print(pro,products[pro]["price"])
    print(pro,products[pro]["stock"])
    if products[pro]["price"] > 100:
        print(pro)
products["Laptop"]["stock"] = 20
products["Tv"] = {"price": 1950, "stock": 52}

employees = [    ("David", "Development", 15000),    ("Moshe", "Marketing", 12000),    ("Dana", "Development", 18000),    ("Noa", "HR", 11000)]

print(*[emp[0] for emp in employees])
print(*[emp[0] for emp in employees if emp[1] == "Development"])
print(max(employees, key=lambda emp : emp[2]))
print(sum([emp[-1] for emp in employees]) / len(employees))

inventory = {    "Laptop": 10,    "Mouse": 50,    "Keyboard": 20}
name = input()

if inventory.get(name):
    amount = int(input())
    if amount < inventory[name]:
        inventory[name] -= amount 
        print(inventory[name])
    else: print("@#!@@#")
else: print("Not found")

votes = {    "David": 0,    "Moshe": 0,    "Dana": 0}
name = input()
while name != "stop":
    votes[name] += 1
    name = input()
print (votes)
print(max(votes))

contacts = {"Dan Cohen": "050-1234567", "Ronit Levi": "052-7654321", "Yossi Israeli": "054-9876543", "Maya Mizrahi": "053-1122334", "Noa Shapira": "058-4455667", "Omer Katz": "052-9988776", "Tamar Golan": "050-3344556"}
while True:
    choose = int(input("""
1. Add a contact.
2.Search for a contact.
3. Update a phone number.
4. Delete a contact.
5. View all contacts.
6. Exit """))
    if choose == 1:
        name = input()
        num = input()
        contacts[name] = num
    elif choose == 2:
        name = input()
        print(contacts.get(name))
    elif choose == 3:
        name = input()
        num = input()
        contacts[name] = num
    elif choose == 4:
        name = input()
        del contacts[name]
    elif choose == 5:
        print(contacts)
    elif choose == 6:
        break
    else: continue


products = [    {"name": "Laptop", "price": 4500, "stock": 10},    {"name": "Mouse", "price": 80, "stock": 50},    {"name": "Keyboard", "price": 150, "stock": 20},    {"name": "Screen", "price": 900, "stock": 15}]
while True:
    choose = input("""
===== Store Management =====

1. Show all products
2. Add product
3. Search product
4. Update product price
5. Update product stock
6. Sell product
7. Show products by price
8. Show products with low stock
9. Show total inventory value
0. Exit""")
    if choose == "1":
        print(products)
    elif choose == "2":
        products.append({"name": input(), "price": int(input()), "stock": int(input())})
    elif choose == "3":
        name_ = input()
        print([pro for pro in products if pro["name"] == name_][0])
    elif choose == "4":
        name_ = input()
        [pro for pro in products if pro["name"] == name_][0]["price"] = int(input())
    elif choose == "5":
        name_ = input()
        [pro for pro in products if pro["name"] == name_][0]["stock"] = int(input())
    elif choose == "6":
        name_ = input()
        amount = int(input())
        p = [pro for pro in products if pro["name"] == name_][0]
        p["stock"] -= amount if amount < p["stock"] else 0
    elif choose == "7":
        num = int(input())
        print([p for p in products if p["price"] > num][0]) 
    elif choose == "8":
        print([p for p in products if p["stock"] < 10][0]) 
    elif choose == "9":
        print(sum(list(map(lambda p : p["price"] * p["stock"],products))))
    elif choose == "10":
        break
    else: continue    







