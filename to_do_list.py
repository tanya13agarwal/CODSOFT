from tkinter import *
from tkinter.font import Font
from tkinter import filedialog
import pickle

gui=Tk()
gui.title('To-Do List')
gui.geometry("500x500")

# Defining the font to be used 
font_used=Font(size=30)

# Creating frame for containing the list
my_frame=Frame(gui)
my_frame.pack(pady=10)

# Creating listbox
my_list=Listbox(my_frame,font=font_used,width=25,height=5,bg="SystemButtonFace",bd=0,fg='#464646',
                highlightthickness=0,
                selectbackground="#a6a6a6",
                activestyle="none")

my_list.pack(side=LEFT,fill=BOTH)

# items contains the list of to-do things
items=["prepare breakfast","do yoga","take a shower","pack all necessary items","meet coco at lunch"]

# add items to listbox
for i in items:
    my_list.insert(END,i)

# creating scrollbar
my_scrollbar=Scrollbar(my_frame)
my_scrollbar.pack(side=RIGHT,fill=BOTH)

# add scrollbar
my_list.config(yscrollcommand=my_scrollbar.set)
my_scrollbar.config(command=my_list.yview)

# create entry box to add items to the list
my_entry=Entry(gui,font=("Helvetica",24),width=26)  
my_entry.pack(pady=20)

# create a button frame 
button_frame=Frame(gui)
button_frame.pack(pady=20)

# functions to define buttons
def delete_item():
    my_list.delete(ANCHOR)

def add_item():
    my_list.insert(END,my_entry.get())
    my_entry.delete(0,END)

def cross_off_item():
    # cross off item
    my_list.itemconfig(
        my_list.curselection(),
        fg="#dedede")
    # for no selection bar
    my_list.selection_clear(0,END)

def uncross_item():
    # cross off item
    my_list.itemconfig(
        my_list.curselection(),
        fg="#464646")
    # for no selection bar
    my_list.selection_clear(0,END)

def delete_crossed():
    count=0
    while count<my_list.size():
        if my_list.itemcget(count,"fg")=="#dedede":
            my_list.delete(my_list.index(count))
        else:    
            count+=1   

# functions for menu
def save_list():
    file_name=filedialog.asksaveasfilename(
        initialdir="/Users/tanyaagrawal/Desktop/python projects/to_do_list.py",
        title="Save File",
        filetypes=(("Dat Files","*.dat"),("ALl Files","*.*")))
    if file_name:
        if file_name.endswith(".dat"):
            pass
        else:
            file_name=f'{file_name}.dat'

        # delete crossed off items before saving
        count=0
        while count<my_list.size():
            if my_list.itemcget(count,"fg")=="#dedede":
                my_list.delete(my_list.index(count))
            else:    
                count+=1    

        # grab all stuff from list
        stuff=my_list.get(0,END)

        # open the file
        output_file=open(file_name,'wb')

        # actually add stuff to the file
        pickle.dump(stuff,output_file)
    

def open_list():
    file_name=filedialog.askopenfilename(
        initialdir="/Users/tanyaagrawal/Desktop/python projects/to_do_list.py",
        title="Open File",
        filetypes=(("Dat Files","*.dat"),("ALl Files","*.*")))    
    
    if file_name:
        # delete currently open list
        my_list.delete(0,END)

        # open the file
        input_file=open(file_name,'rb')

        # load data from file
        stuff=pickle.load(input_file)
 
        # output stuff to the screen
        for i in stuff:
            my_list.insert(END,i)


def clear_list():
    my_list.delete(0,END)            


# create menu 
my_menu=Menu(gui)
gui.config(menu=my_menu)

# adding items to the menu
file_menu=Menu(my_menu,tearoff=False)
my_menu.add_cascade(label="File",menu=file_menu)
# add dropdown items
file_menu.add_command(label="Save List",command=save_list)
file_menu.add_command(label="Open List",command=open_list)
file_menu.add_separator()
file_menu.add_command(label="Clear List",command=clear_list)


# adding some buttons
delete_button=Button(button_frame,text="Delete Item",command=delete_item)   
add_button=Button(button_frame,text="Add Item",command=add_item)
cross_off_button=Button(button_frame,text="Cross Off Item",command=cross_off_item)
uncross_button=Button(button_frame,text="Uncross Item",command=uncross_item)
delete_crossed_button=Button(button_frame,text="Deleted Crossed",command=delete_crossed)

delete_button.grid(row=0,column=0)
add_button.grid(row=0,column=1,padx=20)
cross_off_button.grid(row=0,column=2)
uncross_button.grid(row=0,column=3,padx=20)
delete_crossed_button.grid(row=0,column=4)



gui.mainloop()