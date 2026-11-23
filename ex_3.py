#ex_1
age = int(input("Enter your age: "))
print("Adult" if age >= 18 else "Minor")

num = int(input("Enter a number: "))
print("Positive" if num > 0 else "Negative" if num < 0 else "Zero")

num = int(input("Enter a number: "))
print("Even" if num % 2 == 0 else "Odd")

num_1 = int(input("Enter a number: "))
num_2 = int(input("Enter a number: "))
print(f"the bigger number is: {max(num_1, num_2) if num_2 != num_1 else "same"}")

password = input("Enter password: ")
print("Access Granted" if password == "Python123" else "Access Denied")

num = int(input("Enter a number: "))
print("Between 1 - 10" if num in range(1, 11) else "Between 11 - 50" if num in range(11, 51) else "Between 51 - 100" if num in range(51, 101) else "Out of range")

grade = int(input("Enter a number: "))
print("Excellent" if 90 <= num <= 100 else "Negative" if num < 0 else "Zero")

correct_username = "admin"
correct_password = "123456"
user_name = input("Enter your name: ")
password = input("Enter password: ")
if user_name == correct_username and password == correct_password:
    print("Login Successful")
elif user_name == correct_username and password == correct_password:
    print("Wrong Password")
elif user_name != correct_username:
    print("Unknown User")

age = int(input("Enter your age: "))
product_price = float(input("Enter the product price: "))
fee = {60: 20, 18: 10}
if age > fee.keys()[0]:
    print(product_price * (1 - (fee.values()[0] / 100)))
elif age > fee.keys()[1]:
    print(product_price * (1 - (fee.values()[1] / 100)))
else:
    print(product_price)

num = int(input("Enter a number: "))
if  num % 3 == 0 and num % 5 == 0:
    print("The number is divisible by 5 and by 3.")
elif num % 3 == 0:
    print("The number is divisible by 3.")
elif num % 5 == 0:
    print("The number is divisible by 5.")
else:
    print("The number is not divisible by 5 and by 3.")

age = int(input("Enter your age: "))
whit_an_adult = bool(int(input("Accompanied by an adult(1 or 0): ")))
if age>= 18 or whit_an_adult:
    print("success to enter")
else:
    print("not ssucces")

avg_grade = float(input(":"))
monthly_income = int(input(":"))
if avg_grade > 90 or avg_grade > 85 and monthly_income < 5000:
    print("")
else:
    print("")

user_name = input("Enter your name: ")
password = input("Enter password: ")
is_acount_active = bool(int(input("1 or 0")))
correct_username = "admin"
correct_password = "123456"
if user_name == correct_username and password == correct_password and is_acount_active:
    print("")
else:
    print("")


num = int(input(":"))
if 20 <= num <= 80:
    print("")
else:
    print("")

if not(num < 20) and not(num > 80):
    print("")
else:
    print("")

balance = 5000
amount_for_withdrawal = int(input(":"))
if amount_for_withdrawal > 0:
    if amount_for_withdrawal > balance:
        print("")
    else:
        print("")
else:
    print("")

customer_age = int(input(":"))
monthly_income = int(input(""))
seniority_at_the_Workplace = int(input(""))

if customer_age >= 21 and monthly_income  >= 7000 and seniority_at_the_Workplace > 1 :
    print("")
else:
    print("")

veacles = {"motorcycle": 10, "car": 20, "commercial": 30}
veacle = input("Enter vehicle type (motorcycle / car / commercial): ")
hours = float(input("Enter parking hours: "))
price = veacles[veacle] * hours
if hours <= 1:
    price *= 0.9
elif hours > 5:
    price *= 0.85
print(f"Final price: {price}")

operators = {"+","-","*","/"}
num_1 = int(input(":"))
num_2 = int(input(":"))
operator = input(":")
if operator in operators:
    if operator == "-":
        print (num_1 - num_2)
    if operator == "+":
        print (num_1 + num_2)
    if operator == "*":
        print (num_1 * num_2)
    if operator == "/":
        if num_2 > 0:
            print (num_1 + num_2)
        else:
            print(ZeroDivisionError)
else:
    print("operator not in operators")

year = int(input(":"))
if year % 400 == 0:
    print("!")
elif year % 100 == 0 :
    print("?")
elif year % 4 == 0:
    print("!")
else:
    print("?")

hours = float(input(":"))
if hours <= 182:
    print(hours * 50)
elif hours <= 184:
    print(hours * 50 + hours - 182 * (0.25*50))
else:
    print(hours * 50 + (2 * (0.25*50)) + ((hours - 184) * (0.25*50)))

customers_age = int(input(":"))
purchase_amount = float(input(":"))
is_a_club_member = bool(int(input(":")))
has_been_opened = bool(int(input(":")))
a_purchase_invoice_exists = bool(int(input(":")))
days_over = int(input(":"))

if not a_purchase_invoice_exists:
    print("not invoice")
elif has_been_opened:
    print("opend")
elif purchase_amount < 0:
    print("amount need to be posetive")
elif days_over > 14 or is_a_club_member and days_over > 30:
    print("over days...")
else:
    ("מאושר")
    