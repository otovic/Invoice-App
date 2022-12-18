import tkinter as tk
from tkinter import ttk
from util import getData, getInvoices
import time

def renderInvoiceDialog(root):
    invoiceDialog = tk.Toplevel(root)
    #container frame for all other frames
    container = tk.Frame(invoiceDialog)
    container.pack()

    #getting companies data from text file
    companies = getData('./data/companies.txt')
    optionsCompanies = [x['Ime'] for x in companies]
    selectedCompany = tk.StringVar(invoiceDialog)
    selectedCompany.set(optionsCompanies[0])

    #creating companies frame and generating dropdown list for it
    companyFrame = tk.Frame(container)
    companyFrame.pack(pady=10, fill='both', expand=True)
    ttk.Label(companyFrame, text='Firma:').pack(padx=20, anchor='w')
    companiesDropDown = tk.OptionMenu(companyFrame, selectedCompany, *optionsCompanies)
    companiesDropDown.configure(width=30)
    companiesDropDown.pack(padx=20, anchor="w")

    #getting receivers data
    receivers = getData('./data/receivers.txt')
    optionsReceivers = [x['Naziv'] for x in receivers]
    selectedReceiver = tk.StringVar(invoiceDialog)
    selectedReceiver.set(optionsReceivers[0])

    #creating companies frame and generating drop down list for it
    receiverFrame = tk.Frame(container)
    receiverFrame.pack(pady=10,  fill='both', expand=True)
    ttk.Label(receiverFrame, text='Primalac:').pack(padx=20, anchor='w')
    receiverDropDown = tk.OptionMenu(receiverFrame, selectedReceiver, *optionsReceivers)
    receiverDropDown.configure(width=30)
    receiverDropDown.pack(padx=20, anchor="w")

    #creating invoice number frame and filling the field with last invoice number used
    lastInvoiceNum = str(int(getInvoices()) + 1)
    invoiceYear = str(time.localtime().tm_year)
    invoiceNumber = tk.StringVar()
    invoiceNumber.set(lastInvoiceNum + '-' + invoiceYear[-2:])
    invoiceNumberFrame = tk.Frame(container)
    invoiceNumberFrame.pack(pady=10,  fill='both', expand=True)
    ttk.Label(invoiceNumberFrame, text='Broj Fakture:').pack(padx=20, anchor='w')
    invoiceNumberEntry = tk.Entry(invoiceNumberFrame, textvariable=invoiceNumber)
    invoiceNumberEntry.pack(pady=10, padx=22, fill='both', expand=True)

    productFrame = tk.Frame(container)
    productFrame.pack(pady=10, padx=20, fill='both', expand=True)

    products = getData('./data/products.txt')
    optionProducts = [x['Ime'] for x in products]
    selectedproduct = tk.StringVar()
    selectedproduct.set(optionProducts[0])

    quantity = tk.StringVar()
    quantity.set(0)

    selectedProducts = []
    existingLabels = []

    def insertProduct():
        if int(quantity.get()) != 0:
            if any(x[0] == selectedproduct.get() for x in selectedProducts):
                index = [i for i, sublist in enumerate(selectedProducts) for x in sublist if x == selectedproduct.get()]
                selectedProducts[index[0]][1] += int(quantity.get())
                insertProductInList(existingLabels)
            else:
                cena = next(int(x['Cena'].strip()) for x in products if x['Ime'] == selectedproduct.get())
                product = [selectedproduct.get(), int(quantity.get()), cena]
                selectedProducts.append(product)
                existingLabels = insertProductInList(existingLabels)

    productsDropDown = tk.OptionMenu(productFrame, selectedproduct, *optionProducts)
    productsDropDown.configure(width=25)
    productsDropDown.pack(side='left')
    quantityEntry = tk.Entry(productFrame, textvariable=quantity, width=3)
    quantityEntry.pack(side='left')
    ttk.Button(productFrame, text="+", width=3, command=insertProduct).pack(side='left')

    selectedProductsFrame = tk.Frame(container)
    selectedProductsFrame.pack(pady=10, padx=20, fill='both', expand=True)

    def insertProductInList(lbls):
        for x, sublist in enumerate(lbls):
            print(sublist[0])
            sublist[0].pack_forget()
            sublist[1].pack_forget()
        lbls = []
        for x in range(len(selectedProducts)):
            lbl = ttk.Label(selectedProductsFrame, text=f"{x + 1}: {selectedProducts[x][0]} ({selectedProducts[x][2]}) x {selectedProducts[x][1]}")
            lbl.grid(row=x, column=0)
            btn = ttk.Button(selectedProductsFrame, text="X", width=1, command=lambda: on_click(x, lbls))
            btn.grid(row=x, column=1)
            lbls.append([lbl, btn])
        return lbls
    
    def on_click(pos, arrlbl):
        selectedProducts.pop(pos)
        insertProductInList(existingLabels)
        # for x, sublist in enumerate(existingLabels):
        #     btn = sublist[1]
        #     print(btn['text'])