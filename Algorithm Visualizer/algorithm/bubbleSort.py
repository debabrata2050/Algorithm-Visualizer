from time import sleep
colorData=[]

def BubbleSort(data, drawData,stepTime):

    colorData=['#5b84c4' for x in range(len(data))]
    for i in range(len(data)-1):
        for j in range(len(data)-i-1):
            colorData[j]=colorData[j+1]='white'
            drawData(data,colorData)
            colorData[j]=colorData[j+1]='#5b84c4'
            sleep(stepTime)
            if data[j]>data[j+1]:
                data[j],data[j+1]=data[j+1],data[j]
                colorData[j]=colorData[j+1]='#f0756c'
                drawData(data,colorData)
                colorData[j]=colorData[j+1]='#5b84c4'
                sleep(stepTime)
        colorData[len(data)-1-i]='green'
        drawData(data,colorData)
    colorData[0]='green'
    drawData(data,colorData)