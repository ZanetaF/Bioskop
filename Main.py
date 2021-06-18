from tkinter import *
from tkinter import simpledialog,messagebox
from PIL import ImageTk, Image
import os,cv2,numpy as np


root = Tk()
root.title("Movie")
root.geometry('900x700')
root.eval('tk::PlaceWindow . center')

# Movie
photo_movie = PhotoImage(file=r"movie.png")
btn_movie = Button(root, text="Movie",image=photo_movie)
btn_movie.place(x=10, y=10, width=128, height=128)
label_movie = Label(root,text="Movie",font=('Helvatical bold',16))
label_movie.place(x=10, y=140, width=128, height=25)

# Time
photo_time = PhotoImage(file=r"time.png")
btn_time = Button(root, text="Time",image=photo_time)
btn_time.place(x=150, y=10, width=128, height=128)
label_time = Label(root,text="Time",font=('Helvatical bold',16))
label_time.place(x=150, y=140, width=128, height=25)

# Price
photo_price = PhotoImage(file=r"price.png")
btn_price = Button(root, text="Time",image=photo_price)
btn_price.place(x=290, y=10, width=128, height=128)
label_price = Label(root,text="Price",font=('Helvatical bold',16))
label_price.place(x=290, y=140, width=128, height=25)

# seat
photo_seat = PhotoImage(file=r"seat.png")
btn_seat = Button(root, text="Time",image=photo_seat)
btn_seat.place(x=430, y=10, width=128, height=128)
label_seat = Label(root,text="Seat",font=('Helvatical bold',16))
label_seat.place(x=430, y=140, width=128, height=25)

# transaction
photo_transaction = PhotoImage(file=r"transaction.png")
btn_transaction = Button(root, text="Time",image=photo_transaction)
btn_transaction.place(x=570, y=10, width=128, height=128)
label_transaction = Label(root,text="Transaction",font=('Helvatical bold',16))
label_transaction.place(x=570, y=140, width=128, height=25)


# M1
image_m1 = ImageTk.PhotoImage(Image.open('AV2.jpg'))
pic_m1 = Label(root, text="Time",image=image_m1)
pic_m1.place(x=10, y=175, width=375, height=210)
label_m1 = Label(root,text="Avatar2",font=('Helvatical bold',16))
label_m1.place(x=10, y=385, width=320, height=25)

# M2
image_m2 = ImageTk.PhotoImage(Image.open('ETR.jpg'))
pic_m2 = Label(root, text="Eternals",image=image_m2)
pic_m2.place(x=385, y=175, width=375, height=210)
label_m2 = Label(root,text="Eternals",font=('Helvatical bold',16))
label_m2.place(x=385, y=385, width=320, height=25)

# M3
image_m3 = ImageTk.PhotoImage(Image.open('FF9.jpg'))
pic_m3 = Label(root, text="Time",image=image_m3)
pic_m3.place(x=10, y=425, width=375, height=210)
label_m3 = Label(root,text="Fast & Furious 9",font=('Helvatical bold',16))
label_m3.place(x=10, y=640, width=320, height=25)

# M4
image_m4 = ImageTk.PhotoImage(Image.open('SB2.jpg'))
pic_m4 = Label(root, text="Eternals",image=image_m4)
pic_m4.place(x=385, y=425, width=375, height=210)
label_m4 = Label(root,text="Spongebob 2",font=('Helvatical bold',16))
label_m4.place(x=385, y=640, width=320, height=25)

root.mainloop()