from tkinter import *
root=Tk()

root.geometry('1000x500')
logo = PhotoImage(file="ht.png")
background=Label(root, image=logo).place(x=0,y=0,relwidth=1, relheight=1)

chat_button=Button(root,justify = LEFT)
photo_chat=PhotoImage(file="chat1.png", height=100, width=100)
chat_button.config(image=photo_chat,width=100,height=100)
chat_button.place(x=850, y=20)

history_button = Button(root, justify = RIGHT)
photo_history=PhotoImage(file="hstic.png", height=100, width=100)
history_button.config(image=photo_history,width=100, height=100)
history_button.place(x=850, y=140)



root.mainloop()
