# # while True:
# #     age = input("yoshizni K: ")
# #     if age.lower() == "exit" or age.lower()=="quit":
# #         break
# #     age = int(age)
# #     if age < 7:
# #         print(2000)
# #     elif 7 <= age <= 18:
# #         print(3000)
# #     else:
# #         print("bepul")
# # kitob = input("kitob K: ")

# # Dictionary ==> lug'at
# # "apple":"olma"

# dict_ = {
#     "ism":"Ali",
#     "yosh":45,
#     "familiya":"Valiyev"
# }
# # from .home import dict_
# print(len(dict_))
# # print(dict_["karta raqam"])
# print(dict_.get("ism", "karta raqam mavjud emas"))
# dict_["karta raqam"] = "9860....2627"
# print(dict_)
# dict_.update({
#     "username":"ali01",
#     "prof_pic":"https://example.com/user_1"
# })
# dict_["ism"]='Vali'
# print(dict_)
# my_dict={
#     5:"besh",
#     "ism":"Ali",
#     3.4:"3 butun 4",
#     True:"True",
#     (12, 34, "ali"):"Tuple", 
#     # [1,2,3,4]:"list elems",
#     # {5:"besh",
#     # "ism":"Ali"}:"assadxs"
# }
# print(my_dict)
# # Mutable: list, dict
# # Immutable: int, str, float, bool, tuple

# del my_dict["ism"]
# menyu = {
#     "osh":30000,
#     "shashlik":52000,
#     "manti":8000,
#     "salat":10000,
#     "non":5000,
#     "choy":3000
# }
# while True:
#     ovqat_nomi = input("Nima yeysiz: ")
#     if ovqat_nomi == "stop":
#         print("Osh bo'lsin!")
#         break
#     print(menyu.get(ovqat_nomi, f"bizda {ovqat_nomi} yo'q"))

my_list = ['Ali', "Vali", "Ali", "Vali", "vali", "Oysha"]
my_dict = {
}
# for ism in my_list:
#     my_dict[ism] = my_list.count(ism)
# print(my_dict)
import time
start = time.time()
for ism in my_list:
    if my_dict.get(ism):
        my_dict[ism] += 1
    else:
        my_dict[ism] = 1
print(my_dict)
end = time.time()
print(f"mening kodim {end-start} vaqt oldi")
# a= {
#     "Ali":2,
#     "Vali":3,
#     "Oysha":1
# }