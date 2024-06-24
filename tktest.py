# import threading
# from tkinter import Image, Tk

# from ttkthemes import ThemedTk

# from A import CommandsList, clearScreen, mainframe

import datetime,wikipedia,webbrowser,os,random,requests,pyautogui,subprocess,time
import urllib.request,bs4 as bs,sys,threading
import Annex,wolframalpha
from ttkthemes import themed_tk
from tkinter import ttk
import tkinter as tk
from tkinter import scrolledtext
from PIL import ImageTk,Image
# import sqlite3,pyjokes,pywhatkit
from functools import partial
import getpass,calendar
import socket
def gen(n):
    for i in range(n):
        yield i
class MainframeThread(threading.Thread):
    def __init__(self, threadID, name):
        threading.Thread.__init__(self)
        self.threadID = threadID
        self.name = name
    # def run(self):
    #     mainframe()

def Launching_thread():
    Thread_ID=gen(1000)
    global MainframeThread_object
    MainframeThread_object=MainframeThread(Thread_ID.__next__(),"Mainframe")
    MainframeThread_object.start()
   

if __name__=="__main__":
        #tkinter code
        root=themed_tk.ThemedTk()
        root.set_theme("winnative")
        root.geometry("{}x{}+{}+{}".format(920,460,int(root.winfo_screenwidth()/2 - 700/2),int(root.winfo_screenheight()/2 - 520/2)))
        root.resizable(0,0)
        root.title("AIVA")
        root.iconbitmap('aiva.ico')
        root.configure(bg='#000099')
        scrollable_text=scrolledtext.ScrolledText(root,state='disabled',height=20,width=87,relief='sunken',bd=5,wrap=tk.WORD,bg='#9999eb',fg='#190000')
        scrollable_text.place(x=10,y=10)
        mic_img=Image.open("Mic.png")
        mic_img=mic_img.resize((55,55),Image.ANTIALIAS)
        mic_img=Image.PhotoImage(mic_img)
        Speak_label=tk.Label(root,text="SPEAK:",fg="#FFD700",font='"Times New Roman" 12 ',borderwidth=0,bg='#2c4557')
        Speak_label.place(x=390,y=400)
        """Setting up objects"""
        # SR=Annex.SpeakRecog(scrollable_text)    #Speak and Recognition class instance
        Listen_Button=tk.Button(root,image=mic_img,borderwidth=0,activebackground='#2c4557',bg='#2c4557',command=Launching_thread)
        Listen_Button.place(x=460,y=380)
        myMenu=tk.Menu(root)
        m1=tk.Menu(myMenu,tearoff=0) #tearoff=0 means the submenu can't be teared of from the window
        # m1.add_command(label='Commands List',command=CommandsList)
        myMenu.add_cascade(label="Help",menu=m1)
        # stng_win=Annex.SettingWindow()
        # myMenu.add_cascade(label="Settings",command=partial(stng_win.settingWindow,root))
        # myMenu.add_cascade(label="Clear Screen",command=clearScreen)
        root.config(menu=myMenu)
        root.mainloop()