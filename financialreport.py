from util import readData
import tkinter as tk
from tkinter import ttk
import matplotlib.pyplot as plt

class FinancialDialog():
    def __init__(self, root) -> None:
        #get financial data from file
        self.financialData = readData('data/financialdata.ottoshop')

        #get only names of the companies
        self.companiesNames = [x for x in self.financialData.keys()]

        #set selected company
        self.selectedCompany = tk.StringVar()
        self.selectedCompany.set(self.companiesNames[0])

        #get only years
        self.years = [x for x in self.financialData[self.selectedCompany.get()].keys()]
        self.selectedYear = tk.StringVar()
        self.selectedYear.set(self.years[0])

        self.totalRevenue = sum([sum(x) for x in self.financialData[self.selectedCompany.get()][int(self.selectedYear.get())].values()])
        self.totalRevenue = f'{self.totalRevenue:,.2f} RSD'.replace(',', ' ')

        self.financialWindow = tk.Toplevel(root)
        self.financialWindow.title('Finansijski Izvestaj - Ottoshop')
        self.container = tk.Frame(self.financialWindow)
        self.container.pack()
        self.companyFrame = tk.Frame(self.container)
        self.companyFrame.pack(pady=10, fill='both', expand=True)
        self.yearsFrame = tk.Frame(self.container)
        self.yearsFrame.pack(pady=10, fill='both', expand=True)
        self.totalRevenueFrame = tk.Frame(self.container)
        self.totalRevenueFrame.pack(pady=10, fill='both', expand=True)
        self.showChartFrame = tk.Frame(self.container)
        self.showChartFrame.pack(pady=10, fill='both', expand=True)
        self.lbl = 'p'

    def updateSelectedCompany(self, company):
        self.selectedCompany.set(company)
        self.years = [x for x in self.financialData[self.selectedCompany.get()].keys()]

    def updateSelectedYear(self, year):
        self.selectedYear.set(year)
        self.totalRevenue = sum([sum(x) for x in self.financialData[self.selectedCompany.get()][int(self.selectedYear.get())].values()])
        self.totalRevenue = f'{self.totalRevenue:,.2f} RSD'.replace(',', ' ')
        self.lbl.configure(text=f"Ukupan promet: {self.totalRevenue}")

    def showChart(self):
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
        xosa = [meseci[x] for x in self.financialData[self.selectedCompany.get()][int(self.selectedYear.get())].keys()]
        yosa = [sum(x) for x in self.financialData[self.selectedCompany.get()][int(self.selectedYear.get())].values()]

        fig, a = plt.subplots()
        fig.set_size_inches(15, 5)
        a.bar(xosa, yosa)

        plt.title(f"Ukupan promet po mesecima za godinu {self.selectedYear.get()}")
        plt.xlabel("Meseci")
        plt.ylabel("Ukupan Promet")

        plt.show()

    def showDialog(self):
        ttk.Label(self.companyFrame, text='Firma:').pack(padx=20, anchor='w')
        companiesDropDown = tk.OptionMenu(self.companyFrame, self.selectedCompany, *self.companiesNames, command=self.updateSelectedCompany)
        companiesDropDown.configure(width=30)
        companiesDropDown.pack(padx=20, anchor="w")

        ttk.Label(self.yearsFrame, text='Godina:').pack(padx=20, anchor='w')
        yearsDropDown = tk.OptionMenu(self.yearsFrame, self.selectedYear, *self.years, command=self.updateSelectedYear)
        yearsDropDown.configure(width=30)
        yearsDropDown.pack(padx=20, anchor="w")
        lbl = ttk.Label(self.totalRevenueFrame, text=f"Ukupan promet: {self.totalRevenue}")
        lbl.pack()
        self.lbl = lbl

        ttk.Button(self.showChartFrame, width=30, text="Graficki Prikaz", command=self.showChart).pack(anchor='center')