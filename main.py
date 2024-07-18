# import car_info_mod
# #Bu joyda funksiylarmzni 'import' yordamida chaqiramiz

# car1 = car_info_mod.car_info("Ferrari", "Spyder 701", "Red", "Sport", 2024, 400000)
# car_info_mod.infocar_print(car1)

# import 'chaqirmoqchi bo'lgan fayl nomi' as 'nima deb main faylda chaqirmoqchi bo'lsak shu nomni qo'yish'

# import car_info_mod as ccc

# car1 = ccc.car_info("Ferrari", "Spyder 701", "Red", "Sport", 2024, 400000)
# ccc.infocar_print(car1)

# 'from' modul_nomi 'import' funksiyalar nomi kerakli bo'lgan

# from car_info_mod import car_info, infocar_print

# car1 = car_info("Ferrari", "Spyder 701", "Red", "Sport", 2024, 400000)
# infocar_print(car1)

# as yordamida funksiylarga ham qisqa nom bersak bo'ladi

# moduldan barcha funksiyalarni ko'chirib olish uchun "from modul_nomi import *" dangerous ehtiyot bo'lish

# from car_info_mod import *

# car1 = car_info("Ferrari", "Spyder 701", "Red", "Sport", 2024, 400000)
# infocar_print(car1)

import datetime as dt

now = dt.datetime.now()
a = input("Time ? ")

if a == "Time" or a == "time" :
    print(now.time())
else:
    print('Error')


# weather = input("How's the weather? ")

# # Correct usage with 'or'
# if weather == "Good" or weather == "Great":
#     print("Glad to hear!")
# else:
#     print("That's too bad!")
