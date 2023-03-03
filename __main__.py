from tkinter import *
import numpy as np
import cv2
from PIL import Image, ImageTk

def initGUI():
    win = Tk()
    win.attributes('-zoomed', True)
    menubar = Menu(win)
    filemenu = Menu(menubar, tearoff=0)
    donothing = lambda: None
    filemenu.add_command(label="New", command=donothing)
    filemenu.add_command(label="Open", command=donothing)
    filemenu.add_command(label="Save", command=donothing)
    filemenu.add_separator()
    filemenu.add_command(label="Exit", command=win.quit)
    menubar.add_cascade(label="File", menu=filemenu)
    win.config(menu=menubar)
    return win

def main():
    win = initGUI()
    win.mainloop()

if __name__ == "__main__":
    main()

#     img = cv2.imread('img/family.jpg')
#     blue,green,red = cv2.split(img)
#     img = cv2.merge((red,green,blue))
#     img = np.zeros((1,1,3), np.uint8)
#     im = Image.fromarray(img)
#     imgtk = ImageTk.PhotoImage(image=im)
#     Label(win, image= imgtk).pack()


