import sys
from tkinter import *
from tkinter import ttk
import random
import tkinter

# importing our desired algorithms from the algorithms folder
from algorithm.linearSearch import LinearSearch
from algorithm.binarySearch import BinarySearch
from algorithm.bubbleSort import BubbleSort
from algorithm.insertionSort import InsertionSort
from algorithm.selectionSort import SelectionSort
from algorithm.mergeSort import MergeSort
from algorithm.quickSort import QuickSort

root = Tk()
root.geometry('900x500')
root.title("Algorithm Visualizer")
root.resizable(0,0)
photo = tkinter.PhotoImage(file = 'fabicon.png')
root.wm_iconphoto(False, photo)

global sizeStart, sizeEnd
sizeStart, sizeEnd = 3, 60

#to store the array/heights of rectangle
data = []
#to store the colour of respective rectangles
colorData = []

#to start visualization
def visualize(algorithm,stepTime):
    stepTime/=10

    if algorithm=="Bubble Sort":
        BubbleSort(data,drawData,stepTime)
    elif algorithm=="Linear Search":
        LinearSearch(data,drawData,stepTime)
    elif algorithm=="Binary Search":
        BinarySearch(data,drawData,stepTime)
    elif algorithm=="Merge Sort":
        MergeSort(data,drawData,stepTime)
    elif algorithm=="Selection Sort":
        SelectionSort(data,drawData,stepTime)
    elif algorithm=="Insertion Sort":
        InsertionSort(data,drawData,stepTime)
    elif algorithm=="Quick Sort":
        QuickSort(data,drawData,stepTime)
    elif algorithm=="Radix Sort":
        MergeSort(data,drawData,stepTime)
    elif algorithm=="Heap Sort":
        MergeSort(data,drawData,stepTime)

def random_Data():
    setVal = random.randint(sizeStart,sizeEnd)
    sizeBar.set(setVal)
    genData(setVal)

def dispDelay(delay):
    speedl.config(text=str(format(float(delay)/10, ">03.1f")+" sec"))
    
#function to generate random data for visualization
def genData(data_size):
    global data, colorData
    data=colorData=[]

    minVal, maxVal = 5, 100

    #set initial color of elements
    colorData=['#5b84c4' for x in range(int(float(data_size)))]
    for _ in range(int(float(data_size))):
        data.append(random.randrange(minVal,maxVal))

    #draw the elemets on canvas
    drawData(data,colorData)
    sizel.config(text=str(int(float(data_size))))

# Function to Draw Bar Graph : 'data' is a list of Bar heights and 'colorData' is the respective colors
def drawData(data,colorData):
    
    #clears canvas before drawing new data
    canvas.delete("all")

    c_height = 300
    c_width = 900

    barC = len(data)
    
    # Spacing between 2 Bar
    offset = 2

    c_barheight = c_height - 10

    space = (c_width - ((barC+1) * offset)) / barC 
   
    #normalizing the data

    normalizedData = [ i / max(data) for i in data]
    
    # Drawing the normalized data
    for i, height in enumerate(normalizedData):
        #Top Right
        x0 = offset if i==0 else x1 + offset
        y0 = c_height - height * (c_height-40)

        #Bottom Right
        x1 = x0 + space
        y1 = c_barheight

        canvas.create_rectangle(x0,y0,x1,y1, fill=colorData[i])
        canvas.create_text(x0+2, y0, anchor=SW, text=str(data[i]),font=('Helvetica',8))

    canvas.create_line(0, y1, c_width, y1)
    root.update_idletasks()

#-----------------------------------------------------------------------------------------------------------------------------------------------#
# Main Frame
#-----------------------------------------------------------------------------------------------------------------------------------------------#
def main():
    global width,height
    width=1100
    height=610

    frame3=Frame(root,width=width,height=height)
    frame3.pack()

    titlef=Frame(root,width=width,height=height)
    titlef.pack()

    frame2=Frame(root,width=width,height=height)
    frame2.pack()

    c_width, c_height = 900, 300
    fontSize = 16

    sizec=Label(titlef,text="Size:",font=('Helvetica',fontSize,))
    sizec.pack(side=LEFT)

    global sizel, speedl
    sizel=Label(titlef,text="50",font=('Helvetica',fontSize,'bold'))
    sizel.pack(side=LEFT,padx=(0,200))

    global size, speed
    size = IntVar()
    speed = IntVar()

    global sizeBar
    sizeBar = ttk.Scale(titlef, variable = size, from_ = sizeStart, to = sizeEnd, length = 300, command=genData)
    sizeBar.pack()
    size.set(15)

    speedc=Label(frame2,text="Delay:",font=('Helvetica',fontSize,))
    speedc.pack(side=LEFT)

    speedl=Label(frame2,text="0.0 sec",font=('Helvetica',fontSize,'bold'))
    speedl.pack(side=LEFT,padx=(0,130))

    speedBar = ttk.Scale(frame2, variable = speed, from_ = 0, to = 10, length = 300, command=dispDelay)
    speedBar.pack()

    algol=Label(frame3,text="Select Algorithm:",font=('Helvetica',fontSize,))
    algol.grid(row=0,column=0,padx=(0,200))

    algorithm=StringVar()
    algorithm_menu=ttk.Combobox(frame3,textvariable=algorithm,state='readonly',values=['Linear Search','Binary Search','Bubble Sort','Selection Sort','Insertion Sort','Merge Sort','Quick Sort','Radix Sort'])
    algorithm_menu.grid(row=0,column=2)
    algorithm_menu.current(0)

    global canvas
    canvas = Canvas(root, width=c_width, height=c_height)
    canvas.pack()

    # Button to Visualize
    b1_Button = Button(root, text="Generate", font=('Helvetica',20,'bold'), command=lambda : visualize(algorithm.get(),speed.get()), padx=50,  bg="#f0756c", fg="white")
    b1_Button.pack(side=LEFT)

    b2_Button = Button(root, text="Random", font=('Helvetica',20,'bold'), command=random_Data, padx=50,  bg="#f0756c", fg="white")
    b2_Button.pack(side=RIGHT)

    genData(20)

    root.mainloop()

if __name__ == "__main__":
    main()
