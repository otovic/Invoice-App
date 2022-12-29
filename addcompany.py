import tkinter as tk
from tkinter import ttk
from util import readData, updateCompanyinfo

class addCompanyDialog():
    def __init__(self, root) -> None:
        self.data = readData('data/companies.pickle')
        self.companyName = tk.StringVar()
        self.maticniBroj = tk.StringVar()
        self.companyAdress = tk.StringVar()
        self.city = tk.StringVar()
        self.email = tk.StringVar()
        self.delatnost = tk.StringVar()
        self.PIB = tk.StringVar()
        self.racun = tk.StringVar()

        self.addCompanyWindow = tk.Toplevel(root)
        self.addCompanyWindow.geometry("300x450")
        self.addCompanyWindow.title('Dodaj Firmu - Ottoshop')
        self.container = tk.Frame(self.addCompanyWindow)
        self.container.pack()
        self.companyNameFrame = tk.Frame(self.container)
        self.companyNameFrame.pack(pady=10, padx=15, fill='both', expand=True)
        self.maticniBrojFrame = tk.Frame(self.container)
        self.maticniBrojFrame.pack(pady=0, padx=15, fill='both', expand=True)
        self.adressFrame = tk.Frame(self.container)
        self.adressFrame.pack(pady=0, padx=15, fill='both', expand=True)
        self.cityFrame = tk.Frame(self.container)
        self.cityFrame.pack(pady=0, padx=15, fill='both', expand=True)
        self.emailFrame = tk.Frame(self.container)
        self.emailFrame.pack(pady=00, padx=15, fill='both', expand=True)
        self.delatnostFrame = tk.Frame(self.container)
        self.delatnostFrame.pack(pady=00, padx=15, fill='both', expand=True)
        self.PIBFrame = tk.Frame(self.container)
        self.PIBFrame.pack(pady=0, padx=15, fill='both', expand=True)
        self.bankAccountFrame= tk.Frame(self.container)
        self.bankAccountFrame.pack(pady=0, padx=15, fill='both', expand=True)
        self.submitFrame= tk.Frame(self.container)
        self.submitFrame.pack(pady=0, padx=15, fill='both', expand=True)

    def pro(self):
        print(self.data)
    
    def Submit(self):
        company = {
            'Ime': self.companyName.get(),
            'Maticni': self.maticniBroj.get(),
            'Adresa': self.companyAdress.get(),
            'Grad': self.city.get(),
            'Email': self.email.get(),
            'Delatnost': self.delatnost.get(),
            'PIB': self.PIB.get(),
            'Path': '',
            'Account': self.racun.get(),
            'Invoices': {}
        }
        self.data.append(company)
        updateCompanyinfo(self.data)

    def showAddCompanyDialog(self):
        ttk.Label(self.companyNameFrame, text='Ime Firme:').pack(padx=0, anchor='w')
        tk.Entry(self.companyNameFrame, textvariable=self.companyName, width=35).pack(anchor='center', pady=5)

        ttk.Label(self.maticniBrojFrame, text='Maticni Broj:').pack(padx=0, anchor='w')
        tk.Entry(self.maticniBrojFrame, textvariable=self.maticniBroj, width=35).pack(anchor='center', pady=5)

        ttk.Label(self.adressFrame, text='Adresa Firme:').pack(padx=0, anchor='w')
        tk.Entry(self.adressFrame, textvariable=self.companyAdress, width=35).pack(anchor='center', pady=5)

        ttk.Label(self.cityFrame, text='Grad:').pack(padx=0, anchor='w')
        tk.Entry(self.cityFrame, textvariable=self.city, width=35).pack(anchor='center', pady=5)

        ttk.Label(self.emailFrame, text='Email:').pack(padx=0, anchor='w')
        tk.Entry(self.emailFrame, textvariable=self.email, width=35).pack(anchor='center', pady=5)

        ttk.Label(self.delatnostFrame, text='Sifra Delatnosti:').pack(padx=0, anchor='w')
        tk.Entry(self.delatnostFrame, textvariable=self.delatnost, width=35).pack(anchor='center', pady=5)

        ttk.Label(self.PIBFrame, text='PIB:').pack(padx=0, anchor='w')
        tk.Entry(self.PIBFrame, textvariable=self.PIB, width=35).pack(anchor='center', pady=5)

        ttk.Label(self.bankAccountFrame, text='Racun:').pack(padx=0, anchor='w')
        tk.Entry(self.bankAccountFrame, textvariable=self.racun, width=35).pack(anchor='center', pady=5)

        ttk.Button(self.submitFrame, width=30, text="Dodaj", command=self.Submit).pack(anchor='center')