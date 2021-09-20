from tkinter import *
from tkinter import ttk
import requests, random, string, threading
import tkinter as tk
from tkinter.filedialog import askopenfilename, asksaveasfilename
import requests
from requests.api import get, request
import time
import codecs
import os
import string
from random import shuffle
import csv
import os.path
import webbrowser
import keyring

service_id = 'PassPY'
username = ""

def mainwindow():
    def LogWindow():
        ws = Tk()
        ws.title('PassPY Login')
        ws.geometry('400x300')
        ws.config(bg='#ffffff')
        message =''
        title = tk.Label(text="Welcome to PassPY!", font=("Arial", 25))
        title.place(x=0, y=0)

        def RegWinButton():
            DestroyButton()
            RegWindow()
        
        regbutton = tk.Button(text="No account? Register!", command=RegWinButton)
        regbutton.place(x=255, y=275)

        def DestroyButton():
            ws.destroy()

        username_text_box = Entry(ws)

        usernametitle = tk.Label(text="username")
        usernametitle.place(x=20, y=75)
        username_text_box.place(x=20, y=100)
        username_text_box.config(state='normal', bg='#e1e8f2')

        password_text_box = Entry(ws)
        passwordtitle = tk.Label(text="password")
        passwordtitle.place(x=20, y=175)
        password_text_box.place(x=20, y=200)
        password_text_box.config(state='normal', bg='#e1e8f2')

        exitbutton = tk.Button(text="exit", command=quit)
        exitbutton.place(x=3, y=275)

        global username

        username = username_text_box.get()

        # creds = username_text_box.get(), password_text_box.get() 
        # cache = username + 'cache' + '.txt'
        # try:
        #     usersearch = open(cache)  #search for user's password file
        #     usersearch.close()
        #     print("User name not available")
        #     NewUserLogin = input("Try another Username:  ")
        #     nametest1 = NewUserLogin + "login" + ".txt"
        # except FileNotFoundError:
        #     print('created')
            
        # create = open(cache,"a")  #create user's password file
        # #password = input("Enter password:  ")
        # cypher = codecs.encode(username, 'ROT13')
        # create.write(cypher)
        # create.close()



        # use me when server integration comes:
        # def DataPacket():
        #      message = input("message test: ")
        #      requests.post(url='http://127.0.0.1:8080', data={creds})

        keyring.set_password(service_id, 'username', 'username')
        
        def MenuButton():
            DestroyButton()
            MainMenu()

        def sendcreds():
            print(username_text_box.get(), password_text_box.get())
            MenuButton()
            
        loginbutton = tk.Button(text="Login", command=sendcreds)
        loginbutton.place(x=20, y=250)

        ws.mainloop()

    def RegWindow():
        ws = Tk()
        ws.title('PassPY Register')
        ws.geometry('350x400')
        ws.config(bg='#ffffff')
        message =''
        title = tk.Label(text="Welcome to PassPY!", font=("Arial", 25))
        title.place(x=0, y=0)

        regusername_text_box = Entry(ws)

        regusernametitle = tk.Label(text="username")
        regusernametitle.place(x=20, y=75)
        regusername_text_box.place(x=20, y=100)
        regusername_text_box.config(state='normal', bg='#e1e8f2')

        passwordr_text_box = Entry(ws)
        passwordrtitle = tk.Label(text="password")
        passwordrtitle.place(x=20, y=175)
        passwordr_text_box.place(x=20, y=200)
        passwordr_text_box.config(state='normal', bg='#e1e8f2')

        confirm_text_box = Entry(ws)
        confirmtitle = tk.Label(text="Confirm Password")
        confirmtitle.place(x=20, y=275)
        confirm_text_box.place(x=20, y=300)
        confirm_text_box.config(state='normal', bg='#e1e8f2')

        credsr = regusername_text_box.get(), passwordr_text_box.get()

        def labelT():
            avalible_labels = tk.Label(text="Username is avalible!", bg='green') 
            avalible_labels.place(x=100, y=375)
            time.sleep(30)
            LogWindow()
            ws.destroy()

        def labelF():
            avalible_labels = tk.Label(text="Username is NOT avalible.", bg='red')
            avalible_labels.place(x=100, y=375)
            time.sleep(5)
            avalible_labels.destroy()
        def register():
            user_name = regusername_text_box.get()
            nametest1 = user_name + "login" + ".txt"
            try:
                usersearch = open(nametest1)  #search for user's password file
                usersearch.close()
                labelF()
            except FileNotFoundError:
                create = open(nametest1,"a")  #create user's password file
                password1 = passwordr_text_box.get()
                confirmed = confirm_text_box.get()
                if confirmed == password1:
                    cypher = codecs.encode(password1, 'ROT13')
                    create.write(cypher)
                    create.close()
                    labelT()
        
        def LogWinButton():
            register()
            DestroyButton()
            LogWindow()

        registerbutton = tk.Button(text="register!", command=LogWinButton)
        registerbutton.place(x=20, y=350)
        exitbutton = tk.Button(text="exit", command=quit)
        exitbutton.place(x=3, y=375)

        def DestroyButton():
            ws.destroy()

        ws.mainloop()
    #-------------------------------------------------------------------------------------------------

    def listWindow():
        import tkinter
        import tkinter.ttk as ttk
    
        keyuser = keyring.get_password(service_id, username)

        filer = open( + "passwords" + ".txt","r") 
        contents = filer.read()
        passwords = codecs.encode(contents, 'ROT13') 
        count = contents.splitlines()
        ReadSize = "mode con: cols=100 lines=" + str(int(len(count)) + 13)
        os.system(ReadSize)


        class TextScrollCombo(ttk.Frame):
            def __init__(self, *args, **kwargs):
                super().__init__(*args, **kwargs)
                
            # ensure a consistent GUI size
                self.grid_propagate(False)
            # implement stretchability
                self.grid_rowconfigure(0, weight=1)
                self.grid_columnconfigure(0, weight=1)

            # create a Text widget
                self.txt = tkinter.Text(self)
                self.txt.grid(row=0, column=0, sticky="nsew", padx=2, pady=2)
                self.txt.insert(tk.END, passwords)

            # create a Scrollbar and associate it with txt
                scrollb = ttk.Scrollbar(self, command=self.txt.yview)
                scrollb.grid(row=0, column=1, sticky='nsew')
                self.txt['yscrollcommand'] = scrollb.set

        main_window = tkinter.Tk()
        main_window.geometry('300x300')
        main_window.title('list')

        combo = TextScrollCombo(main_window)
        combo.pack(fill="both", expand=False)
        combo.config(width=300, height=300)
        combo.place(x='0', y='0')
        combo.config(state='disabled')

        combo.txt.config(font=("consolas", 12), undo=True, wrap='word')
        combo.txt.config(borderwidth=3, relief="sunken")

        style = ttk.Style()
        style.theme_use('clam')

        main_window.mainloop()
        

    def DonateMenu():
        new = 1
        url = "https://paypal.me/Morgandri1?locale.x=en_US"

        def openweb():
            webbrowser.open(url,new=new)
        
        openweb()

    def ListMenu():
        tk.Label(text='text')

    def MainMenu():
        ws = Tk()
        ws.title('PassPY Menu')
        ws.geometry('350x300')
        ws.config(bg='#ffffff')
        message =''
        title = tk.Label(text="Welcome back!", font=("Arial", 25))
        title.place(x=0, y=0)
        #donate button
        donate = tk.Button(text="Donate to support the project!", command=DonateMenu)
        donate.place(x=50, y=250)
        #search for a password
        search = tk.Button(text="List all passwords", command=listWindow)
        search.place(x=50, y=200)
        #register new password
        addPass = tk.Button(text='add a new password', )
        

        ws.mainloop()

#-----------------------------------------------------------------------------------------------------------------
    LogWindow()
   
#-----------------------------------------------------------------------------------------------------------------
mainwindow()
    
        