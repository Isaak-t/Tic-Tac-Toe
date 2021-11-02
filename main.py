from tkinter import *
from tkinter import messagebox
# tkinter name
root = Tk()

root.geometry("730x730")
root.configure(bg='blue')
#labels
first_label = Label(root, text='user input-1', font=('calibre', 10, 'bold'))
first_label.grid(row=0, column=0)

def popup ():
    print("pop up")
    messagebox.showwarning("showwarning", "Waring")
def popup2 ():
    print("wghujk")

popupbutton = Button(root, text='pop up', command=popup)
popupbutton.grid(row=2, column=3)
popupbutton = Button(root, text='pop up 2', command=popup2)
popupbutton.grid(row=4, column=5)
def radiobut ():
    print ("radio")
def radiobut2 ():
    print ("radio 2")

R1 = Radiobutton(root, text="option 1", value=0, command=radiobut)
R1.grid(row=5, column=1)
R2 = Radiobutton(root, text="option 2", value=1, command=radiobut2)
R2.grid(row=6, column=1)
def radiobut3 ():
    print ("radio")
def radiobut4 ():
    print ("radio 2")

R1 = Radiobutton(root, text="option 3", value=2, command=radiobut3)
R1.grid(row=4, column=1)
R2 = Radiobutton(root, text="option 4", value=3, command=radiobut4)
R2.grid(row=3, column=1)

clicked= StringVar()
main_menu = OptionMenu(root, clicked, "C++", 'Java', "Python", "Rust", "Go", "Ruby")
main_menu.grid(row=6, column=2)

sliderred = Scale(root,from_=0, to=255, orient=HORIZONTAL, background='red', fg='grey')
sliderred.grid(row=7, column=1)
sliderblue = Scale(root,from_=0, to=255, orient=HORIZONTAL, background='blue', fg='grey')
sliderblue.grid(row=8, column=1)
slidergreen = Scale(root,from_=0, to=255, orient=HORIZONTAL, background='green', fg='grey')
slidergreen.grid(row=9, column=1)

spinbox = Spinbox(root, from_=0, to=10)
spinbox.grid(row=7, column=2)
def testfun ():
    print("testfun")
checkbox = Checkbutton(root, text='python', onvalue=1, offvalue=0, command=testfun)
checkbox.grid(row=7, column=3)

entrybox = Entry(root, font=("calibre", 10, "bold"))
entrybox.grid(row=10, column=10)
root.mainloop()
