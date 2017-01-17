from sense_hat import SenseHat
import tkinter as tk

sense = SenseHat()
sense.set_rotation(270) #changes row graphing to column
go = False
#readingHistory = [] #can kep detailed record of each reading

###used to print on color-grid
'''rows0-7 are y axis arrays of each graph point along the x axis
the sub arrays are [red,green,blue]'''
row0 = [[0,0,0],[0,0,0],[0,0,0],[0,0,0],[0,0,0],[0,0,0],[0,0,0],[0,0,0]]
row1 = [[0,0,0],[0,0,0],[0,0,0],[0,0,0],[0,0,0],[0,0,0],[0,0,0],[0,0,0]]
row2 = [[0,0,0],[0,0,0],[0,0,0],[0,0,0],[0,0,0],[0,0,0],[0,0,0],[0,0,0]]
row3 = [[0,0,0],[0,0,0],[0,0,0],[0,0,0],[0,0,0],[0,0,0],[0,0,0],[0,0,0]]
row4 = [[0,0,0],[0,0,0],[0,0,0],[0,0,0],[0,0,0],[0,0,0],[0,0,0],[0,0,0]]
row5 = [[0,0,0],[0,0,0],[0,0,0],[0,0,0],[0,0,0],[0,0,0],[0,0,0],[0,0,0]]
row6 = [[0,0,0],[0,0,0],[0,0,0],[0,0,0],[0,0,0],[0,0,0],[0,0,0],[0,0,0]]
row7 = [[0,0,0],[0,0,0],[0,0,0],[0,0,0],[0,0,0],[0,0,0],[0,0,0],[0,0,0]]
###


###function to graph humidity
def graphLastReading(h):
    #must use global keyword so python doesnt make new fucking local variables
    global row0,row1,row2,row3,row4,row5,row6,row7
    #moves previous readings back 1 before overwriting them, creating a visual memory
    row0 = row1
    row1 = row2
    row2 = row3
    row3 = row4
    row4 = row5
    row5 = row6
    row6 = row7

    #change humidity ranges by changing values compred to h in the if statements
    if (h > 30): #7 very high
        row7 = [[0,200,0],[20,180,0],[30,170,0],[50,150,0],
                [100,100,0],[120,80,0],[140,50,0],[190,10,0]]
        print('humidity above normal ranges: ' + str(h))
    elif (h > 29): #6
        row7 = [[0,200,0],[20,180,0],[30,170,0],[50,150,0],
                [100,100,0],[120,80,0],[140,50,0],[0,0,0]]
        print('reading ' + str(h))
    elif (h > 28): #5
        row7 = [[0,200,0],[20,180,0],[30,170,0],[50,150,0],
                [100,100,0],[120,80,0],[0,0,0],[0,0,0]]
        print('reading ' + str(h))
    elif (h > 27): #4 middle high
        row7 = [[0,200,0],[20,180,0],[30,170,0],[50,150,0],
                [100,100,0],[0,0,0],[0,0,0],[0,0,0]]
        print('reading ' + str(h))
    elif (h > 26): #3 middle low
        row7 = [[0,200,0],[20,180,0],[30,170,0],[50,150,0],
                [0,0,0],[0,0,0],[0,0,0],[0,0,0]]
        print('reading ' + str(h))
    elif (h > 16): #2
        row7 = [[0,200,0],[20,180,0],[30,170,0],[0,0,0],
                [0,0,0],[0,0,0],[0,0,0],[0,0,0]]
        print('reading ' + str(h))
    elif (h > 15): #1
        row7 = [[0,200,0],[20,180,0],[0,0,0],[0,0,0],
                [0,0,0],[0,0,0],[0,0,0],[0,0,0]]
        print('reading ' + str(h))
    elif (h > 14): #0 very low
        row7 = [[0,200,0],[0,0,0],[0,0,0],[0,0,0],
                [0,0,0],[0,0,0],[0,0,0],[0,0,0]]
        print('reading ' + str(h))
    elif (h <= 14): #far below norm
        row7 = [[0,0,200],[0,0,0],[0,0,0],[0,0,0],
                [0,0,0],[0,0,0],[0,0,0],[0,0,0]]
        print('humidity below normal ranges: ' + str(h))
    else: #error message
        row7 = [[200,0,0],[0,0,0],[0,0,0],[0,0,0],
                [0,0,0],[0,0,0],[0,0,0],[200,0,0]]
        print('error, humidity ' + str(h))
###

 
###loop to read humidity
def readHum():
    global go, image, top

    if (go):
        hum = sense.get_humidity()
        #readingHistory.append(hum) #see lines 21-22
        graphLastReading(hum)

        #repaints the graph images each loop
        image = [row0[0],row0[1],row0[2],row0[3],row0[4],row0[5],row0[6],row0[7],
                 row1[0],row1[1],row1[2],row1[3],row1[4],row1[5],row1[6],row1[7],
                 row2[0],row2[1],row2[2],row2[3],row2[4],row2[5],row2[6],row2[7],
                 row3[0],row3[1],row3[2],row3[3],row3[4],row3[5],row3[6],row3[7],
                 row4[0],row4[1],row4[2],row4[3],row4[4],row4[5],row4[6],row4[7],
                 row5[0],row5[1],row5[2],row5[3],row5[4],row5[5],row5[6],row5[7],
                 row6[0],row6[1],row6[2],row6[3],row6[4],row6[5],row6[6],row6[7],
                 row7[0],row7[1],row7[2],row7[3],row7[4],row7[5],row7[6],row7[7]]
        sense.set_pixels(image)
        top.after(3000, readHum)
'''time in mili-seconds betwen each new reading
the tkinter documentation states calling the function inside itself is the
best way to achieve a while loop without breaking the gui window'''
###


### tkinter gui window
top = tk.Tk() #sets top window
top.geometry("500x500+0+0") #size and position
top.title("Humidity Sensor")

def senseToggle():
    global go
    if (go == True):
        go = False
        humButton["text"] = "Start"
    elif (go == False):
        go = True
        readHum()
        humButton["text"] = "Stop"

humButton = tk.Button(top, text = "Start", command = senseToggle, height = 1, width = 2)
humButton.grid(row = 0)

#display box is breaking/hiding humbutton. and no lobel shown
displayBox = tk.LabelFrame(top, text = "Display Options", height = 400, width = 200,
                           padx = 20, pady = 20)

clearButton = tk.Button(top, text = "Clear Display", command = sense.clear, height = 1, width = 8)
clearButton.grid(row = 0)

top.mainloop() #nothing else can run after this call
###
