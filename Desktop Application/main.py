from tkinter import *
root=Tk()


root.geometry('1000x500')
logo = PhotoImage(file="ht1.png")
background=Label(root, image=logo).place(x=0,y=0,relwidth=1, relheight=1)

chat_button=Button(root,justify = LEFT, bg="#b0966b", bd=0)
chat_photo=PhotoImage(file="chat1tp.png", width=80, height=80)
chat_button.config(image=chat_photo, width=78, height=78)
chat_button.place(x=835, y=50)

history_button = Button(root, justify = RIGHT, bg="#b0966b", bd=0)
history_photo=PhotoImage(file="hstictp.png", width=50, height=50)
history_button.config(image=history_photo, width=48, height=48)
history_button.place(x=850, y=180)

fav_button = Button(root, justify = RIGHT, bd=0)
fav_photo=PhotoImage(file="favictp.png", width=47, height=47)
fav_button.config(image=fav_photo, width=40, height=40)
fav_button.place(x=850, y=250)

aboutus_button = Button(root)
aboutus_photo = PhotoImage(file="aboutus.png", width=50, height=50)
aboutus_button.config(image=aboutus_photo, width=50, height=50)
aboutus_button.place(x=850, y=390)

reset_button = Button(root)
reset_photo = PhotoImage(file="reset.png", height=50, width=50)
reset_button.config(image=reset_photo, width=50, height=50)
reset_button.place(x=850, y=320)




root.mainloop()
