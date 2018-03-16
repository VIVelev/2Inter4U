from tkinter import *
import os
from chat import main
root=Tk()

def chat():
	main()

root.geometry('1000x500')
logo = PhotoImage(file="ht1.png")
background=Label(root, image=logo).place(x=0,y=0,relwidth=1, relheight=1)

chat_button=Button(root,justify = LEFT)
chat_photo=PhotoImage(file="chat1.png", width=80, height=80)
chat_button.config(image=chat_photo, width=80, height=80, command=lambda: main())
chat_button.place(x=835, y=50)

history_button = Button(root, justify = RIGHT, bg="#b0966b")
history_photo=PhotoImage(file="hstic.png", width=50, height=50)
history_button.config(image=history_photo, width=50, height=50)
history_button.place(x=850, y=180)

fav_button = Button(root, justify = RIGHT)
fav_photo=PhotoImage(file="favic.png", width=50, height=50)
fav_button.config(image=fav_photo, width=50, height=50)
fav_button.place(x=850, y=250)

aboutus_button = Button(root)
aboutus_photo = PhotoImage(file="aboutus.png", width=50, height=50)
aboutus_button.config(image=aboutus_photo, width=50, height=50)
aboutus_button.place(x=850, y=320)

reset_button = Button(root)
reset_photo = PhotoImage(file="reset.png", height=50, width=50)
reset_button.config(image=reset_photo, width=50, height=50)
reset_button.place(x=850, y=390)




root.mainloop()
