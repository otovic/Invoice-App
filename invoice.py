import tkinter as tk
from tkinter import ttk
from util import getData

def renderInvoiceDialog(root):
    invoiceDialog = tk.Toplevel(root)

    receivers = getData('./data/receivers.txt')
    optionsReceivers = [x['Naziv'] for x in receivers]
    selectedReceiver = tk.StringVar(invoiceDialog)
    selectedReceiver.set(optionsReceivers[0])

    companies = getData('./data/companies.txt')
    optionsCompanies = [x['Ime'] for x in companies]
    selectedCompany = tk.StringVar(invoiceDialog)
    selectedCompany.set(optionsCompanies[0])

    container = tk.Frame(invoiceDialog)
    container.pack()

    company = tk.Frame(container)
    company.pack(pady=10, fill='both', expand=True)
    ttk.Label(company, text='Firma:').pack(padx=20, anchor='w')
    dropDown = tk.OptionMenu(company, selectedCompany, *optionsCompanies)
    dropDown.configure(width=30)
    dropDown.pack(padx=20, anchor="w")

    frame = tk.Frame(container)
    frame.pack(pady=10)

    ttk.Label(frame, text='Primalac:').pack(padx=20, anchor='w')
    dropDown = tk.OptionMenu(frame, selectedReceiver, *optionsReceivers)
    dropDown.configure(width=30)
    dropDown.pack(padx=20, anchor="w")