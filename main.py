#Ex_1
first_name = "Menachem" 
last_name = "Levi"
age = 26
city = "Beit Shemesh"
email = "Men@gamil.com"
print(f"""
===== User Details =====
First Name: {first_name}
Last Name: {last_name}
Age: {age}
City: {city}
Email: {email}
========================

""")
#ex_2
birth_year = 2000
current_year = 2026
my_age = current_year - birth_year
print(f"You are approximately {my_age} years old.")

#ex_3
width = 8
height = 3
area = width * height
scope = width * 2 + height * 2
print(f"In a rectangle whose length is {height} and whose width is {width}, its area is {area} and its perimeter is {scope}.")

#ex_4
name = "David"
age = 25
height = 1.78
is_student = True
salary = 8500
print(
    type(name),
    type(age),
    type(height),
    type(is_student),
    type(salary)
)

#ex_5
first_name = input("Enter your first name: ").title()
last_name = input("Enter your last name: ").title()
city = input("Enter yiur city: ").title()
age = int(input("Enter your age: "))
print(f'Hello {first_name} {last_name} from {city}, he is {age} yers old')

#ex_6
num_1 = int(input("Enter a number: "))
num_2 = int(input("Enter a number: "))
print(f"""
The result of the addition: {num_1} + {num_2}
The result of the subtraction: {num_1} - {num_2}
The result of the multiplication: {num_1} * {num_2}
The result of the division: {num_1} / {num_2}
""")

#x_7
name = input("Enter the product name: ").title()
price = int(input("Enter the price: "))
quantity = int(input("Enter the quantity of product: "))
total = quantity * price
print(f"""
====== Purchase Receipt ======
Product: {name}
Price: {price}
Quantity: {quantity}
Total: {total}
==============================

""")

#ex_9
name = input("Enter employ name: ").title()
hours = int(input("Enter amount hours in month: "))
salary_per_hour = int(input("Enter salary: "))
print(f'''
employ: {name}
salary: {salary}
for {hours} hours working
''')

#ex_10
price = float(input("Enter the price: "))
tip = price * 0.15
num_of_pepule = int(input("Enter nom of diners: "))
total_price = price * 1 + tip
print(f'Tip: {tip}, total price: {total_price}, for any diner:{total_price / num_of_pepule}.')

#ex_12
a = 10
b = 20
# a, b = b, a
temp = a
a = b
b = temp
print(a,b)

#ex_D
student_first_name = input("Enter student name: ")
student_last_name = input("Enter student name: ")
studemt_age = int(input("Enter the student age "))
mossad_name = input("Enter the mossad name: ")
course = ("Enter the course name: ")
months_lorren = int(input("Enter months of Study: "))
months_cast = float(input("Enter the cast per months: "))
total = months_cast * months_lorren
print(f"""
================================
       STUDENT REGISTRATION
================================

Student: {student_first_name} {student_last_name}
Age: {studemt_age}
Institution: {mossad_name}
Course: {course}
Duration: {months_lorren} Months
Monthly Price: {months_cast}

Total Course Price: {total}

================================
Registration completed!
================================

""")
