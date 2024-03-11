from tkinter import *
from PIL import Image

window = Tk()
width=1298
height=800
scr_width=window.winfo_screenwidth()
scr_height=window.winfo_screenheight()

x=int((scr_width/2)-(width/2))
y=int((scr_height/2)-(height/2))

window.geometry(f'{width}x{height}+{x}+{y}')
window.title("Bite o'Clock")
window.configure(bg = "#e36c4c")
canvas = Canvas(window,bg = "#e36c4c",height = 800,width = 1298,bd = 0,highlightthickness = 0,relief = "ridge")
canvas.place(x = 0, y = 0)

background_img = PhotoImage(file = f"Delivery-Management-System/assets/images/start_animation_bg.png")
background = canvas.create_image(
    649.0, 400.0,
    image=background_img)

def end(event):
    window.destroy()

def player():
    file="Delivery-Management-System/assets/images/start_animation_gif.gif"
    info = Image.open(file)
    frames = info.n_frames
    im=[]
    for i in range(frames):
        im.append(PhotoImage(file=file,format=f"gif -index {i}"))
        
    count = 0
    def animation(count):
        im2 = im[count]

        gif_label.configure(image=im2)
        count += 1
        anim=window.after(30,lambda :animation(count))
        if count == frames:
            window.after_cancel(anim)
    gif_label = Label(image="",bg="#D97049")
    gif_label.place(x=40,y=300)
    animation(count)

window.after(10,player)
window.bind("<Button-1>",end)
window.resizable(False, False)
window.mainloop()
