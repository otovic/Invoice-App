# a = [{"petko":100, "age":20}, {"petkos":200, "age":22}]
# index = 0
# index = [(i, sublist[x]) for i, sublist in enumerate(a) for x in sublist if x == "petkos"]

# def power(x, n):
#     if n == 0:
#         return 1
#     else:
#         return x * power(x, n-1)

# print(power(2, 2))

# from docx import Document

# # Open an existing document
# document = Document('test.docx')

# # Get a list of all the styles in the document
# styles = document.styles.names

# # Print the list of styles
# print(styles)

# import pickle

companies = [{
    'Ime': 'OTTO-DIVISION',
    'Maticni': '64807234',
    'Adresa': 'Stevana Sremca 19/32',
    'Grad': 'Nis',
    'Email': 'ottosrbija@gmail.com',
    'Delatnost': '1413',
    'PIB': '110319347',
    'Path': '',
    'Account': '200-2910030101002-39',
    'Invoices': {'2022': []}
}]

import pickle

# with open('data/products.pickle', 'rb') as rb:
#     a = pickle.load(rb)
#     a.pop(len(a) - 1)

# with open('data/products.pickle', 'wb') as rb:
#     pickle.dump(a, rb)

# receivers = [{
#     'Naziv': '011',
#     'Ime': 'SOUVENIR SHOP',
#     'Maticni': '20121122',
#     'Grad': 'Beograd (Novi Beograd)',
#     'Ulica': 'Gandijeva 99B',
#     'PIB': '104223365'
# }]

# products = [{
#     'Ime': 'Pamucni Duks Sa logom',
#     'Cena': 2700
# },
# {
#     'Ime': 'Pamucni Duks Blanko',
#     'Cena': 2200
# }]

# with open('data/receivers.pickle', 'wb') as fw:
#     pickle.dump(receivers, fw)

# with open('data/reecivers.pickle', 'rb') as fw:
#     data = pickle.load(fw)
#     print(data)

import pyautogui
import time

while True:
    pyautogui.moveTo(100, 100, duration=0.25)
    pyautogui.moveTo(200, 100, duration=0.25)
    pyautogui.moveTo(200, 200, duration=0.25)
    pyautogui.moveTo(100, 200, duration=0.25)
    time.sleep(30)