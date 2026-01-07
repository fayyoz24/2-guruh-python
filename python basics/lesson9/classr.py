# ValueError
# ZeroDivisionError
# Uyga vazifa 146-bet, 2-amaliyot
# len()
# sum()
# max()
# min()
# tepadagi func larni kodini yozib kelish
# try:
#     x = int(input("son k: "))
#     y = int(input("son k: "))
#     print(x/y)
# except ValueError:
#     print("int son kiritng")
# except ZeroDivisionError:
#     print("nolga bolish mn emas")
# except Exception as e:
#     print(f"caught an errorr: {e}")

davlatlar = {
}
# davlatlar.get("ism", f"{key } topilmadi!")
# FUNKSIYA
# print()
# input()
# len()
# sum()
# max()
# min()

# def salom_beruvchi():
#     return "Assalomu Alaykum!"
# print(salom_beruvchi())

# def salom_beruvchi(ism):
#     return f"Assalomu Alaykum! {ism}"
# print(salom_beruvchi(ism="Ali"))

def salom_beruvchi(ism):
    return f"Assalomu Alaykum! {ism}"

def salom_beruvchi(ism="Fayyoz"):
    return f"Assalomu Alaykum! {ism}"

# print(salom_beruvchi())
# # print(salom_beruvchi(ism="Ali"))
# print(salom_beruvchi(ism="Ali"))
# print(salom_beruvchi(ism="Vali"))
# print(salom_beruvchi(ism="Oysha"))
# print(salom_beruvchi(ism="Aziz"))
# list().pop(2)

def katta_kichik(num1, num2, num3):
    if num1 >= num2:
        return num1
    return num2

# print(katta_kichik(num1=4, num2=3)) # to'g'ri
# print(katta_kichik(4, 3, num3=6)) # To'g'ri
# print(katta_kichik(num1=4, 3)) # xato
# print(katta_kichik(4,3))
# print(katta_kichik(num1=3, num2=3))
# print(katta_kichik(num1=1, num2=7))
list_ = [1,2,23,2,5,34,10]
def custom_max(a):
    if not a:
        return "list bo'sh"
    max_num = a[0] # 1
    for num in a:
        if num > max_num:
            max_num = num
    return max_num
# print(custom_max(list_))
# dict(yosh=)
# {"yosh":23, "voyaga_yetgan":True}
# import time
# from datetime import datetime
# datetime.year
def func_nomi(t_yil, h_yil=2025):
    yosh = h_yil - t_yil
    v_yetgan = False
    if yosh >= 18:
        v_yetgan=True
    return dict(yosh=yosh, voyaga_yetgan=v_yetgan)
print(func_nomi(t_yil=2009))
print(func_nomi(t_yil=2003, h_yil=2015))
print(func_nomi(t_yil=2005))