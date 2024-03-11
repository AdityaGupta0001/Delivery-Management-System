from tkinter import *
import random
from pygame import mixer
import Signup_Menu
import Checkoutwindow

def creator(order):
    global d
    d=order
    global root
    emp3={}
    emp4={}

    def btn_clicked(t):
        if "+" in t:
            t1=t.rstrip("+")
            t2=t1
            if d[t2]<12:
                x=emp4[t2]
                x.configure(text=str(d[t2]+1))
                d[t2]+=1
        if "-" in t:
            t1=t.rstrip("-")
            t2=t1
            if d[t2]>0:
                x=emp4[t2]
                x.configure(text=str(d[t2]-1))
                d[t2]-=1

    root = Tk()
    width1=1298
    height1=800

    scr_width=root.winfo_screenwidth()
    scr_height=root.winfo_screenheight()

    width2=int((scr_width/2)-(width1/2))
    height2=int((scr_height/2)-(height1/2))

    root.geometry(f'{width1}x{height1}+{width2}+{height2}')
    root.configure(bg="white")
    root.title("Bite o'Clock - Cart")
    
    main_frame = Frame(root)
    main_frame.pack(fill=BOTH, expand=1)

    yscrollbar=Scrollbar(root,orient=VERTICAL)
    yscrollbar.pack(side=RIGHT, fill=Y)

    canvas = Canvas(root,width=1298,height=800,scrollregion=(0,0,1298,1600),yscrollcommand=yscrollbar.set,bg="white")
    canvas.pack(side=LEFT, fill=BOTH, expand=1)

    yscrollbar.config(command=canvas.yview)


    bullet_list=[PhotoImage(file = f"Delivery-Management-System/assets/images/rand5.png"),PhotoImage(file = f"Delivery-Management-System/assets/images/rand6.png"),PhotoImage(file = f"Delivery-Management-System/assets/images/rand7.png"),PhotoImage(file = f"Delivery-Management-System/assets/images/rand8.png"),PhotoImage(file = f"Delivery-Management-System/assets/images/rand9.png")]
    bullety3=156

    for i in range(len(d)):
        canvas.create_image(49,bullety3,image=random.choice(bullet_list))
        bullety3+=71




    labelimages=PhotoImage(file = f"Delivery-Management-System/assets/images/item labels.png")
    img4 = PhotoImage(file = f"Delivery-Management-System/assets/images/max.png")
    img7=PhotoImage(file = f"Delivery-Management-System/assets/images/cart box 2.png")
    img3=PhotoImage(file = f"Delivery-Management-System/assets/images/min.png")
    bullety=156
    bullety2=156
    bullety3=156
    bullety4=156
    labelyimg=157
    labely=130
    emp1=[]
    emp2=[]
    for j,r in d.items():
        
        canvas.create_image(588.0, labelyimg,image = labelimages)
        emp3[j]=Label(bd = 0,bg = "#ffffff",highlightthickness = 0,text=str(" ")+str(j),anchor=W,font=("Jokerman",28),fg="#B73770")
        
        
        emp1.append(Button(image = img4,borderwidth = 0,highlightthickness = 0,command = lambda j=j: btn_clicked(str(j)+"+"),relief = "flat"))

        canvas.create_image(1170.0, labelyimg,image = img7)
        emp4[j]=Label(bd = 0,bg = "#ffffff",highlightthickness = 0,text=r,font=("Helvetica",21))
        

        emp2.append(Button(image = img3,borderwidth = 0,highlightthickness = 0,command = lambda j=j: btn_clicked(str(j)+"-"),relief = "flat"))

        labelyimg+=71

    for o in emp3.keys():

        canvas.create_window(588,bullety,width=980,height=54,window=emp3[o])
        bullety+=71

    for p in emp4.keys():

        canvas.create_window(1170,bullety4,width=52,height=49,window=emp4[p])
        bullety4+=71
        
    for k in range(len(d)):
        
        canvas.create_window(1112,bullety2,window=emp1[k])

        canvas.create_window(1230,bullety2,window=emp2[k])
        
        bullety2+=71

    def checkout_win():
        global root,d
        j=mixer.Sound("Delivery-Management-System/assets/sounds/Error Tone.mp3")
        total=0
        for i in d.values():
            total+=int(i)
        if total!=0:
            root.destroy()
            Checkoutwindow.checkout_win(d)
        else:
            j.play()
        
    img10 = PhotoImage(file = f"Delivery-Management-System/assets/images/back.png")
    b10 = Button(
        image = img10,
        borderwidth = 0,
        highlightthickness = 0,
        command = destructor,
        relief = "flat")
    canvas.create_window(44,42,window=b10)

    img11=PhotoImage(file = f"Delivery-Management-System/assets/images/CART2.png")
    canvas.create_image(159,44,image=img11)

    img12=PhotoImage(file = f"Delivery-Management-System/assets/images/checkout.png")
    b12 = Button(
        image = img12,
        borderwidth = 0,
        highlightthickness = 0,
        command = checkout_win,
        relief = "flat")
    canvas.create_window(640,bullety+30,window=b12)

    bullety+=100

    canvas.configure(scrollregion=(0,0,1298,bullety))

    
    root.resizable(False,False)
    main_frame.mainloop()


    print(d)

def destructor():
    global root
    root.destroy()
    Signup_Menu.first_menu()