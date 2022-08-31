from logging import disable
from tkinter import Label
from tkinter import * 
import datetime 

def Time():

    time = datetime.datetime.now()
    hour = time.strftime('%I')
    min = time.strftime('%M')
    sec = time.strftime('%S')
    a_p = time.strftime('%p')

    hh.config(text=hour)
    mm.config(text=min)
    ss.config(text=sec)
    ampm.config(text=a_p)
    hh.after(50,Time)

def Date():

    date = datetime.datetime.now()
    dat = date.strftime("%d")
    month = date.strftime("%m")
    year = date.strftime("%y")
    dayy = date.strftime("%a")

    dd.config(text=dat)
    mon.config(text = month)
    yy.config(text=year)
    day.config(text=dayy)


display = Tk()

display.geometry("760x500+325+150")
display.resizable(False,False)

display.title(' Digi Clock')
display.config(bg = 'black')
display.protocol("WM_DELETE_WINDOW",disable)

hh = Label(display,text ="00", font=("ComicSansms 40 bold"), bg = 'black' , fg = 'cyan', borderwidth = 6, relief = RAISED)
hh.place(x=140,y=50,height=80,width=80)

mm = Label(display,text ="00", font=("ComicSansms 40 bold"), bg = 'black' , fg = 'cyan', borderwidth = 6, relief = RAISED)
mm.place(x=280,y=50,height=80,width=80)

ss = Label(display,text ="00", font=("ComicSansms 40 bold"), bg = 'black' , fg = 'cyan', borderwidth = 6, relief = RAISED)
ss.place(x=420,y=50,height=80,width=80)

ampm = Label(display,text ="00", font=("ComicSansms 20 bold"), bg = 'black' , fg = 'cyan',borderwidth = 6, relief = SUNKEN)
ampm.place(x=560,y=50,height=80,width=80)

h = Label(display,text ="Hour", font=("ComicSansms 12 bold"), bg = 'black' , fg = '#FFFC00')
h.place(x=140,y=150,height=35,width=80)

m = Label(display,text ="Minute", font=("ComicSansms 12 bold"), bg = 'black' , fg = '#FFFC00')
m.place(x=280,y=150,height=35,width=80)

s = Label(display,text ="Second", font=("ComicSansms 12 bold"), bg = 'black' , fg = '#FFFC00')
s.place(x=420,y=150,height=35,width=80)

z = Label(display,text ="Meridiem", font=("ComicSansms 12 bold"), bg = 'black' , fg = '#FFFC00')
z.place(x=560,y=150,height=35,width=80)

Time()

dd = Label(display,text ="00", font=("ComicSansms 40 bold"), bg = 'black' , fg = 'cyan',borderwidth = 6, relief = RAISED)
dd.place(x=140,y=235,height=80,width=80)

mon = Label(display,text ="00", font=("ComicSansms 40 bold"), bg = 'black' , fg = 'cyan',borderwidth = 6, relief = RAISED)
mon.place(x=280,y=235,height=80,width=80)

yy = Label(display,text ="0000", font=("ComicSansms 40 bold"), bg = 'black' , fg = 'cyan',borderwidth = 6, relief = RAISED)
yy.place(x=420,y=235,height=80,width=80)

day = Label(display,text ="", font=("ComicSansms 20 bold"), bg = 'black' , fg = 'cyan',borderwidth = 6, relief = SUNKEN)
day.place(x=560,y=235,height=80,width=80)

mo = Label(display,text ="Date", font=("ComicSansms 12 bold"), bg = 'black' , fg = '#FFFC00')
mo.place(x=140,y=335,height=35,width=80)

y = Label(display,text ="Month", font=("ComicSansms 12 bold"), bg = 'black' , fg = '#FFFC00')
y.place(x=280,y=335,height=35,width=80)

dayy = Label(display,text ="Year", font=("ComicSansms 12 bold"), bg = 'black' , fg = '#FFFC00')
dayy.place(x=420,y=335,height=35,width=80)

z = Label(display,text ="Day", font=("ComicSansms 12 bold"), bg = 'black' , fg = '#FFFC00')
z.place(x=560,y=335,height=35,width=80)

Date()

def Dest():
    display.destroy()

cls = Button(display,text = "CLOSE",  font=("ComicSansms 12 bold"), bg = 'black', fg = 'orange', command = Dest)
cls.place(x=340,y=450)

display.mainloop()