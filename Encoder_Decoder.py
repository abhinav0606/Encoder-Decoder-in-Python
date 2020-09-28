from tkinter import *
import base64
def moding():
    if mode.get()=="d":
        Result.set(Decode(Pvt_key.get(),Text.get()))
    elif mode.get()=="e":
        Result.set(Encode(Pvt_key.get(),Text.get()))
    else:
        Result.set("Invalid mode of conduct")
def Decode(pvt,message):
    decode=[]
    message=base64.urlsafe_b64decode(message).decode()
    for i in range(len(message)):
        key_c=pvt[i%len(pvt)]
        decode.append(chr((256 + ord(message[i])- ord(key_c)) % 256))
    return "".join(decode)
def Encode(pvt,message):
    encode=[]
    for i in range(len(message)):
        key_c=pvt[i%len(pvt)]
        encode.append(chr((ord(message[i]) + ord(key_c)) % 256))
    return base64.urlsafe_b64encode("".join(encode).encode()).decode()
root=Tk()
root.geometry("500x300")
root.resizable(0,0)
root.title("Encoder-Decoder")
Text=StringVar()
Pvt_key=StringVar()
Result=StringVar()
mode=StringVar()
def Reset():
    Text.set("")
    Pvt_key.set("")
    Result.set("")
    mode.set("")
Label(root,text="Encoder-Decoder",font="arial 15 italic").pack(side=TOP)
Label(root,text="Abhinav Creations",font="arial 15 italic").pack(side=BOTTOM)
Label(root,text="Enter the Text",font="arial 12 bold").place(x=60,y=80)
Entry(root,textvariable=Text,bg="ghost white").place(x=220,y=80)
Label(root,text="Enter the Key",font="arial 12 bold").place(x=60,y=120)
Entry(root,textvariable=Pvt_key,show="*",bg="ghost white").place(x=220,y=120)
Label(root,text="Enter the mode(e/d)",font="arial 12 bold").place(x=50,y=160)
Entry(root,textvariable=mode,bg="ghost white").place(x=220,y=160)
Button(root,text="Result",font="arial 12 bold",command=moding).place(x=50,y=200)
Entry(root,textvariable=Result,bg="ghost white").place(x=220,y=200)
Button(root,text="Reset",font="arial 12 bold",command=Reset).place(x=50,y=240)
root.mainloop()