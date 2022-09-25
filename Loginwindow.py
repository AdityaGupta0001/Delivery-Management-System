from tkinter import *
import signup_login
from pygame import mixer
import Signup_Menu

#pygame.init()

def login():

    def back():
        window.destroy()
        signup_login.display()
    def validation():
        existing=False
        password=False
        if entry0.get()=="" or entry1.get()=="":
            label1.config(text="Please enter the required information")
            j=mixer.Sound("Error Tone.mp3")
            j.play()
        elif entry0.get()!="" or entry1.get()!="":
            with open("Account.txt","r") as acc:
                reader1=acc.readlines()
                for i in reader1:
                    lst0=i.replace("\n","")
                    lst=lst0.split(",")
                    if lst[0]==entry0.get() or lst[1]==entry0.get():
                        existing=True
                        break
            if existing==False:
                label1.config(text="This account (Username) does not exist")
                j=mixer.Sound("Error Tone.mp3")
                j.play()
            elif existing==True:
                with open("Account.txt","r") as acc:
                    reader1=acc.readlines()
                    for i in reader1:
                        lst0=i.replace("\n","")
                        lst=lst0.split(",")
                        if lst[2]==entry1.get():
                            password=True
                if password==False:
                    label1.config(text="Incorrect Password")
                    j=mixer.Sound("Error Tone.mp3")
                    j.play()
                else:
                    window.destroy()
                    Signup_Menu.first_menu()
        
    window = Tk()
    width=1298
    height=800

    scr_width=window.winfo_screenwidth()
    scr_height=window.winfo_screenheight()

    x=int((scr_width/2)-(width/2))
    y=int((scr_height/2)-(height/2))

    window.geometry(f'{width}x{height}+{x}+{y}')
    window.title("Bite o'Clock - Login")
    window.configure(bg = "#ffffff")

    canvas = Canvas(window,bg = "#ffffff",height = 800,width = 1298,bd = 0,highlightthickness = 0,relief = "ridge")
    canvas.place(x = 0, y = 0)

    background_img = PhotoImage(file = f"loginbackground.png")
    background = canvas.create_image(649.0, 400.0,image=background_img)

    img0 = PhotoImage(file = f"loginbutton.png")
    b0 = Button(image = img0,borderwidth = 0,highlightthickness = 0,command = validation,relief = "flat")
    b0.place(x = 790, y = 709,width = 403,height = 66)

    entry0_img = PhotoImage(file = f"textbox1.png")
    entry0_bg = canvas.create_image(992.0, 336.5,image = entry0_img)
    entry0 = Entry(bd = 0,bg = "#ffffff",highlightthickness = 0,font = ('Helvetica',18,'normal'))
    entry0.place(x = 782.0, y = 314,width = 420.0,height = 41)

    entry1_img = PhotoImage(file = f"textbox1.png")
    entry1_bg = canvas.create_image(992.0, 432.5,image = entry1_img)
    entry1 = Entry(bd = 0,bg = "#ffffff",highlightthickness = 0,font = ('Helvetica',18,'normal'))
    entry1.place(x = 782.0, y = 410,width = 420.0,height = 41)

    img1 = PhotoImage(file = f"noaccount.png")
    b1 = Button(image = img1,borderwidth = 0,highlightthickness = 0,command = back,relief = "flat")
    b1.place(x = 790, y = 477,width = 403,height = 31)

    label1=Label(window, text="", font = ('Helvetica',18,'normal'), bg="#ffffff", fg="#ff0000")
    label1.place(x = 756.0, y = 510,width = 473.0,height = 44)

    window.resizable(False, False)
    window.mainloop()

