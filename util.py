import pickle

def getNextInvoiceNumber(invoicenums) -> max([1, 2, 3]):
    invoicenums = [int(x) for x in invoicenums]
    return invoicenums[len(invoicenums) - 1] + 1

def readData(filename):
    with open(filename, 'rb') as frb:
       return pickle.load(frb)

def updateCompanyinfo(data):
    with open('data/companies.pickle', 'wb') as fwb:
        pickle.dump(data, fwb)

def updateFinancialData(data):
    with open('data/financialdata.ottoshop', 'wb') as fwb:
        pickle.dump(data, fwb)

def updateData(fileName: str, data):
    with open(fileName, 'wb') as fwb:
        pickle.dump(data, fwb)