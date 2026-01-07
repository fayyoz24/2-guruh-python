# a = 7
# b = 7
# if a >= b:
#     print("A")
# else:
#     print("d")

# # AND, OR, NOT operatorlari

# # and va
# # or yoki
# # not emas

# yosh = 40
# print(yosh != 7)

# if not(yosh <= 7 or yosh > 65):
#     print("bepul")
# else:
#     print("PULLIK")

# numbers = []
# for number in range(1, 11):
#     numbers.append(number)
# print(numbers)

# # n = 5
# # 12345
# # n=3
# # 123
# # n=6
# # 123456

# n = 5
# # num_str = ""
# for a in range(1, n+1):
#     # print(f"{a}")
#     pass
# #     num_str+=str(a)
# # print(num_str)

# ismlar = ["Ali", "Vali", "Bek", "Xon", "Oysha"]
# for ism in ismlar[1:4]:
#     print(f"Assalomu alaykum {ism}")
#     # vali, bek, xon
# n = 5
# b = 0
# for a in range(1, n+1):
#     b += 10 ** (n-a)*a

# # print(b)
# # print(type(b))
# # WHILE loopi
# # n = 5
# # # n = 4
# # # n = 3
# # # n = 2
# # # n = 1
# # # n = 0
# while n > 0:
#     print(n)
#     n -= 1

# n = 0
# while n < 5:
#     print(n)
#     n+=1

# # break. to'xtatmoq
# # continue davom etmoq
# # pass o'tqazib yubormoq

# while True:
#     user_inp = input("Raqam kiriting: to'xtatish uchun 0 kriting: ")
#     if user_inp == "exit":
#         break
#     else:
#         print(user_inp)

# for i in "ali":
#     pass

# n = int(input("enter a num: "))
# for num in range(10):
#     if num == 5:
#         continue
#     elif num == n:
#         break
#     elif num == 2:
#         pass
#     else:
#         print(num)

import random
kom_num = random.randint(1, 10)
# print(kom_num)
n = 1
while n < 6:
    user_guess = int(input(f"{n}-taxmin raqamni kiriting: "))
    if user_guess == kom_num:
        print(f"{n}-urinishda topdingiz va {(6-n)*10} bal oldiz!")
        print("Siz yuttiz!!!")
        break
    n += 1
print("yutqazdiz")