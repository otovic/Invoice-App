from util import readData, updateData
import tkinter as tk
from tkinter import ttk

class ChangeProductDialog():
    def __init__(self, root) -> None:
        self.ChangeProductWindow = tk.Toplevel(root)
        self.ChangeProductWindow.geometry('300x210')
        self.ChangeProductWindow.title('Izmeni Proizvod')

        self.container = tk.Frame(self.ChangeProductWindow)
        self.container.pack()

        self.products = readData('data/products.pickle')
        self.ddo_products = [name['Ime'] for name in self.products]
        self.selectedProduct = tk.StringVar()
        self.selectedProduct.set(self.products[0]['Ime'])

        self.productsListFrame = tk.Frame(self.container)
        self.productsListFrame.pack(pady=10, padx=15, fill='both', expand=True)

        self.fr_productPrice = tk.Frame(self.container)
        self.fr_productPrice.pack(pady=10, padx=15, fill='both', expand=True)
        self.sv_productPrice = tk.StringVar()
        self.sv_productPrice.set(self.products[0]['Cena'])

        self.fr_submitFrame = tk.Frame(self.container)
        self.fr_submitFrame.pack(pady=10, padx=15, fill='both', expand=True)

    def __del__(self):
        print('Aj cao')

    def updateSelectedProduct(self, product):
        for index, crr_product in enumerate(self.products):
            if product == crr_product['Ime']:
                self.sv_productPrice.set(crr_product['Cena'])

    def Submit(self):
        for index, crr_product in enumerate(self.products):
            if self.selectedProduct.get() == crr_product['Ime']:
                self.products[index]['Cena'] = int(self.sv_productPrice.get())
                break
        updateData('data/products.pickle', self.products)
        self.ChangeProductWindow.destroy()
        del self     

    def render_dialog(self):
        print(self.selectedProduct)
        ttk.Label(self.productsListFrame, text='Proizvod:').pack(padx=20, anchor='w')
        companiesDropDown = tk.OptionMenu(self.productsListFrame, self.selectedProduct, *self.ddo_products, command=self.updateSelectedProduct)
        companiesDropDown.configure(width=30)
        companiesDropDown.pack(padx=20, anchor="w")

        ttk.Label(self.fr_productPrice, text='Cena Proizvoda:').pack(padx=0, anchor='w')
        tk.Entry(self.fr_productPrice, textvariable=self.sv_productPrice, width=35).pack(anchor='center', pady=5)

        ttk.Button(self.fr_submitFrame, width=30, text="Izmeni", command=self.Submit).pack(anchor='center')