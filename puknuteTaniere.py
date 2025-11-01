WIDTH = 800
rTan = WIDTH//12
HEIGHT = WIDTH//6
vyhraText = HEIGHT//6

import tkinter as tk
from random import *
c = tk.Canvas(width=WIDTH, height=HEIGHT)
c.pack()

kliky = []
pocetKlikov = [0,]*10
znaky = 'ABCDEFGHIJ'
puknuty = znaky[randint(0,9)]

for i in range(1,11):
    c.create_oval(rTan*i, 0.5*rTan,   rTan+rTan*i, 1.5*rTan, fill='blue', width=3)
    c.create_oval(rTan*i+8, 0.5*rTan+8,   rTan+rTan*i-8, 1.5*rTan-8, outline='grey')
    c.create_text(rTan//2+rTan*i,rTan, text=znaky[i-1], font=('Arial', rTan//2))

def klik(sur):
    global pocetKlikov
    x = sur.x
    y = sur.y
    if pocetKlikov == [0,]*10:
        for i in range(1,11):
            if x>rTan*i and x<rTan+rTan*i and y>0.5*rTan and y<1.5*rTan:
                kliky.append(znaky[i-1])
        if puknuty in kliky:
            vyhra()

def vyhra():
    global pocetKlikov
    for klik in kliky:
        for j in range(len(znaky)):
            if klik == znaky[j]:
                pocetKlikov[j] = pocetKlikov[j]+1

    opakovanie = ''
    for i in range(len(pocetKlikov)):
        if pocetKlikov[i] >= 2:
            opakovanie = opakovanie + znaky[i]

    c.delete('all')
    c.create_text(WIDTH//2,vyhraText*2,text='Gratulujem, označil si puknutý tanier!', font=('Arial', vyhraText), fill='blue')
    c.create_text(WIDTH//2,vyhraText*4,text='Viackrát si klikol na taniere: '+opakovanie, font=('Arial', vyhraText), fill='red')

c.bind('<Button-1>', klik)

c.mainloop()