import tkinter as tk
master=tk.Tk()
def onFrameConfigure(canvas):
    '''Reset the scroll region to encompass the inner frame'''
    canvas.configure(scrollregion=canvas.bbox("all"))

canvas = tk.Canvas(master, borderwidth=0, background="#ffffff")
frame = tk.Frame(canvas, background="#ffffff")
vsb = tk.Scrollbar(master, orient="vertical", command=canvas.yview)
canvas.configure(yscrollcommand=vsb.set)

vsb.pack(side="right", fill="y")
canvas.pack(side="right", fill="both", expand=True)
canvas.create_window((4,4), window=frame, anchor="nw")

frame.bind("<Configure>", lambda event, canvas=canvas: onFrameConfigure(canvas))

open_file = open("./botsaid.txt", "r")

labels=[]
string = "Bot said -> "
while True:
    i=open_file.readline()
    if i is "":
        break
#    print (i,type(i))
    jk = string + i
    label = tk.Label(frame,text=jk,width=85)
    label.pack(pady = 50)
    labels.append(label)




'''string = 'Question #'
nums = ['1', '2', '3','4','5' , '6' , '7' , '8']
labels=[]
for x in nums:
    jk = string + x
    label = tk.Label(frame,text=jk,width=85)
    label.pack(pady = 50)
    labels.append(label)'''
master.minsize(width = 600,height = 700)
master.maxsize(width = 600, height = 700)
master.configure(background='wheat3')
master.mainloop()
