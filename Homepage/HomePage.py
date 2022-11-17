from tkinter import *
from PIL import ImageTk,Image
from tkinter import filedialog
import os
import shutil


"""root=Tk()
root.title('Upload')
"""



window = Tk()
window.title('Automatic Video Captioning')
window.geometry("1000x600")

window.configure(bg = "#ffffff")
canvas = Canvas(
    window,
    bg = "#ffffff",
    height = 600,
    width = 875,
    bd = 0,
    highlightthickness = 0,
    relief = "ridge")
canvas.place(x = 0, y = 0)

background_img = PhotoImage(master=canvas,file = f"homepage_bg.png")
background = canvas.create_image(
    440, 300,
    image=background_img)
def btn_clicked():
    print("Button Clicked")
'''

def update(data):
    my_list.delete(0,END)
    for item in data:
        my_list.insert(END,item)


def fillout(e):
    my_entry.delete(0,END)

    #adding clicked list item to entry  box
    my_entry.insert(0,my_list.get(ANCHOR))
def check(e):
    typed=my_entry.get()
    
    if typed=='':
        data=toppings
    else:
        data=[]
        for item in toppings:
            if typed.lower() in item.lower():
                data.append(item)
        
        #update listbox with sleected items
        update(data)
'''

def search():
    '''#Label
    my_label=Label(window,text="Search for a word..",font=("Helvetica",14),fg="grey")
    my_label.pack(pady=20)
    #Entry box
    global my_entry
    my_entry=Entry(window,font=("Helvetica",20))
    my_entry.pack()
    #Listbox
    global my_list
    my_list=Listbox(window,width=50)
    my_list.pack(pady=40)
    #List
    global toppings
    toppings=["Boy","horse","dancing","cooking","cutting","carrot","hill"]
    update(toppings)

    #Create a binding on listbox onclick
    my_list.bind("<<ListboxSelect>>",fillout)

    #Create a binding on entry box
    my_entry.bind("<KeyRelease>",check)'''
    os.chdir('..')
    os.chdir('GetEvent')
    print("Sus")
    os.system('python3 GetEvent.py')
    
        

def open(event=None):
    filename=filedialog.askopenfilename()
    print('Selected',filename)
    origin=filename
    target=r'C:\Users\User\Documents\CAPSTONE'
    """files=os.listdir(origin)
    for f in files:
        shutil.move(origin+f,target)"""
    shutil.copy(origin,target)
    


def open_path():
    os.startfile(r'C:\Users\User\Documents\CAPSTONE')

    




img0 = PhotoImage(file = f"getevent.png")
b0 = Button(
    image = img0,
    borderwidth = 0,
    highlightthickness = 0,
    command = search,
    relief = "flat")

b0.place(
    x = 500, y = 197,
    width = 426,
    height = 90)
#b0.pack()

img1 = PhotoImage(file = f"uploadvideo.png")
b1 = Button(
    window,
    image = img1,
    borderwidth = 0,
    highlightthickness = 0,
    command=open,
    relief = "flat")

b1.place(
    x = 500, y = 308,
    width = 426,
    height = 103)
#b1.pack(pady=100)

img2 = PhotoImage(file = f"viewgallery.png")
b2 = Button(
    image = img2,
    borderwidth = 0,
    highlightthickness = 0,
    command = open_path,
    relief = "flat")

b2.place(
    x = 500, y = 419,
    width = 426,
    height = 110)
#b2.pack()

window.resizable(False, False)
window.mainloop()
#root.mainloop()
