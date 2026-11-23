# num = 1 
# while num <= 10:
#     print(num)
#     num += 1

# num = 10
# while num:
#     print(num)
#     num -= 1
# print("STAR!")

# num = 1
# while num <= 50:
#     if num % 2 == 0:
#         print(num)
#     num += 1

# num = int(input(""))
# for i in range(1,6):
#     print(num * i)

# num = 0
# for i in range(1, 100):
#     num += i
# print(num)

# password = input(":")
# while password != "Python123":
#     password = input(":")
# print("WELCOME!")

# num = int(input(":"))
# secret_number = 27
# while num != secret_number:
#     num = int(input(":"))
# print("success!")

# sum = 0 
# num = int(input(":"))
# while num != 0:
#     sum += num
#     num = int(input(":"))
# print(sum)

# greade = float(input(""))
# count = 0
# sum = 0
# while greade != 999:
#     count += 1
#     sum += greade
# print(count, sum, sum / count)

# num = int(input(""))
# count = 0
# sum = 0
# while num > 0:
#     count += 1
#     sum += num
# print(sum, count)

# num = int(input(""))
# for i in range(1, 11):
#     print(f'{num} * {i} = {num * i}')

# num = int(input(":"))
# count = 0
# while num :
#     num //= 10
#     count += 1
# print(count)

# num = int(input(":"))
# new = 0
# while num :
#     new += (num % 10)
#     num //= 10
#     new *= 10
# print(new // 10)

# num = int(input(":"))
# flag = True
# for i in range(2, num ** 0.5):
#     if num % i != 0:
#         flag = False
# print(flag)

# balance = 5000
# choice = int(input(":"))
# while True and choice != 4 :
#     print("""
# 1. Check balance.
# 2. Deposit money.
# 3. Withdraw money.
# 4. Log out.
# """)
#     if choice == 1:
#         print(balance)
#     elif choice == 2:
#         deposit = int(input(":"))
#         if deposit < 0:
#             print("Deposit need to be posative")
#         else:
#             balance += deposit
#     elif choice == 3:
#         attraction = int(input(":"))
#         if attraction < 0:
#             print("Deposit need to be posative")
#         elif attraction > balance:
#             print("you dont heve inof mony")
#         else:
#             balance -= attraction
#     else:
#         break

# num = 1
# while True:
#     print(num)
#     num += 1
#     if num == 15:
#         break


# for i in range(1, 30):
#     if i % 3 == 0:
#         continue
#     print(i)

# num = int(input(":"))
# while True:
#     if num == 100:
#         print("Success")
#         break

# for i in range(1, 20):
#     print(i)

# for i in range(0, 100, 5):
#     print(i)

# sum = 0
# for i in range(1, 100):
#     sum += i
# print(i)

# num = int(input(":"))
# for i in range(1,11):
#     print(f'{num} * {i} = {num*i}')

# num_1 = int(input(":"))
# num_2 = int(input(":"))
# sum = 0
# for i in range(num_1, num_2+1):
#     sum += i
# print(i)

# for i in range(15,100,15):
#     print(i)

# num_1 = int(input(":"))
# num_2 = int(input(":"))
# for _ in range(num_1):
#     for _ in range(num_2):
#         print("*", end='')
#     print()

# for i in range(1,7):
#     print('*'*i)


# for i in range(1,11):
#     for j in range(1,11):
#         print( i*j, end=' ')
#     print()

# for i in range(1,6):
#     for j in range(1,6):
#         print( i, j)

pount = 0
while True:
    choose = int(input("""
===== MATH GAME =====

1. Start Game
2. View Instructions
3. Exit

Choose: """))
    if choose == 3:
        break
    if choose == 1:
        pount += 1 if int(input(" 1 + 1")) == 2 else 0
        pount += 1 if int(input(" 1 + 2")) == 3 else 0
        pount += 1 if int(input(" 1 * 1")) == 1 else 0
        pount += 1 if int(input(" 1 + 10")) == 11 else 0
        pount += 1 if int(input(" 14 + 1")) == 15 else 0
        pount += 1 if int(input(" 10- 1")) == 9 else 0
        pount += 1 if int(input(" 110 * 2")) == 220 else 0
        pount += 1 if int(input("3 ** 2")) == 9 else 0
        pount += 1 if int(input("6 * 4")) == 24 else 0
        pount += 1 if int(input("5 * 6")) == 30      else 0
    if choose == 2:
        print(pount)