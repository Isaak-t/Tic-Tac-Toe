import random
from PIL import Image
import tkinter.messagebox
from tkinter import *
from tkinter import messagebox
root = Tk()
root.geometry("300x300")
def getfile ():
    global my_image
    #filename = input("please give a file name")
    my_image = Image.open("cat.jpg")

    #y_image = Image.open(filename)
getfile()


def Myimage():
    rows = my_image.size[0]
    colos = my_image.size[1]
    print (rows,colos)
    px=my_image.load()
    for i in range (0, rows):
        start = random.randint(0, rows)
        end = random.randint(0,colos)
        num = random.randint(1,5)
        if i % 2 == 0:
            start=0
        else:
            start = i

    for j in range (start,colos, num):
        red = random.randint(0,0)
        green = random.randint(255,255)
        blue = random.randint(0,0)
        px[i,j] = (red,blue,green)
    my_image.show()
Myimage()

glitchbutton = Button(root, text="glitch", command=Myimage)
glitchbutton.grid(row=1, column=1)
redslider = Scale(root,from_=0, to_=255, orient=HORIZONTAL)
redslider.grid(row=1, column=1)
greenslider = Scale(root,from_=0, to_=255, orient=HORIZONTAL)
greenslider.grid(row=2, column=1)
blueslider = Scale(root,from_=0, to_=255, orient=HORIZONTAL)
blueslider.grid(row=3, column=1)
#myimage = Image.open("Pizza.jpg")
print (greenslider.get())

root.mainloop()

