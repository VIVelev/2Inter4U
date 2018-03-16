from tkinter import *

class MyFirstGUI:
    def __init__(self, master):
        self.master = master
        master.title("Your new smart friend!")

        self.label = Label(master, text="Welcome to our project!", font = "Times 16 bold")
        self.label.pack()

        self.write_button = Button(master, text="Chat",fg="blue",bg ="yellow", font="Times", command=self.greet)
        self.write_button.pack(pady = 15)

        self.open_button = Button(master, text="History",fg="blue",bg ="yellow", font="Times", command=self.greet)
        self.open_button.pack(pady = 15)

        self.write_button = Button(master, text="Favourites",fg="blue",bg ="yellow", font="Times", command=self.greet)
        self.write_button.pack(pady = 15)

        self.open_button = Button(master, text="Reset",fg="blue",bg ="yellow", font="Times", command=self.greet)
        self.open_button.pack(pady = 15)


        self.open_button = Button(master, text="About us",fg="blue",bg ="yellow", font="Times", command=self.greet)
        self.open_button.pack(pady = 15)

        self.quit_button = Button(master, text="    QUIT    ", fg="red", font = "Times",bg = "white",  command=quit)
        self.quit_button.pack(pady = 15)

    def greet(self):
        print("Greetings!")


master = Tk()
my_gui = MyFirstGUI(master)
master.title("Your new smart friend")
master.geometry("900x600")
master.mainloop()
