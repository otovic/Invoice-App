import tkinter as tk
from tkinter import ttk
from util import getData, getInvoices
import time
import docx
import datetime
from tkinter import filedialog as fd
from docx.table import Table
from docx.shared import RGBColor, Pt
from docx.enum.style import WD_STYLE_TYPE

class invoiceDialog:
    def __init__(self, root) -> None:
        self.optionsCompanies = [x['Ime'] for x in getData('data/companies.txt')]
        self.selectedCompany = tk.StringVar()
        self.selectedCompany.set('OTTO-DIVISION')
        self.companiesData = [x for x in getData('data/companies.txt') if x['Ime'] == self.selectedCompany.get()]
        self.selectedCompany.set(self.optionsCompanies[0])
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
        self.productFrame.pack(pady=10, padx=15, fill='both', expand=True)
        self.selectedProductsFrame = tk.Frame(self.container)
        self.selectedProductsFrame.pack(pady=10, padx=10, fill='both', expand=True)
        self.invoicePathFrame = tk.Frame(self.container)
        self.invoicePathFrame.pack(pady=10, padx=10, fill='both', expand=True)
        self.invoicePath = tk.StringVar()
        self.invoicePath.set(self.companiesData[0]['path'])

    def saveDocument(self):
        print(self.companiesData)
        # Create a new document
        
        doc = docx.Document()
        table = doc.add_table(rows=6, cols=2)

        titleP = doc.add_paragraph()
        titleStyle = doc.styles
        title_charstyle = titleStyle.add_style('TitleStyle', WD_STYLE_TYPE.CHARACTER)
        title_charstyle.font.size = Pt(10)
        title_charstyle.font.name = 'Calibri'
        titleP.paragraph_format.space_after = Pt(0)

        table = doc.add_table(rows=6, cols=2)
        cell = table.cell(0, 2)

        textStyle = doc.styles
        text_charstyle = textStyle.add_style('TextStyle', WD_STYLE_TYPE.CHARACTER)
        text_charstyle.font.size = Pt(12)
        text_charstyle.font.name = 'Calibri'

        runner = titleP.add_run(self.companiesData[0]['Ime'], style='TitleStyle')
        runner.bold = True
        runner.italic = True
        runner.font.size = Pt(20)
        cell.add_paragraph('PETRICA')

        companyIDNum = doc.add_paragraph()
        companyIDNum.paragraph_format.space_after = Pt(0)
        runner = companyIDNum.add_run(f"Maticni broj: {self.companiesData[0]['Maticni']}", style ='TextStyle')
        runner.font.size = Pt(12)

        companyTaxNumber = doc.add_paragraph()
        companyTaxNumber.paragraph_format.space_after = Pt(0)
        runner = companyTaxNumber.add_run(f"PIB: {self.companiesData[0]['PIB']}", style ='TextStyle')
        runner.font.size = Pt(12)

        companyAdress = doc.add_paragraph()
        companyAdress.paragraph_format.space_after = Pt(0)
        runner = companyAdress.add_run(f"Adresa: {self.companiesData[0]['Adresa']}, {self.companiesData[0]['Grad']}", style ='TextStyle')
        runner.font.size = Pt(12)

        companyEmail = doc.add_paragraph()
        companyEmail.paragraph_format.space_after = Pt(0)
        runner = companyEmail.add_run(f"Email: {self.companiesData[0]['Email']}", style ='TextStyle')
        runner.font.size = Pt(12)

        date = datetime.datetime.now()
        meseci = {
            1: 'Januar',
            2: 'Februar',
            3: 'Mart',
            4: 'April',
            5: 'Maj',
            6: 'Jun',
            7: 'Jul',
            8: 'Avgust',
            9: 'Septembar',
            10: 'Oktobar',
            11: 'Novembar',
            12: 'Decembar'
        }

        todaysDate = doc.add_paragraph()
        todaysDate.paragraph_format.space_after = Pt(0)
        runner = todaysDate.add_run(f"Datum: {date.day}-{meseci[date.month]}-{date.year}", style ='TextStyle')
        runner.font.size = Pt(12)

        # Save the document
        doc.save("table.docx")

    def updateCompanyData(self, company):
        self.companiesData = [x for x in getData('data/companies.txt') if x['Ime'] == company]

    def printData(self):
        print(self.optionsCompanies)

    def getFilePath(self):
        file = fd.askdirectory()
        self.invoicePath.set(file)

    def removeProduct(self, product):
        index = [i for i, list in enumerate(self.selectedProducts) if list[0] == product]
        self.selectedProducts[index[0]][4].destroy()
        self.selectedProducts.pop(index[0])

    def insertProduct(self, frame):
        price = None
        if int(self.quantity.get()) != 0:
            if any(x[0] == self.selectedproduct.get() for x in self.selectedProducts):
                index = [i for i, sublist in enumerate(self.selectedProducts) if sublist[0] == self.selectedproduct.get()]
                self.selectedProducts[index[0]][1] += int(self.quantity.get())
                self.selectedProducts[index[0]][3].configure(text=f"{index[0] + 1}: {self.selectedProducts[index[0]][0]} ({self.selectedProducts[index[0]][2]}) {self.selectedProducts[index[0]][1]}")
            else:
                price = next(int(x['Cena'].strip()) for x in self.products if x['Ime'] == self.selectedproduct.get())
                frm = tk.Frame(self.selectedProductsFrame)
                frm.pack(padx=3, fill='both', expand=True)
                lbl = ttk.Label(frm)
                lbl.pack(side='left')
                prdct = self.selectedproduct.get()
                btn = ttk.Button(frm, text="X", width=1, command=lambda: self.removeProduct(prdct))
                btn.pack(side='left')
                product = [self.selectedproduct.get(), int(self.quantity.get()), price, lbl, frm]
                self.selectedProducts.append(product)
                lenght = len(self.selectedProducts) - 1
                lbl.configure(text=f"{lenght + 1}: {self.selectedProducts[lenght][0]} ({self.selectedProducts[lenght][2]}) {self.selectedProducts[lenght][1]}")

    def renderDialog(self):
        #getting companies data from text file

        #creating companies frame and generating dropdown list for it
        ttk.Label(self.companyFrame, text='Firma:').pack(padx=20, anchor='w')
        companiesDropDown = tk.OptionMenu(self.companyFrame, self.selectedCompany, *self.optionsCompanies, command=self.updateCompanyData)
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

        ttk.Button(self.invoicePathFrame, width=30, text="Folder", command=self.getFilePath).pack(anchor='center')
        tk.Entry(self.invoicePathFrame, textvariable=self.invoicePath, width=35).pack(anchor='center', pady=10)
        ttk.Button(self.invoicePathFrame, width=30, text="Stampaj", command=self.saveDocument).pack(anchor='center')