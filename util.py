def getData(fileName) -> [{}]:
    with open(fileName, 'r') as fr:
        receivers = []
        dataLines = fr.readlines()
        for data in dataLines:
            data = data.split(':')
            receiver = dict()
            for key in data:
                currentKey = key.split('/')
                receiver.setdefault(currentKey[0], currentKey[1])
            receivers.append(receiver)
        return receivers