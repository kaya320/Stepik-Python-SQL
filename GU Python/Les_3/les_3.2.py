def person(name, surname, year, city, email, tel):
    print(f' Пассажира зовут {name} {surname}, {year} года рождения,'
          f' проживает в городе {city}, связаться можно по почте {email} или по телефону {tel}')


person(name='Кристина', surname='Иванова', city='Нью-Йорк', email='newmail.com', tel=7339000, year=1990)


def personal_info(**kwargs):
    return kwargs


print(personal_info(name=input("Enter your name: "), surname=input("Enter Your surname: ")))