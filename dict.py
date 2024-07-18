# fruit = dict(
#     apple = "olma",
#     banana = "banan",
#     watermelon = "melon"
# )

# fruit = {
#     'banana':"banan",
#     'strawberry':"qulpunay",
#     'watermelon':"tarvuz",
#     'peach':"shaftoli",
#     'grapes':"uzum"}

# user1 = input("Kalit so'zni kiriting :").lower()
# answer = fruit.get(user1)

# if answer == None:
#     print("Bunday Qiymat mavjud emas")
# else:
#     print(f"{user1.title()} so'zi {answer} deb tarjima qilinadi")

# fruit = {
#     'banana':"banan",
#     'strawberry':"qulpunay",
#     'watermelon':"tarvuz",
#     'peach':"shaftoli",
#     'grapes':"uzum"}

# nono = fruit.get('apple', 'Bunday qiymat mavjud emas')

# print(fruit)

# user1 = input("Kalit so'zni kiriting :").lower()
# answer = fruit.get(user1)

data = {
    'Kamron' : "Guliston",
    'Ali' : "Toshkent",
    'Muslima' : "Sirdaryo",
    'Hasan' : "Samarqand",
    'Doston' : "Qashqadaryo",
    'Ma`lumot yo`q' : "Ma'lumot yo'q"
}

for key, answer in data.items():
    print(f"Ism : {key}")
    print(f"Manzil : {answer} \n")
