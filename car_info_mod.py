def car_info(company, model, color, type, year, price = None):
    # lug'at
    car = { 'company' : company,
            'model' : model,
            'color' : color,
            'type' : type,
            'year' : year,
            'price' : price
            }
    #return car 
    return car


def car_input():

    # car infoni to'ldirish uchun userdan kerakli data ma'lumotlarni olish funksiyasi

    cars = []
    while True:
        print("\nPlease answer to questions ", end = '')
        company = input   ("Which Company you choose for your future Car ?")
        model   = input   ("Enter Your Car Model ")
        color   = input   ("How about Color ?")
        type     = input  ("Sport, SUV, OffRoad or another ?")
        year    = input   ("Which year you want ?")
        price   = input   ("How much You can pay for your Car ?")

    # ma'lumotlar olingandan keyin lug'at ko'rinishida Ro'yxatga qo'shamiz car_info funksiyadan foydalanib

        cars.append(car_info(company, model, color, type, year, price))
    
    # Yana avtomobil qo'shidami yo'qmi so'rimiz

        answer = input("You wanna add another car also or not ?")

        if answer == 'no':
            break
            
    return cars

def infocar_print(car_info):

    # saqlab olingan ma'lumotlarni chiqarb olish 
    
    print(f"{car_info['color'].title()}, {car_info['company'].upper()} "
          f"{car_info['model'].upper()}, {car_info['type']} type, "
          f"{car_info['year']} year, {car_info['price']}$")
    