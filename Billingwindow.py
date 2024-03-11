from tkinter import *
import os
import pygame
from pygame import mixer
import Luhn
import Checkoutwindow
import Deliverystatus
import Menuprices
import random
import csv

pygame.init()

global y
y=""
for i in range(4):
    y+=str(random.randint(0,10))

def billing(total,final,items,name):
    global val,totalp,finalp,data,cust_name
    data=items
    cust_name=name
    totalp=total
    finalp=final
    val="POD"
    def to_order():
        global val
        if val=="Card":
            if entry2.get()=="" or entry3.get()=="" or entry4.get()=="":
                label2.configure(text="Please enter the required information")
                j=mixer.Sound("Delivery-Management-System/assets/sounds/Error Tone.mp3")
                j.play()
            elif (entry2.get()).isdigit()==False:
                label2.configure(text="Card Number needs to be a number")
                j=mixer.Sound("Delivery-Management-System/assets/sounds/Error Tone.mp3")
                j.play()
            elif (entry4.get()).isdigit()==False:
                label2.configure(text="CVV needs to be a number")
                j=mixer.Sound("Delivery-Management-System/assets/sounds/Error Tone.mp3")
                j.play()
            else:
                check=Luhn.validator(entry2.get(),entry3.get())
                if check==False:
                    label2.configure(text="Card Validation Failed")
                    j=mixer.Sound("Delivery-Management-System/assets/sounds/Error Tone.mp3")
                    j.play()
                elif check=="Invalid":
                    label2.configure(text="Invalid Card Type")
                    j=mixer.Sound("Delivery-Management-System/assets/sounds/Error Tone.mp3")
                    j.play()
                else:
                    total_price=0
                    fname=f"Order_Invoice_{cust_name}_{y}.csv"
                    f=open(fname,"a",newline="")
                    file_writer=csv.writer(f,delimiter=",")
                    file_writer.writerow(["Invoice Number",y])
                    file_writer.writerow(["Customer Name",cust_name])
                    file_writer.writerow(["Account Number",entry2.get()])
                    file_writer.writerow([""])
                    file_writer.writerow(["     Item     ","     Quantity     ","     Price     ","     Tax     ","     Total Price     "])
                    for i in data:
                        item_price=int(data[i])*int(Menuprices.menu[i])
                        total_price+=item_price+(item_price/20)
                        file_writer.writerow([i,data[i],"Rs "+str(Menuprices.menu[i]),"5%","Rs "+str(item_price)])
                    file_writer.writerow(["       ","      ","     ","Grand Total      ","Rs "+str(final)])
                    f.close()
                    root.destroy()
                    Deliverystatus.Pacmanplayer(fname)
        else:
            total_price=0
            fname=f"Order_Invoice_{cust_name}_{y}.csv"
            f=open(fname,"a",newline="")
            file_writer=csv.writer(f,delimiter=",")
            file_writer.writerow(["Invoice Number   ",y])
            file_writer.writerow(["Customer Name    ",cust_name])
            file_writer.writerow([""])
            file_writer.writerow(["     Item     ","     Quantity     ","     Price     ","     Tax     ","     Total Price     "])
            for i in data:
                item_price=int(data[i])*int(Menuprices.menu[i])
                file_writer.writerow([i,data[i],"Rs "+str(Menuprices.menu[i]),"5%","Rs "+str(item_price)])
            file_writer.writerow(["       ","      ","     ","Grand Total     ","Rs "+str(final)])
            f.close()
            root.destroy()
            Deliverystatus.Pacmanplayer(fname)
            
    global root
    def backing():
        root.destroy()
        Checkoutwindow.checkout_win(d)
            
    def radio(r):
            global img1,img2,val
            if r=="Card":
                val="Card"
                b2.configure(image=img1)
                b1.configure(image=img2)
                entry2.place(x = 326.0, y = 617,width = 327.0,height = 41)
                entry3.place(x = 326.0, y = 559,width = 327.0,height = 41)
                entry4.place(x = 326.0, y = 674,width = 91.0,height = 41)
            elif r=="POD":
                val="POD"
                b2.configure(image=img2)
                b1.configure(image=img1)
                entry2.place_forget()
                entry3.place_forget()
                entry4.place_forget()
    def geoservice():
        global label2
        if os.path.exists("Bite o'Clock Geolocation Services.html"):
            os.startfile(r"Bite o'Clock Geolocation Services.html")
        else:
            label2.configure(text="Geolocation Services Unavailable")
            j=mixer.Sound("Delivery-Management-System/assets/sounds/Error Tone.mp3")
            j.play()
                
    global root
    global label2
    global entry2,entry3,entry4,img1,img2

    root = Tk()
    
    width1=1298
    height1=800

    scr_width=root.winfo_screenwidth()
    scr_height=root.winfo_screenheight()

    width2=int((scr_width/2)-(width1/2))
    height2=int((scr_height/2)-(height1/2))

    root.geometry(f'{width1}x{height1}+{width2}+{height2}')
    root.title("Bite o'Clock - Billing")
    root.configure(bg = "#ffffff")
    canvas = Canvas(root,bg = "#ffffff",height = 800,width = 1298,bd = 0,highlightthickness = 0,relief = "ridge")
    canvas.place(x = 0, y = 0)

    background_img = PhotoImage(file = f"Delivery-Management-System/assets/images/billbackground.png")
    background = canvas.create_image(649.0, 400.0,image=background_img)

    entry0_img = PhotoImage(file = f"Delivery-Management-System/assets/images/billimg_textBox0.png")
    entry0_bg = canvas.create_image(423.0, 131.5,image = entry0_img)
    label0 = Label(bd = 0,bg = "#ffffff",text="₹"+str(float(totalp)),highlightthickness = 0,anchor="e",font = ('Helvetica',18,'normal'))
    label0.place(x = 326.0, y = 109,width = 194.0,height = 41)

    entry1_img = PhotoImage(file = f"Delivery-Management-System/assets/images/billimg_textBox1.png")
    entry1_bg = canvas.create_image(423.0, 243.5,image = entry1_img)
    label1 = Label(bd = 0,bg = "#ffffff",text="₹"+str(float(finalp)),highlightthickness = 0,anchor="e",font = ('Helvetica',18,'normal'))
    label1.place(x = 326.0, y = 221,width = 194.0,height = 41)

    entry2_img = PhotoImage(file = f"Delivery-Management-System/assets/images/billimg_textBox2.png")
    entry2_bg = canvas.create_image(489.5, 639.5,image = entry2_img)
    entry2 = Entry(bd = 0,bg = "#ffffff",highlightthickness = 0,font = ('Helvetica',18,'normal'))

    entry3_img = PhotoImage(file = f"Delivery-Management-System/assets/images/billimg_textBox3.png")
    entry3_bg = canvas.create_image(489.5, 581.5,image = entry3_img)
    entry3 = Entry(bd = 0,bg = "#ffffff",highlightthickness = 0,font = ('Helvetica',18,'normal'))

    entry4_img = PhotoImage(file = f"Delivery-Management-System/assets/images/billimg_textBox4.png")
    entry4_bg = canvas.create_image(371.5, 696.5,image = entry4_img)
    entry4 = Entry(bd = 0,bg = "#ffffff",highlightthickness = 0,font = ('Helvetica',18,'normal'))

    img0 = PhotoImage(file = f"Delivery-Management-System/assets/images/back.png")
    b0 = Button(image = img0,borderwidth = 0,highlightthickness = 0,command = backing,relief = "flat")
    b0.place(x = 19, y = 15,width = 59,height = 59)

    img1 = PhotoImage(file = f"Delivery-Management-System/assets/images/unchecked.png")
    b1 = Button(image = img1,borderwidth = 0,highlightthickness = 0,command = lambda: radio("Card"),relief = "flat")
    b1.place(x = 33, y = 404,width = 22,height = 22)

    img2 = PhotoImage(file = f"Delivery-Management-System/assets/images/checked.png")
    b2 = Button(image = img2,borderwidth = 0,highlightthickness = 0,command = lambda: radio("POD"),relief = "flat")
    b2.place(x = 33, y = 501,width = 22,height = 22)

    img3 = PhotoImage(file = f"Delivery-Management-System/assets/images/billimg3.png")
    b3 = Button(image = img3,borderwidth = 0,highlightthickness = 0,command = geoservice,relief = "flat")
    b3.place(x = 888, y = 577,width = 352,height = 47)

    img4 = PhotoImage(file = f"Delivery-Management-System/assets/images/billimg4.png")
    b4 = Button(image = img4,borderwidth = 0,highlightthickness = 0,command = to_order,relief = "flat")
    b4.place(x = 888, y = 681,width = 352,height = 47)

    label1=Label(root, text="5%", font = ('Helvetica',20,'normal'), bg="#ffffff", fg="#000000")
    label1.place(x = 474, y = 164.5,width = 73.0,height = 44)
    
    label2=Label(root, text="", font = ('Helvetica',18,'normal'), bg="#ffffff", fg="#ff0000")
    label2.place(x = 256.0, y = 740,width = 473.0,height = 44)

    root.resizable(False, False)
    root.mainloop()

