# A very simple Invoice App made with Python.
This is a simple desktop application that uses Python's tkinter library to construct GUI.

# Before you can use this code you need to install few modules:
1. Office Word module, to work with docx files - pip install python-docx
2. Docx to pdf module to convert docx files to pdf files - pip install docx2pdf
3. Matplotlib module for showing financial data graphs - pip install matplotlib

# What can be done with this app:
1. Create Invoices - Select the company that is sending the package, select receiver, product and ammount and then click print. The app will fill all the data of the 
company and receiver, create a table with products and prices calculated and generate a docx file. Then your default pdf viewer will open with the invoice and all you 
need to do is print it.

2. Financial Report - In this section you can check your financial data for selected year and company. It will show you your total revenue for the year and also you can
check revenue by each month in a year with a graph.

3. Print Bar Codes - You can select a path to bar code and select the ammount you want to print. After that you will get a printing dialog with bar codes arranged for
printing. NOTE: This is designed for clothing company, so you will see labels with clothing sizes such as S, M etc. but you can choose any bar code and print it.

4. Print Declarations - This section is for printing clothing declarations such as information about a product, country of origin etc. You can also print anything else.

5. Add company - Add your company along with its info. It will be available to choose when se;ecting company that is issuing an invoice.

6. Add client - Simple section where you can add a client that will be available to choose when issuing an invoice.

7. Add product - here you can add a product that you can be later added to invoice along with the ammount you enter.

9. Change product - Change info about product thats already added

This is all the functionality in the app.

# NOTE: 
I still need to polish this app, all the functionality works but there are few tweaks left i need to do. The app is also on Serbian language.
