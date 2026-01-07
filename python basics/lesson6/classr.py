# son = int(input("Juft son k: "))
# # None, 0, "", [], {}, ()
# print(bool(None))
# if son % 2: 
#     print("BU son juft emas!")
# else:
#     print("Rahmat!")

# yosh = int(input("yosh K: "))
# if yosh <= 4 or yosh >= 60:
#     print("bepul")
# elif yosh <= 18:
#     print("10 ming")
# else:
#     print("20 ming")
# # 'ali'[0]

# ismlar = ['aliBEK', 'vali', "Asilbek", 'anora', "olimBek"]
# for ism in ismlar:
#     if ism.lower()[0] == 'a':
#         print(ism)

# # while qachonki, toki
# x = 0
# # x = 1
# # x= 2
# # x=3
# # x=4
# # x=5
# while x < 5: # True, 5
#     print(x)
#     x += 1
#     while True:
#         if x == 5:
#             break
#         print(x)

# x = 1
# yigindi = 0
# while x < 6:
#     user_raqam = float(input("raqam k: "))
#     yigindi += user_raqam
#     x += 1
# print(yigindi)


qizlar = []
bolalar = []
x = 0
while x < 4:
    x += 1
    familiya = input("Familiya k: ")
    if familiya[-1].lower() == "a":
        qizlar.append(familiya)
    elif familiya[-1].lower() == 'v':
        bolalar.append(familiya)
print(f"Qizlar: {qizlar}")
print(f"o'g'il bolalar {bolalar}")