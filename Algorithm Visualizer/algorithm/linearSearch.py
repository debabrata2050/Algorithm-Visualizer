from time import sleep
from random import randrange
colorData=[]

def LinearSearch(data, drawData,stepTime):
    index=randrange(0,len(data))
    colorData=['#5b84c4' for x in range(len(data))]
    for x in range(len(data)):
        if data[x]==data[index]:
            colorData[x]='orange'
            break
    for i in range(len(data)):
        colorData[i]='white'
        drawData(data,colorData)
        sleep(stepTime)
        if data[i]==data[index]:
            colorData[i]='green'
            drawData(data,colorData)
            sleep(stepTime)
            break
        else:
            colorData[i]='#f0756c'
            sleep(stepTime)