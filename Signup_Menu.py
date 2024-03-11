#Importing modules
from tkinter import *
import os
import smtplib
from email.message import EmailMessage
import random
import string
import pygame
from pygame import mixer
import webbrowser
import Cartwindow
from dotenv import load_dotenv

load_dotenv()

#Initializing pygame
pygame.init()

item_count=0
item_list=[]

#Function for centering the tkinter window on the screen
def center():
    global root
    width=1298
    height=800

    scr_width=root.winfo_screenwidth()
    scr_height=root.winfo_screenheight()

    x=int((scr_width/2)-(width/2))
    y=int((scr_height/2)-(height/2))

    root.geometry(f'{width}x{height}+{x}+{y}')

#Function to redifine the root object after returning to the window before
def rooter():
    global win
    try:
        if root.winfo_exists():
            root.destroy()
            win = Tk()
    except:
        win = Tk()

#Function to generate list of items selected       
def itemcounter(labelname):
    global item_count
    item_count+=1
    labelname.configure(text=str(item_count))

#Signup window   
def signup_win():
    global entry4,entry3,entry0
    global root
    root=Tk()
    center()
    EMAIL_ADDRESS=os.getenv("MAILING_ADDRESS")
    EMAIL_PASSWORD=os.getenv("MAILING_PASSWORD")

    #Validation of username
    def username(f):
        global user
        user=False
        user_check=0
        user_check2=0
        if len(f)>=6:
            user_check+=1
        for i in f:
            if i=="_":
                user_check2+=1
            if i.isdigit():
                user_check2+=1
        if user_check==1 and user_check2>=0:
            user=True

    #Validation of emailid
    def mailid(a):
        global mailcheck
        mailcheck=False
        ctr=0
        y=[".com",".co",".in",".co.in",".org",".net",".info"]
        p="@"
        a=str(a).lower()
        if p in a:
            ctr+=1
        for i in y:
            if i in a:
                z=i
                ctr+=1
                break
        if a.index(z)==len(a)-len(z):
            ctr+=1
        if ctr==3:
                mailcheck=True
        return mailcheck

    #Validation of password
    def password(b):
        global passcheck
        passcheck=0
        special=string.punctuation
        l, u, p, d = 0, 0, 0, 0
        if (len(b) >= 8):
            for i in b:
                if (i.islower()):
                    l+=1            
                if (i.isupper()):
                    u+=1            
                if (i.isdigit()):
                    d+=1            
                if(i in special):
                    p+=1           
            if (l>=1 and u>=1 and p>=1 and d>=1 and l+p+u+d==len(b)):
                passcheck=1
            else:
                passcheck=0

    #Validation of existing users (during signup)
    def existinguser(a,b):
        global existing
        existing=False
        with open("Delivery-Management-System/Account.txt","r") as acc:
            reader1=acc.readlines()
            for i in reader1:
                lst0=i.replace("\n","")
                lst=lst0.split(",")
                if lst[0]==a or lst[1]==b:
                    existing=True
                    break
    global flag
    flag=0
    global x
    x=""

    #Function for a hyperlink button
    def websiter():
        webbrowser.open("https://bite-oclock.jimdosite.com/privacy-policy/")

    #Signup window
    def signup():
        global entry3_img
        global entry3_bg
        global flag
        global x
        if flag==0:
            if entry0.get() =="" or  entry1.get() =="" or entry3.get() =="" or entry4.get() =="":
                label1.config(text="Please Enter the required information")
                j=mixer.Sound("Delivery-Management-System/assets/sounds/Error Tone.mp3")
                j.play()
                flag=0

            elif entry1.get()!=entry3.get():
                label1.config(text="Confirmation password does not match")
                j=mixer.Sound("Delivery-Management-System/assets/sounds/Error Tone.mp3")
                j.play()
                flag=0

                
            elif entry0.get() !="" and  entry1.get() !="" and entry4.get() !="" and entry3.get() !="" and (entry1.get()==entry3.get()):
                username(entry4.get())
                mailid(entry0.get())
                password(entry1.get())
                existinguser(entry4.get(),entry0.get())
                if mailcheck==True and passcheck==1 and user==True and existing==False:
                    label1.config(text="")
                    for i in range(8):
                        x=x+str(random.randint(0,9))
                    entry2.place(x = 782.0, y = 500,width = 420.0,height = 41)
                    #Sending otp via email
                    msg=EmailMessage()
                    msg['Subject'] = f"Your Bite o'Clock OTP [{x}]"
                    msg["From"] = EMAIL_ADDRESS
                    msg["To"] = entry0.get()
                    msg.set_content(f"Greetings from Team Bite o'Clock\n\nThank you for signing up with us\n\nPlease proceed with the following OTP: {x}\n\n For more information visit our site: https://bite-oclock.jimdosite.com/ \n\n Happy eating!!")
                    with smtplib.SMTP_SSL('smtp.gmail.com', 465) as smtp:
                        smtp.login(EMAIL_ADDRESS,EMAIL_PASSWORD)
                        smtp.send_message(msg)
                    flag=1
                elif existing==True:
                    label1.config(text="This account already exists")
                    j=mixer.Sound("Delivery-Management-System/assets/sounds/Error Tone.mp3")
                    j.play()
                elif mailcheck==False:
                    label1.config(text="Please enter a valid email id")
                    j=mixer.Sound("Delivery-Management-System/assets/sounds/Error Tone.mp3")
                    j.play()
                elif passcheck==0:
                    label1.config(text="Password does not match conditions")
                    j=mixer.Sound("Delivery-Management-System/assets/sounds/Error Tone.mp3")
                    j.play()
                elif user==False:
                    label1.config(text="Please enter a valid username")
                    j=mixer.Sound("Delivery-Management-System/assets/sounds/Error Tone.mp3")
                    j.play()
                
                    
        elif flag==1:
            with open("Delivery-Management-System/Account.txt",mode='a') as Acc:
                a=f"{entry4.get()},{entry0.get()},{entry3.get()}\n"
                Acc.write(a)
            if entry2.get() == x:
                label1.config(text="")
                flag=0
                first_menu()
            elif entry3.get() != x:
                label1.config(text="Please recheck and re-enter the code")
                j=mixer.Sound("Delivery-Management-System/assets/sounds/Error Tone.mp3")
                j.play()
                flag=1
            
    #Defining tkinter window for signup window      
    root.geometry("1298x800")
    root.title("Bite o'Clock - Sign Up")
    
    root.configure(bg = "#ffffff")
    canvas = Canvas(root,bg = "#ffffff",height = 800,width = 1298,bd = 0,highlightthickness = 0,relief = "ridge")
    canvas.place(x = 0, y = 0)

    background_img = PhotoImage(file = f"Delivery-Management-System/assets/images/signbackground.png")
    background = canvas.create_image(649.0, 400.0,image=background_img)

    img0 = PhotoImage(file = f"Delivery-Management-System/assets/images/signbutton.png")
    b0 = Button(image = img0,borderwidth = 0,highlightthickness = 0,command = signup,relief = "flat")
    b0.place(x = 790, y = 709,width = 403,height = 66)

    entry_img = PhotoImage(file = f"Delivery-Management-System/assets/images/img_textBox.png")
    
    entry0_bg = canvas.create_image(992.0, 254.5,image = entry_img)
    entry0 = Entry(bd = 0,bg = "#ffffff",highlightthickness = 0,font = ('Helvetica',18,'normal'))
    entry0.place(x = 782.0, y = 232,width = 420.0,height = 41)

    entry4_bg = canvas.create_image(992.0, 165.5,image = entry_img)
    entry4 = Entry(bd = 0,bg = "#ffffff",highlightthickness = 0,font = ('Helvetica',18,'normal'))
    entry4.place(x = 782.0, y = 143,width = 420.0,height = 41)

    entry1_bg = canvas.create_image(992.0, 343.5,image = entry_img)
    entry1 = Entry(bd = 0,bg = "#ffffff",highlightthickness = 0,font = ('Helvetica',18,'normal'))
    entry1.place(x = 782.0, y = 321,width = 420.0,height = 41)

    entry2_bg = canvas.create_image(992.0, 522.5,image = entry_img)
    entry2 = Entry(bd = 0,bg = "#ffffff",highlightthickness = 0,font = ('Helvetica',18,'normal'))
    

    entry3_bg = canvas.create_image(992.0, 432.5,image = entry_img)
    entry3 = Entry(bd = 0,bg = "#ffffff",highlightthickness = 0,font = ('Helvetica',18,'normal'))
    entry3.place(x = 782.0, y = 410,width = 420.0,height = 41)

    img1 = PhotoImage(file = f"Delivery-Management-System/assets/images/radioyes.png")
    b1 = Button(image = img1,borderwidth = 0,highlightthickness = 0,command = websiter,relief = "flat")
    b1.place(x = 1242, y = 668,width = 22,height = 22)

    label1=Label(root, text="", font = ('Helvetica',18,'normal'), bg="#ffffff", fg="#ff0000")
    label1.place(x = 756.0, y = 570,width = 473.0,height = 44)
    
    root.resizable(False, False)
    root.mainloop()
        
#FIRST MENU ------------------------------------------------
#Starting menu
def first_menu():
    global root
    rooter()
    root=win
    center()
    root.geometry("1298x800")
    root.configure(bg = "#ffffff")
    
    root.title("Bite o'Clock - Main Menu")
    canvas = Canvas(root,bg = "#ffffff",height = 800,width = 1298,bd = 0,highlightthickness = 0,relief = "ridge")
    canvas.place(x = 0, y = 0)

    background_img = PhotoImage(file = f"Delivery-Management-System/assets/images/background 2.png")
    background = canvas.create_image(649.0, 400.0,image=background_img)

    img0 = PhotoImage(file = f"Delivery-Management-System/assets/images/menu1.png")
    b0 = Button(image = img0,borderwidth = 0,highlightthickness = 0,command = north_indiansub,relief = "flat")
    b0.place(x = 27, y = 121,width = 1244,height = 109)

    img1 = PhotoImage(file = f"Delivery-Management-System/assets/images/menu2.png")
    b1 = Button(image = img1,borderwidth = 0,highlightthickness = 0,command = beverages,relief = "flat")
    b1.place(x = 27, y = 657,width = 1244,height = 109)

    img2 = PhotoImage(file = f"Delivery-Management-System/assets/images/img2.png")
    b2 = Button(image = img2,borderwidth = 0,highlightthickness = 0,command = continental,relief = "flat")
    b2.place(x = 27, y = 389,width = 1244,height = 109)

    img3 = PhotoImage(file = f"Delivery-Management-System/assets/images/img3.png")
    b3 = Button(image = img3,borderwidth = 0,highlightthickness = 0,command = soupsal,relief = "flat")
    b3.place(x = 27, y = 523,width = 1244,height = 109)

    img4 = PhotoImage(file = f"Delivery-Management-System/assets/images/img4.png")
    b4 = Button(image = img4,borderwidth = 0,highlightthickness = 0,command = southindian,relief = "flat")
    b4.place(x = 27, y = 255,width = 1244,height = 109)

    root.resizable(False, False)
    root.mainloop()


#NORTH INDIAN SUB MENU--------------------------------------
def north_indiansub():
    global item_count
    global root
    rooter()
    root=win
    center()

    root.geometry("1298x800")
    root.configure(bg = "#ffffff")
    root.title("Bite o'Clock - North Indian")
    
    canvas = Canvas(root,bg = "#ffffff",height = 800,width = 1298,bd = 0,highlightthickness = 0,relief = "ridge")
    canvas.place(x = 0, y = 0)

    background_img = PhotoImage(file = f"Delivery-Management-System/assets/images/background_subn.png")
    background = canvas.create_image(649.0, 400.0,image=background_img)

    img0 = PhotoImage(file = f"Delivery-Management-System/assets/images/cart.png")
    b0 = Button(image = img0,borderwidth = 0,highlightthickness = 0,command = lambda: cart_window("north_indiansub"),relief = "flat")
    b0.place(x = 1133, y = 6,width = 83,height = 71)

    img1 = PhotoImage(file = f"Delivery-Management-System/assets/images/subn_1.png")
    b1 = Button(image = img1,borderwidth = 0,highlightthickness = 0,command = dessert,relief = "flat")
    b1.place(x = 978, y = 83,width = 309,height = 707)

    img2 = PhotoImage(file = f"Delivery-Management-System/assets/images/subn_2.png")
    b2 = Button(image = img2,borderwidth = 0,highlightthickness = 0,command = snacks,relief = "flat")
    b2.place(x = 13, y = 83,width = 309,height = 707)

    img3 = PhotoImage(file = f"Delivery-Management-System/assets/images/subn_3.png")
    b3 = Button(image = img3,borderwidth = 0,highlightthickness = 0,command = combos,relief = "flat")
    b3.place(x = 657, y = 83,width = 309,height = 707)

    img4 = PhotoImage(file = f"Delivery-Management-System/assets/images/subn_4.png")
    b4 = Button(image = img4,borderwidth = 0,highlightthickness = 0,command = maincourse_sub,relief = "flat")
    b4.place(x = 334, y = 83,width = 309,height = 707)

    img5 = PhotoImage(file = f"Delivery-Management-System/assets/images/back.png")
    b5 = Button(image = img5,borderwidth = 0,highlightthickness = 0,command = first_menu,relief = "flat")
    b5.place(x = 13, y = 15,width = 59,height = 59)

    label1=Label(root, text=str(item_count), font = ('Righteous',32,'normal'), bg="#ffffff", fg="#000000")
    label1.place(x = 1215.0, y = 14,width = 55.0,height = 54)
    
    
    root.resizable(False, False)
    root.mainloop()


#NORTH INDIAN SUB MENU (SNACKS)--------------------------------------
def snacks():
    global item_list
    global root
    rooter()
    root=win
    center()
        
    root.geometry("1298x800")
    root.configure(bg = "#ffffff")
    root.title("Bite o'Clock - Snacks")
    
    canvas = Canvas(root,bg = "#ffffff",height = 800,width = 1298,bd = 0,highlightthickness = 0,relief = "ridge")
    canvas.place(x = 0, y = 0)

    background_img = PhotoImage(file = f"Delivery-Management-System/assets/images/background_snacks.png")
    background = canvas.create_image(649.0, 400.0,image=background_img)

    img0 = PhotoImage(file = f"Delivery-Management-System/assets/images/sn0.png")
    b0 = Button(image = img0,borderwidth = 0,highlightthickness = 0,command = lambda: [item_list.append("Aloo Tikki"),itemcounter(label1)],relief = "flat")
    b0.place(x = 19, y = 84,width = 309,height = 350)

    img1 = PhotoImage(file = f"Delivery-Management-System/assets/images/sn1.png")
    b1 = Button(image = img1,borderwidth = 0,highlightthickness = 0,command = lambda: [item_list.append("Samosa With Chutney"),itemcounter(label1)],relief = "flat")
    b1.place(x = 336, y = 84,width = 309,height = 350)

    img2 = PhotoImage(file = f"Delivery-Management-System/assets/images/sn2.png")
    b2 = Button(image = img2,borderwidth = 0,highlightthickness = 0,command = lambda: [item_list.append("Dhokla"),itemcounter(label1)],relief = "flat")
    b2.place(x = 653, y = 84,width = 309,height = 350)

    img3 = PhotoImage(file = f"Delivery-Management-System/assets/images/sn3.png")
    b3 = Button(image = img3,borderwidth = 0,highlightthickness = 0,command = lambda: [item_list.append("Pakora(Assorted)"),itemcounter(label1)],relief = "flat")
    b3.place(x = 970, y = 84,width = 309,height = 350)

    img4 = PhotoImage(file = f"Delivery-Management-System/assets/images/sn4.png")
    b4 = Button(image = img4,borderwidth = 0,highlightthickness = 0,command = lambda: [item_list.append("Chicken Cutlet"),itemcounter(label1)],relief = "flat")
    b4.place(x = 970, y = 441,width = 309,height = 350)

    img5 = PhotoImage(file = f"Delivery-Management-System/assets/images/sn5.png")
    b5 = Button(image = img5,borderwidth = 0,highlightthickness = 0,command = lambda: [item_list.append("Raj Kachori"),itemcounter(label1)],relief = "flat")
    b5.place(x = 336, y = 441,width = 309,height = 350)

    img6 = PhotoImage(file = f"Delivery-Management-System/assets/images/sn6.png")
    b6 = Button(image = img6,borderwidth = 0,highlightthickness = 0,command = lambda: [item_list.append("Chicken Lollipop"),itemcounter(label1)],relief = "flat")
    b6.place(x = 653, y = 441,width = 309,height = 350)

    img7 = PhotoImage(file = f"Delivery-Management-System/assets/images/sn7.png")
    b7 = Button(image = img7,borderwidth = 0,highlightthickness = 0,command = lambda: [item_list.append("Chicken Nugget"),itemcounter(label1)],relief = "flat")
    b7.place(x = 19, y = 441,width = 309,height = 350)

    img8 = PhotoImage(file = f"Delivery-Management-System/assets/images/back.png")
    b8 = Button(image = img8,borderwidth = 0,highlightthickness = 0,command = north_indiansub,relief = "flat")
    b8.place(x = 19, y = 15,width = 59,height = 59)

    img9 = PhotoImage(file = f"Delivery-Management-System/assets/images/cart.png")
    b9 = Button(image = img9,borderwidth = 0,highlightthickness = 0,command = lambda: cart_window("snacks"),relief = "flat")
    b9.place(x = 1133, y = 6,width = 83,height = 71)

    label1=Label(root, text=str(item_count), font = ('Righteous',32,'normal'), bg="#ffffff", fg="#000000")
    label1.place(x = 1215.0, y = 14,width = 55.0,height = 54)

    root.resizable(False, False)
    root.mainloop()

#NORTH INDIAN SUB MENU (MAINCOURSE SUB)--------------------------------------
def maincourse_sub():
    global root
    rooter()
    root=win
    center()

    root.geometry("1298x800")
    root.configure(bg = "#ffffff")
    root.title("Bite o'Clock - Maincourse")
    
    canvas = Canvas(root,bg = "#ffffff",height = 800,width = 1298,bd = 0,highlightthickness = 0,relief = "ridge")
    canvas.place(x = 0, y = 0)

    background_img = PhotoImage(file = f"Delivery-Management-System/assets/images/background_submain.png")
    background = canvas.create_image(649.0, 400.0,image=background_img)

    img0 = PhotoImage(file = f"Delivery-Management-System/assets/images/m0.png")
    b0 = Button(image = img0,borderwidth = 0,highlightthickness = 0,command = mainmaincourse,relief = "flat")
    b0.place(x = 20, y = 91,width = 1257,height = 192)

    img1 = PhotoImage(file = f"Delivery-Management-System/assets/images/m1.png")
    b1 = Button(image = img1,borderwidth = 0,highlightthickness = 0,command = roti,relief = "flat")
    b1.place(x = 20, y = 318,width = 1257,height = 203)

    img2 = PhotoImage(file = f"Delivery-Management-System/assets/images/m2.png")
    b2 = Button(image = img2,borderwidth = 0,highlightthickness = 0,command = nonveg,relief = "flat")
    b2.place(x = 20, y = 556,width = 1257,height = 203)

    img3 = PhotoImage(file = f"Delivery-Management-System/assets/images/back.png")
    b3 = Button(image = img3,borderwidth = 0,highlightthickness = 0,command = north_indiansub,relief = "flat")
    b3.place(x = 0, y = 13,width = 59,height = 59)

    img4 = PhotoImage(file = f"Delivery-Management-System/assets/images/cart.png")
    b4 = Button(image = img4,borderwidth = 0,highlightthickness = 0,command = lambda: cart_window("maincourse_sub"),relief = "flat")
    b4.place(x = 1133, y = 6,width = 83,height = 71)

    label1=Label(root, text=str(item_count), font = ('Righteous',32,'normal'), bg="#ffffff", fg="#000000")
    label1.place(x = 1215.0, y = 14,width = 55.0,height = 54)

    root.resizable(False, False)
    root.mainloop()
 
#NORTH INDIAN SUB MENU (MAINCOURSE SUB)- MEALS----------------------------------
def mainmaincourse():
    global root
    rooter()
    root=win
    center()
    global item_list

    root.geometry("1298x800")
    root.configure(bg = "#ffffff")
    root.title("Bite o'Clock - Jannat-e-Khana")
    
    canvas = Canvas(root,bg = "#ffffff",height = 800,width = 1298,bd = 0,highlightthickness = 0,relief = "ridge")
    canvas.place(x = 0, y = 0)

    background_img = PhotoImage(file = f"Delivery-Management-System/assets/images/background_main.png")
    background = canvas.create_image(649.0, 400.0,image=background_img)

    img0 = PhotoImage(file = f"Delivery-Management-System/assets/images/main0.png")
    b0 = Button(image = img0,borderwidth = 0,highlightthickness = 0,command = lambda: [item_list.append("Chole Bhature"),itemcounter(label1)],relief = "flat")
    b0.place(x = 19, y = 84,width = 309,height = 350)

    img1 = PhotoImage(file = f"Delivery-Management-System/assets/images/main1.png")
    b1 = Button(image = img1,borderwidth = 0,highlightthickness = 0,command = lambda: [item_list.append("Paneer Tikka"),itemcounter(label1)],relief = "flat")
    b1.place(x = 336, y = 84,width = 309,height = 350)

    img2 = PhotoImage(file = f"Delivery-Management-System/assets/images/main2.png")
    b2 = Button(image = img2,borderwidth = 0,highlightthickness = 0,command = lambda: [item_list.append("Pao Bhaji"),itemcounter(label1)],relief = "flat")
    b2.place(x = 653, y = 83,width = 309,height = 352)

    img3 = PhotoImage(file = f"Delivery-Management-System/assets/images/main3.png")
    b3 = Button(image = img3,borderwidth = 0,highlightthickness = 0,command = lambda: [item_list.append("Matar Kulcha"),itemcounter(label1)],relief = "flat")
    b3.place(x = 970, y = 84,width = 309,height = 350)

    img4 = PhotoImage(file = f"Delivery-Management-System/assets/images/main4.png")
    b4 = Button(image = img4,borderwidth = 0,highlightthickness = 0,command = lambda: [item_list.append("Dal Tadka"),itemcounter(label1)],relief = "flat")
    b4.place(x = 970, y = 441,width = 309,height = 350)

    img5 = PhotoImage(file = f"Delivery-Management-System/assets/images/main5.png")
    b5 = Button(image = img5,borderwidth = 0,highlightthickness = 0,command = lambda: [item_list.append("Paneer Butter Masala"),itemcounter(label1)],relief = "flat")
    b5.place(x = 336, y = 441,width = 309,height = 350)

    img6 = PhotoImage(file = f"Delivery-Management-System/assets/images/main6.png")
    b6 = Button(image = img6,borderwidth = 0,highlightthickness = 0,command = lambda: [item_list.append("Dal Makhni"),itemcounter(label1)],relief = "flat")
    b6.place(x = 653, y = 441,width = 309,height = 350)

    img7 = PhotoImage(file = f"Delivery-Management-System/assets/images/main7.png")
    b7 = Button(image = img7,borderwidth = 0,highlightthickness = 0,command = lambda: [item_list.append("Chana Masala"),itemcounter(label1)],relief = "flat")
    b7.place(x = 19, y = 441,width = 309,height = 350)

    img8 = PhotoImage(file = f"Delivery-Management-System/assets/images/back.png")
    b8 = Button(image = img8,borderwidth = 0,highlightthickness = 0,command = maincourse_sub,relief = "flat")
    b8.place(x = 19, y = 15,width = 59,height = 59)

    img9 = PhotoImage(file = f"Delivery-Management-System/assets/images/cart.png")
    b9 = Button(image = img9,borderwidth = 0,highlightthickness = 0,command = lambda: cart_window("mainmaincourse"),relief = "flat")
    b9.place(x = 1133, y = 6,width = 83,height = 71)

    label1=Label(root, text=str(item_count), font = ('Righteous',32,'normal'), bg="#ffffff", fg="#000000")
    label1.place(x = 1215.0, y = 14,width = 55.0,height = 54)

    root.resizable(False, False)
    root.mainloop()

#NORTH INDIAN SUB MENU (MAINCOURSE SUB)- ROTI----------------------------------
def roti():
    global item_list
    global root
    rooter()
    root=win
    center()

    root.geometry("1298x800")
    root.configure(bg = "#ffffff")
    root.title("Bite o'Clock - Roti, Naan & Rice")
    
    canvas = Canvas(root,bg = "#ffffff",height = 800,width = 1298,bd = 0,highlightthickness = 0,relief = "ridge")
    canvas.place(x = 0, y = 0)

    background_img = PhotoImage(file = f"Delivery-Management-System/assets/images/background_roti.png")
    background = canvas.create_image(649.0, 400.0,image=background_img)

    img0 = PhotoImage(file = f"Delivery-Management-System/assets/images/ro0.png")
    b0 = Button(image = img0,borderwidth = 0,highlightthickness = 0,command = lambda: [item_list.append("Aloo Paneer Parantha"),itemcounter(label1)],relief = "flat")
    b0.place(x = 19, y = 84,width = 309,height = 352)

    img1 = PhotoImage(file = f"Delivery-Management-System/assets/images/ro1.png")
    b1 = Button(image = img1,borderwidth = 0,highlightthickness = 0,command = lambda: [item_list.append("Butter Roti"),itemcounter(label1)],relief = "flat")
    b1.place(x = 336, y = 84,width = 308,height = 352)

    img2 = PhotoImage(file = f"Delivery-Management-System/assets/images/ro2.png")
    b2 = Button(image = img2,borderwidth = 0,highlightthickness = 0,command = lambda: [item_list.append("Naan"),itemcounter(label1)],relief = "flat")
    b2.place(x = 653, y = 83,width = 309,height = 352)

    img3 = PhotoImage(file = f"Delivery-Management-System/assets/images/ro3.png")
    b3 = Button(image = img3,borderwidth = 0,highlightthickness = 0,command = lambda: [item_list.append("Lachha Parantha"),itemcounter(label1)],relief = "flat")
    b3.place(x = 970, y = 84,width = 309,height = 352)

    img4 = PhotoImage(file = f"Delivery-Management-System/assets/images/ro4.png")
    b4 = Button(image = img4,borderwidth = 0,highlightthickness = 0,command = lambda: [item_list.append("Veg Raita"),itemcounter(label1)],relief = "flat")
    b4.place(x = 970, y = 441,width = 309,height = 349)

    img5 = PhotoImage(file = f"Delivery-Management-System/assets/images/ro5.png")
    b5 = Button(image = img5,borderwidth = 0,highlightthickness = 0,command = lambda: [item_list.append("Jeera Rice"),itemcounter(label1)],relief = "flat")
    b5.place(x = 336, y = 441,width = 308,height = 349)

    img6 = PhotoImage(file = f"Delivery-Management-System/assets/images/ro6.png")
    b6 = Button(image = img6,borderwidth = 0,highlightthickness = 0,command = lambda: [item_list.append("Veg Pulao"),itemcounter(label1)],relief = "flat")
    b6.place(x = 653, y = 441,width = 309,height = 349)

    img7 = PhotoImage(file = f"Delivery-Management-System/assets/images/ro7.png")
    b7 = Button(image = img7,borderwidth = 0,highlightthickness = 0,command = lambda: [item_list.append("Plain Rice"),itemcounter(label1)],relief = "flat")
    b7.place(x = 19, y = 441,width = 309,height = 349)

    img8 = PhotoImage(file = f"Delivery-Management-System/assets/images/back.png")
    b8 = Button(image = img8,borderwidth = 0,highlightthickness = 0,command = maincourse_sub,relief = "flat")
    b8.place(x = 19, y = 15,width = 59,height = 59)

    img9 = PhotoImage(file = f"Delivery-Management-System/assets/images/cart.png")
    b9 = Button(image = img9,borderwidth = 0,highlightthickness = 0,command = lambda: cart_window("roti"),relief = "flat")
    b9.place(x = 1133, y = 6,width = 83,height = 71)

    label1=Label(root, text=str(item_count), font = ('Righteous',32,'normal'), bg="#ffffff", fg="#000000")
    label1.place(x = 1215.0, y = 14,width = 55.0,height = 54)

    root.resizable(False, False)
    root.mainloop()

#NORTH INDIAN SUB MENU (MAINCOURSE SUB)- NONVEG----------------------------------
def nonveg():
    global item_list
    global root
    rooter()
    root=win
    center()

    root.geometry("1298x800")
    root.configure(bg = "#ffffff")
    root.title("Bite o'Clock - Non-Vegetarian")
    
    canvas = Canvas(root,bg = "#ffffff",height = 800,width = 1298,bd = 0,highlightthickness = 0,relief = "ridge")
    canvas.place(x = 0, y = 0)

    background_img = PhotoImage(file = f"Delivery-Management-System/assets/images/background_nv.png")
    background = canvas.create_image(649.0, 400.0,image=background_img)

    img0 = PhotoImage(file = f"Delivery-Management-System/assets/images/nv0.png")
    b0 = Button(image = img0,borderwidth = 0,highlightthickness = 0,command = lambda: [item_list.append("Rogan Josh"),itemcounter(label1)],relief = "flat")
    b0.place(x = 19, y = 84,width = 309,height = 350)

    img1 = PhotoImage(file = f"Delivery-Management-System/assets/images/nv1.png")
    b1 = Button(image = img1,borderwidth = 0,highlightthickness = 0,command = lambda: [item_list.append("Nihari Gosht"),itemcounter(label1)],relief = "flat")
    b1.place(x = 336, y = 84,width = 309,height = 350)

    img2 = PhotoImage(file = f"Delivery-Management-System/assets/images/nv2.png")
    b2 = Button(image = img2,borderwidth = 0,highlightthickness = 0,command = lambda: [item_list.append("Butter Chicken"),itemcounter(label1)],relief = "flat")
    b2.place(x = 653, y = 83,width = 309,height = 352)

    img3 = PhotoImage(file = f"Delivery-Management-System/assets/images/nv3.png")
    b3 = Button(image = img3,borderwidth = 0,highlightthickness = 0,command = lambda: [item_list.append("Mutton Curry"),itemcounter(label1)],relief = "flat")
    b3.place(x = 970, y = 84,width = 309,height = 350)

    img4 = PhotoImage(file = f"Delivery-Management-System/assets/images/nv4.png")
    b4 = Button(image = img4,borderwidth = 0,highlightthickness = 0,command = lambda: [item_list.append("Chicken Dum Biryani"),itemcounter(label1)],relief = "flat")
    b4.place(x = 970, y = 441,width = 309,height = 350)

    img5 = PhotoImage(file = f"Delivery-Management-System/assets/images/nv5.png")
    b5 = Button(image = img5,borderwidth = 0,highlightthickness = 0,command = lambda: [item_list.append("Rajasthani Laal Maas"),itemcounter(label1)],relief = "flat")
    b5.place(x = 336, y = 441,width = 309,height = 350)

    img6 = PhotoImage(file = f"Delivery-Management-System/assets/images/nv6.png")
    b6 = Button(image = img6,borderwidth = 0,highlightthickness = 0,command = lambda: [item_list.append("Chicken Shawarma"),itemcounter(label1)],relief = "flat")
    b6.place(x = 653, y = 441,width = 309,height = 350)

    img7 = PhotoImage(file = f"Delivery-Management-System/assets/images/nv7.png")
    b7 = Button(image = img7,borderwidth = 0,highlightthickness = 0,command = lambda: [item_list.append("Prawn Curry"),itemcounter(label1)],relief = "flat")
    b7.place(x = 19, y = 441,width = 309,height = 350)

    img8 = PhotoImage(file = f"Delivery-Management-System/assets/images/back.png")
    b8 = Button(image = img8,borderwidth = 0,highlightthickness = 0,command = maincourse_sub,relief = "flat")
    b8.place(x = 19, y = 15,width = 59,height = 59)

    img9 = PhotoImage(file = f"Delivery-Management-System/assets/images/cart.png")
    b9 = Button(image = img9,borderwidth = 0,highlightthickness = 0,command = lambda: cart_window("nonveg"),relief = "flat")
    b9.place(x = 1133, y = 6,width = 83,height = 71)

    label1=Label(root, text=str(item_count), font = ('Righteous',32,'normal'), bg="#ffffff", fg="#000000")
    label1.place(x = 1215.0, y = 14,width = 55.0,height = 54)

    root.resizable(False, False)
    root.mainloop()

#NORTH INDIAN SUB MENU (MAINCOURSE SUB)- COMBOS----------------------------------
def combos():
    global item_list
    global root
    rooter()
    root=win
    center()
        
    root.geometry("1298x800")
    root.configure(bg = "#ffffff")
    root.title("Bite o'Clock - Combos")
    
    canvas = Canvas(root,bg = "#ffffff",height = 800,width = 1298,bd = 0,highlightthickness = 0,relief = "ridge")
    canvas.place(x = 0, y = 0)

    background_img = PhotoImage(file = f"Delivery-Management-System/assets/images/background_combos.png")
    background = canvas.create_image(649.0, 400.0,image=background_img)

    img0 = PhotoImage(file = f"Delivery-Management-System/assets/images/cm0.png")
    b0 = Button(image = img0,borderwidth = 0,highlightthickness = 0,command = lambda: [item_list.append("Special Thali"),itemcounter(label1)],relief = "flat")
    b0.place(x = 19, y = 84,width = 309,height = 700)

    img1 = PhotoImage(file = f"Delivery-Management-System/assets/images/cm1.png")
    b1 = Button(image = img1,borderwidth = 0,highlightthickness = 0,command = lambda: [item_list.append("Deluxe Thali"),itemcounter(label1)],relief = "flat")
    b1.place(x = 353, y = 85,width = 309,height = 700)

    img2 = PhotoImage(file = f"Delivery-Management-System/assets/images/cm2.png")
    b2 = Button(image = img2,borderwidth = 0,highlightthickness = 0,command = lambda: [item_list.append("Rajma Rice Bowl"),itemcounter(label1)],relief = "flat")
    b2.place(x = 687, y = 85,width = 593,height = 169)

    img3 = PhotoImage(file = f"Delivery-Management-System/assets/images/cm3.png")
    b3 = Button(image = img3,borderwidth = 0,highlightthickness = 0,command = lambda: [item_list.append("Chicken Rice Bowl"),itemcounter(label1)],relief = "flat")
    b3.place(x = 687, y = 605,width = 593,height = 170)

    img4 = PhotoImage(file = f"Delivery-Management-System/assets/images/cm4.png")
    b4 = Button(image = img4,borderwidth = 0,highlightthickness = 0,command = lambda: [item_list.append("Manchurian Rice Bowl"),itemcounter(label1)],relief = "flat")
    b4.place(x = 687, y = 432,width = 593,height = 169)

    img5 = PhotoImage(file = f"Delivery-Management-System/assets/images/cm5.png")
    b5 = Button(image = img5,borderwidth = 0,highlightthickness = 0,command = lambda: [item_list.append("Choley Rice Bowl"),itemcounter(label1)],relief = "flat")
    b5.place(x = 687, y = 259,width = 593,height = 169)

    img6 = PhotoImage(file = f"Delivery-Management-System/assets/images/cart.png")
    b6 = Button(image = img6,borderwidth = 0,highlightthickness = 0,command =lambda: cart_window("combos"),relief = "flat")
    b6.place(x = 1133, y = 6,width = 83,height = 71)

    img7 = PhotoImage(file = f"Delivery-Management-System/assets/images/back.png")
    b7 = Button(image = img7,borderwidth = 0,highlightthickness = 0,command = north_indiansub,relief = "flat")
    b7.place(x = 19, y = 15,width = 59,height = 59)

    label1=Label(root, text=str(item_count), font = ('Righteous',32,'normal'), bg="#ffffff", fg="#000000")
    label1.place(x = 1215.0, y = 14,width = 55.0,height = 54)

    root.resizable(False, False)
    root.mainloop()

#NORTH INDIAN SUB MENU (MAINCOURSE SUB)- DESSSERT----------------------------------
def dessert():
    global item_list
    global root
    rooter()
    root=win
    center()

    root.geometry("1298x800")
    root.configure(bg = "#ffffff")
    root.title("Bite o'Clock - Desserts")
    
    canvas = Canvas(root,bg = "#ffffff",height = 800,width = 1298,bd = 0,highlightthickness = 0,relief = "ridge")
    canvas.place(x = 0, y = 0)

    background_img = PhotoImage(file = f"Delivery-Management-System/assets/images/background_dessert.png")
    background = canvas.create_image(649.0, 400.0,image=background_img)

    img0 = PhotoImage(file = f"Delivery-Management-System/assets/images/de0.png")
    b0 = Button(image = img0,borderwidth = 0,highlightthickness = 0,command = lambda: [item_list.append("Ras Malai"),itemcounter(label1)],relief = "flat")
    b0.place(x = 19, y = 84,width = 309,height = 352)

    img1 = PhotoImage(file = f"Delivery-Management-System/assets/images/de1.png")
    b1 = Button(image = img1,borderwidth = 0,highlightthickness = 0,command = lambda: [item_list.append("Rasgulla"),itemcounter(label1)],relief = "flat")
    b1.place(x = 336, y = 84,width = 308,height = 352)

    img2 = PhotoImage(file = f"Delivery-Management-System/assets/images/de2.png")
    b2 = Button(image = img2,borderwidth = 0,highlightthickness = 0,command = lambda: [item_list.append("Gulab Jamun"),itemcounter(label1)],relief = "flat")
    b2.place(x = 653, y = 83,width = 309,height = 352)

    img3 = PhotoImage(file = f"Delivery-Management-System/assets/images/de3.png")
    b3 = Button(image = img3,borderwidth = 0,highlightthickness = 0,command = lambda: [item_list.append("Moong Dal Halwa"),itemcounter(label1)],relief = "flat")
    b3.place(x = 970, y = 84,width = 309,height = 352)

    img4 = PhotoImage(file = f"Delivery-Management-System/assets/images/de4.png")
    b4 = Button(image = img4,borderwidth = 0,highlightthickness = 0,command = lambda: [item_list.append("Pastry(Assorted)"),itemcounter(label1)],relief = "flat")
    b4.place(x = 970, y = 441,width = 309,height = 349)

    img5 = PhotoImage(file = f"Delivery-Management-System/assets/images/de5.png")
    b5 = Button(image = img5,borderwidth = 0,highlightthickness = 0,command = lambda: [item_list.append("Imarti"),itemcounter(label1)],relief = "flat")
    b5.place(x = 336, y = 441,width = 309,height = 349)

    img6 = PhotoImage(file = f"Delivery-Management-System/assets/images/de6.png")
    b6 = Button(image = img6,borderwidth = 0,highlightthickness = 0,command = lambda: [item_list.append("Kesar Kheer"),itemcounter(label1)],relief = "flat")
    b6.place(x = 653, y = 441,width = 309,height = 349)

    img7 = PhotoImage(file = f"Delivery-Management-System/assets/images/de7.png")
    b7 = Button(image = img7,borderwidth = 0,highlightthickness = 0,command = lambda: [item_list.append("Kesar Kulfi"),itemcounter(label1)],relief = "flat")
    b7.place(x = 19, y = 441,width = 309,height = 349)

    img8 = PhotoImage(file = f"Delivery-Management-System/assets/images/back.png")
    b8 = Button(image = img8,borderwidth = 0,highlightthickness = 0,command = north_indiansub,relief = "flat")
    b8.place(x = 19, y = 15,width = 59,height = 59)

    img9 = PhotoImage(file = f"Delivery-Management-System/assets/images/cart.png")
    b9 = Button(image = img9,borderwidth = 0,highlightthickness = 0,command = lambda: cart_window("dessert"),relief = "flat")
    b9.place(x = 1133, y = 6,width = 83,height = 71)

    label1=Label(root, text=str(item_count), font = ('Righteous',32,'normal'), bg="#ffffff", fg="#000000")
    label1.place(x = 1215.0, y = 14,width = 55.0,height = 54)

    root.resizable(False, False)
    root.mainloop()

    
#SOUTH INDIAN MENU--------------------------------------
def southindian():
    global item_list
    global root
    rooter()
    root=win
    center()
    
    root.geometry("1298x800")
    root.configure(bg = "#ffffff")
    root.title("Bite o'Clock - South Indian")
    
    canvas = Canvas(root,bg = "#ffffff",height = 800,width = 1298,bd = 0,highlightthickness = 0,relief = "ridge")
    canvas.place(x = 0, y = 0)

    background_img = PhotoImage(file = f"Delivery-Management-System/assets/images/background_south.png")
    background = canvas.create_image(649.0, 400.0,image=background_img)

    img0 = PhotoImage(file = f"Delivery-Management-System/assets/images/south0.png")
    b0 = Button(image = img0,borderwidth = 0,highlightthickness = 0,command = lambda: [item_list.append("Rawa Masala Dosa"),itemcounter(label1)],relief = "flat")
    b0.place(x = 19, y = 84,width = 309,height = 350)

    img1 = PhotoImage(file = f"Delivery-Management-System/assets/images/south1.png")
    b1 = Button(image = img1,borderwidth = 0,highlightthickness = 0,command = lambda: [item_list.append("Sambar Dosa"),itemcounter(label1)],relief = "flat")
    b1.place(x = 336, y = 84,width = 309,height = 350)

    img2 = PhotoImage(file = f"Delivery-Management-System/assets/images/south2.png")
    b2 = Button(image = img2,borderwidth = 0,highlightthickness = 0,command = lambda: [item_list.append("Sambar Idli"),itemcounter(label1)],relief = "flat")
    b2.place(x = 653, y = 83,width = 309,height = 352)

    img3 = PhotoImage(file = f"Delivery-Management-System/assets/images/south3.png")
    b3 = Button(image = img3,borderwidth = 0,highlightthickness = 0,command = lambda: [item_list.append("South Indian Platter"),itemcounter(label1)],relief = "flat")
    b3.place(x = 970, y = 84,width = 309,height = 708)

    img4 = PhotoImage(file = f"Delivery-Management-System/assets/images/south4.png")
    b4 = Button(image = img4,borderwidth = 0,highlightthickness = 0,command = lambda: [item_list.append("Masala Dosa"),itemcounter(label1)],relief = "flat")
    b4.place(x = 336, y = 441,width = 309,height = 350)

    img5 = PhotoImage(file = f"Delivery-Management-System/assets/images/south5.png")
    b5 = Button(image = img5,borderwidth = 0,highlightthickness = 0,command = lambda: [item_list.append("Chicken Dosa"),itemcounter(label1)],relief = "flat")

    b5.place(x = 653, y = 441,width = 309,height = 350)

    img6 = PhotoImage(file = f"Delivery-Management-System/assets/images/south6.png")
    b6 = Button(image = img6,borderwidth = 0,highlightthickness = 0,command = lambda: [item_list.append("Plain Dosa"),itemcounter(label1)],relief = "flat")
    b6.place(x = 19, y = 441,width = 309,height = 350)

    img7 = PhotoImage(file = f"Delivery-Management-System/assets/images/back.png")
    b7 = Button(image = img7,borderwidth = 0,highlightthickness = 0,command = first_menu,relief = "flat")
    b7.place(x = 19, y = 15,width = 59,height = 59)

    img8 = PhotoImage(file = f"Delivery-Management-System/assets/images/cart.png")
    b8 = Button(image = img8,borderwidth = 0,highlightthickness = 0,command = lambda: cart_window("southindian"),relief = "flat")
    b8.place(x = 1133, y = 6,width = 83,height = 71)

    label1=Label(root, text=str(item_count), font = ('Righteous',32,'normal'), bg="#ffffff", fg="#000000")
    label1.place(x = 1215.0, y = 14,width = 55.0,height = 54)

    root.resizable(False, False)
    root.mainloop()


#CONTINENTAL MENU--------------------------------------
def continental():
    global item_list
    global root
    rooter()
    root=win
    center()
        
    root.geometry("1298x800")
    root.configure(bg = "#ffffff")
    root.title("Bite o'Clock - Continental")
    
    canvas = Canvas(root,bg = "#ffffff",height = 800,width = 1298,bd = 0,highlightthickness = 0,relief = "ridge")
    canvas.place(x = 0, y = 0)

    background_img = PhotoImage(file = f"Delivery-Management-System/assets/images/background_con.png")
    background = canvas.create_image(649.0, 400.0,image=background_img)

    img0 = PhotoImage(file = f"Delivery-Management-System/assets/images/con0.png")
    b0 = Button(image = img0,borderwidth = 0,highlightthickness = 0,command = lambda: [item_list.append("Pizza"),itemcounter(label1)],relief = "flat")
    b0.place(x = 19, y = 84,width = 309,height = 350)

    img1 = PhotoImage(file = f"Delivery-Management-System/assets/images/con1.png")
    b1 = Button(image = img1,borderwidth = 0,highlightthickness = 0,command = lambda: [item_list.append("Crispy Calamari Rings"),itemcounter(label1)],relief = "flat")
    b1.place(x = 336, y = 84,width = 309,height = 350)

    img2 = PhotoImage(file = f"Delivery-Management-System/assets/images/con2.png")
    b2 = Button(image = img2,borderwidth = 0,highlightthickness = 0,command = lambda: [item_list.append("Paneer Steak"),itemcounter(label1)],relief = "flat")
    b2.place(x = 653, y = 83,width = 309,height = 352)

    img3 = PhotoImage(file = f"Delivery-Management-System/assets/images/con3.png")
    b3 = Button(image = img3,borderwidth = 0,highlightthickness = 0,command = lambda: [item_list.append("Sausage Pepper Burger"),itemcounter(label1)],relief = "flat")
    b3.place(x = 970, y = 84,width = 309,height = 350)

    img4 = PhotoImage(file = f"Delivery-Management-System/assets/images/con4.png")
    b4 = Button(image = img4,borderwidth = 0,highlightthickness = 0,command = lambda: [item_list.append("Walnut Pudding"),itemcounter(label1)],relief = "flat")
    b4.place(x = 970, y = 441,width = 309,height = 350)

    img5 = PhotoImage(file = f"Delivery-Management-System/assets/images/con5.png")
    b5 = Button(image = img5,borderwidth = 0,highlightthickness = 0,command = lambda: [item_list.append("Corn Toasties"),itemcounter(label1)],relief = "flat")
    b5.place(x = 336, y = 441,width = 309,height = 350)

    img6 = PhotoImage(file = f"Delivery-Management-System/assets/images/con6.png")
    b6 = Button(image = img6,borderwidth = 0,highlightthickness = 0,command = lambda: [item_list.append("Chocolate Pudding"),itemcounter(label1)],relief = "flat")
    b6.place(x = 653, y = 441,width = 309,height = 350)

    img7 = PhotoImage(file = f"Delivery-Management-System/assets/images/con7.png")
    b7 = Button(image = img7,borderwidth = 0,highlightthickness = 0,command = lambda: [item_list.append("Mutton Stew"),itemcounter(label1)],relief = "flat")
    b7.place(x = 19, y = 441,width = 309,height = 350)

    img8 = PhotoImage(file = f"Delivery-Management-System/assets/images/back.png")
    b8 = Button(image = img8,borderwidth = 0,highlightthickness = 0,command = first_menu,relief = "flat")
    b8.place(x = 19, y = 15,width = 59,height = 59)

    img9 = PhotoImage(file = f"Delivery-Management-System/assets/images/cart.png")
    b9 = Button(image = img9,borderwidth = 0,highlightthickness = 0,command = lambda: cart_window("continental"),relief = "flat")
    b9.place(x = 1133, y = 6,width = 83,height = 71)

    label1=Label(root, text=str(item_count), font = ('Righteous',32,'normal'), bg="#ffffff", fg="#000000")
    label1.place(x = 1215.0, y = 14,width = 55.0,height = 54)

    root.resizable(False, False)
    root.mainloop()

#BEVERAGES MENU--------------------------------------
def beverages():
    global item_list
    global root
    rooter()
    root=win
    center()
    
    root.geometry("1298x800")
    root.configure(bg = "#ffffff")
    root.title("Bite o'Clock - Beverages")
    
    canvas = Canvas(root,bg = "#ffffff",height = 800,width = 1298,bd = 0,highlightthickness = 0,relief = "ridge")
    canvas.place(x = 0, y = 0)

    background_img = PhotoImage(file = f"Delivery-Management-System/assets/images/background_bev.png")
    background = canvas.create_image(649.0, 400.0,image=background_img)

    img0 = PhotoImage(file = f"Delivery-Management-System/assets/images/bev0.png")
    b0 = Button(image = img0,borderwidth = 0,highlightthickness = 0,command = lambda: [item_list.append("Fresh Lime Soda"),itemcounter(label1)],relief = "flat")
    b0.place(x = 19, y = 84,width = 309,height = 350)

    img1 = PhotoImage(file = f"Delivery-Management-System/assets/images/bev1.png")
    b1 = Button(image = img1,borderwidth = 0,highlightthickness = 0,command = lambda: [item_list.append("Coffee(Espresso)"),itemcounter(label1)],relief = "flat")
    b1.place(x = 336, y = 84,width = 309,height = 350)

    img2 = PhotoImage(file = f"Delivery-Management-System/assetsimages/vbev2.png")
    b2 = Button(image = img2,borderwidth = 0,highlightthickness = 0,command = lambda: [item_list.append("Water"),itemcounter(label1)],relief = "flat")
    b2.place(x = 653, y = 83,width = 309,height = 352)

    img3 = PhotoImage(file = f"Delivery-Management-System/assets/images/bev3.png")
    b3 = Button(image = img3,borderwidth = 0,highlightthickness = 0,command = lambda: [item_list.append("Coca Cola"),itemcounter(label1)],relief = "flat")
    b3.place(x = 970, y = 84,width = 309,height = 350)

    img4 = PhotoImage(file = f"Delivery-Management-System/assets/images/bev4.png")
    b4 = Button(image = img4,borderwidth = 0,highlightthickness = 0,command = lambda: [item_list.append("Mixed Fruit Juice"),itemcounter(label1)],relief = "flat")
    b4.place(x = 970, y = 441,width = 309,height = 350)

    img5 = PhotoImage(file = f"Delivery-Management-System/assets/images/bev5.png")
    b5 = Button(image = img5,borderwidth = 0,highlightthickness = 0,command = lambda: [item_list.append("Hot Chocolate"),itemcounter(label1)],relief = "flat")
    b5.place(x = 336, y = 441,width = 309,height = 350)

    img6 = PhotoImage(file = f"Delivery-Management-System/assets/images/bev6.png")
    b6 = Button(image = img6,borderwidth = 0,highlightthickness = 0,command = lambda: [item_list.append("Classic Mojito"),itemcounter(label1)],relief = "flat")
    b6.place(x = 653, y = 441,width = 309,height = 350)

    img7 = PhotoImage(file = f"Delivery-Management-System/assets/images/bev7.png")
    b7 = Button(image = img7,borderwidth = 0,highlightthickness = 0,command = lambda: [item_list.append("Tea"),itemcounter(label1)],relief = "flat")
    b7.place(x = 19, y = 441,width = 309,height = 350)

    img8 = PhotoImage(file = f"Delivery-Management-System/assets/images/back.png")
    b8 = Button(image = img8,borderwidth = 0,highlightthickness = 0,command = first_menu,relief = "flat")
    b8.place( x = 19, y = 15,width = 59,height = 59)

    img9 = PhotoImage(file = f"Delivery-Management-System/assets/images/cart.png")
    b9 = Button(image = img9,borderwidth = 0,highlightthickness = 0,command = lambda: cart_window("beverages"),relief = "flat")
    b9.place(x = 1133, y = 6,width = 83,height = 71)

    label1=Label(root, text=str(item_count), font = ('Righteous',32,'normal'), bg="#ffffff", fg="#000000")
    label1.place(x = 1215.0, y = 14,width = 55.0,height = 54)

    root.resizable(False, False)
    root.mainloop()

#SOUPS AND SALADS SUB MENU--------------------------------------
def soupsal():
    global root    
    rooter()
    root=win
    center()
        
    root.geometry("1298x800")
    root.configure(bg = "#ffffff")
    root.title("Bite o'Clock - Soups & Salads")
    
    canvas = Canvas(root,bg = "#ffffff",height = 800,width = 1298,bd = 0,highlightthickness = 0,relief = "ridge")
    canvas.place(x = 0, y = 0)

    background_img = PhotoImage(file = f"Delivery-Management-System/assets/images/background_ss.png")
    background = canvas.create_image(647.0, 400.0,image=background_img)

    img0 = PhotoImage(file = f"Delivery-Management-System/assets/images/back.png")
    b0 = Button(image = img0,borderwidth = 0,highlightthickness = 0,command = first_menu,relief = "flat")
    b0.place(x = 19, y = 15,width = 59,height = 59)

    img1 = PhotoImage(file = f"Delivery-Management-System/assets/images/cart.png")
    b1 = Button(image = img1,borderwidth = 0,highlightthickness = 0,command = lambda: cart_window("soupsal"),relief = "flat")
    b1.place(x = 1133, y = 6,width = 83,height = 71)

    img2 = PhotoImage(file = f"Delivery-Management-System/assets/images/ss2.png")
    b2 = Button(image = img2,borderwidth = 0,highlightthickness = 0,command = soupmenu,relief = "flat")
    b2.place(x = 14, y = 92,width = 630,height = 690)

    img3 = PhotoImage(file = f"Delivery-Management-System/assets/images/ss3.png")
    b3 = Button(image = img3,borderwidth = 0,highlightthickness = 0,command = saladmenu,relief = "flat")
    b3.place(x = 654, y = 92,width = 630,height = 690)

    label1=Label(root, text=str(item_count), font = ('Righteous',32,'normal'), bg="#ffffff", fg="#000000")
    label1.place(x = 1215.0, y = 14,width = 55.0,height = 54)

    root.resizable(False, False)
    root.mainloop()

#SOUPS MENU--------------------------------------
def soupmenu():
    global root
    rooter()
    root=win
    center()
    global item_list

    root.geometry("1298x800")
    root.configure(bg = "#ffffff")
    root.title("Bite o'Clock - Soups")
    
    canvas = Canvas(root,bg = "#ffffff",height = 800,width = 1298,bd = 0,highlightthickness = 0,relief = "ridge")
    canvas.place(x = 0, y = 0)

    background_img = PhotoImage(file = f"Delivery-Management-System/assets/images/background_soup.png")
    background = canvas.create_image(649.0, 400.0,image=background_img)

    img0 = PhotoImage(file = f"Delivery-Management-System/assets/images/soup0.png")
    b0 = Button(image = img0,borderwidth = 0,highlightthickness = 0,command = lambda: [item_list.append("Tomato Soup"),itemcounter(label1)],relief = "flat")
    b0.place(x = 19, y = 84,width = 309,height = 350)

    img1 = PhotoImage(file = f"Delivery-Management-System/assets/images/soup1.png")
    b1 = Button(image = img1,borderwidth = 0,highlightthickness = 0,command = lambda: [item_list.append("Lentil Soup"),itemcounter(label1)],relief = "flat")
    b1.place(x = 336, y = 84,width = 309,height = 350)

    img2 = PhotoImage(file = f"Delivery-Management-System/assets/images/soup2.png")
    b2 = Button(image = img2,borderwidth = 0,highlightthickness = 0,command = lambda: [item_list.append("French Onion Soup"),itemcounter(label1)],relief = "flat")
    b2.place(x = 653, y = 83,width = 309,height = 352)

    img3 = PhotoImage(file = f"Delivery-Management-System/assets/images/soup3.png")
    b3 = Button(image = img3,borderwidth = 0,highlightthickness = 0,command = lambda: [item_list.append("Sweet Corn Soup"),itemcounter(label1)],relief = "flat")
    b3.place(x = 970, y = 84,width = 309,height = 350)

    img4 = PhotoImage(file = f"Delivery-Management-System/assets/images/soup4.png")
    b4 = Button(image = img4,borderwidth = 0,highlightthickness = 0,command = lambda: [item_list.append("Hot And Sour Soup"),itemcounter(label1)],relief = "flat")
    b4.place(x = 970, y = 441,width = 309,height = 350)

    img5 = PhotoImage(file = f"Delivery-Management-System/assets/images/soup5.png")
    b5 = Button(image = img5,borderwidth = 0,highlightthickness = 0,command = lambda: [item_list.append("Chicken and Rice Soup"),itemcounter(label1)],relief = "flat")
    b5.place(x = 336, y = 441,width = 309,height = 350)

    img6 = PhotoImage(file = f"Delivery-Management-System/assets/images/soup6.png")
    b6 = Button(image = img6,borderwidth = 0,highlightthickness = 0,command = lambda: [item_list.append("Chicken Noodle Soup"),itemcounter(label1)],relief = "flat")
    b6.place(x = 653, y = 441,width = 309,height = 350)

    img7 = PhotoImage(file = f"Delivery-Management-System/assets/images/soup7.png")
    b7 = Button(image = img7,borderwidth = 0,highlightthickness = 0,command = lambda: [item_list.append("Pea Soup"),itemcounter(label1)],relief = "flat")
    b7.place(x = 19, y = 441,width = 309,height = 350)

    img8 = PhotoImage(file = f"Delivery-Management-System/assets/images/back.png")
    b8 = Button(image = img8,borderwidth = 0,highlightthickness = 0,command = soupsal,relief = "flat")
    b8.place(x = 19, y = 15,width = 59,height = 59)

    img9 = PhotoImage(file = f"Delivery-Management-System/assets/images/cart.png")
    b9 = Button(image = img9,borderwidth = 0,highlightthickness = 0,command =lambda: cart_window("soup") ,relief = "flat")
    b9.place(x = 1133, y = 6,width = 83,height = 71)

    label1=Label(root, text=str(item_count), font = ('Righteous',32,'normal'), bg="#ffffff", fg="#000000")
    label1.place(x = 1215.0, y = 14,width = 55.0,height = 54)

    root.resizable(False, False)
    root.mainloop()

#SALADS MENU--------------------------------------
def saladmenu():
    global item_list
    global root
    rooter()
    root=win
    center()
    
    root.geometry("1298x800")
    root.configure(bg = "#ffffff")
    root.title("Bite o'Clock - Salads")
    
    canvas = Canvas(root,bg = "#ffffff",height = 800,width = 1298,bd = 0,highlightthickness = 0,relief = "ridge")
    canvas.place(x = 0, y = 0)

    background_img = PhotoImage(file = f"Delivery-Management-System/assets/images/background_salad.png")
    background = canvas.create_image(649.0, 400.0,image=background_img)

    img0 = PhotoImage(file = f"Delivery-Management-System/assets/images/salad0.png")
    b0 = Button(image = img0,borderwidth = 0,highlightthickness = 0,command = lambda: [item_list.append("Summer Asian Slaw"),itemcounter(label1)],relief = "flat")
    b0.place(x = 19, y = 87,width = 309,height = 706)

    img1 = PhotoImage(file = f"Delivery-Management-System/assets/images/salad1.png")
    b1 = Button(image = img1,borderwidth = 0,highlightthickness = 0,command = lambda: [item_list.append("Broccoli Salad"),itemcounter(label1)],relief = "flat")
    b1.place(x = 336, y = 87,width = 309,height = 706)

    img2 = PhotoImage(file = f"Delivery-Management-System/assets/images/salad2.png")
    b2 = Button(image = img2,borderwidth = 0,highlightthickness = 0,command = lambda: [item_list.append("Pasta Salad"),itemcounter(label1)],relief = "flat")
    b2.place(x = 653, y = 87,width = 309,height = 706)

    img3 = PhotoImage(file = f"Delivery-Management-System/assets/images/salad3.png")
    b3 = Button(image = img3,borderwidth = 0,highlightthickness = 0,command = lambda: [item_list.append("Broccoli Pasta Salad"),itemcounter(label1)],relief = "flat")
    b3.place(x = 970, y = 87,width = 312,height = 706)

    img4 = PhotoImage(file = f"Delivery-Management-System/assets/images/back.png")
    b4 = Button(image = img4,borderwidth = 0,highlightthickness = 0,command = soupsal,relief = "flat")
    b4.place(x = 19, y = 15,width = 59,height = 59)

    img5 = PhotoImage(file = f"Delivery-Management-System/assets/images/cart.png")
    b5 = Button(image = img5,borderwidth = 0,highlightthickness = 0,command = lambda: cart_window("salad"),relief = "flat")
    b5.place(x = 1133, y = 6,width = 83,height = 71)

    label1=Label(root, text=str(item_count), font = ('Righteous',32,'normal'), bg="#ffffff", fg="#000000")
    label1.place(x = 1215.0, y = 14,width = 55.0,height = 54)

    root.resizable(False, False)
    root.mainloop()

def cart_window(back_var):
    root.destroy()
    global item_list
    item_dict={}
    for i in item_list:
        if i in item_dict.keys():
            item_dict[i]+=1
        else:
            item_dict[i]=1
    for i in item_dict.keys():
        if item_dict[i]>12:
            item_dict[i]=12
    Cartwindow.creator(item_dict)
    


