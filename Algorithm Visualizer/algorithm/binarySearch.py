from time import sleep
from random import randrange
colorData=[]

def BinarySearch(data,drawData,stepTime):
    data = sorted(data)
    index= randrange(0,len(data))
    colorData=['#5b84c4' for x in range(len(data))]
    colorData[index]='orange'
    
    start=0
    end=len(data)-1

    while start<end:
        mid = int((start+end)/2)
        drawData(data,colorData)
        sleep(stepTime)
        if data[index]>data[mid]:
            colorData[start:mid+1]=['#f0756c' for x in range(mid-start+1)]
            drawData(data,colorData)
            sleep(stepTime)
            start=mid+1
        elif data[index]<data[mid]:
            colorData[mid:end+1]=['#f0756c' for x in range(end-mid+1)]
            drawData(data,colorData)
            sleep(stepTime)
            end=mid-1
        else:
            break
    colorData[index]='green'
    drawData(data,colorData)
    sleep(stepTime)