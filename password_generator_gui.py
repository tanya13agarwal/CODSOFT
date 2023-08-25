from tkinter import *
from random import randint

root=Tk()
root.title("Stong Password Generator")
root.geometry("500x300")


def new_rand():  # generate random strong password
    # clear our entry box
    pw_entry.delete(0,END)
    # get password length and convert to integer
    pw_length=int(my_entry.get())
    # create variable to hold our password
    my_password=''
    # loop through password length
    for x in range(pw_length):
        my_password+=chr(randint(33,126))
    # output password to the screen
    pw_entry.insert(0, my_password)


def clipper():  # copy to clipboard
    # clear clipboard
    root.clipboard_clear()
    # copy to clipboard
    root.clipboard_append(pw_entry.get())


# Label Frame
lf= LabelFrame(root, text="Enter Length of password")
lf.pack(pady=20)

# create entry box to designate number of characters
my_entry=Entry(lf,font=(24))
my_entry.pack(pady=20,padx=20)

# create entry box for our generated password
pw_entry=Entry(root, text='',font=(24),bd=0)
pw_entry.pack(pady=20)

# create a frame for our buttons
my_frame=Frame(root)
my_frame.pack(pady=20)

# create our buttons
my_button=Button(my_frame,text="Generate strong password",command=new_rand)
my_button.grid(row=0,column=0,padx=10)

clip_button=Button(my_frame,text="Copy to Clipboard",command=clipper)
clip_button.grid(row=0,column=1,padx=10)

root.mainloop()
