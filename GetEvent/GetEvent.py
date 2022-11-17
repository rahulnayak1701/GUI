from tkinter import *




window = Tk()

window.geometry("700x500")
window.configure(bg = "#ffffff")
canvas = Canvas(
    window,
    bg = "#ffffff",
    height = 500,
    width = 700,
    bd = 0,
    highlightthickness = 0,
    relief = "ridge")
canvas.place(x = 0, y = 0)

background_img = PhotoImage(file = f"getevent_bg.png")
background = canvas.create_image(
    360, 40,
    image=background_img)

entry0_img = PhotoImage(file = f"searchbar.png")
entry0_bg = canvas.create_image(
    330, 140,
    image = entry0_img)

entry0 = Entry(
    bd = 0,
    bg = "#d9d9d9",
    highlightthickness = 0)


entry0.place(
    x =200, y = 120,
    width = 270,
    height = 40)

def showVideo():
    print("Showing video")
    

li_label=[]
li_play=[]
def btn_clicked():
    
    if(len(li_label)!=0):
        #print("yes")
        for i in li_label:
            i.destroy()
            li_label.pop(0)
    if(len(li_label)>0):
        while(len(li_label)!=0):
            li_label[-1].destroy()
            li_label.pop()
    if(len(li_play)!=0):
        for i in li_play:
            i.destroy()
            li_play.pop(0)
    if(len(li_play)>0):
        while(len(li_play)!=0):
            li_play[-1].destroy()
            li_play.pop()

    print(len(li_label))
    
    print(entry0.get())
    event=entry0.get()
    xcord=150
    ycord=160
    
    for key in dict:
        if(event in key):
            for video in dict[key]:
                print(video[0],'',video[1])
                label=Label(text=video[0]+" "+str(video[1]))
                #print(label.winfo_x(),label.winfo_y())
                label.place(x=xcord,y=ycord)
                li_label.append(label)
                #li_label[-1].place(x=10,y=10)
                
                if(label!=None):
                    label.pack()
                play=Button(text="PLAY",command=showVideo)
                li_play.append(play)
                if(play!=None):
                    play.pack()
                #play.place(x=label.winfo_x()+50,y=label.winfo_y()+50)
                xcord+=30
                ycord+=30
                
    
    print(li_label)

    """for i in li_label:
        i.destroy()
    for j in li_play:
        j.destroy()"""




            


            #play=Button(text="Play",command=showVideo(dict[key]))



dict={
    "walking":[[r"C:\Users\User\Documents\CAPSTONE\volcano.jpg",7],
                [r"C:\Users\User\Documents\CAPSTONE\cat.jpg",87],
                

                ],
    "running":[[r"C:\Users\User\Documents\CAPSTONE\VGG16_MNIST\hammer.png",12],
                [r"C:\Users\User\Documents\CAPSTONE\VGG16_MNIST\volano.jpg",15],
                
    ]
}

img0 = PhotoImage(file = f"submitbutton.png")
b0 = Button(
    image = img0,
    borderwidth = 0,
    highlightthickness = 0,
    command = btn_clicked,
    relief = "raised")

b0.place(
    x = 271, y = 201,
    width = 130,
    height = 35)


window.resizable(False, False)
window.mainloop()
