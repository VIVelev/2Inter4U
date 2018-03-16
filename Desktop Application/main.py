from tkinter import *
root=Tk()

root.geometry('1000x500')
logo = PhotoImage(file="ht.png")
background=Label(root, image=logo).place(x=0,y=0,relwidth=1, relheight=1)

chat_button=Button(root,justify = LEFT)
chat_photo=PhotoImage(file="chat1.png", width=50, height=50)
chat_button.config(image=chat_photo, width=50, height=50)
chat_button.place(x=850, y=20)

history_button = Button(root, justify = RIGHT)
history_photo=PhotoImage(file="hstic.png", width=50, height=50)
history_button.config(image=history_photo, width=50, height=50)
history_button.place(x=850, y=140)

fav_button = Button(root, justify = RIGHT)
fav_photo=PhotoImage(file="favic.png", width=50, height=50)
fav_button.config(image=fav_photo, width=50, height=50)
fav_button.place(x=850, y=260)

aboutus_button = Button(root)
aboutus_photo = PhotoImage(file="aboutus.png", width=50, height=50)
aboutus_button.config(image=aboutus_photo, width=50, height=50)
aboutus_button.place(x=850, y=380)




root.mainloop()
