from tkinter import *
from pygame import mixer
import os
mixer.init()
def endwin(fname):
    def Thanks():
        window.destroy()

    def openinvoice():
        if os.path.exists(fname):
            os.startfile(fname)
        else:
            j=mixer.Sound("Error Tone.mp3")
            j.play()


    window = Tk()

    width=1298
    height=800

    scr_width=window.winfo_screenwidth()
    scr_height=window.winfo_screenheight()

    x=int((scr_width/2)-(width/2))
    y=int((scr_height/2)-(height/2))

    window.geometry(f'{width}x{height}+{x}+{y}')
    window.title("Bite o'Clock")

    window.configure(bg = "#ffffff")
    canvas = Canvas(window,bg = "#ffffff",height = 800,width = 1298,bd = 0,highlightthickness = 0,relief = "ridge")
    canvas.place(x = 0, y = 0)

    background_img = PhotoImage(file = f"endbackground.png")
    background = canvas.create_image(649.0, 400.0,image=background_img)

    img0 = PhotoImage(file = f"endimg0.png")
    b0 = Button(image = img0,borderwidth = 0,highlightthickness = 0,command = Thanks,relief = "flat")
    b0.place(x = 389, y = 383,width = 520,height = 136)

    img1 = PhotoImage(file = f"invoice_button.png")
    b1 = Button(image = img1,borderwidth = 0,highlightthickness = 0,command = openinvoice,relief = "flat")
    b1.place(x = 460, y = 562,width = 377,height = 61)

    window.resizable(False, False)
    window.mainloop()

