from tkinter import *
from PIL import Image , ImageTk
window = Tk()

window.title("Pokemon Game")
window.geometry("600x600")
window.config(background="orange2")


img1 = ImageTk.PhotoImage(Image.open("squirtle.jpg"))
img2 = ImageTk.PhotoImage(Image.open("abra.jpg"))
img3 = ImageTk.PhotoImage(Image.open("jigglypuff.jpg"))
img4 = ImageTk.PhotoImage(Image.open("bulbasour.jpg"))
img5 = ImageTk.PhotoImage(Image.open("button.jpg"))
img6 = ImageTk.PhotoImage(Image.open("charmender.jpg"))
img7 = ImageTk.PhotoImage(Image.open("lyvasour.jpg"))
img8 = ImageTk.PhotoImage(Image.open("kadabra.jpg"))
img9 = ImageTk.PhotoImage(Image.open("meowth.jpg"))
img10 = ImageTk.PhotoImage(Image.open("nidoking.jpg"))
img11 = ImageTk.PhotoImage(Image.open("paras.jpg"))
img12 = ImageTk.PhotoImage(Image.open("persion.jpg"))
img13 = ImageTk.PhotoImage(Image.open("pickachu.jpg"))
img14 = ImageTk.PhotoImage(Image.open("ratata.jpg"))


label1 = Label(window , text = "Player1")
label1.place(relx = 0.1 , rely = 0.3 , anchor = CENTER)


label2 = Label(window , text = "Player2")
label2.place(relx = 0.1 , rely = 0.3 , anchor = CENTER)


score1 = Label(window)
score1.place(relx = 0.1 , rely =0.4 , anchor = CENTER)


score2 = Label(window)
score2.place(relx = 0.9 , rely =0.4 , anchor = CENTER)


Cscore = Label(window)
Cscore.place(relx = 0.5 , rely =0.5 , anchor = CENTER)


window.mainloop()