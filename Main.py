import tkinter
from tkinter import *
from tkinter import ttk, Canvas
import random
import winsound
import time
import threading
from BubbleSort import bubbleSort
from QuickSort import quickSort
from MergeSort import mergeSort

window = tkinter.Tk()

data = [] # array that will be sorted

window.title("Algorithm Visualiser") #title at the top of the gui bar


window.geometry("1200x720")
#window.state('zoomed') # sets the gui to go fullscreen
window.config(bg="#3e3d38")

for i in range(1,101):
    data.append(i)

def Shuffle(): #shuffles the items
    random.shuffle(data)
    Visual(data, ["#A79986" for x in range(len(data))])

def Visual(data, colour):  #Takes the data array and adds rectangles to the canvas to display it
    canvas.delete("all") #removes old rectangles

    #Usable size
    Canvas_width = 1190
    Canvas_height = 665
    
    X_width = Canvas_width / (len(data) + 1)
    for i, height in enumerate(data):
        x0 = i * X_width + 10 + 10
        y0 = Canvas_height - height * 6.5
        x1 = (i+1) * X_width
        y1 = Canvas_height
        canvas.create_rectangle(x0, y0, x1, y1, fill = colour[i])
    
    window.update_idletasks()

def RunAlgorithm():
    print("Running Algorithm")
    SelectedAlgorithm = AlgorithmMenu.get()
    if(SelectedAlgorithm == "Bubble Sort"):
        bubbleSort(data, Visual)
    elif(SelectedAlgorithm == "Quick Sort"):
        quickSort(data, 0, len(data)-1, Visual)
    elif(SelectedAlgorithm == "Merge Sort"):
        mergeSort(data, 0, len(data) - 1, Visual)
    
    ResetColour(data, Visual)

    
def ResetColour(data, visual):
    time.sleep(1)
    for i in range(len(data)):
       winsound.Beep((((i)*2) + i*10 + 100), 20)
       visual(data, ['#A79986' if x == i else '#803E2F' for x in range(len(data))])   
    time.sleep(0.2)
    winsound.Beep((3000), 50)
    visual(data, ['#A79986' for x in range(len(data))])
    
def Close():
    exit()

#Gui Components
AlgorithmLabel = Label(window, text= "Algorithm: ", font=("Comfortaa", 20, "bold"), bg = "#a79986", relief=GROOVE)
AlgorithmLabel.grid(row=1, column=0)

AlgorithmMenu = ttk.Combobox(window, state="readonly", width = 15, font=("Comfortaa", 20, "bold"), values = ["Bubble Sort", "Merge Sort", "Quick Sort"])
AlgorithmMenu.grid(row=1, column=2)
AlgorithmMenu.current(0)

ShuffleItems = Button(window, text="Shuffle", width = 8, font=("Comfortaa", 15, "bold"), bg = "#a79986", relief=GROOVE, activebackground= "#803e2f", command=Shuffle)
ShuffleItems.grid(row=1, column= 3)

Run = Button(window, text="Run",width = 8, font=("Comfortaa", 15, "bold"), bg = "#a79986", relief=GROOVE, activebackground= "#803e2f", command= RunAlgorithm)
Run.grid(row=1, column=4)

Close = Button(window, text="Close",width = 8, font=("Comfortaa", 15, "bold"), bg = "#a79986", relief=GROOVE, activebackground= "#803e2f", command=Close)
Close.grid(row=1, column=970)

canvas = Canvas(window, width=1190, height= 665, bg="#1f1d20", highlightbackground="Black") #canvas had to be on top cause it wanted to cause mega issues
canvas.grid(row=2, column=0, columnspan= 1000)

Visual(data, ["#A79986" for x in range(len(data))])

window.mainloop() #runs the gui