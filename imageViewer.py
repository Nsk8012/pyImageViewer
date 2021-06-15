from tkinter import *
from PIL import ImageTk, Image

#Window install
window = Tk()
window.title("Image Viewer")

#Window icon
window.call('wm', 'iconphoto', window._w, PhotoImage(file="/Users/Nsk/Desktop/Project/Image Viewer/image.png"))

#Adding Image
img1 = Image.open("/Users/Nsk/Desktop/Project/Image Viewer/img1.jpg")
img2 = Image.open("/Users/Nsk/Desktop/Project/Image Viewer/img2.jpg")
img3 = Image.open("/Users/Nsk/Desktop/Project/Image Viewer/img3.jpg")
img4 = Image.open("/Users/Nsk/Desktop/Project/Image Viewer/img4.jpg")
img5 = Image.open("/Users/Nsk/Desktop/Project/Image Viewer/img5.jpg")

#Changing resolution
img1= img1.resize((200,200), Image.ANTIALIAS)
img2= img2.resize((200,200), Image.ANTIALIAS)
img3= img3.resize((200,200), Image.ANTIALIAS)
img4= img4.resize((200,200), Image.ANTIALIAS)
img5= img5.resize((200,200), Image.ANTIALIAS)

#ImageTk is used to Load Image
img1 = ImageTk.PhotoImage(img1)
img2 = ImageTk.PhotoImage(img2)
img3 = ImageTk.PhotoImage(img3)
img4 = ImageTk.PhotoImage(img4)
img5 = ImageTk.PhotoImage(img5)

#put in list
myImages = [img1, img2, img3, img4, img5]

#We should put in widget to show in window
i=0
myLabel =Label(image=myImages[0])
myLabel.grid(row=0,column=0,columnspan=3)

#Forward function
def forward():
    global i
    i = i + 1
    myLabel.config(image=myImages[i])
    if myImages[i] == myImages[-1]:
        nxtButton.config(state=DISABLED)
    if nxtButton['state'] == DISABLED:
        nxtButton.config(state=NORMAL)

#Backward Function
def backward():
    global i
    if i == 0:
        i = 0
    else:
        i = i - 1
    myLabel.config(image=myImages[i])
    if myImages[i] == myImages[0]:
        preButton.config(state=DISABLED) 
    if preButton['state'] == DISABLED:
        preButton.config(state=NORMAL)

#Adding Button
exitButton = Button(window, text="Exit", command=window.quit)
nxtButton = Button(window, text=">>", command=forward, relief=GROOVE)
preButton = Button(window, text="<<", command=backward, relief=GROOVE)

#put that in position
exitButton.grid(row=1, column=1,columnspan=1)
nxtButton.grid(row=1, column=2, columnspan=1)
preButton.grid(row=1,column=0,columnspan=1)

window.geometry("210x230")
window.mainloop()