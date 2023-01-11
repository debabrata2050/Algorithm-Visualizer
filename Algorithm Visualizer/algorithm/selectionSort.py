from time import sleep
colorData=[]

def SelectionSort(data, drawData,stepTime):

    colorData=['#5b84c4' for x in range(len(data))]
    for i in range(len(data)):
        min=data[i]
        min_index=i
        colorData[i]='orange'
        for j in range(i+1,len(data)):
            colorData[j]='white'
            drawData(data,colorData)
            colorData[j]='#5b84c4'
            sleep(stepTime)
            if data[j]<min:
                colorData[min_index]='#5b84c4'
                min=data[j]
                min_index=j
                colorData[j]='orange'
                if j!=len(data)-1:
                    colorData[j+1]='white'
                drawData(data,colorData)
                # colorData[j]='blue'
                sleep(stepTime)
        data[min_index],data[i]=data[i],data[min_index]
        colorData[i+1:]=['#5b84c4' for x in range(i+1,len(data))]
        colorData[i]='green'
        drawData(data,colorData)
        sleep(stepTime)