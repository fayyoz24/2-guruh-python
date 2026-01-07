# DICTIONARY
# fanlar = {
#     "banana":20000,
#     "cherry":10000,
#     "grapes":30000,
#     "pineapple":25000
# }
# fanlar['apple']=10000
# fanlar["banana"]=50000
# print(fanlar)
# # print(fanlar['apple'])
# # print(fanlar.get("apple", "topilmadi!"))
# arzon_mevalar = []
# for k, v in fanlar.items():
#     if v < 20000:
#         arzon_mevalar.append(k)
# print(arzon_mevalar)
# print(list(fanlar.keys()))
# print(list(fanlar.values()))

# SET, To'plam
# mevalar = {"olma","olma", "anor", "anjir", "banan", "ananas"} # Unordered
# print(mevalar)
# print(mevalar)
# import random
# random
# ERROR lar
# IndexError
# my_list = [1,2,3,4]
# print(my_list[5])

# ZeroDivisionError
# x = 0
# y = 5
# print(y/x)

# TypeError
# x = "a"
# y = 5
# print(x+y)

# try: harakat qq, urinib ko'rmoq
# except: istisno, ...dan tashqari

# try:
#     print(7/0)
# except ZeroDivisionError:
#     pass
#     # print(10/7)
#     print("nolga bo'lib bo'lmaydi!")

# try:
#     x = "a"
#     y = 5
#     print(x+y)
# except Exception as e:
#     # print(e)
#     print(f"{e}")
# else:
#     print("Men faqatgina try ishlasa ishlayman!")
# finally:
#     print("Men har doim ishlayman, menga try niham\nexceptniham farqi yo'q!")
# # x = "a"
# # y = 5
# # print(x+y)
# print("FINISH!")

students_ortacha={

}

students = {
    'ali':[75, 80, 72, 65],
    'vali':[98, 88, 90, 97],
    "oysha":[56, 60, 58, 70]
}

for key, value in students.items():
    students_ortacha[key] = sum(value) // len(value)

print(students_ortacha)

# Uyga vazifa shunga davom: agar o'rtacha baho 56 < x< 71 bo'lsa 3
# Uyga vazifa shunga davom: agar o'rtacha baho 71 < x< 86 bo'lsa 4
# Uyga vazifa shunga davom: agar o'rtacha baho 86 < x < 100 bo'lsa 5
{
    "ali":"beshlik stp",
    "vali":"3 lik stp",
    "oysha": "4 lik stp"
}
# amaliyotlar 92-116, 128-146