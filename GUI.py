from tkinter import *
win = Tk()
width= win.winfo_screenwidth()
height= win.winfo_screenheight()
win.geometry("%dx%d" % (width, height))
win.title("Area Calculator")

def add_entry():
    selected =  str(v.get())
    if selected == "1":
        A = int(entry_hide_area.get())
        x=int(total_area_count["text"])
        x=x+A
        total_area_count["text"]=x
        
    elif selected == "2":
        A = int(entry_hide_area.get())
        x=int(total_area_count["text"])
        A = A*929
        x=x+A
        total_area_count["text"]=x
    #entry_hide_area.delete(0, END)
    y=int(hide_number_1["text"])
    y=y+1
    hide_number_1["text"]=y
        
def cancel():
    selected =  str(v.get())
    if selected == "1":
        B = int(entry_hide_area.get())
        D = int(total_area_count["text"])
        C = D - B
        total_area_count["text"] = C
    elif selected == "2":
        B = int(entry_hide_area.get())
        D = int(total_area_count["text"])
        E = B*929
        C = D - E
        total_area_count["text"] = C
        
        
        
    
    

    
def finish():
    z=int(batch_number_1["text"])
    z=z+1
    batch_number_1["text"]=z
    y=0
    hide_number_1["text"]=y
    x=0
    total_area_count["text"]=x
    

select_unit = Label(text = "Select Unit",font = 60)
measuring_indicator = Label(text = "Measuring", font = 60)
hide_number = Label(text = "Hide Number = ", font = 60)
hide_area = Label(text = "Hide Area = ", font = 60)
total_batch_area = Label(text = "Total Batch Area In Sq.cm = ",font = 60)
batch_number = Label(text = "Batch Number = ", font = 60)
batch_number_1 = Label(text = "1", font = 60)
total_area_count = Label(win,text = "0",font = 60)


hide_number_1 = Label(win,text= "1",font = 60)
entry_hide_area = Entry(win, font = 60)



button_add_entry = Button(win, text = "Add Entry",font = 60,command = add_entry)
button_finish = Button(win, text = "Finish",font = 60,command = finish)
button_cancle_last_entry = Button(win, text = "Cancle Last Entry",font = 60, command = cancel)



my_canvas = Canvas(win, width=100, height=100)
my_oval = my_canvas.create_oval(30, 30, 60, 60)
my_canvas.itemconfig(my_oval, fill="dark green")



select_unit.grid(row=0, column=0)
measuring_indicator.grid(row=0, column=3)
hide_number.grid(row=1, column=0)
hide_number_1.grid(row=1, column=1)
hide_area.grid(row=1, column=2)
entry_hide_area.grid(row=1, column=3)
button_add_entry.grid(row=1, column=4)
total_batch_area.grid(row=2, column=0)
total_area_count.grid(row=2, column=1)
batch_number.grid(row=2, column=3)
batch_number_1.grid(row=2, column=4)
button_finish.grid(row=3, column=0)
button_cancle_last_entry.grid(row=3, column=1)
my_canvas.grid(row=0, column=4)


v = IntVar()
Radiobutton(win, text = "Sq.cm",font = 60, variable=v,  value = "1").grid(row=0, column=1)
Radiobutton(win, text = "Sq.ft",font = 60,  variable=v,  value = "2").grid(row=0, column=2)


mainloop()
