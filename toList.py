def txtToDict(fileName):
    with open ('creatures.txt') as data:
        dataRaw = data.readlines()
    #Data to Dict
    dataDict = {}
    dataListTemp=[]
    for i in range(len(dataRaw)):
        dataListTemp.append(dataRaw[i][:-1])
        if dataRaw[i] == '\n' or '':
            #first = key second = value
            dataDict.update({dataListTemp[0]:[dataListTemp[1]]})
            #start work from third to end of dict list
            for i in range(len(dataListTemp[2:])):
                dataDict[dataListTemp[0]].append(dataListTemp[2:][i])
            dataDict[dataListTemp[0]].pop()
            dataListTemp=[]
    return dataDict

def createFolderStructure():
#create folders with value name inside each key automatically creates KEYS folders!
    for key in list(data.keys()):
        for value in data[key]:
            path = ('structure/{}/'.format(key))
            os.makedirs(path + value)