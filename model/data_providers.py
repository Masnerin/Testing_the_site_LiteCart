from model.input_data import Customer, Admin, Product
import os
import time
import random


# Функция вывода текущего времени в милисекундах:
def current_time_millis():
    return int(round(time.time() * 1000))


# Функция создания уникального e-mail:
def gen_email():
    array = [chr(i) for i in range(65, 91)]
    random.shuffle(array)
    key = ""
    for i in range(7):
        key += array.pop()
    email = key.lower() + '@random-email.com'
    return email


# Функция создания уникального имени пользователя:
def gen_user_name():
    array = [chr(i) for i in range(65, 91)]
    random.shuffle(array)
    key = ""
    for i in range(7):
        key += array.pop()
    user_name = key.title()
    return user_name


# Функция создания уникального кода (32 символа: латинские буквы и цифры):
def random_kod():
    kod = ''
    for x in range(32):
        kod = kod + random.choice(list('1234567890abcdefghigklmnopqrstuvyxwz'))
    return kod


def file_address():
    address = str(os.getcwd() + "\product_new.jpg")
    return address


admin = [Admin(username="admin",
               password="admin"
               )
         ]

new_customer = [Customer(firstname="Emma",
                         lastname="Brown",
                         phone="+0123456789",
                         address="New Street, 123",
                         postcode="12345",
                         city="New City",
                         country="US",
                         zone="KS",
                         email="emma%s@brown.com" % current_time_millis(),
                         password="password"
                         )
                ]

new_user = [Customer(firstname="%s" % gen_user_name(),
                     lastname="%s" % gen_user_name(),
                     phone="+016907734234",
                     address="Old Street, 27",
                     postcode="64100",
                     city="Old City",
                     country="US",
                     zone="KS",
                     email="%s" % gen_email(),
                     password="password"
                     )
            ]

new_product = [Product(username="admin",
                       password="admin",
                       product_name="New product",
                       code_product="%s" % random_kod(),
                       quantity="10",
                       image="%s" % file_address(),
                       date_valid_from="30052018",
                       date_valid_to="31122018",
                       keywords="product, new product",
                       short_description="New product for sale",
                       trumbowyg_editor="Why do we use it?\nGirl quit if case mr sing as no have. Small for ask shade water manor think men begin.",
                       head_title="New product",
                       meta_description="Very good product.",
                       purchase_price="19,99",
                       prices_usd="34,99",
                       prices_eur="29,99",
                       )
               ]
