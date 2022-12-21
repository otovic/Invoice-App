import tkinter as tk
from tkinter import ttk
from util import getData, getInvoices
import time

class invoiceDialog:
    def __init__(self, root) -> None:
        self.optionsCompanies = [x['Ime'] for x in getData('data/companies.txt')]
        self.optionsReceivers = [x['Naziv'] for x in getData('./data/receivers.txt')]
        self.invoiceNumber = str(int(getInvoices()) + 1)
        self.lastInvoiceNum = str(int(getInvoices()) + 1)
        self.invoiceYear = str(time.localtime().tm_year)
        self.products = getData('./data/products.txt')
        self.optionProducts = [x['Ime'] for x in self.products]
        self.quantity = tk.StringVar()
        self.quantity.set(0)
        self.selectedproduct = tk.StringVar()
        self.selectedproduct.set(self.optionProducts[0])
        self.selectedProducts = []
        self.existingLabels = []
        self.invoiceWindow = tk.Toplevel(root)
        self.invoiceWindow.title('Fakturisanje - Ottoshop')
        self.container = tk.Frame(self.invoiceWindow)
        self.container.pack()
        self.companyFrame = tk.Frame(self.container)
        self.companyFrame.pack(pady=10, fill='both', expand=True)
        self.receiverFrame = tk.Frame(self.container)
        self.receiverFrame.pack(pady=10,  fill='both', expand=True)
        self.invoiceNumberFrame = tk.Frame(self.container)
        self.invoiceNumberFrame.pack(pady=10,  fill='both', expand=True)
        self.productFrame = tk.Frame(self.container)
        self.productFrame.pack(pady=10, padx=10, fill='both', expand=True)
        self.selectedProductsFrame = tk.Frame(self.container)
        self.selectedProductsFrame.pack(pady=10, padx=22, fill='both', expand=True)

    def printData(self):
        print(self.optionsCompanies)

    def removeProduct():
        print('petar')

    def insertProductInList(self, selectedProductsFrame):
        for x, sublist in enumerate(self.existingLabels):
            print(self.existingLabels)
            sublist[0].pack_forget()
        self.existingLabels = []
        for x in range(len(self.selectedProducts)):
            frm = tk.Frame(self.selectedProductsFrame)
            frm.pack(pady=10, padx=3, fill='both', expand=True)
            lbl = ttk.Label(frm, text=f"{x + 1}: {self.selectedProducts[x][0]} ({self.selectedProducts[x][2]}) x {self.selectedProducts[x][1]}")
            lbl.pack(side='left')
            btn = ttk.Button(frm, text="X", width=1, command=lambda: self.removeProduct())
            btn.pack(side='left')
            self.existingLabels.append([frm])

    def testy(self):
        for i, sub in enumerate(self.products):
            print(sub)
            for y in sub:
                print(y[0])
                if y[0] == self.selectedproduct.get():
                    print('AAAAAAAAAA')

    def insertProduct(self, frame):
        price = None
        if int(self.quantity.get()) != 0:
            if any(x[0] == self.selectedproduct.get() for x in self.selectedProducts):
                index = [i for i, sublist in enumerate(self.products) if sublist['Ime'] == self.selectedproduct.get()]
                print(index)
                self.selectedProducts[index[0]][1] += int(self.quantity.get())
                self.insertProductInList(frame)
            else:
                print(self.optionProducts)
                price = next(int(x['Cena'].strip()) for x in self.products if x['Ime'] == self.selectedproduct.get())
                product = [self.selectedproduct.get(), int(self.quantity.get()), price]
                self.selectedProducts.append(product)
                self.insertProductInList(frame)

    def renderDialog(self):
        #getting companies data from text file
        selectedCompany = tk.StringVar(self.invoiceWindow)
        selectedCompany.set(self.optionsCompanies[0])

        #creating companies frame and generating dropdown list for it
        ttk.Label(self.companyFrame, text='Firma:').pack(padx=20, anchor='w')
        companiesDropDown = tk.OptionMenu(self.companyFrame, selectedCompany, *self.optionsCompanies)
        companiesDropDown.configure(width=30)
        companiesDropDown.pack(padx=20, anchor="w")

        #getting receivers data
        selectedReceiver = tk.StringVar(self.invoiceWindow)
        selectedReceiver.set(self.optionsReceivers[0])

        ttk.Label(self.receiverFrame, text='Primalac:').pack(padx=20, anchor='w')
        receiverDropDown = tk.OptionMenu(self.receiverFrame, selectedReceiver, *self.optionsReceivers)
        receiverDropDown.configure(width=30)
        receiverDropDown.pack(padx=20, anchor="w")

        invoiceNumberFrame = tk.Frame(self.container)
        invoiceNumberFrame.pack(fill='both', expand=True)
        #creating invoice number frame and filling the field with last invoice number used
        invoiceNumberVar = tk.StringVar()
        invoiceNumberVar.set(self.lastInvoiceNum + '-' + self.invoiceYear[-2:])

        ttk.Label(self.invoiceNumberFrame, text='Broj Fakture:').pack(padx=20, anchor='w')
        invoiceNumberEntry = tk.Entry(self.invoiceNumberFrame, textvariable=invoiceNumberVar)
        invoiceNumberEntry.pack(pady=10, padx=22, fill='both', expand=True)

        productsDropDown = tk.OptionMenu(self.productFrame, self.selectedproduct, *self.optionProducts)
        productsDropDown.configure(width=22)
        productsDropDown.pack(side='left')
        quantityEntry = tk.Entry(self.productFrame, textvariable=self.quantity, width=3)
        quantityEntry.pack(side='left')
        ttk.Button(self.productFrame, text="+", width=3, command=lambda: self.insertProduct(self.selectedProductsFrame)).pack(side='left')