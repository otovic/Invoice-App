def getData(fileName) -> [{}]:
    with open(fileName, 'r') as fr:
        dataArray = []
        dataLines = fr.readlines()
        for data in dataLines:
            data = data.split(':')
            receiver = dict()
            for key in data:
                currentKey = key.split('|')
                receiver.setdefault(currentKey[0], currentKey[1])
            dataArray.append(receiver)
        return dataArray

#this function reads invoice numbers from text file 
# and finds the last one so it can be used for the next invoice
def getInvoices() -> max([1, 2, 3]):
    numbers = []
    with open('./data/invoices.txt', 'r') as fr:
        dataLines = fr.readlines()
        for data in dataLines:
            data = data.split(':')
            for num in data:
                numbers.append(num)
    return max(numbers)

def getInvoicePath():
    with open('data/invoicepath.txt', 'r') as fr:
        data = fr.readlines()
