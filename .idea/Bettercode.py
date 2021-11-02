import tkinter as tk
from tkinter import ttk
from tkinter import filedialog as fd
import random
from tkinter import*
from PIL import Image


# create the root window
root = tk.Tk()
root.geometry('300x150')

# comment this function
'''
def get_file():
    global my_image
    filename = input("please give a file name ")
    my_image = Image.open(filename)
'''


# add this function to your code
def select_files():
    filetypes = (('image files', '*.jpg *.png'), ('All files', '*.*'))
    filename = fd.askopenfilename(title='Open files', initialdir='/', filetypes=filetypes)
    my_image = Image.open(filename)
    # change this call to your function name
    loop_img(my_image)
    # change this call to your function name


# add the parameter my_image to your function
def loop_img(my_image):
    # random_int = random.randint(0,10)
    # my_image = Image.new(mode="RGB",size=(10,10),color=(0,0,0))
    sliderred2 = sliderred.get()
    sliderblue2 = sliderblue.get()
    slidergreen2 = slidergreen.get()

    skiplines = spin1.get()
    skiplines_int = int(skiplines)

    skip_pixels = spin2.get()
    skip_pixels_int = int(skip_pixels)

    print (slidergreen2,sliderred2,sliderblue2)


    rows = my_image.size[0]
    cols = my_image.size[1]


    px = my_image.load()

    for i in range(0, rows, skiplines_int):
        start = random.randint(0, rows)
        end = random.randint(0, cols)
        nub = random.randint(1, 10)

        if i % 2 == 0:
            start = 0
        else:
            start = 1

        for j in range(start, cols, nub):
            # you should have your slider code here
            # you should have your slider code here
            # you should have your slider code here
            red = random.randint(0, sliderred2)
            green = random.randint(0, slidergreen2)
            blue = random.randint(0, sliderblue2)
            '''
            if j % 2 == 0:
                red = 0
                green = 0
                blue = 0
            else:
                red = 255
                green = 255
                blue = 255
                '''
            px[i, j] = (red, green, blue)

    my_image.show()

sliderred = Scale(root,from_=0, to=255, orient=HORIZONTAL, background='red', fg='grey')
sliderred.grid(row=7, column=1)
sliderblue = Scale(root,from_=0, to=255, orient=HORIZONTAL, background='blue', fg='grey')
sliderblue.grid(row=8, column=1)
slidergreen = Scale(root,from_=0, to=255, orient=HORIZONTAL, background='green', fg='grey')
slidergreen.grid(row=8, column=2)

spin1 = Spinbox(root, from_=1, to=10, width=3)
spin1.grid(row=1, column=1)
spin2 = Spinbox(root, from_=1, to=10, width=3)
spin2.grid(row=1, column=0)
# open button --- add this to your code
open_button = ttk.Button(root, text='Open Files', command=select_files)
open_button.grid(row=0, column=2)

root.mainloop()