from tkinter import *
from math import tan
from math import radians
def clicked():
    global ex1, ez1, eang1, ex2, ez2, eang2, textx, textz
    x1=float(format(ex1.get()))
    z1=float(format(ez1.get()))
    f1=float(format(eang1.get()))
    x2=float(format(ex2.get()))
    z2=float(format(ez2.get()))
    f2=float(format(eang2.get()))
    if f1 == 90.0 or f1 == -90.0:
        z = float(z1)
        x = float(tan(radians(-1*f2))*z + x2 - tan(radians(-1*f2)*z2))
    elif f2 == 90.0 or f2 == -90.0:
        z = float(z2)
        x = float(tan(radians(-1*f1))*z + x1 - tan(radians(-1*f1))*z1)
    else:
        z = float((x2 - tan(radians(-1*f2))*z2 - x1 + tan(radians(-1*f1))*z1)/(tan(radians(-1*f1)) - tan(radians(-1*f2))))
        x = float(tan(radians(-1*f1))*z + x1 - tan(radians(-1*f1))*z1)
    x = round(x)
    z = round(z)
    textx.config(text=str(x))
    textz.config(text=str(z))
    text4 = Label(window, text='X:', font=('Minecraft Rus Regular', 20), fg='#ff0000', bg='#03fcba')
    text4.place(x = 0, y = 185)
    text5 = Label(window, text='Z:', font=('Minecraft Rus Regular', 20), fg='#0022ff', bg='#03fcba')
    text5.place(x = 150, y = 185)
    text6 = Label(window, text = 'Here are your stronghold coordinates:', font=('Minecraft Rus Regular', 15), fg='#2e2e2e', bg='#03fcba')
    text6.place(x = 0, y = 160)
    
window = Tk()
window.title("Minecraft Stronghold Finder")
window.geometry('710x320')
window['bg'] = '#03fcba'

text = Label(window, text="Welcome to the Minecraft Stronghold Finder", font = ('Minecraft Rus Regular', 20), fg='#2e2e2e', bg='#03fcba')
text.grid(column = 0, row = 0)
text1 = Label(window, text="Input your coordinates and angles of view", font = ('Minecraft Rus Regular', 15), fg='#2e2e2e', bg='#03fcba')
text1.place(x = 0, y = 30)
text2 = Label(window, text="First throw:", font = ('Minecraft Rus Regular', 15), fg='#ff00b7', bg='#03fcba')
text2.place(x = 0, y = 55)
text3 = Label(window, text="Second throw:", font = ('Minecraft Rus Regular', 15), fg='#ff00b7', bg='#03fcba')
text3.place(x = 0, y = 105)

tx1 = Label(window, text="X:", font = ('Minecraft Rus Regular', 15), fg='#ff2600', bg='#03fcba')
tx1.place(x = 0, y = 80)
ex1 = Entry(window, width = 10)
ex1.place(x = 25, y = 85)
tz1 = Label(window, text="Z:", font = ('Minecraft Rus Regular', 15), fg='#0080ff', bg='#03fcba')
tz1.place(x = 100, y = 80)
ez1 = Entry(window, width = 10)
ez1.place(x = 125, y = 85)
tang1 = Label(window, text="Angle:", font = ('Minecraft Rus Regular', 15), fg='#8800ff', bg='#03fcba')
tang1.place(x = 200, y = 80)
eang1 = Entry(window, width = 10)
eang1.place(x = 279, y = 85)

tx2 = Label(window, text="X:", font = ('Minecraft Rus Regular', 15), fg='#ff2600', bg='#03fcba')
tx2.place(x = 0, y = 130)
ex2 = Entry(window, width = 10)
ex2.place(x = 25, y = 135)
tz2 = Label(window, text="Z:", font = ('Minecraft Rus Regular', 15), fg='#0080ff', bg='#03fcba')
tz2.place(x = 100, y = 130)
ez2 = Entry(window, width = 10)
ez2.place(x = 125, y = 135)
tang2 = Label(window, text="Angle:", font = ('Minecraft Rus Regular', 15), fg='#8800ff', bg='#03fcba')
tang2.place(x = 200, y = 130)
eang2 = Entry(window, width = 10)
eang2.place(x = 279, y = 135)

btn = Button(window, text="Calculate!", font = ('Minecraft Rus Regular', 15), command = clicked, fg='#fffb00', bg='#03fcba')
btn.place(x = 350, y = 95)
    
textx = Label(window, font=('Minecraft Rus Regular', 20), fg='#ff0000', bg='#03fcba')
textz = Label(window, font=('Minecraft Rus Regular', 20), fg='#0022ff', bg='#03fcba')
textx.place(x = 35, y = 185)
textz.place(x = 185, y = 185)
text7 = Label(window, text = 'Copyright PhantomRaccoon,  2020', font=('Minecraft Rus Regular', 10), bg='#03fcba')
text7.place(x = 0, y = 300)

window.mainloop()
