from tkinter import *
import random

import base64

wind =Tk()
wind.geometry('1200x600')
wind.title("Message Encoding and Decoding")
# wind.config(bg="dark violet")

top=Frame(wind,width=1200,relief=SUNKEN)
top.pack(side=TOP)

title_info = Label(top,font=("helvetica",20,"bold"),
                    text="SECRET MESSAGING",
                    fg="Black",bd=10,anchor='w')               
title_info.grid(row=0,column=0)

p1=Frame(wind,width=600,relief=SUNKEN)
p1.pack(side=LEFT)

msg=StringVar()
key=StringVar()
mode=StringVar()
result=StringVar()

lblmsg = Label(p1, font=('arial',16,'bold'),
                text="Message",bd=16,anchor="w")
lblmsg.grid(row=1,column=0)

txtmsg = Entry(p1,font=('arial',16,'bold'),
                textvariable=msg,bd=10,
                bg='light yellow',justify='center')
txtmsg.grid(row=1,column=1)
# ///////////////////////////////////////////////////////////////
lblkey = Label(p1, font=('arial',16,'bold'),
                text="Key (Integer)",bd=16,anchor="w")
lblkey.grid(row=2,column=0)

txtkey = Entry(p1,font=('arial',16,'bold'),
                textvariable=key,bd=10,
                bg='light yellow',justify='center')
txtkey.grid(row=2,column=1)

# //////////////////////////////////////////////////////////////////
lblmode = Label(p1, font=('arial',16,'bold'),
                text="Mode(e=Enocode/d=Decode)",bd=16,anchor="w")
lblmode.grid(row=3,column=0)

txtmode = Entry(p1,font=('arial',16,'bold'),
                textvariable=mode,bd=10,
                bg='light yellow',justify='center')
txtmode.grid(row=3,column=1)

# //////////////////////////////////////////////////////////////////

lblresult = Label(p1, font=('arial',16,'bold'),
                text="Result",bd=16,anchor="w")
lblresult.grid(row=2,column=2,padx=50)

txtresult = Entry(p1,font=('arial',16,'bold'),
                textvariable=result,bd=10,
                bg='light yellow',justify='center')
txtresult.grid(row=2,column=3)

# ////////////////////////////////////////////////////////////////////
def encode(key,msg):
    enc=[]
    for i in range(len(msg)):
        key_c=key[i % len(key)]
        enc_c=chr((ord(msg[i])+ord(key_c))%256)
        enc.append(enc_c)
    return base64.urlsafe_b64encode("".join(enc).encode()).decode()

def decode(key,enc):
    dec=[]

    enc=base64.urlsafe_b64decode(enc).decode()
    for i in range(len(enc)):
        key_c=key[i%len(key)]
        dec_c=chr((256+ord(enc[i])-ord(key_c))% 256)
        dec.append(dec_c)
    return "".join(dec)
def calculate():
    MSG=msg.get()
    KEY=key.get()
    MODE=mode.get()

    if MODE=='e':
        result.set(encode(KEY,MSG))
    else:
        result.set(decode(KEY,MSG))

calculate=Button(p1,text="Calculate",font=('arial',16,'bold'),bg="light green",command=calculate)
calculate.grid(row=3,column=2)




wind.mainloop()