import tkinter

def main():
	master=tkinter.Tk()
	master.title("Chat")
	fr=tkinter.Frame(master)
	msg=tkinter.StringVar()
	msg.set("Type here")
	sc=tkinter.Scrollbar(fr)
	msglist=tkinter.Listbox(fr, height=15, width=50, yscrollcommand=sc.set)
	sc.pack(side=tkinter.RIGHT, fill=tkinter.Y)
	msglist.pack(side=tkinter.LEFT, fill=tkinter.BOTH)
	msglist.pack()
	fr.pack()
	
	inputfield=tkinter.Entry(master, textvariable=msg)
	inputfield.bind("<Return>", lambda: null)
	inputfield.pack()
	send=tkinter.Button(master, text="Send", command=lambda: None)
	send.pack()
	master.mainloop()

main()	
