from util import readData, updateData
import tkinter as tk
from tkinter import ttk

class AddProductDialog():
    def __init__(self, root):
        self.AddProductWindow = tk.Toplevel(root)
        self.AddProductWindow.geometry("300x300")
        self.AddProductWindow.title('Dodaj Proizvod - Ottoshop')
        self.data = readData('data/products.pickle')
        self.container = tk.Frame(self.AddProductWindow)
        self.container.pack()
        self.productName = tk.StringVar()
        self.productNameFrame = tk.Frame(self.container)
        self.productNameFrame.pack(pady=10, padx=15, fill='both', expand=True)
        self.productPrice = tk.StringVar()
        self.productPriceFrame = tk.Frame(self.container)
        self.productPriceFrame.pack(pady=10, padx=15, fill='both', expand=True)
        self.SubmitFrame = tk.Frame(self.container)
        self.SubmitFrame.pack(pady=10, padx=15, fill='both', expand=True)

    def __del__(self):
        print("odoh")

    def Submit(self):
        if self.productName.get() != '' and self.productPrice.get() != '':
            self.data.append({
                'Ime': self.productName.get(),
                'Cena': int(self.productPrice.get())
            })
            updateData('data/products.pickle', self.data)
            self.AddProductWindow.destroy()
            del self
    
    def showAddProductDialog(self):
        ttk.Label(self.productNameFrame, text='Naziv Proizvoda:').pack(padx=0, anchor='w')
        tk.Entry(self.productNameFrame, textvariable=self.productName, width=35).pack(anchor='center', pady=5)

        ttk.Label(self.productPriceFrame, text='Cena Proizvoda:').pack(padx=0, anchor='w')
        tk.Entry(self.productPriceFrame, textvariable=self.productPrice, width=35).pack(anchor='center', pady=5)

        ttk.Button(self.SubmitFrame, width=30, text="Dodaj", command=self.Submit).pack(anchor='center')