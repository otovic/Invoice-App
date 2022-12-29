# def getData(fileName) -> [{}]:
#     with open(fileName, 'r') as fr:
#         dataArray = []
#         dataLines = fr.readlines()
#         for data in dataLines:
#             data = data.split(';')
#             receiver = dict()
#             for key in data:
#                 currentKey = key.split('|')
#                 receiver.setdefault(currentKey[0], currentKey[1])
#             dataArray.append(receiver)
#         print(dataArray)
#         return dataArray

#this function reads invoice numbers from text file 
# and finds the last one so it can be used for the next invoice
import pickle

def getNextInvoiceNumber(invoicenums) -> max([1, 2, 3]):
    invoicenums = [int(x) for x in invoicenums]
    return invoicenums[len(invoicenums) - 1] + 1

def readData(filename):
    with open(filename, 'rb') as frb:
       return pickle.load(frb)

readData('data/financialdata.ottoshop')
companies = [{
    'Ime': 'OTTO-DIVISION',
    'Maticni': '64807234',
    'Adresa': 'Stevana Sremca 19/32',
    'Grad': 'Nis',
    'Email': 'ottosrbija@gmail.com',
    'Delatnost': '1413',
    'PIB': '110319347',
    'Path': '',
    'Account': '200-2910030101002-39',
    'Invoices': {2022: []}
}]

def updateCompanyinfo(data):
    with open('data/companies.pickle', 'wb') as fwb:
        pickle.dump(data, fwb)

def updateFinancialData(data):
    with open('data/financialdata.ottoshop', 'wb') as fwb:
        pickle.dump(data, fwb)
finances = {
    
}

def updateData(fileName: str, data):
    with open(fileName, 'wb') as fwb:
        pickle.dump(data, fwb)

def writeCompanyPath(data):
    allcompanies = getData('data/companies.txt')
    for x in allcompanies:
        if x['Ime'] not in [a['Ime'] for a in data]:
            data.append(x)
    with open("data/companies.txt", "w") as fw:
        for x in data:
            fw.write(f"Ime|{x['Ime']};Maticni|{x['Maticni']};Adresa|{x['Adresa']};Grad|{x['Grad']};Email|{x['Email']};Delatnost|{x['Delatnost']};PIB|{x['PIB']};path|{x['path']};Account|{x['Account']};invnum|{x['invnum']}")