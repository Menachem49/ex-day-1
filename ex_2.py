# #ex_1
# num1 = 25
# num2 = 7
# print(num1 + num2)
# print(num1 - num2)
# print(num1 * num2)
# print(num1 / num2)
# print(num1 // num2)
# print(num1 % num2)
# print(num1 ** num2)

# #ex_2
# balance = 1000
# print(balance)
# balance += 250
# print(balance)
# balance -= 100
# print(balance)
# balance *= 2
# print(balance)
# balance /= 4
# print(balance)

# #ex_3
# price = float(input("Enter price: "))
# percentage = int(input("Enter percentage: ")) / 100
# print(price * percentage)
# print(price * (1 - percentage))

# #ex_4
# price = float(input("Enter price: "))
# Interest = int(input("Enter Interest: ")) / 100
# print(price * Interest)
# print(price * (1 + Interest))

# #ex_5
# greade_1 = float(input("Enter a greade: "))
# greade_2 = float(input("Enter a greade: "))
# greade_3 = float(input("Enter a greade: "))
# print((greade_1 + greade_2 + greade_3) / 3)

# #ex_6
# first_name = input("Enter a first name: ") 
# last_name = input("Enter a last name: ")
# city = input("Enter a city: ")
# print(f"Hello, my name is {first_name} {last_name} and I live in {city}.")
# print('Hello, my name is ' + first_name + ' '+ last_name +' and I live in '+ city + '.')

# #ex_7
# name = input("Enter your name: ")
# print(name)
# print(len(name))
# print(name.upper())
# print(name.lower())

# #ex_8
# txt = input("Enter a text: ")
# print(txt.upper())
# print(txt.lower())
# print(txt.capitalize())
# print(txt.title())

# #ex_9
# name = input("Enter your name: ")
# print(name)
# print(name.strip())
# print(len(name))
# print(len(name.strip()))

# #ex_10
# sentence = "I love Java programming"
# print(sentence.replace("Java", "Python"))
# print(sentence.count("love"))
# print(sentence.startswith("I"))
# print(sentence.endswith("programming"))

# # ex_11
# word = "Programming"
# print(f'''
# {word[0]}
# {word[-1]}
# {word[2]}
# {word[:3]}
# {word[-4:]}
# {word[::-1]}
# ''')

# #ex_12
# a = "100"
# b = "25"
# c = 10
# d = 5.5
# a = int(a)
# b = float(b)
# c = str(c)
# d = int(d)
# print(a, type(a))
# print(b, type(b))
# print(c, type(c))
# print(d, type(d))

# #ex_13
# age = input("Enter your age: ")
# # print(age + 10)
# # Type Error
# print(int(age) + 10)

# #ex_14
# price = int(input("Enter a price: "))
# VAT = 18
# print(price * (1 + (VAT / 100)))

# #ex_15
# first_name = input("Enter employ first name: ")
# last_hours = input("Enter your last name")
# age = int(input("Enter your name: "))
# salary = float(input("Enter the employ salary: "))
# years_of_seniority = int(input("Enter years in campeny: "))
# print(f'''
# employ: {first_name} {last_hours}
# age: {age}
# months salary: {salary}
# years in campeny: {years_of_seniority}
# ''')
# months_in_year = 12
# total = salary * months_in_year
# print(f'''
# year salary: {total}
# The salary after a 5% increase {total * 1.05}
# name len {len(first_name) +len(last_hours)}
# ''')

# #ex_16
# usd_rate = 3.25
# euro_rate = 3.75
# sum_input = float(input("Enter a sum in shekels: "))
# fee = 2
# print(sum_input / usd_rate)
# print(sum_input / euro_rate)
# print(sum_input * (1 + (fee / 100)))

# #ex_17
# first_name = input("Enter employ first name: ").lower()
# last_name = input("Enter your last name").lower
# birth_year = int(input("Enter your birth year: "))
# email = f'{first_name}.{last_name}.{birth_year}@gmail.com'

# #ex_18
# txt = input("Enter a text: ")
# print(txt)
# print(len(txt))
# print(txt.upper())
# print(txt.lower())
# print(txt[::-1])
# print(txt.replace(" ","-"))

#ex_19
customer_name = input("Enter customer name: ")
product_name = input("Enter product name: ")
product_price = float(input("Enter product price: "))
quantity_of_products = int(input("Enter product quantity: "))
discount_percentage = float(input("Enter discount: "))/100
VAT = float(input("Enter sum of vat: "))
sub_total = product_price * quantity_of_products
sum_dis = sub_total * discount_percentage
sub_total_after_dis = sub_total - sum_dis
vat_amount = sub_total_after_dis * (VAT / 100)
total_plus_vat = sub_total_after_dis + vat_amount
print(f"""
================================
          PURCHASE INVOICE
================================

Customer: {customer_name}
Product: {product_name}

Unit Price: {product_name}
Quantity: {quantity_of_products}

Subtotal: {sub_total}
Discount: {sum_dis}
After Discount: {sub_total_after_dis}

VAT: {VAT}%
VAT Amount: {vat_amount}

TOTAL: {total_plus_vat}

================================
       THANK YOU FOR SHOPPING
================================

""")