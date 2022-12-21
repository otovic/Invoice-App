import tkinter as tk
from tkinter import ttk
from invoice import invoiceDialog

invoiceDialogObj = None

def showInvoiceDialog():
    global invoiceDialogObj
    invoiceDialogObj = invoiceDialog(rootApp)
    invoiceDialogObj.renderDialog()

def test():
    print(p)

def closeApp():
    rootApp.quit()                                                               

#create root app (window)
rootApp = tk.Tk()
rootApp.title("Ottoshop")
rootApp.geometry("300x355")

#change window icon
icon = tk.PhotoImage(file='./content/logo.png')
rootApp.wm_iconphoto(True, icon)

#create each button on starting form
ttk.Button(rootApp, text='Fakturisanje', command=showInvoiceDialog, width=20).pack(padx=30, pady=10)
ttk.Button(rootApp, text='Bar Kodovi', command=test, width=20).pack(padx=30, pady=10)
ttk.Button(rootApp, text='Etikete', command=showInvoiceDialog, width=20).pack(padx=30, pady=10)
ttk.Button(rootApp, text='Dodaj Firmu', command=showInvoiceDialog, width=20).pack(padx=30, pady=10)
ttk.Button(rootApp, text='Dodaj Proizvod', command=showInvoiceDialog, width=20).pack(padx=30, pady=10)
ttk.Button(rootApp, text='Izmeni Proizvod', command=closeApp, width=20).pack(padx=30, pady=10)
ttk.Button(rootApp, text='Izadji', command=closeApp, width=10).pack(padx=30, pady=30)

#initiate main form
rootApp.mainloop()

# import tkinter as tk

# # Create the main window
# window1 = tk.Tk()
# window1.title("Window 1")

# # Create a button to open window 2
# button = tk.Button(window1, text="Open Window 2", command=lambda: open_window2())
# button.pack()

# # Create window 2
# window2 = tk.Toplevel(window1)
# window2.title("Window 2")

# # Create a button to close window 2 and open window 1
# button = tk.Button(window2, text="Close Window 2", command=lambda: close_window2())
# button.pack()

# def open_window2():
#     # Hide window 1 and show window 2
#     window1.withdraw()
#     window2.deiconify()

# def close_window2():
#     # Hide window 2 and show window 1
#     window2.withdraw()
#     window1.deiconify()

# window1.mainloop()


# import sys
# import docx
# from PyQt5.QtPrintSupport import QPrinter, QPrintDialog
# from PyQt5.QtWidgets import QApplication

# # Create a QCoreApplication object
# app = QApplication.instance()
# if not app:
#     app = QApplication(sys.argv)

# # Open the DOCX file
# document = docx.Document('test.docx')

# # Create a QPrinter object
# printer = QPrinter()

# # Open the print dialog
# print_dialog = QPrintDialog(printer)
# if print_dialog.exec_() == QPrintDialog.Accepted:
#     # If the user clicks "Print", print the document
#     document.print(printer)