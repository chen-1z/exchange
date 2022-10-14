import tkinter
from tkinter import *
from tkinter import messagebox
import os

class App:
	def __init__(self,master):
		frame=Frame(master)
		frame.pack(fill=BOTH,expand=1)
		#listbox=Listbox(frame)
		#listbox.grid(row=0,column=0,sticky=W+E+N+S)   # sticky 适配
		#text=Text(frame,relief=SUNKEN)
		#text.grid(row=0,column=1,sticky=W+E+N+S)

		frame.columnconfigure(1,weight=1)    #尺寸适配
		frame.rowconfigure(0,weight=1)       #尺寸适配


def stop():
    print('暂停')

def conti():
    print('继续')

def start():
    print('继续')

def helloCallBack():
    messagebox.showinfo("Hello Python", "Hello Runoob")

def addface():
	os.system("python F:/研究生/服务机器人/人脸识别/face-add/face-add.py")

def create():
	top = Toplevel()
	top.title('Python')

	v1 = StringVar()
	e1 = Entry(top, textvariable=v1, width=10)
	e1.grid(row=1, column=0, padx=1, pady=1)


window = tkinter.Tk()
window.title('Ros_Robot')
app=App(window)
window.geometry("700x600+0+0")     #尺寸适配

#window.iconbitmap('h8.ico')


photo = tkinter.PhotoImage(file="1.gif")
theLabel = tkinter.Label(window,justify=tkinter.CENTER,image=photo,compound = tkinter.CENTER)
theLabel.pack()

button1 = tkinter.Button(window, text='人脸识别', command=start)
button1.place(x=100,y=100,width=100,height=100,bordermode=INSIDE)

button2 = tkinter.Button(window, text='语音对话', command=stop)
button2.place(x=300,y=100,width=100,height=100,bordermode=INSIDE)

button3 = tkinter.Button(window, text='单点导航', command=conti)
button3.place(x=500,y=100,width=100,height=100,bordermode=INSIDE)

button4 = tkinter.Button(window, text="建立地图", command=create)
button4.place(x=100,y=250,width=100,height=100,bordermode=INSIDE)

button6 = tkinter.Button(window, text="多点导航", command=helloCallBack)
button6.place(x=300,y=250,width=100,height=100,bordermode=INSIDE)

B = tkinter.Button(window, text="添加人脸", command=addface)
B.place(x=500,y=250,width=100,height=100,bordermode=INSIDE)

B = tkinter.Button(window, text="视频播放", command=helloCallBack)
B.place(x=100,y=400,width=100,height=100,bordermode=INSIDE)

B = tkinter.Button(window, text="设置", command=helloCallBack)
B.place(x=300,y=400,width=100,height=100,bordermode=INSIDE)

button5 = tkinter.Button(window, text="关于我们", command=helloCallBack)
button5.place(x=500,y=400,width=100,height=100,bordermode=INSIDE)


window.mainloop()