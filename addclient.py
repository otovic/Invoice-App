from util import readData, updateData
import tkinter as tk
from tkinter import ttk

class addClientDialog():
    def __init__(self, root) -> None:
        self.data = readData('data/receivers.pickle')
        self.nazivFirme = tk.StringVar()
        self.imeFirme = tk.StringVar()
        self.maticniBrojFirme = tk.StringVar()
        self.gradFirme = tk.StringVar()
        self.ulicaFirme = tk.StringVar()
        self.PIBFirme = tk.StringVar()

        self.addClientWindow = tk.Toplevel(root)
        self.addClientWindow.geometry("300x510")
        self.addClientWindow.title('Dodaj Klijenta - Ottoshop')
        self.container = tk.Frame(self.addClientWindow)
        self.container.pack()
        self.nazivFrame = tk.Frame(self.container)
        self.nazivFrame.pack(pady=10, padx=15, fill='both', expand=True)
        self.imeFrame = tk.Frame(self.container)
        self.imeFrame.pack(pady=10, padx=15, fill='both', expand=True)
        self.maticniFrame = tk.Frame(self.container)
        self.maticniFrame.pack(pady=10, padx=15, fill='both', expand=True)
        self.gradFrame = tk.Frame(self.container)
        self.gradFrame.pack(pady=10, padx=15, fill='both', expand=True)
        self.ulicaFrame = tk.Frame(self.container)
        self.ulicaFrame.pack(pady=10, padx=15, fill='both', expand=True)
        self.PIBFrame = tk.Frame(self.container)
        self.PIBFrame.pack(pady=10, padx=15, fill='both', expand=True)
        self.SubmitFrame = tk.Frame(self.container)
        self.SubmitFrame.pack(pady=10, padx=15, fill='both', expand=True)
    
    def __del__(self):
        print('Otiso sam')

    def Submit(self):
        if self.nazivFirme.get() != '' and self.imeFirme.get() != '' and self.maticniBrojFirme.get() != '' and self.gradFirme.get() != '' and self.ulicaFirme.get() != '' and self.PIBFirme.get() != '':
            self.data.append({
                'Naziv': self.nazivFirme.get(),
                'Ime': self.imeFirme.get(),
                'Maticni': self.maticniBrojFirme.get(),
                'Grad': self.gradFirme.get(),
                'Ulica': self.ulicaFirme.get(),
                'PIB': self.PIBFirme.get()
            })

            updateData('data/receivers.pickle', self.data)
            self.addClientWindow.destroy()
            del self

    def renderDialog(self):
        ttk.Label(self.nazivFrame, text='Naziv Firme:').pack(padx=0, anchor='w')
        tk.Entry(self.nazivFrame, textvariable=self.nazivFirme, width=35).pack(anchor='center', pady=5)

        ttk.Label(self.imeFrame, text='Ime Firme:').pack(padx=0, anchor='w')
        tk.Entry(self.imeFrame, textvariable=self.imeFirme, width=35).pack(anchor='center', pady=5)

        ttk.Label(self.maticniFrame, text='Maticni Broj Firme:').pack(padx=0, anchor='w')
        tk.Entry(self.maticniFrame, textvariable=self.maticniBrojFirme, width=35).pack(anchor='center', pady=5)

        ttk.Label(self.gradFrame, text='Grad Firme:').pack(padx=0, anchor='w')
        tk.Entry(self.gradFrame, textvariable=self.gradFirme, width=35).pack(anchor='center', pady=5)

        ttk.Label(self.ulicaFrame, text='Ulica Firme:').pack(padx=0, anchor='w')
        tk.Entry(self.ulicaFrame, textvariable=self.ulicaFirme, width=35).pack(anchor='center', pady=5)

        ttk.Label(self.PIBFrame, text='PIB Firme:').pack(padx=0, anchor='w')
        tk.Entry(self.PIBFrame, textvariable=self.PIBFirme, width=35).pack(anchor='center', pady=5)

        ttk.Button(self.SubmitFrame, width=30, text="Dodaj", command=self.Submit).pack(anchor='center')