from tkinter import *
import Signup_Menu
import Loginwindow

def display():
    
    def signwin():
        window.destroy()
        Signup_Menu.signup_win()
    def logwin():
        window.destroy()
        Loginwindow.login()
    window = Tk()

    width=1298
    height=800

    scr_width=window.winfo_screenwidth()
    scr_height=window.winfo_screenheight()

    x=int((scr_width/2)-(width/2))
    y=int((scr_height/2)-(height/2))

    window.geometry(f'{width}x{height}+{x}+{y}')
    window.title("Bite o'Clock - Sign Up/Login")
    window.configure(bg = "#ffffff")
    
    canvas = Canvas(window,bg = "#ffffff",height = 800,width = 1298,bd = 0,highlightthickness = 0,relief = "ridge")
    canvas.place(x = 0, y = 0)

    background_img = PhotoImage(file = f"slbackground.png")
    background = canvas.create_image(649.0, 400.0,image=background_img)

    img0 = PhotoImage(file = f"signupbox.png")
    b0 = Button(image = img0,borderwidth = 0,highlightthickness = 0,command = signwin,relief = "flat")
    b0.place(x = 772, y = 425,width = 403,height = 136)

    img1 = PhotoImage(file = f"loginbox.png")
    b1 = Button(image = img1,borderwidth = 0,highlightthickness = 0,command = logwin,relief = "flat")
    b1.place(x = 123, y = 425,width = 403,height = 136)

    window.resizable(False, False)
    window.mainloop()
