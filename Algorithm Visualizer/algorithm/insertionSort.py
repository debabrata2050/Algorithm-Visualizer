from time import sleep
colorData=[]

def InsertionSort(data, drawData,stepTime):

    colorData=['#5b84c4' for x in range(len(data))]
    for i in range(1,len(data)):
        key=data[i]
        j=i-1

        colorData[i]='orange'
        drawData(data,colorData)
        sleep(stepTime)
        
        while j>=0 and data[j]>key:

            colorData[j]='white'
            drawData(data,colorData)
            sleep(stepTime)
            colorData[j]='#5b84c4'

            data[j+1]=data[j]
            j-=1

        data[j+1]=key

        colorData[j+1]='#f0756c'
        drawData(data,colorData)
        sleep(stepTime)
        colorData[j+1]='#5b84c4'
        colorData[i]='#5b84c4'

    colorData=['green' for x in range(len(data))]
    drawData(data,colorData)

