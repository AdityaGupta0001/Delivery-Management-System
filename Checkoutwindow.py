#Importing modules
from tkinter import *
import json
from urllib.request import urlopen
from pygame import mixer

#Special ip locator module
from ipdata import ipdata

#Importing user-defined modules
import cartwindow
import Geoservices
import Billingwindow
import menuprices

#Main checkout window 
def checkout_win(d):
    global root
    global ipdata,order
    order={}
    for i in d:
        if d[i]!=0:
            order[i]=d[i]
            
        
    def backer():
        root.destroy()
        cartwindow.creator(order)
    AdressEntryType="Auto"
    def Billing():
        
        States_Suppliedto=["Delhi","Rajasthan","Haryana","Uttarakhand","Chandigarh","Uttar Pradesh","UP","Punjab"]
        States_NotSuppliedto=["Delhi","Rajasthan","Haryana","Uttarakhand","Chandigarh","Uttar Pradesh","UP","Punjab",
                              "Andhra Pradesh","Assam","Bihar","Chhattisgarh","Goa","Gujarat","Himachal Pradesh","Jharkhand",
                              "Karnataka","Kerala","Madhya Pradesh","Maharashtra","Manipur","Meghalaya","Mizoram","Nagaland",
                              "Odisha","Sikkim","Tamil Nadu","Telangana","Tripura","West Bengal","Andaman and Nicobar Islands",
                              "Dadra & Nagar Haveli","Dadra And Nagar Haveli","Daman And Diu","Daman & Diu",
                              "Jammu and Kashmir","Lakshadweep","Puducherry","Ladakh"]
        #Validation of user-info entry boxes
        if entry3.get()=="" or entry4.get()=="" or entry6.get()=="":
            label2.configure(text="Please fill in the required fields")
            j=mixer.Sound("Error Tone.mp3")
            j.play()
        elif (entry6.get()).isdigit()==False:
            label2.configure(text="This field requires a phone numer as an input")
            j=mixer.Sound("Error Tone.mp3")
            j.play()
        elif len(entry6.get())!=10:
            label2.configure(text="Phone Number Validation failed")
            j=mixer.Sound("Error Tone.mp3")
            j.play()

        #Validation of address if the entry type is "Manual"
        elif AdressEntryType=="Manual":
            if entry0.get()=="" or entry1.get()=="" or entry2.get()=="" or entry5.get()=="":
                label2.configure(text="Please fill in the required fields")
                j=mixer.Sound("Error Tone.mp3")
                j.play()
            elif (entry0.get()).title() not in States_Suppliedto and (entry0.get()).title() in States_NotSuppliedto:
                label2.configure(text="We currently do not supply to this state")
                j=mixer.Sound("Error Tone.mp3")
                j.play()
            elif (entry0.get()).title() not in States_NotSuppliedto:
                label2.configure(text="State name invalid")
                j=mixer.Sound("Error Tone.mp3")
                j.play()
            elif (entry1.get()).title() not in City_Data.Supplied and (entry1.get()).title() in City_Data.All:
                label2.configure(text="We currently do not supply to this city")
                j=mixer.Sound("Error Tone.mp3")
                j.play()
            elif (entry1.get()).title() not in City_Data.All:
                label2.configure(text="City name invalid")
                j=mixer.Sound("Error Tone.mp3")
                j.play()
            elif (entry2.get()).isdigit()==False:
                label2.configure(text="Postal Code has to be a digit")
                j=mixer.Sound("Error Tone.mp3")
                j.play()
            elif len(entry2.get())!=6:
                label2.configure(text="Postal Code has to be 6 digit long")
                j=mixer.Sound("Error Tone.mp3")
                j.play()
            elif entry5.get()==str(entry2.get()):
                label2.configure(text="Street Adress cannot be only digits")
                j=mixer.Sound("Error Tone.mp3")
                j.play()
       
        else:
            #Creating web file for map showing the route of delivery
            url = 'http://ipinfo.io/json'
            r1 = urlopen(url)
            data1 = json.load(r1)
            IP1=data1['ip']
            ipdat1 = ipdata.IPData('c8c021241765062f795d5bf8d004b69f37485ee1a3a06246f9e97cd7')
            out = ipdat1.lookup(IP1)
            reg=(entry0.get()).lower()
            if reg.title() in States_Suppliedto:
                label2.configure(text="")
                Geoservices.auto_mapper(out["longitude"],out["latitude"],reg.title())
                #Saving the address in a text file
                addressentry=f"{entry0.get()}-{entry1.get()}-{entry2.get()}-{entry5.get()}"
                with open("Customer.txt",mode='a') as Cus:
                    b1=f"{entry3.get()},{entry4.get()},{entry6.get()},{addressentry},{IP1}\n"
                    Cus.write(b1)
                #Calculating total price
                total_price=0
                prices=menuprices.menu
                for i in order.keys():
                    if i in prices.keys():
                        item_total=prices[i]*order[i]
                        total_price+=item_total
                final_price=total_price+(total_price/20)
                nam=entry3.get()+" "+entry4.get()
                root.destroy()
                Billingwindow.billing(total_price,final_price,d,nam)
            else:
                label2.configure(text="Please manually enter the State name")
                j=mixer.Sound("Error Tone.mp3")
                j.play()   
       
    #Function to auto locate a device
    def locateme():
        global AdressEntryType,ipdata
        url = 'http://ipinfo.io/json'
        response = urlopen(url)
        data = json.load(response)
        IP=data['ip']
        AdressEntryType="Auto"
        ipdat = ipdata.IPData('c8c021241765062f795d5bf8d004b69f37485ee1a3a06246f9e97cd7')
        response = ipdat.lookup(IP)
        entry0.insert(END, response["region"])
        entry1.insert(END, response["city"])
        entry2.insert(END, response["postal"])
        entry5.insert(END, str(response["latitude"])+","+str(response["longitude"]))
    def manual():
        global AdressEntryType
        AdressEntryType="Manual"
        entry0.delete(0,END)
        entry1.delete(0,END)
        entry2.delete(0,END)
        entry5.delete(0,END)
        

    #Custom radio buttons   
    def radio(r):
        global img1,img2
        if r=="Auto":
            b2.configure(image=img1)
            b1.configure(image=img2)
            locateme()
        elif r=="Manual":
            b2.configure(image=img2)
            b1.configure(image=img1)
            manual()
    
    #Definig tkinter window
    global root
    root = Tk()
    
    width1=1298
    height1=800

    scr_width=root.winfo_screenwidth()
    scr_height=root.winfo_screenheight()

    width2=int((scr_width/2)-(width1/2))
    height2=int((scr_height/2)-(height1/2))

    root.geometry(f'{width1}x{height1}+{width2}+{height2}')
    root.title("Bite o'Clock - Checkout")
   
    root.configure(bg = "#ffffff")
    canvas = Canvas(root,bg = "#ffffff",height = 800,width = 1298,bd = 0,highlightthickness = 0,relief = "ridge")
    canvas.place(x = 0, y = 0)

    background_img = PhotoImage(file = f"checkoutbackground.png")
    background = canvas.create_image(649.0, 400.0,image=background_img)

    entry0_img = PhotoImage(file = f"check_textBox0.png")
    entry0_bg = canvas.create_image(155.0, 613.5,image = entry0_img)
    entry0 = Entry(bd = 0,bg = "#ffffff",highlightthickness = 0,font=("Helvetica",18))

    entry1_img = PhotoImage(file = f"check_textBox1.png")
    entry1_bg = canvas.create_image(397.0, 613.5,image = entry1_img)
    entry1 = Entry(bd = 0,bg = "#ffffff",highlightthickness = 0,font=("Helvetica",18))

    entry2_img = PhotoImage(file = f"check_textBox2.png")
    entry2_bg = canvas.create_image(639.0, 613.5,image = entry2_img)
    entry2 = Entry(bd = 0,bg = "#ffffff",highlightthickness = 0,font=("Helvetica",18))

    entry3_img = PhotoImage(file = f"check_textBox3.png")
    entry3_bg = canvas.create_image(155.0, 215.5,image = entry3_img)
    entry3 = Entry(bd = 0,bg = "#ffffff",highlightthickness = 0,font=("Helvetica",18))
    entry3.place(x = 58.0, y = 193,width = 194.0,height = 41)

    entry4_img = PhotoImage(file = f"check_textBox4.png")
    entry4_bg = canvas.create_image(397.0, 215.5,image = entry4_img)
    entry4 = Entry(bd = 0,bg = "#ffffff",highlightthickness = 0,font=("Helvetica",18))
    entry4.place(x = 300.0, y = 193,width = 194.0,height = 41)

    entry5_img = PhotoImage(file = f"check_textBox5.png")
    entry5_bg = canvas.create_image(397.0, 700.5,image = entry5_img)
    entry5 = Entry(bd = 0,bg = "#ffffff",highlightthickness = 0,font=("Helvetica",18))

    entry6_img = PhotoImage(file = f"check_textBox6.png")
    entry6_bg = canvas.create_image(276.0, 306.5,image = entry6_img)
    entry6 = Entry(bd = 0,bg = "#ffffff",highlightthickness = 0,font=("Helvetica",18))
    entry6.place(x = 58.0, y = 284,width = 436.0,height = 41)

    entry0.place(x = 58.0, y = 591,width = 194.0,height = 41)
    entry1.place(x = 300.0, y = 591,width = 194.0,height = 41)
    entry2.place(x = 542.0, y = 591,width = 194.0,height = 41)
    entry5.place(x = 58.0, y = 678,width = 678.0,height = 41)

    img0 = PhotoImage(file = f"back.png")
    b0 = Button(image = img0,borderwidth = 0,highlightthickness = 0,command = backer,relief = "flat")
    b0.place(x = 19, y = 15,width = 59,height = 59)

    global img1,img2
    img2 = PhotoImage(file = f"checked.png")
    img1 = PhotoImage(file = f"unchecked.png")
    
    b1 = Button(image = img1,borderwidth = 0,highlightthickness = 0,command = lambda: radio("Auto"),relief = "flat")
    b1.place(x = 43, y = 453,width = 22,height = 22)

    
    b2 = Button(image = img2,borderwidth = 0,highlightthickness = 0,command = lambda: radio("Manual"),relief = "flat")
    b2.place(x = 43, y = 510,width = 22,height = 22)

    img3 = PhotoImage(file = f"Terms.png")
    b3 = Button(image = img3,borderwidth = 0,highlightthickness = 0,command = Billing,relief = "flat")
    b3.place(x = 873, y = 586,width = 352,height = 47)

    label2=Label(root, text="", font = ('Helvetica',18,'normal'), bg="#ffffff", fg="#ff0000")
    label2.place(x = 156.0, y = 740,width = 523.0,height = 44)


    root.resizable(False, False)
    root.mainloop()

