from tkinter import Tk, Text, Button, filedialog

root=Tk()

root.title('Epic Text Editor | v1.0')

root.resizable(0, 0) 

text=Text(root)

text.configure(font=("Sans", 15))

text.grid()

o = [text] 
for wid in o:
    wid.configure(bg = 'white')

def saveas():
    global text  

    t = text.get('1.0', 'end-1c')

    savelocation=filedialog.asksaveasfilename()

    file1=open(savelocation, 'w+')

    file1.write(t)

    file1.close()
button=Button(root, text='Save', command=saveas)

button.grid() 

def night():
    myWidgets = [text] 
    for wid in myWidgets:
        wid.configure(bg = 'black')
        text.configure(fg='white', font=("Sans", 15))

night=Button(root, text='Dark', command=night)

night.grid()

def day():
    myWidgets = [text] 
    for wid in myWidgets:
        wid.configure(bg = 'white')
        text.configure(fg='black', font=("Sans", 15))

day=Button(root, text='Light', command=day)

day.grid()

root.mainloop()