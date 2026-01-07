# a = int(input("1-sonni k: "))
# b = int(input("2-sonni k: "))
# print(a**b)

def daraja(a, b):
    return a**b
# print(daraja(3, 4))
def daraja(a, b=2):
    return a**b
# print(daraja(4))
my_list = [1,2,3,4,5,6]
my_list[3] = 90
# print(my_list)

def bolinish(n):
    bolinadiganlar=[]
    bolinadiganlar_dict={}
    for i in range(2, 11):
        if n % i == 0:
            bolinadiganlar.append(i)
            bolinadiganlar_dict[i] = n // i #24
            # return f"{i} ga qoldiqsiz bo'linadi"
    return bolinadiganlar, bolinadiganlar_dict

# print(bolinish(n=48))
# print(bolinish(n=43))
# print(bolinish(n=38))
# print(bolinish(n=100))
def fibonachchi(n):
    sonlar = []
    # n = 1 # [1]
    # n = 2 # [1]
    # n = 3 # [1, 1, 2]
    # n = 4 # [1, 1, 2, 3]
    # n = 5 # [1, 1, 2, 3, 5]
    a, b = 0, 1
    for i in range(n):
        sonlar.append(a)
        a, b = b, a + b
    return sonlar

def aylana(r):
    dict_aylana={}
    pi = 3.14
    d = 2 * r
    p = round(2*pi*r, 2)
    s = round(pi * r ** 2, 2)
    dict_aylana.update({
        "radius": r,
        "diametr": d,
        "perimetr": p,
        "yuza":s
    })
    return dict_aylana
# print(aylana(5))
# # print(fibonachchi(n=5))
# max, min, len, sum, str.title(), str.capitalize(),
# list.pop(n=-1), list.append(), list.remove()
# Uyga vazifa
# map(), zip(), filter(), *args, **kwargs


text = "map(), zip(), filter(), *args, **kwargs"
print(text.split("*"))