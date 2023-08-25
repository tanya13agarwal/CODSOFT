from tkinter import *

def click(event):
    global scvalue
    text = event.widget.cget("text")
    print(text)
    if text == "=":
        if scvalue.get().isdigit():
            value = int(scvalue.get())
        else:
            value = eval(screen.get())
        scvalue.set(value)
        screen.update()

    elif text == "c":
        scvalue.set("")
        scvalue.update()


    else:
        scvalue.set(scvalue.get() + text)
        scvalue.update()

root =Tk()
root.geometry("644x600")
root.title("Tanya's Calculator")
root.configure(bg='pink')
# root.colormapwindows

scvalue = StringVar()
scvalue.set("")
screen = Entry(root,textvar = scvalue,font = "lucida 40 bold")
screen.pack(fill = X , ipadx=8, pady=10, padx=10)


frame1=Frame(root, bg="aquamarine3")

b = Button(frame1,padx=31,pady=18, text="(", font="lucida 21 bold")
b.pack(side=LEFT, padx=18,pady=5)
b.bind("<Button-1>",click)

b = Button(frame1,padx=31,pady=18, text=")", font="lucida 21 bold")
b.pack(side=LEFT, padx=16.3,pady=5)
b.bind("<Button-1>",click)

b = Button(frame1,padx=31,pady=18, text="/", font="lucida 22 bold")
b.pack(side=LEFT, padx=18,pady=5)
b.bind("<Button-1>",click)

b = Button(frame1,padx=23,pady=18, text="%", font="lucida 22 bold")
b.pack(side=LEFT, padx=20,pady=5)
b.bind("<Button-1>",click)

frame1.pack()

frame1=Frame(root, bg="aquamarine3")

b = Button(frame1,padx=28,pady=18, text="9", font="lucida 20 bold")
b.pack(side=LEFT, padx=17.5,pady=5)
b.bind("<Button-1>",click)

b = Button(frame1,padx=28,pady=18, text="8", font="lucida 20 bold")
b.pack(side=LEFT, padx=16,pady=5)
b.bind("<Button-1>",click)

b = Button(frame1,padx=28,pady=18, text="7", font="lucida 20 bold")
b.pack(side=LEFT, padx=18.5,pady=5)
b.bind("<Button-1>",click)

b = Button(frame1,padx=32,pady=18, text="-", font="lucida 20 bold")
b.pack(side=LEFT, padx=18.5,pady=5)
b.bind("<Button-1>",click)


frame1.pack()


frame1=Frame(root, bg="aquamarine3")

b = Button(frame1,padx=28,pady=18, text="6", font="lucida 20 bold")
b.pack(side=LEFT, padx=17,pady=5)
b.bind("<Button-1>",click)

b = Button(frame1,padx=28,pady=18, text="5", font="lucida 20 bold")
b.pack(side=LEFT, padx=18,pady=5)
b.bind("<Button-1>",click)

b = Button(frame1,padx=28.5,pady=18, text="4", font="lucida 20 bold")
b.pack(side=LEFT, padx=17,pady=5)
b.bind("<Button-1>",click)

b = Button(frame1,padx=29,pady=18, text="+", font="lucida 20 bold")
b.pack(side=LEFT, padx=18,pady=5)
b.bind("<Button-1>",click)

frame1.pack()



frame1=Frame(root, bg="aquamarine3")

b = Button(frame1,padx=28,pady=18, text="3", font="lucida 20 bold")
b.pack(side=LEFT, padx=18,pady=5)
b.bind("<Button-1>",click)

b = Button(frame1,padx=28,pady=18, text="2", font="lucida 20 bold")
b.pack(side=LEFT, padx=18,pady=5)
b.bind("<Button-1>",click)

b = Button(frame1,padx=29,pady=18, text="1", font="lucida 20 bold")
b.pack(side=LEFT, padx=16,pady=5)
b.bind("<Button-1>",click)

b = Button(frame1,padx=30.5,pady=18, text="*", font="lucida 22 bold")
b.pack(side=LEFT, padx=18,pady=5)
b.bind("<Button-1>",click)

frame1.pack()





frame1=Frame(root, bg="aquamarine3")

b = Button(frame1,padx=28,pady=18, text="0", font="lucida 21 bold")
b.pack(side=LEFT, padx=17,pady=5)
b.bind("<Button-1>",click)

b = Button(frame1,padx=32,pady=18, text=".", font="lucida 21 bold")
b.pack(side=LEFT, padx=17,pady=5)
b.bind("<Button-1>",click)

b = Button(frame1,padx=28,pady=18, text="c", font="lucida 20 bold")
b.pack(side=LEFT, padx=18,pady=5)
b.bind("<Button-1>",click)

b = Button(frame1,padx=29,pady=18, text="=", font="lucida 20 bold")
b.pack(side=LEFT, padx=18,pady=5)
b.bind("<Button-1>",click)

frame1.pack()


root.mainloop()