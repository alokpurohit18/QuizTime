import os
from tkinter import *
from tkinter import messagebox
from PIL import ImageTk,Image
from pygame import mixer
from random import *
import random
import mysql.connector
from pathlib import Path

mydb = mysql.connector.connect(host='localhost', user='root', passwd='Alok1823!', database='kbc')
mycursor = mydb.cursor()
localcursor = mydb.cursor()
mixer.init()
path = Path(__file__).parent.parent

screen = Tk()
screen.title("Kaun Banega Crorepati - The Game")
screen.iconbitmap(os.path.join(path, 'Images and Icons\kbc_logo.ico'))
screen.geometry('1920x1080+0+0')
screen.configure(background='#2e004d')

startframe = Frame(screen, bg='#2e004d')
ruleframe = Frame(screen, bg='#2e004d')
developerframe = Frame(screen, bg='#2e004d')
loginframe = Frame(screen, bg='#2e004d')
accountframe = Frame(screen, bg='#2e004d')
gameframe = Frame(screen, bg='#2e004d')

panel = Label(screen)
filename = os.path.join(path, 'Images and icons\kbc.png')
iconfile = os.path.join(path, 'Images and icons\login.png')
icon= Image.open(iconfile)

ruleframedestroy = 0
developerframedestroy = 0
loginframedestroy = 0
accountframedestroy = 0
startframedestroy = 0
gameframedestroy=0

username = StringVar()
password = StringVar()
denomination=5000 # RULE CHANGE AFFECTED

optiona=Button()
optionb=Button()
optionc=Button()
optiond=Button()

friend1=StringVar()
friend2=StringVar()
friend3=StringVar()
friend1.set("friend1")
friend2.set("friend2")
friend3.set("friend3")

lifelinebutton1 = Button()
lifelinebutton2 = Button()
lifelinebutton3 = Button()
lifelinebutton4 = Button()

fiftyfiftydone=0
phonedone=0
audiencedone=0
expertdone=0

aactive=1
bactive=1
cactive=1
dactive=1
sameq_flag=0




def set_background():
    global  panel
    img = Image.open(filename)
    img = img.resize((1600, 900), Image.ANTIALIAS)
    img = ImageTk.PhotoImage(img)
    if ruleframedestroy != 0:
        panel = Label(ruleframe, image=img, width=1920, height=1080)
    if developerframedestroy != 0:
        panel = Label(developerframe, image=img, width=1920, height=1080)
    if loginframedestroy != 0:
        panel = Label(loginframe, image=img, width=1920, height=1080)
    if accountframedestroy != 0:
        panel = Label(accountframe, image=img, width=1920, height=1080)
    if startframedestroy!=0:
        panel = Label(startframe, image=img, width=1920, height=1080)
    if gameframedestroy!=0:
        panel = Label(gameframe, image=img, width=1920, height=1080)

    panel.image = img
    panel.pack(side='top')

def set_icon():
    global  icon
    icon= Image.open(iconfile)
    icon = ImageTk.PhotoImage(icon)

def lifeline_icon():
        global icon
        icon = Image.open(iconfile)
        icon = icon.resize((60, 48), Image.ANTIALIAS)
        icon = ImageTk.PhotoImage(icon)





def startingwindow():
    global startframe, ruleframedestroy, developerframedestroy, loginframedestroy, accountframedestroy,startframedestroy, gameframedestroy
    global username, password, filename, iconfile
    username.set('')
    password.set('')
    if gameframedestroy!=0:
        gameframe.destroy()
    if ruleframedestroy != 0:
        ruleframe.destroy()
    if developerframedestroy != 0:
        developerframe.destroy()
    if loginframedestroy != 0:
        loginframe.destroy()
    if accountframedestroy != 0:
        accountframe.destroy()
    ruleframedestroy = 0
    developerframedestroy = 0
    loginframedestroy = 0
    accountframedestroy = 0
    gameframedestroy = 0
    mixer.music.load(os.path.join(path, 'Images and icons\kbc_tune.mp3'))
    mixer.music.play()
    startframe = Frame(screen, bg='#2e004d')
    startframe.pack()
    startframedestroy = 1
    filename = os.path.join(path, 'Images and icons\kbc.png')
    set_background()

    iconfile= os.path.join(path, 'Images and icons\login.png')
    set_icon()
    loginbutton = Button(panel, text='LOGIN ',image=icon,compound=RIGHT, font='Arial 38 bold', bg='black', fg='white', border=5,
                         command=loginwindow1)
    loginbutton.image=icon
    loginbutton.pack(side='top', pady=160, padx=50, ipadx=15)

    rulebutton = Button(panel, text='RULES OF THE\nGAME', font='Arial 36 bold', bg='black', fg='white', border=5,
                        command=rulewindow1)
    rulebutton.pack(side='left', pady=130, padx=80)

    createuser = Button(panel, text='CREATE\nACCOUNT', font='Arial 36 bold', bg='black', fg='white', border=5,
                        command=createaccount)
    createuser.pack(side='left', pady=130, padx=40)

    infobutton = Button(panel, text='DEVELOPER\n  INFORMATION  ', font='Arial 36 bold', bg='black', fg='white',
                        border=5, command=developerinfo)
    infobutton.pack(side='left', pady=130, padx=80)





def rulewindow1():
    global ruleframedestroy, ruleframe, filename , startframedestroy
    if startframedestroy == 1:
        startframe.destroy()
        startframedestroy = 0
    if ruleframedestroy == 1:
        ruleframe.destroy()
    ruleframe = Frame(screen, bg='#2e004d')
    ruleframe.pack()
    ruleframedestroy = 1
    counter = 1
    mixer.music.load(os.path.join(path, 'Images and icons\play.mp3'))
    mixer.music.play()
    filename = os.path.join(path, 'Images and icons\kbc.png')
    set_background()

    heading = Label(panel, bg='#2e004d', fg='white', text='RULES', font='Arial 36 bold underline')
    heading.pack(side='top', anchor=W, padx=70, pady=30)

    mycursor.execute("select rdescription from rule")
    for i in mycursor:
        rulemessage = Label(panel, bg='#2e004d', fg='yellow', text=str(counter) + '.' + str(i)[2:-3],
                            font='Arial 16 bold')
        rulemessage.pack(side='top', anchor=W, padx=70, pady=20)
        counter = counter + 1

    backbutton = Button(panel, text='BACK', font='Arial 32 bold', bg='black', fg='white', border=5,
                        command=startingwindow)
    backbutton.pack(side='left', anchor=W, padx=80, pady=100)

    nextbutton = Button(panel, text='NEXT', font='Arial 32 bold', bg='black', fg='white', border=5,
                        command=rulewindow2)
    nextbutton.pack(side='left', anchor=E, padx=40, pady=100)

def rulewindow2():
    global ruleframe, filename
    ruleframe.destroy()
    ruleframe = Frame(screen, bg='#2e004d')
    ruleframe.pack()
    mixer.music.load(os.path.join(path, 'Images and icons\play.mp3'))
    mixer.music.play()
    filename = os.path.join(path, 'Images and icons\kbc.png')
    set_background()

    waste = Label(panel, bg='#2e004d', fg='white', text='',
                  font='Arial 3 bold underline')
    waste.pack(side='top', anchor=W, padx=840)

    heading = Label(panel, bg='#2e004d', fg='white', text='CHECKPOINTS', font='Arial 36 bold underline')
    heading.pack(side='top', anchor=W, pady=20, padx=120)

    mycursor.execute("select distinct(denomination) from question order by denomination desc")
    j = int(65 / 5)  # RULE CHANGE AFFECTED
    for i in mycursor:
        if i == (10000,) or i == (320000,) or i == (10000000,):  # RULE CHANGE AFFECTED
            rulemessage = Label(panel, bg='#2e004d', fg='yellow', text=str(j) + ' # ' + (str(i)[1:-2]),
                                font='Arial 24 bold')
            rulemessage.pack(side='top', anchor=W, padx=180)
            j = j - 1
        else:
            rulemessage = Label(panel, bg='#2e004d', fg='white', text=str(j) + ' # ' + (str(i)[1:-2]),
                                font='Arial 24 bold')
            rulemessage.pack(side='top', anchor=W, padx=180)
            j = j - 1

    backbutton = Button(panel, text='BACK', font='Arial 32 bold', bg='black', fg='white', border=5,
                        command=rulewindow1)
    backbutton.pack(side='left', anchor=W, pady=35,padx=80)

    nextbutton = Button(panel, text='NEXT', font='Arial 32 bold', bg='black', fg='white', border=5,
                        command=rulewindow3)
    nextbutton.pack(side='left', anchor=W, pady=35)

def rulewindow3():
    global ruleframe, filename, iconfile, icon
    ruleframe.destroy()
    ruleframe = Frame(screen, bg='#2e004d')
    ruleframe.pack()
    mixer.music.load(os.path.join(path, 'Images and icons\play.mp3'))
    mixer.music.play()
    filename = os.path.join(path, 'Images and icons\kbc.png')
    set_background()

    waste = Label(panel, bg='#2e004d', fg='white', text='',
                  font='Arial 3 bold underline')
    waste.pack(side='top', anchor=W, padx=840)

    heading = Label(panel, bg='#2e004d', fg='white', text='LIFELINES', font='Arial 36 bold underline')
    heading.pack(side='top',padx=180, pady=42,anchor=W)

    j = 1
    mycursor.execute("select lname from lifeline")
    for i in mycursor:
        if j == 1:
            iconfile = os.path.join(path, 'Images and icons\Audiencepoll.png')
            icon = Image.open(iconfile)
            icon = icon.resize((60, 48), Image.ANTIALIAS)
            icon = ImageTk.PhotoImage(icon)
            lifelinebutton1 = Button(panel, text=' '+str(i)[2:-3]+' ',image=icon,compound=LEFT, font='Arial 24 bold', bg='black', fg='yellow',
                                     border=5, command=lifelinedescription1)
            lifelinebutton1.image = icon
            lifelinebutton1.pack(side='top',padx=150, pady=20,anchor=W)
        elif j == 2:
            iconfile = os.path.join(path, 'Images and icons\phoneafriend.png')
            icon = Image.open(iconfile)
            icon = icon.resize((60, 48), Image.ANTIALIAS)
            icon = ImageTk.PhotoImage(icon)
            lifelinebutton2 = Button(panel, text=' '+str(i)[2:-3]+' ',image=icon,compound=LEFT, font='Arial 24 bold', bg='black', fg='yellow',
                                     border=5, command=lifelinedescription2)
            lifelinebutton2.image=icon
            lifelinebutton2.pack(side='top',padx=150, pady=20,anchor=W)
        elif j == 3:
            iconfile = os.path.join(path, 'Images and icons\expertadvice.png')
            icon = Image.open(iconfile)
            icon = icon.resize((65, 52), Image.ANTIALIAS)
            icon = ImageTk.PhotoImage(icon)
            lifelinebutton3 = Button(panel, text=' '+str(i)[2:-3]+' ',image=icon,compound=LEFT, font='Arial 24 bold', bg='black', fg='yellow',
                                     border=5, command=lifelinedescription3)
            lifelinebutton3.image=icon
            lifelinebutton3.pack(side='top',padx=150, pady=20,anchor=W)
        else:
            iconfile = os.path.join(path, 'Images and icons\\fifty-fifty.png')
            icon = Image.open(iconfile)
            icon = icon.resize((60, 48), Image.ANTIALIAS)
            icon = ImageTk.PhotoImage(icon)
            lifelinebutton4 = Button(panel, text=' '+str(i)[2:-3]+' ',image=icon,compound=LEFT, font='Arial 24 bold', bg='black', fg='yellow',
                                     border=5, command=lifelinedescription4)
            lifelinebutton4.image=icon
            lifelinebutton4.pack(side='top',padx=150, pady=20,anchor=W)
        j = j + 1

    backbutton = Button(panel, text='BACK', font='Arial 32 bold', bg='black', fg='white', border=5,
                        command=rulewindow2)
    backbutton.pack(side='left', pady=70, padx=85,anchor=W)

    iconfile = os.path.join(path, 'Images and icons\home.png')
    set_icon()
    homebutton = Button(panel, text=' HOME ',image=icon,compound=LEFT, font='Arial 32 bold', bg='black', fg='white', border=5,
                        command=startingwindow)
    homebutton.image=icon
    homebutton.pack(side='left',ipadx=10,ipady=10, pady=75,anchor=W)

def rulewindow4():
    global ruleframe,filename
    ruleframe.destroy()
    ruleframe = Frame(screen, bg='#2e004d')
    ruleframe.pack()
    mixer.music.load(os.path.join(path, 'Images and icons\play.mp3'))
    mixer.music.play()
    filename = os.path.join(path, 'Images and icons\kbc.png')
    set_background()

    waste = Label(panel, bg='#2e004d', fg='white', text='',
                  font='Arial 3 bold underline')
    waste.pack(side='top', anchor=W, padx=840)

    backbutton = Button(panel, text='BACK', font='Arial 32 bold', bg='black', fg='white', border=5,command=rulewindow3)
    backbutton.pack(side='bottom', anchor=W, padx=60, pady=250)

    heading = Label(panel, bg='#2e004d', fg='white', text='LIFELINE DESCRIPTION', font='Arial 36 bold underline')
    heading.pack(side='top', anchor=W, pady=50, padx=60)

def lifelinedescription1():
    rulewindow4()

    mycursor.execute("select ldescription from lifeline where lnumber=1")
    for i in mycursor:
        rulemessage1 = Label(panel, bg='#2e004d', fg='yellow', text='1.' + str(i)[2:100],
                             font='Arial 22 bold')  # RULE CHANGE AFFECTED
        rulemessage1.pack(side='top', anchor=W, padx=40)
        rulemessage2 = Label(panel, bg='#2e004d', fg='yellow', text='2.' + str(i)[100:-3],
                             font='Arial 22 bold')  # RULE CHANGE AFFECTED
        rulemessage2.pack(side='top', anchor=W, padx=40)

def lifelinedescription2():
    rulewindow4()

    mycursor.execute("select ldescription from lifeline where lnumber=2")
    for i in mycursor:
        rulemessage1 = Label(panel, bg='#2e004d', fg='yellow', text='1.' + str(i)[2:96],
                             font='Arial 22 bold')  # RULE CHANGE AFFECTED
        rulemessage1.pack(side='top', anchor=W, padx=50)
        rulemessage2 = Label(panel, bg='#2e004d', fg='yellow', text='2.' + str(i)[96:-3],
                             font='Arial 22 bold')  # RULE CHANGE AFFECTED
        rulemessage2.pack(side='top', anchor=W, padx=50)

def lifelinedescription3():
    rulewindow4()

    mycursor.execute("select ldescription from lifeline where lnumber=3")
    for i in mycursor:
        rulemessage1 = Label(panel, bg='#2e004d', fg='yellow', text='1.' + str(i)[2:105],
                             font='Arial 22 bold')  # RULE CHANGE AFFECTED
        rulemessage1.pack(side='top', anchor=W, padx=50)
        rulemessage2 = Label(panel, bg='#2e004d', fg='yellow', text='2.' + str(i)[106:-3],
                             font='Arial 22 bold')  # RULE CHANGE AFFECTED
        rulemessage2.pack(side='top', anchor=W, padx=50)

def lifelinedescription4():
    rulewindow4()

    mycursor.execute("select ldescription from lifeline where lnumber=4")
    for i in mycursor:
        rulemessage1 = Label(panel, bg='#2e004d', fg='yellow', text='1.' + str(i)[2:61],
                             font='Arial 22 bold')  # RULE CHANGE AFFECTED
        rulemessage1.pack(side='top', anchor=W, padx=50)
        rulemessage2 = Label(panel, bg='#2e004d', fg='yellow', text='2.' + str(i)[61:-3],
                             font='Arial 22 bold')  # RULE CHANGE AFFECTED
        rulemessage2.pack(side='top', anchor=W, padx=50)





def developerinfo():
    global developerframedestroy,startframedestroy, developerframe , filename
    developerframedestroy = 1
    startframe.destroy()
    startframedestroy=0
    developerframe = Frame(screen, bg='#2e004d')
    developerframe.pack()
    mixer.music.load(os.path.join(path, 'Images and icons\play.mp3'))
    mixer.music.play()
    filename = os.path.join(path, 'Images and icons\kbc.png')
    set_background()

    waste = Label(panel, bg='#2e004d', fg='white', text='',
                    font='Arial 10 bold underline')
    waste.pack(side='top', anchor=W,padx=840)

    heading = Label(panel, bg='#2e004d', fg='white', text='DEVELOPER INFORMATION',
                  font='Arial 36 bold underline')
    heading.pack(side='top', anchor=W, pady=50, padx=30)

    developer1 = Label(panel, bg='#2e004d', fg='yellow',
                       text='NAME - ALOK PUROHIT\nPHONE - 7718064605\nEMAIL - alokpurohit18@gmail.com',
                       font='Arial 28 bold')
    developer1.pack(side='top', pady=30,anchor=W,padx=45)

    developer2 = Label(panel, bg='#2e004d', fg='yellow',
                       text='NAME - ANIKET RAMAN\nPHONE - 9769910607\nEMAIL - aniketraman@hotmail.com',
                       font='Arial 28 bold')
    developer2.pack(side='top',anchor=W,padx=45)

    backbutton = Button(panel, text='BACK', font='Arial 32 bold', bg='black', fg='white', border=5,
                        command=startingwindow)
    backbutton.pack(side='top', pady=110,padx=250,anchor=W)





def loginwindow1():
    global loginframe, loginframedestroy,startframedestroy,filename,iconfile

    startframe.destroy()
    startframedestroy=0

    loginframe = Frame(screen, bg='#2e004d')
    loginframe.pack()
    loginframedestroy = 1

    mixer.music.load(os.path.join(path, 'Images and icons\play.mp3'))
    mixer.music.play()
    filename = os.path.join(path, 'Images and icons\kbc.png')
    set_background()

    waste = Label(panel, bg='#2e004d', fg='white', text='',
                  font='Arial 3 bold underline')
    waste.pack(side='top', anchor=W, padx=840)

    waste2 = Label(panel, bg='#2e004d', fg='white', text='',
                  font='Arial 3 bold underline')
    waste2.pack(side='bottom', anchor=W, padx=840)

    heading = Label(panel, bg='#2e004d', fg='white', text='LOGIN PAGE', font='Arial 36 bold underline')
    heading.pack(side='top',padx=150, pady=50,anchor=W)

    text1 = Label(panel, bg='#2e004d', fg='yellow', text='USERNAME', font='Arial 24 bold')
    text1.pack(side='top',padx=210, pady=40,anchor=W)

    usernameentry = Entry(panel, textvariable=username, bg='white', fg='black', font='Arial 24 bold')
    usernameentry.pack(side='top',anchor=W,padx=120)

    text2 = Label(panel, bg='#2e004d', fg='yellow', text='PASSWORD', font='Arial 24 bold')
    text2.pack(side='top', pady=30,anchor=W,padx=210)

    passwordentry = Entry(panel, textvariable=password, bg='white', fg='black', font='Arial 24 bold', show='*')
    passwordentry.pack(side='top',anchor=W,padx=120)

    iconfile = os.path.join(path, 'Images and icons\login.png')
    set_icon()
    loginbutton = Button(panel, text=' LOGIN ',image=icon,compound=LEFT, font='Arial 30 bold', bg='black', fg='white', border=5,
                         command=loginwindow2)
    loginbutton.image = icon
    loginbutton.pack(side='top', padx=200, pady=60,anchor=W)

    backbutton = Button(panel, text='BACK', font='Arial 32 bold', bg='black', fg='white', border=5,
                        command=startingwindow)
    backbutton.pack(side='left', padx=90,anchor=W,pady=20)

    createaccountbutton = Button(panel, text='CREATE\nACCOUNT', font='Arial 22 bold', bg='black', fg='white',
                                 border=5, command=createaccount)
    createaccountbutton.pack(side='left',anchor=W,pady=20)

def loginwindow2():
    flag = 0
    mycursor.reset()
    if username.get() == '' or password.get() == '':
        messagebox.showinfo("Kaun Banega Crorepati - The Game", "ALL FIELDS ARE REQUIRED.")
    else:
        mycursor.execute("select username,password from player")
        for i in mycursor:
            if i[0] == username.get() and i[1] == password.get():
                messagebox.showinfo("Kaun Banega Crorepati - The Game", "LOGIN SUCCESSFUL.")
                flag = 2
                break
            elif i[0] == username.get() and i[1] != password.get():
                messagebox.showinfo("Kaun Banega Crorepati - The Game", "INVALID PASSWORD.")
                flag = 1
                break
            else:
                continue

        if flag == 0:
            messagebox.showinfo("Kaun Banega Crorepati - The Game", "INVALID USERNAME.")
        elif flag == 1:
            pass
        else:
            accountwindow()





def createaccount():
    global accountframedestroy, accountframe,startframedestroy,loginframedestroy,filename
    user = StringVar()
    passwd = StringVar()
    age = IntVar()
    name = StringVar()
    gender = StringVar()
    email = StringVar()
    localpassword = StringVar()
    age.set(12)

    if accountframedestroy == 1:
        accountframe.destroy()

    elif loginframedestroy == 0:
        startframe.destroy()
        startframedestroy=0
    else:
        loginframe.destroy()
        loginframedestroy=0

    accountframe = Frame(screen, bg='#2e004d')
    accountframe.pack()
    accountframedestroy = 1

    mixer.music.load(os.path.join(path, 'Images and icons\play.mp3'))
    mixer.music.play()
    file = os.path.join(path, 'Images and icons\kone.jpeg')
    img = Image.open(file)
    img = img.resize((600, 300), Image.ANTIALIAS)
    img = ImageTk.PhotoImage(img)

    waste = Label(accountframe, bg='#2e004d', fg='white', text='',
                  font='Arial 3 bold underline')
    waste.pack(side='top', anchor=W, padx=840)

    panel = Label(accountframe, image=img, width=600, height=300)
    panel.image = img
    panel.pack(side='right', padx=120,anchor=W)

    heading = Label(accountframe, bg='black', fg='white', text='NEW ACCOUNT', font='Arial 36 bold underline')
    heading.pack(side='top', pady=40,anchor=W,padx=150)


    text1 = Label(accountframe, bg='#2e004d', fg='yellow', text='FULL NAME', font='Arial 22 bold')
    text1.pack(side='top', pady=30, padx=250,anchor=W)

    nameentry = Entry(accountframe, textvariable=name, bg='white', fg='black', font='Arial 22 bold')
    nameentry.pack(side='top', padx=170,anchor=W)

    text2 = Label(accountframe, bg='#2e004d', fg='yellow', text='USERNAME', font='Arial 22 bold')
    text2.pack(side='top', pady=30, padx=250,anchor=W)

    usernameentry = Entry(accountframe, textvariable=user, bg='white', fg='black', font='Arial 22 bold')
    usernameentry.pack(side='top', padx=170,anchor=W)

    text3 = Label(accountframe, bg='#2e004d', fg='yellow', text='GENDER', font='Arial 22 bold')
    text3.pack(side='top', padx=270, pady=30,anchor=W)

    genderentry = OptionMenu(accountframe, gender, 'MALE', 'FEMALE', 'OTHER')
    genderentry.configure(font='Arial 22 bold', bg='white', fg='black')
    genderentry.pack(side='top', padx=270,anchor=W)

    def nextwindow():
        localcursor.reset()
        flag = 0
        if user.get() == '' or name.get() == '' or gender.get() == '':
            messagebox.showinfo("Kaun Banega Crorepati - The Game", "ALL FIELDS ARE REQUIRED.")
        else:
            localcursor.execute("select username from player")
            for i in localcursor:
                if str(i)[2:-3] == user.get():
                    flag = 1
                    break
            if flag == 1:
                messagebox.showinfo("Kaun Banega Crorepat - The Game",
                                    "USERNAME ALRAEDY EXISTS. PLEASE CHOOSE ANOTHER ONE.")
            else:
                global accountframe
                accountframe.destroy()
                accountframe = Frame(screen, bg='#2e004d')
                accountframe.pack()

                mixer.music.load(os.path.join(path, 'Images and icons\play.mp3'))
                mixer.music.play()
                file = os.path.join(path, 'Images and icons\kone.jpeg')
                img = Image.open(file)
                img = img.resize((600, 300), Image.ANTIALIAS)
                img = ImageTk.PhotoImage(img)

                waste = Label(accountframe, bg='#2e004d', fg='white', text='',
                              font='Arial 3 bold underline')
                waste.pack(side='top', anchor=W, padx=840)

                panel = Label(accountframe, image=img, width=600, height=300)
                panel.image = img
                panel.pack(side='right', padx=120, anchor=W)

                heading = Label(accountframe, bg='black', fg='white', text='NEW ACCOUNT',
                                font='Arial 36 bold underline')
                heading.pack(side='top', pady=25,anchor=W,padx=140)

                text1 = Label(accountframe, bg='#2e004d', fg='yellow', text='AGE', font='Arial 22 bold')
                text1.pack(side='top', pady=20,anchor=W,padx=290)

                ageentry = Entry(accountframe, textvariable=age, bg='white', fg='black', font='Arial 22 bold')
                ageentry.pack(side='top',anchor=W,padx=160)

                text2 = Label(accountframe, bg='#2e004d', fg='yellow', text='EMAIL', font='Arial 22 bold')
                text2.pack(side='top', pady=20,anchor=W,padx=280)

                emailentry = Entry(accountframe, textvariable=email, bg='white', fg='black', font='Arial 22 bold')
                emailentry.pack(side='top',anchor=W,padx=160)

                text3 = Label(accountframe, bg='#2e004d', fg='yellow', text='PASSWORD', font='Arial 22 bold')
                text3.pack(side='top', pady=20, padx=240,anchor=W)

                passwordentry = Entry(accountframe, textvariable=passwd, bg='white', fg='black', font='Arial 22 bold',
                                      show='*')
                passwordentry.pack(side='top', padx=160,anchor=W)

                text4 = Label(accountframe, bg='#2e004d', fg='yellow', text='CONFIRM\nPASSWORD', font='Arial 22 bold')
                text4.pack(side='top', padx=240, pady=20,anchor=W)

                passwordentry2 = Entry(accountframe, textvariable=localpassword, bg='white', fg='black',
                                       font='Arial 22 bold', show='*')
                passwordentry2.pack(side='top', padx=160,anchor=W)

                backbutton = Button(accountframe, text='BACK', font='Arial 32 bold', bg='black', fg='white', border=5,
                                    command=createaccount)
                backbutton.pack(side='left', padx=90, pady=40,anchor=W,ipady=5)

                createaccountbutton = Button(accountframe, text='CREATE\nACCOUNT', font='Arial 24 bold', bg='black',
                                             fg='white', border=5, command=validateaccount)
                createaccountbutton.pack(side='left', padx=10, pady=40,anchor=W)

    def validateaccount():
        mycursor.reset()
        localcursor.reset()
        k=[0]
        localcursor.execute("select email from player")
        for i in localcursor:
            if email.get()==str(i)[2:-3]:
                k[0]=1
                break

        if email.get() == '' or passwd.get() == '' or localpassword.get() == '':
            messagebox.showinfo("Kaun Banega Crorepati - The Game", "ALL FIELDS ARE REQUIRED.")
        elif age.get() < 12:
            messagebox.showinfo("Kaun Banega Crorepati - The Game", "MINIMUM AGE REQUIRED FOR THIS GAME IS 12.")
        elif k[0]==1:
            messagebox.showinfo("Kaun Banega Crorepati - The Game", "THERE IS ALREADY AN ACCOUNT WITH THIS EMAIL ID.")
        elif passwd.get() != localpassword.get():
            messagebox.showinfo("Kaun Banega Crorepati - The Game", "PLEASE ENTER SAME PASSWORDS.")
        else:
            messagebox.showinfo("Kaun Banega Crorepati - The Game", "ACCOUNT SUCCESSFULLY CREATED.")
            if gender.get() == 'MALE':
                g = 'M'
            elif gender.get() == 'FEMALE':
                g = 'F'
            else:
                g = 'O'
            mycursor.execute(
                "insert into player (username, password, age , name , gender, email, highest_score) value ('{}', '{}', '{}', '{}', '{}', '{}',0);".format(
                    user.get(), passwd.get(), age.get(), name.get(), g, email.get()))
            mydb.commit()
            startingwindow()

    def previouswindow():
        user.set('')
        name.set('')
        gender.set('')
        startingwindow()

    backbutton = Button(accountframe, text='  BACK', font='Arial 32 bold', bg='black', fg='white', border=5,anchor=W,
                        command=previouswindow)
    backbutton.pack(side='left', padx=90, pady=60,ipady=5)

    nextbutton = Button(accountframe, text='  NEXT', font='Arial 33 bold', bg='black', fg='white', border=5,anchor=W,
                        command=nextwindow)
    nextbutton.pack(side='left', padx=20, pady=60,ipady=5)






def accountwindow():
    global gameframedestroy,filename,loginframedestroy,gameframe,iconfile,denomination
    mycursor.reset()
    denomination=5000
    if loginframedestroy==1:
         loginframe.destroy()
         loginframedestroy=0
    if gameframedestroy==1:
        gameframe.destroy()
    gameframe = Frame(screen, bg='#2e004d')
    gameframe.pack()
    gameframedestroy=1
    mixer.music.load(os.path.join(path, 'Images and icons\play.mp3'))
    mixer.music.play()
    filename = os.path.join(path, 'Images and icons\kbc.png')
    set_background()

    name = ['']
    mycursor.execute("select name from player where username = '{}'".format(username.get()))
    for i in mycursor:
        name[0] = str(i)[2:-3]

    waste = Label(panel, bg='#2e004d', fg='white', text='',
                  font='Arial 3 bold underline')
    waste.pack(side='top', anchor=W, padx=840)

    iconfile = os.path.join(path, 'Images and icons\logout.png')
    set_icon()

    userheading = Label(panel, bg='#2e004d', fg='yellow', text=username.get()+"\n"+name[0], font='Arial 24 bold',border=10)
    userheading.pack(side='left', anchor=NW,padx=20, pady=20)

    logoutbutton = Button(panel, text=' LOGOUT ', image=icon,compound=LEFT, font='Arial 24 bold', bg='black', fg='white', border=5,command=startingwindow)
    logoutbutton.image = icon
    logoutbutton.pack(side='right', padx=20, anchor=NE, pady=20)

    startgamebutton = Button(panel, text='START\nGAME',  font='Arial 42 bold', bg='black',
                          fg='white', border=5,command=startgame1)
    startgamebutton.pack(side='left',anchor=NW, padx=60, pady=320,ipadx=20)

    highscorebutton = Button(panel, text='HIGH\nSCORES', font='Arial 42 bold', bg='black',
                        fg='white', border=5,command=highscores)
    highscorebutton.pack(side='right', padx=60, pady=320,ipadx=20)





def highscores():
    global filename, loginframedestroy, gameframe, iconfile
    mycursor.reset()
    gameframe.destroy()
    gameframe = Frame(screen, bg='#2e004d')
    gameframe.pack()
    mixer.music.load(os.path.join(path, 'Images and icons\play.mp3'))
    mixer.music.play()
    filename = os.path.join(path, 'Images and icons\kbc.png')
    set_background()

    waste = Label(panel, bg='#2e004d', fg='white', text='',
                  font='Arial 3 bold underline')
    waste.pack(side='top', anchor=W, padx=840)

    iconfile = os.path.join(path, 'Images and icons\logout.png')
    set_icon()

    mycursor.reset()
    name = ['']
    mycursor.execute("select name from player where username = '{}'".format(username.get()))
    for i in mycursor:
        name[0] = str(i)[2:-3]

    score = ['']
    mycursor.reset()
    mycursor.execute("select highest_score from player where username = '{}'".format(username.get()))
    for i in mycursor:
        score[0] = str(i)[1:-2]

    userheading = Label(panel, bg='#2e004d', fg='yellow', text=username.get() + "\n" + name[0], font='Arial 24 bold',border=10)
    userheading.pack(side='left', anchor=NW, padx=20, pady=20)

    logoutbutton = Button(panel, text=' LOGOUT ', image=icon, compound=LEFT, font='Arial 24 bold', bg='black',fg='white', border=5, command=startingwindow)
    logoutbutton.image = icon
    logoutbutton.pack(side='right', padx=20, anchor=NE, pady=20)

    localhighscore = Label(panel, bg='black', fg='yellow', text="YOUR HIGH SCORE = "+score[0], font='Arial 34 bold', border=10)
    localhighscore.pack(side='top',  padx=80, pady=180)

    mycursor.reset()
    mycursor.execute("select max(highest_score) from player")
    for i in mycursor:
        score[0] = str(i)[1:-2]

    globalhighscore = Label(panel, bg='black', fg='yellow', text="GLOBAL HIGH SCORE = " + score[0], font='Arial 34 bold',border=10)
    globalhighscore.pack(side='top', padx=80,pady=20)

    backbutton = Button(panel, text='BACK', font='Arial 32 bold', bg='black', fg='white', border=5,
                        command=accountwindow)
    backbutton.pack(side='top', padx=80, pady=90)





def startgame2(friend1,friend2,friend3):
        global filename, gameframe, iconfile
        gameframe.destroy()
        gameframe = Frame(screen, bg='#2e004d')
        gameframe.pack()
        mixer.music.load(os.path.join(path, 'Images and icons\play.mp3'))
        mixer.music.play()
        filename = os.path.join(path, 'Images and icons\kbc.png')
        set_background()
        iconfile = os.path.join(path, 'Images and icons\quit.png')
        set_icon()

        waste = Label(panel, bg='#2e004d', fg='white', text='',
                      font='Arial 3 bold underline')
        waste.pack(side='top', anchor=W, padx=840)

        mycursor.reset()
        name = ['']
        mycursor.execute("select name from player where username = '{}'".format(username.get()))
        for i in mycursor:
            name[0] = str(i)[2:-3]

        userheading = Label(panel, bg='#2e004d', fg='yellow', text=username.get() + "\n" + name[0],
                            font='Arial 24 bold',
                            border=10)
        userheading.pack(side='left', anchor=NW, padx=20, pady=20)

        quitbutton = Button(panel, text=' QUIT ', image=icon, compound=LEFT, font='Arial 24 bold', bg='black',
                            fg='white',
                            border=5, command=quitgame)
        quitbutton.image = icon
        quitbutton.pack(side='right', padx=40, anchor=NE, pady=40)

        displayquestion(friend1,friend2,friend3)

def startgame1():
    global  gameframe,phonedone,fiftyfiftydone,audiencedone,expertdone

    phonedone=0
    fiftyfiftydone=0
    audiencedone=0
    expertdone=0

    mycursor.reset()
    mixer.music.load(os.path.join(path, 'Images and icons\play.mp3'))
    mixer.music.play()

    gameframe.destroy()
    gameframe = Frame(screen, bg='#2e004d')
    gameframe.pack()

    waste = Label(gameframe, bg='#2e004d', fg='white', text='',
                  font='Arial 3 bold underline')
    waste.pack(side='top', anchor=W, padx=840)

    userheading = Label(gameframe, bg='#2e004d', fg='yellow', text='PLEASE ENTER THE NAMES OF THE 3 FRIENDS,\nWHO YOU WOULD WANT TO CALL FOR HELP.', font='Arial 32 bold',
                        border=10)
    userheading.pack(side='top', padx=100, pady=40)

    friendentry1 = Entry(gameframe, bg='white',text=friend1.get(),textvariable=friend1, fg='black', font='Arial 22 bold')
    friendentry1.pack(side='top', padx=170, pady=40)

    friendentry2 = Entry(gameframe, bg='white',text=friend2.get(),textvariable=friend2, fg='black', font='Arial 22 bold')
    friendentry2.pack(side='top', padx=170, pady =40)

    friendentry3 = Entry(gameframe,  bg='white',text=friend3.get(),textvariable=friend3, fg='black', font='Arial 22 bold')
    friendentry3.pack(side='top', padx=170, pady=40)

    okbutton = Button(gameframe, text='  OK  ', font='Arial 32 bold', bg='black', fg='white',
                        border=5, command=lambda :startgame2(friend1.get(),friend2.get(),friend3.get()))
    okbutton.pack(side='top', padx=250, pady=40)





def displayquestion(friend1,friend2,friend3):

    global denomination,optiona,optionb,optionc,optiond,sameq_flag
    sameq_flag=0

    if denomination==10000 or denomination==320000 or denomination==10000000:
        userheading = Label(panel, bg='black', fg='yellow', text=str(denomination), font='Arial 28 bold underline',
                            border=10)
        userheading.pack(side='top', padx=50, anchor=N, pady=40)
    else:
        userheading = Label(panel, bg='black', fg='white', text=str(denomination), font='Arial 28 bold underline',
                            border=10)
        userheading.pack(side='top', padx=50, anchor=N,pady=40)

    mixer.music.load(os.path.join(path, 'Images and icons\kbc.mp3'))
    mixer.music.play()

    mycursor.reset()
    mycursor.execute("select qnumber from gets where username = '{}'".format(username.get()))
    chr=mycursor.fetchall()

    qnumber=0
    mycursor.reset()
    mycursor.execute("select qnumber from question where denomination = {}".format(denomination))
    for i in mycursor:
        if i not in chr:
            qnumber=i[0]
            break

    mycursor.reset()
    mycursor.execute("select description from question where qnumber = {}".format(qnumber))
    j = mycursor.fetchone()
    question = str(j)[2:-3]

    mycursor.reset()
    mycursor.execute(
        "insert into gets(username, qnumber) values ('{}', {});".format(username.get(), qnumber))
    mydb.commit()

    mycursor.reset()
    mycursor.execute("select max(gnumber) from game")
    i = mycursor.fetchone()
    gnumber = i[0] + 1

    mycursor.reset()
    mycursor.execute("insert into uses(gnumber, qnumber) values ({}, {});".format(gnumber, qnumber))  # RULE CHANGE AFFECTED
    mydb.commit()

    if len(question) < 81:
        questionlabel = Label(panel, bg='black', fg='yellow', text='Q.'+question,
                         font='Arial 18 bold', border=5)
        questionlabel.pack(side='top', anchor=N, padx=20, pady=40)

        waste2 = Label(panel, bg='#2e004d', fg='white', text='',
                       font='Arial 3 bold underline')
        waste2.pack(side='bottom', anchor=W, padx=840, pady=22)

    else:
        questionlabel = Label(panel, bg='black', fg='yellow', text='Q.' + str(j)[2:81]+'-\n-'+str(j)[81:-3],
                         font='Arial 18 bold', border=5)
        questionlabel.pack(side='top', anchor=N, padx=10, pady=40)

        waste2 = Label(panel, bg='#2e004d', fg='white', text='',
                       font='Arial 3 bold underline')
        waste2.pack(side='bottom', anchor=W, padx=840, pady=7)


    mycursor.reset()
    mycursor.execute("select option_a,option_b,option_c,option_d from question where qnumber = '{}'".format(qnumber))
    i=mycursor.fetchone()

    optiona = Button(panel, text='A.'+i[0], font='Arial 18 bold', bg='black', fg='yellow',command= lambda: set_optionA(qnumber))
    optiona.pack(side='top', padx=40,pady=20)

    optionb = Button(panel, text='B.'+i[1], font='Arial 18 bold', bg='black', fg='yellow',command= lambda: set_optionB(qnumber))
    optionb.pack(side='top', padx=40,pady=20)

    optionc = Button(panel, text='C.'+i[2], font='Arial 18 bold', bg='black', fg='yellow',command= lambda: set_optionC(qnumber))
    optionc.pack(side='top', padx=40,pady=20)

    optiond = Button(panel, text='D.'+i[3], font='Arial 18 bold', bg='black', fg='yellow',command= lambda : set_optionD(qnumber))
    optiond.pack(side='top', padx=40,pady=20)

    displaylifelines(friend1,friend2,friend3,qnumber)

def displaylifelines(friend1,friend2,friend3,qnumber):
    global lifelinebutton4,lifelinebutton2,lifelinebutton1,lifelinebutton4,icon,iconfile

    mycursor.reset()
    mycursor.execute("select correct from question where qnumber = '{}'".format(qnumber))
    i = mycursor.fetchone()
    correct=i[0]

    if audiencedone==0:
        iconfile = os.path.join(path, 'Images and icons\Audiencepoll.png')
        lifeline_icon()
        lifelinebutton1 = Button(panel, image=icon, compound=LEFT, font='Arial 24 bold', bg='black', fg='yellow',
                                 border=5,command= lambda :audiencepoll(correct))

    else:
        iconfile = os.path.join(path, 'Images and icons\Audiencepoll-done.png')
        lifeline_icon()
        lifelinebutton1 = Button(panel, image=icon, compound=LEFT, font='Arial 24 bold', bg='black', fg='yellow',
                                 border=5)


    lifelinebutton1.image = icon
    lifelinebutton1.pack(side='left', anchor=NW, padx=90, pady=40)

    if phonedone==0:
        iconfile = os.path.join(path, 'Images and icons\phoneafriend.png')
        lifeline_icon()
        lifelinebutton2 = Button(panel, image=icon, compound=LEFT, font='Arial 24 bold', bg='black', fg='yellow', border=5,
                                 command=lambda : phoneafriend(friend1,friend2,friend3,correct))

    else:
        iconfile = os.path.join(path, 'Images and icons\phoneafriend-done.png')
        lifeline_icon()
        lifelinebutton2 = Button(panel, image=icon, compound=LEFT, font='Arial 24 bold', bg='black', fg='yellow', border=5)


    lifelinebutton2.image = icon
    lifelinebutton2.pack(side='left', anchor=NW, padx=90, pady=40)


    if expertdone==0:
        iconfile = os.path.join(path, 'Images and icons\expertadvice.png')
        lifeline_icon()
        lifelinebutton3 = Button(panel, image=icon, compound=LEFT, font='Arial 24 bold', bg='black', fg='yellow', border=5,command= lambda: expertadvice(correct))

    else:
        iconfile = os.path.join(path, 'Images and icons\expertadvice-done.png')
        lifeline_icon()
        lifelinebutton3 = Button(panel, image=icon, compound=LEFT, font='Arial 24 bold', bg='black', fg='yellow',
                                 border=5)

    lifelinebutton3.image = icon
    lifelinebutton3.pack(side='left', anchor=NW, padx=90, pady=40)

    if fiftyfiftydone==0:
        iconfile = os.path.join(path, 'Images and icons\\fifty-fifty.png')
        lifeline_icon()
        lifelinebutton4 = Button(panel, image=icon, compound=LEFT, font='Arial 24 bold', bg='black', fg='yellow', border=5,
                                 command= lambda : fiftyfifty(correct))

    else:
        iconfile = os.path.join(path, 'Images and icons\\fifty-fifty-done.png')
        lifeline_icon()
        lifelinebutton4 = Button(panel, image=icon, compound=LEFT, font='Arial 24 bold', bg='black', fg='yellow',border=5)


    lifelinebutton4.image = icon
    lifelinebutton4.pack(side='left', anchor=NE, padx=90, pady=40)





def set_optionA(qnumber):
    response = messagebox.askyesno("Kaun Banega Crorepati - The Game", "Do you want to lock option A ?")
    if response == 1:
        answer = 'a'
        validateanswer(answer,qnumber)

def set_optionB(qnumber):
    response = messagebox.askyesno("Kaun Banega Crorepati - The Game", "Do you want to lock option B ?")
    if response == 1:
        answer = 'b'
        validateanswer(answer, qnumber)

def set_optionC(qnumber):
    response = messagebox.askyesno("Kaun Banega Crorepati - The Game", "Do you want to lock option C ?")
    if response == 1:
        answer = 'c'
        validateanswer(answer, qnumber)

def set_optionD(qnumber):
    response = messagebox.askyesno("Kaun Banega Crorepati - The Game", "Do you want to lock option D ?")
    if response == 1:
        answer = 'd'
        validateanswer(answer, qnumber)





def validateanswer(answer,qnumber):
    global filename, gameframe, iconfile, denomination
    mycursor.reset()
    gameframe.destroy()
    gameframe = Frame(screen, bg='#2e004d')
    gameframe.pack()
    mixer.music.load(os.path.join(path, 'Images and icons\play.mp3'))
    mixer.music.play()
    filename = os.path.join(path, 'Images and icons\kbc.png')
    set_background()

    waste = Label(panel, bg='#2e004d', fg='white', text='',
                  font='Arial 3 bold underline')
    waste.pack(side='top', anchor=W, padx=840)

    mycursor.execute("select correct from question where qnumber = '{}'".format(qnumber))
    correct = mycursor.fetchone()

    if answer == correct[0]:
        if denomination == 10000:
            winningmessage = Label(panel, bg='black', fg='yellow',
                                   text='THAT IS THE CORRECT ANSWER!!!\nCONGRATULATIONS!!!\nYOU HAVE WON RS ' + str(
                                       denomination)+'.\n\nYOU HAVE CLEARED THE FIRST CHECKPOINT.\nYOU WILL ATLEAST WIN RS '
                                        +str(denomination)+ ' FROM HERE.', font='Arial 28 bold',
                                   border=10)
            winningmessage.pack(side='top', padx=300, pady=120)

            okbutton = Button(panel, text=' OK ', font='Arial 32 bold', bg='black', fg='white', border=5,
                              command=lambda:startgame2(friend1.get(),friend2.get(),friend3.get()))
            okbutton.pack(side='top', padx=80, pady=102)

        elif  denomination == 320000:
            winningmessage = Label(panel, bg='black', fg='yellow',
                                   text='THAT IS THE CORRECT ANSWER!!!\nCONGRATULATIONS!!!\nYOU HAVE WON RS ' + str(
                                       denomination)+'.\n\nYOU HAVE CLEARED THE SECOND CHECKPOINT.\nYOU WILL ATLEAST WIN RS '
                                        +str(denomination)+ ' FROM HERE.', font='Arial 28 bold',
                                   border=10)

            winningmessage.pack(side='top', padx=300, pady=120)

            okbutton = Button(panel, text=' OK ', font='Arial 32 bold', bg='black', fg='white', border=5,
                              command=lambda :startgame2(friend1.get(),friend2.get(),friend3.get()))
            okbutton.pack(side='top', padx=80, pady=102)

        elif denomination == 10000000:
            winningmessage = Label(panel, bg='black', fg='yellow',
                                   text='THAT IS THE CORRECT ANSWER!!!\nCONGRATULATIONS!!!\nYOU HAVE WON RS ' + str(
                                       denomination)+'.\n\nYOU HAVE CLEARED THE LAST CHECKPOINT.\nYOU ARE A CROREPATI !!!\nYOU WILL ATLEAST WIN RS '
                                        +str(denomination)+ ' FROM HERE.', font='Arial 28 bold',
                                   border=10)
            winningmessage.pack(side='top', padx=300, pady=100)

            okbutton = Button(panel, text=' OK ', font='Arial 32 bold', bg='black', fg='white', border=5,
                              command=lambda :startgame2(friend1.get(),friend2.get(),friend3.get()))
            okbutton.pack(side='top', padx=80, pady=102)

        elif denomination == 50000000:
            winningmessage = Label(panel, bg='black', fg='yellow',
                                   text='THAT IS THE CORRECT ANSWER!!!\nCONGRATULATIONS!!!\nYOU HAVE WON RS ' + str(
                                       denomination)+'.\n\nYOU HAVE WON THE JACKPOT!!!\nYOU HAVE COMPLETED THE GAME.YOU NOW OWN RS 50000000 !!!'
                                        , font='Arial 28 bold',
                                   border=10)
            winningmessage.pack(side='top', padx=150, pady=120)

            okbutton = Button(panel, text=' OK ', font='Arial 32 bold', bg='black', fg='white', border=5,
                              command=lambda :startgame2(friend1.get(),friend2.get(),friend3.get()))
            okbutton.pack(side='top', padx=80, pady=102)

        else:
            winningmessage = Label(panel, bg='black', fg='yellow', text='THAT IS THE CORRECT ANSWER!!!\nCONGRATULATIONS!!!\nYOU HAVE WON RS '+str(denomination)+'.', font='Arial 28 bold',
                                border=10)
            winningmessage.pack(side='top', padx=440, anchor=NW, pady=180)

            okbutton = Button(panel, text=' OK ', font='Arial 32 bold', bg='black', fg='white', border=5,
                                command=lambda :startgame2(friend1.get(),friend2.get(),friend3.get()))
            okbutton.pack(side='top', padx=80, pady=110)

    else:
        winning=[0]
        if denomination<=10000:   #RULE CHANGE AFFECTED
            winning[0]=0
        elif denomination>10000 and denomination<=320000:
            winning[0]=10000
        elif denomination>320000 and denomination<=10000000:
            winning[0]=320000
        else:
            winning[0]=10000000

        winningmessage = Label(panel, bg='black', fg='yellow',
                               text='SORRY, THAT IS THE WRONG ANSWER...\nYOU HAVE WON RS ' + str(
                                   winning[0]) + '.\n\nTHANK YOU FOR PLAYING THE GAME!!!', font='Arial 28 bold',
                               border=10)

        winningmessage.pack(side='top', padx=300, pady=200)

        okbutton = Button(panel, text=' OK ', font='Arial 32 bold', bg='black', fg='white', border=5,
                          command=accountwindow)
        okbutton.pack(side='top', padx=80, pady=65)

        mycursor.reset()
        mycursor.execute("select max(gnumber) from game")
        i=mycursor.fetchone()
        gnumber= i[0] + 1


        mycursor.reset()
        mycursor.execute("select highest_score from player where username='{}'".format(username.get()))
        i=mycursor.fetchone()
        highscore=i[0]

        if winning[0]>highscore:
            mycursor.reset()
            mycursor.execute( "update player set highest_score = '{}' where username = '{}';".format(winning[0], username.get()))
            mydb.commit()


        mycursor.reset()
        mycursor.execute("insert into game(gnumber, username, amount_won, quit, friend1, friend2, friend3) values ({}, '{}', {}, 'F', '{}', '{}', '{}');"
                         .format(gnumber, username.get(), winning[0], friend1.get(), friend2.get(), friend3.get()))
        mydb.commit()


        i=1
        while i<=6:
            mycursor.reset()
            mycursor.execute(
                "insert into follow(gnumber, rnumber, game_year) values ({}, {}, {});".format(gnumber, i,  2020))  # RULE CHANGE AFFECTED
            mydb.commit()
            i=i+1


        if audiencedone==1:
            mycursor.reset()
            mycursor.execute(
                "insert into used(lnumber,gnumber) values ({}, {});".format(1, gnumber))  # RULE CHANGE AFFECTED
            mydb.commit()
        if phonedone==1:
            mycursor.reset()
            mycursor.execute(
                "insert into used(lnumber,gnumber) values ({}, {});".format(2, gnumber))  # RULE CHANGE AFFECTED
            mydb.commit()
        if expertdone==1:
            mycursor.reset()
            mycursor.execute(
                "insert into used(lnumber,gnumber) values ({}, {});".format(3, gnumber))  # RULE CHANGE AFFECTED
            mydb.commit()
        if fiftyfiftydone==1:
            mycursor.reset()
            mycursor.execute(
                "insert into used(lnumber,gnumber) values ({}, {});".format(4, gnumber))  # RULE CHANGE AFFECTED
            mydb.commit()



    if denomination==640000:     #RULE CHANGE AFFECTED
        denomination=1250000
    elif denomination==10000000:
        denomination=50000000
    else:
        denomination = denomination*2





def quitgame():
   global filename, gameframe, iconfile, denomination
   winning=[0]
   response =  messagebox.askyesno("Kaun Banega Crorepati - The Game","Do you want to quit the game?")
   if response==1:
       if denomination==1250000:
           winning[0]=640000
       elif denomination==50000000:
           winning[0]=10000000
       elif denomination==5000:
           winning[0]=0
       else:
           winning[0] = int(denomination/2)

       mycursor.reset()
       gameframe.destroy()
       gameframe = Frame(screen, bg='#2e004d')
       gameframe.pack()
       mixer.music.load(os.path.join(path, 'Images and icons\play.mp3'))
       mixer.music.play()
       filename = os.path.join(path, 'Images and icons\kbc.png')
       set_background()

       waste = Label(panel, bg='#2e004d', fg='white', text='',
                     font='Arial 3 bold underline')
       waste.pack(side='top', anchor=W, padx=840)

       winningmessage = Label(panel, bg='black', fg='yellow',
                              text='YOU HAVE QUIT THE GAME .....\nYOU HAVE WON RS ' + str(
                                  winning[0]) + '.\n\nTHANK YOU FOR PLAYING THE GAME!!!', font='Arial 28 bold',
                              border=10)
       winningmessage.pack(side='top', padx=300, pady=200)

       okbutton = Button(panel, text=' OK ', font='Arial 32 bold', bg='black', fg='white', border=5,
                         command=accountwindow)
       okbutton.pack(side='top', padx=80, pady=65)

       mycursor.reset()
       mycursor.execute("select max(gnumber) from game")
       i = mycursor.fetchone()
       gnumber = i[0] + 1

       mycursor.reset()
       mycursor.execute(
           "insert into game(gnumber, username, amount_won, quit, friend1, friend2, friend3) values ({}, '{}', {}, 'T', '{}', '{}', '{}');"
           .format(gnumber, str(username.get()), winning[0], str(friend1.get()), str(friend2.get()), str(friend3.get())))
       mydb.commit()

       mycursor.reset()
       mycursor.execute("select highest_score from player where username='{}'".format(username.get()))
       i = mycursor.fetchone()
       highscore = i[0]

       if winning[0] > highscore:
           mycursor.reset()
           mycursor.execute(
               "update player set highest_score = '{}' where username = '{}';".format(winning[0], username.get()))
           mydb.commit()

       i = 1
       while i <= 6:
           mycursor.reset()
           mycursor.execute(
               "insert into follow(gnumber, rnumber, game_year) values ({}, {}, {});".format(gnumber, i,
                                                                                             2020))  # RULE CHANGE AFFECTED
           mydb.commit()
           i = i + 1

       if audiencedone == 1:
           mycursor.reset()
           mycursor.execute(
               "insert into used(lnumber,gnumber) values ({}, {});".format(1, gnumber))  # RULE CHANGE AFFECTED
           mydb.commit()
       if phonedone == 1:
           mycursor.reset()
           mycursor.execute(
               "insert into used(lnumber,gnumber) values ({}, {});".format(2, gnumber))  # RULE CHANGE AFFECTED
           mydb.commit()
       if expertdone == 1:
           mycursor.reset()
           mycursor.execute(
               "insert into used(lnumber,gnumber) values ({}, {});".format(3, gnumber))  # RULE CHANGE AFFECTED
           mydb.commit()
       if fiftyfiftydone == 1:
           mycursor.reset()
           mycursor.execute(
               "insert into used(lnumber,gnumber) values ({}, {});".format(4, gnumber))  # RULE CHANGE AFFECTED
           mydb.commit()




def fiftyfifty(correct):
    global fiftyfiftydone,aactive, bactive,cactive,dactive,iconfile,lifelinebutton4,sameq_flag
    sameq_flag=1
    fiftyfiftydone=1
    if (correct == 'a'):
        randnumber = randint(2, 4)
        if (randnumber == 2):
            optionc.destroy()
            optiond.destroy()
            cactive=0
            dactive=0
        if (randnumber == 3):
            optionb.destroy()
            optiond.destroy()
            bactive = 0
            dactive = 0
        if (randnumber == 4):
            optionb.destroy()
            optionc.destroy()
            cactive = 0
            bactive = 0

    if (correct == 'b'):
        randnumber = randint(2, 4)
        if (randnumber == 2):
            optionc.destroy()
            optiond.destroy()
            cactive = 0
            dactive = 0
        if (randnumber == 3):
            optiona.destroy()
            optiond.destroy()
            aactive = 0
            dactive = 0
        if (randnumber == 4):
            optiona.destroy()
            optionc.destroy()
            cactive = 0
            aactive = 0

    if (correct == 'c'):
        randnumber = randint(2, 4)
        if (randnumber == 2):
            optionb.destroy()
            optiond.destroy()
            bactive = 0
            dactive = 0
        if (randnumber == 3):
            optiona.destroy()
            optiond.destroy()
            aactive = 0
            dactive = 0
        if (randnumber == 4):
            optionb.destroy()
            optiona.destroy()
            bactive = 0
            aactive = 0

    if (correct == 'd'):
        randnumber = randint(2, 4)
        if (randnumber == 2):
            optionb.destroy()
            optionc.destroy()
            cactive = 0
            bactive = 0
        if (randnumber == 3):
            optiona.destroy()
            optionc.destroy()
            cactive = 0
            aactive = 0
        if (randnumber == 4):
            optionb.destroy()
            optiona.destroy()
            aactive = 0
            bactive = 0

    lifelinebutton4.destroy()
    iconfile = os.path.join(path, 'Images and icons\\fifty-fifty.png')
    lifeline_icon()
    lifelinebutton4 = Button(panel, image=icon, compound=LEFT, font='Arial 24 bold', bg='black', fg='yellow', border=5)
    lifelinebutton4.image = icon
    lifelinebutton4.pack(side='left', anchor=NE, padx=90, pady=40)

def phoneafriend(friend1,friend2,friend3,correct):
    global phonedone,fiftyfiftydone,iconfile
    correct=str(correct)
    correct=correct.upper()
    if phonedone==0:

        tgui = Tk()
        tgui.title("Phone A Friend")
        tgui.geometry('600x400+480+270')
        tgui.iconbitmap(os.path.join(path, 'Images and icons\kbc_logo.ico'))
        tgui.configure(bg='#2e004d')

        if (fiftyfiftydone == 1 and sameq_flag==1):
            friendanswer1 = ["I am confident the answer is ", "I am sure the correct option is ", "My answer would be "]
            friendanswer2 = ["I am confused between ", "According to me the answer might be ",
                             "Maybe the answer is either  "]
            friendanswer3 = ["I am sorry but I have no idea about this question. ",
                             "I apologize, I don't have any answer for this question. ",
                             "I regret to say that I don't the answer to this question. "]
            msg = Label(tgui, text="Who do you want to call?", font='Arial 16 bold', bg="#2e004d", fg='yellow', border=5)
            msg.pack(side='top', padx=100, pady=40)


            def friendbuttonpress1():
                msg.destroy()
                FRIEND1.destroy()
                FRIEND2.destroy()
                FRIEND3.destroy()
                msg1 = Label(tgui, text="Connecting to  " + friend1, font='Arial 16 bold', bg="#2e004d", fg='yellow',
                             border=5)
                msg1.pack(side='top', padx=100, pady=10)
                msg2 = Label(tgui, text="Connected...", font='Arial 16 bold', bg="#2e004d", fg='yellow', border=5)
                msg2.pack(side='top', padx=100, pady=10)

            def friendbuttonpress2():
                msg.destroy()
                FRIEND1.destroy()
                FRIEND2.destroy()
                FRIEND3.destroy()
                msg1 = Label(tgui, text="Connecting to " + friend2, font='Arial 16 bold', bg="#2e004d", fg='yellow',
                             border=5)
                msg1.pack(side='top', padx=100, pady=10)
                msg2 = Label(tgui, text="Connected...", font='Arial 16 bold', bg="#2e004d", fg='yellow', border=5)
                msg2.pack(side='top', padx=100, pady=10)

            def friendbuttonpress3():
                msg.destroy()
                FRIEND1.destroy()
                FRIEND2.destroy()
                FRIEND3.destroy()
                msg1 = Label(tgui, text="Connecting to " + friend3, font='Arial 16 bold', bg="#2e004d", fg='yellow',
                             border=5)
                msg1.pack(side='top', padx=100, pady=10)
                msg2 = Label(tgui, text="Connected...", font='Arial 16 bold', bg="#2e004d", fg='yellow', border=5)
                msg2.pack(side='top', padx=100, pady=10)

            def buttonpressuni():
                if (phonedone == 0):
                    if (denomination < 5000000):
                        randnumber3 = randint(1, 2)
                        if (randnumber3 == 1):
                            randstring = random.choice(friendanswer1)
                            friendanswers = Label(tgui, text=randstring + correct,font='Arial 16 bold',bg="#2e004d",fg='yellow',border=5)
                            friendanswers.pack(side='top', padx=20, pady=10)

                        if (randnumber3 == 2):
                            randstring = random.choice(friendanswer3)
                            friendanswers = Label(tgui, text=randstring,font='Arial 16 bold',bg="#2e004d",fg='yellow',border=5)
                            friendanswers.pack(side='top', padx=20, pady=10)
                    else:
                        randstring = random.choice(friendanswer3)
                        friendanswers = Label(tgui, text=randstring,font='Arial 16 bold',bg="#2e004d",fg='yellow',border=5)
                        friendanswers.pack(side='top', padx=20, pady=10)

            def disconnect():
                global phonedone
                msg3 = Label(tgui, text="Disconnected...", font='Arial 16 bold', bg="#2e004d", fg='yellow', border=5)
                msg3.pack(side='top', padx=200, pady=10)
                phonedone = 1
                OKbutton = Button(tgui, text='  OK  ', font='Arial 22 bold', bg="black", fg='yellow', border=5,
                                 command=tgui.destroy)
                OKbutton.pack(side='top', padx=200, pady=30)

            FRIEND1 = Button(tgui, text=friend1, font='Arial 16 bold', bg="black", fg='yellow', border=5,
                             command=lambda: [friendbuttonpress1(), buttonpressuni(), disconnect()])
            FRIEND1.pack(side='top', padx=200, pady=10)
            FRIEND2 = Button(tgui, text=friend2, font='Arial 16 bold', bg="black", fg='yellow', border=5,
                             command=lambda: [friendbuttonpress2(), buttonpressuni(), disconnect()])
            FRIEND2.pack(side='top', padx=200, pady=10)
            FRIEND3 = Button(tgui, text=friend3, font='Arial 16 bold', bg="black", fg='yellow', border=5,
                             command=lambda: [friendbuttonpress3(), buttonpressuni(), disconnect()])
            FRIEND3.pack(side='top', padx=200, pady=10)


        else:
            friendanswer1 = ["I am confident the answer is ", "I am sure the correct option is ", "My answer would be "]
            friendanswer2 = ["I am confused between ", "According to me the answer might be ",
                             "Maybe the answer is either  "]
            friendanswer3 = ["I am sorry but I have no idea about this question. ",
                             "I apologize, I don't have any answer for this question. ",
                             "I regret to say that I don't the answer to this question. "]
            msg = Label(tgui, text="Who do you want to call?",font='Arial 16 bold',bg="#2e004d",fg='yellow',border=5)
            msg.pack(side='top', padx=100, pady=40)

            def friendbuttonpress1():
                    msg.destroy()
                    FRIEND1.destroy()
                    FRIEND2.destroy()
                    FRIEND3.destroy()
                    msg1 = Label(tgui, text="Connecting to  " + friend1,font='Arial 16 bold',bg="#2e004d",fg='yellow',border=5)
                    msg1.pack(side='top', padx=100, pady=10)
                    msg2 = Label(tgui, text="Connected...",font='Arial 16 bold',bg="#2e004d",fg='yellow',border=5)
                    msg2.pack(side='top', padx=100, pady=10)

            def friendbuttonpress2():
                msg.destroy()
                FRIEND1.destroy()
                FRIEND2.destroy()
                FRIEND3.destroy()
                msg1 = Label(tgui, text="Connecting to " + friend2,font='Arial 16 bold',bg="#2e004d",fg='yellow',border=5)
                msg1.pack(side='top', padx=100, pady=10)
                msg2 = Label(tgui, text="Connected...",font='Arial 16 bold',bg="#2e004d",fg='yellow',border=5)
                msg2.pack(side='top', padx=100, pady=10)

            def friendbuttonpress3():
                msg.destroy()
                FRIEND1.destroy()
                FRIEND2.destroy()
                FRIEND3.destroy()
                msg1 = Label(tgui, text="Connecting to " + friend3,font='Arial 16 bold',bg="#2e004d",fg='yellow',border=5)
                msg1.pack(side='top', padx=100, pady=10)
                msg2 = Label(tgui, text="Connected...",font='Arial 16 bold',bg="#2e004d",fg='yellow',border=5)
                msg2.pack(side='top', padx=100, pady=10)

            def buttonpressuni():
                randnumber2a=0
                randnumber3a=0
                if (phonedone == 0):

                    if (denomination < 160001):
                        randnumber2 = randint(1, 2)
                        if (randnumber2 == 1):
                            randstring = random.choice(friendanswer1)
                            friendanswers = Label(tgui, text=randstring + correct,font='Arial 16 bold',bg="#2e004d",fg='yellow',border=5)
                            friendanswers.pack(side='top', padx=20, pady=10)
                        if (randnumber2 == 2):
                            if (correct == 'A'):
                                randnumber2a = randint(1, 4)
                                while (randnumber2a == 1):
                                    randnumber2a = randint(1, 4)

                            if (correct == 'B'):
                                randnumber2a = randint(1, 4)
                                while (randnumber2a == 2):
                                    randnumber2a = randint(1, 4)

                            if (correct == 'C'):
                                randnumber2a = randint(1, 4)
                                while (randnumber2a == 3):
                                    randnumber2a = randint(1, 4)

                            if (correct == 'D'):
                                randnumber2a = randint(1, 4)
                                while (randnumber2a == 4):
                                    randnumber2a = randint(1, 4)

                            randstring2a = (str)(randnumber2a)
                            if (randstring2a == '1'):
                                randstring2a = 'A'
                            if (randstring2a == '2'):
                                randstring2a = 'B'
                            if (randstring2a == '3'):
                                randstring2a = 'C'
                            if (randstring2a == '4'):
                                randstring2a = 'D'
                            randstring = random.choice(friendanswer2)
                            friendanswers = Label(tgui, text=randstring + correct + "," + randstring2a,font='Arial 16 bold',bg="#2e004d",fg='yellow',border=5)
                            friendanswers.pack(side='top', padx=20, pady=10)

                    elif denomination>=2500000:
                        randstring = random.choice(friendanswer3)
                        friendanswers = Label(tgui, text=randstring, font='Arial 16 bold', bg="#2e004d", fg='yellow',
                                              border=5)
                        friendanswers.pack(side='top', padx=20, pady=10)

                    else:
                        randnumber3 = randint(2, 3)
                        if (randnumber3 == 2):
                            if (correct == 'A'):
                                randnumber3a = randint(1, 4)
                                while (randnumber3a == 1):
                                    randnumber3a = randint(1, 4)

                            if (correct == 'B'):
                                randnumber3a = randint(1, 4)
                                while (randnumber3a == 2):
                                    randnumber3a = randint(1, 4)

                            if (correct == 'C'):
                                randnumber3a = randint(1, 4)
                                while (randnumber3a == 3):
                                    randnumber3a = randint(1, 4)

                            if (correct == 'D'):
                                randnumber3a = randint(1, 4)
                                while (randnumber3a == 4):
                                    randnumber3a = randint(1, 4)

                            randstring3a = (str)(randnumber3a)
                            if (randstring3a == '1'):
                                randstring3a = 'A'
                            if (randstring3a == '2'):
                                randstring3a = 'B'
                            if (randstring3a == '3'):
                                randstring3a = 'C'
                            if (randstring3a == '4'):
                                randstring3a = 'D'
                            randstring = random.choice(friendanswer2)
                            friendanswers = Label(tgui, text=randstring + correct + "," + randstring3a,font='Arial 16 bold',bg="#2e004d",fg='yellow',border=5)
                            friendanswers.pack(side='top', padx=20, pady=10)
                        if (randnumber3 == 3):
                            randstring = random.choice(friendanswer3)
                            friendanswers = Label(tgui, text=randstring,font='Arial 16 bold',bg="#2e004d",fg='yellow',border=5)
                            friendanswers.pack(side='top', padx=20, pady=10)

            def disconnect():
                global phonedone
                msg3 = Label(tgui, text="Disconnected...",font='Arial 16 bold',bg="#2e004d",fg='yellow',border=5)
                msg3.pack(side='top', padx=200, pady=10)
                phonedone = 1
                OKbutton = Button(tgui, text='  OK  ', font='Arial 22 bold', bg="black", fg='yellow', border=5,
                                  command=tgui.destroy)
                OKbutton.pack(side='top', padx=200, pady=30)

            FRIEND1 = Button(tgui, text=friend1,font='Arial 16 bold',bg="black",fg='yellow',border=5, command=lambda: [friendbuttonpress1(), buttonpressuni(), disconnect()])
            FRIEND1.pack(side='top', padx=200, pady=10)
            FRIEND2 = Button(tgui, text=friend2,font='Arial 16 bold',bg="black",fg='yellow',border=5,command=lambda: [friendbuttonpress2(), buttonpressuni(), disconnect()])
            FRIEND2.pack(side='top', padx=200, pady=10)
            FRIEND3 = Button(tgui, text=friend3,font='Arial 16 bold',bg="black",fg='yellow',border=5,command=lambda: [friendbuttonpress3(), buttonpressuni(), disconnect()])
            FRIEND3.pack(side='top', padx=200, pady=10)


        tgui.mainloop()

def audiencepoll(correct):
    global audiencedone
    global fiftyfiftydone
    global audiencedone
    global aactive,bactive,cactive,dactive

    correct=str(correct)
    correct=correct.upper()

    if audiencedone==0:

        if(fiftyfiftydone==1  and sameq_flag==1):
            audiencedone=1
            tgui = Tk()
            tgui.title("Audience Poll")
            tgui.geometry('960x400+300+270')
            tgui.iconbitmap(os.path.join(path, 'Images and icons\kbc_logo.ico'))
            tgui.configure(bg='#2e004d')
            APoll = randint(70, 100)
            BPoll=100-APoll
            if(correct=='A'):
                printa = Label(tgui, text="A",fg='yellow',font='Arial 16 bold',border=5,bg='#2e004d')
                printa.grid(row=15, column=0,padx=40,pady=10)
                printa1 = Label(tgui, text="|" * APoll,fg='yellow',font='Arial 16 bold',border=5,bg='#2e004d')
                printa1.grid(row=15, column=1,padx=40,pady=10)
                APoll = (str)(APoll)
                printa2 = Label(tgui, text=APoll + " %",fg='yellow',font='Arial 16 bold',border=5,bg='#2e004d')
                printa2.grid(row=15, column=2,padx=40,pady=10)

                if(bactive==1):
                    printb=Label(tgui,text="B",fg='yellow',font='Arial 16 bold',border=5,bg='#2e004d')
                    printb.grid(row=16,column=0,padx=40,pady=10)
                    printb1 = Label(tgui, text="|" * BPoll,fg='yellow',font='Arial 16 bold',border=5,bg='#2e004d')
                    printb1.grid(row=16, column=1,padx=40,pady=10)
                    BPoll = (str)(BPoll)
                    printb2 = Label(tgui, text=BPoll + " %",fg='yellow',font='Arial 16 bold',border=5,bg='#2e004d')
                    printb2.grid(row=16, column=2,padx=40,pady=10)

                if (cactive == 1):
                    printc = Label(tgui, text="C",fg='yellow',font='Arial 16 bold',border=5,bg='#2e004d')
                    printc.grid(row=16, column=0,padx=40,pady=10)
                    printc1 = Label(tgui, text="|" * BPoll,fg='yellow',font='Arial 16 bold',border=5,bg='#2e004d')
                    printc1.grid(row=16, column=1,padx=40,pady=10)
                    BPoll = (str)(BPoll)
                    printc2 = Label(tgui, text=BPoll + " %",fg='yellow',font='Arial 16 bold',border=5,bg='#2e004d')
                    printc2.grid(row=16, column=2,padx=40,pady=10)

                if (dactive == 1):
                    printd = Label(tgui, text="D",fg='yellow',font='Arial 16 bold',border=5,bg='#2e004d')
                    printd.grid(row=16, column=0,padx=40,pady=10)
                    printd1 = Label(tgui, text="|" * BPoll,fg='yellow',font='Arial 16 bold',border=5,bg='#2e004d')
                    printd1.grid(row=16, column=1,padx=40,pady=10)
                    BPoll = (str)(BPoll)
                    printd2 = Label(tgui, text=BPoll + " %",fg='yellow',font='Arial 16 bold',border=5,bg='#2e004d')
                    printd2.grid(row=16, column=2,padx=40,pady=10)

            if (correct == 'B'):
                printb = Label(tgui, text="B",fg='yellow',font='Arial 16 bold',border=5,bg='#2e004d')
                printb.grid(row=15, column=0,padx=40,pady=10)
                printb1 = Label(tgui, text="|" * APoll,fg='yellow',font='Arial 16 bold',border=5,bg='#2e004d')
                printb1.grid(row=15, column=1,padx=40,pady=10)
                APoll = (str)(APoll)
                printb2 = Label(tgui, text=APoll + " %",fg='yellow',font='Arial 16 bold',border=5,bg='#2e004d')
                printb2.grid(row=15, column=2,padx=40,pady=10)

                if (aactive == 1):
                    printa = Label(tgui, text="A",fg='yellow',font='Arial 16 bold',border=5,bg='#2e004d')
                    printa.grid(row=16, column=0,padx=40,pady=10)
                    printa1 = Label(tgui, text="|" * BPoll,fg='yellow',font='Arial 16 bold',border=5,bg='#2e004d')
                    printa1.grid(row=16, column=1,padx=40,pady=10)
                    BPoll = (str)(BPoll)
                    printa2 = Label(tgui, text=BPoll + " %",fg='yellow',font='Arial 16 bold',border=5,bg='#2e004d')
                    printa2.grid(row=16, column=2,padx=40,pady=10)


                if (cactive == 1):
                    printc = Label(tgui, text="C",fg='yellow',font='Arial 16 bold',border=5,bg='#2e004d')
                    printc.grid(row=16, column=0,padx=40,pady=10)
                    printc1 = Label(tgui, text="|" * BPoll,fg='yellow',font='Arial 16 bold',border=5,bg='#2e004d')
                    printc1.grid(row=16, column=1,padx=40,pady=10)
                    BPoll = (str)(BPoll)
                    printc2 = Label(tgui, text=BPoll + " %",fg='yellow',font='Arial 16 bold',border=5,bg='#2e004d')
                    printc2.grid(row=16, column=2,padx=40,pady=10)

                if (dactive == 1):
                    printd = Label(tgui, text="D",fg='yellow',font='Arial 16 bold',border=5,bg='#2e004d')
                    printd.grid(row=16, column=0,padx=40,pady=10)
                    printd1 = Label(tgui, text="|" * BPoll,fg='yellow',font='Arial 16 bold',border=5,bg='#2e004d')
                    printd1.grid(row=16, column=1,padx=40,pady=10)
                    BPoll = (str)(BPoll)
                    printd2 = Label(tgui, text=BPoll + " %",fg='yellow',font='Arial 16 bold',border=5,bg='#2e004d')
                    printd2.grid(row=16, column=2,padx=40,pady=10)

            if (correct == 'C'):
                printc = Label(tgui, text="C",fg='yellow',font='Arial 16 bold',border=5,bg='#2e004d')
                printc.grid(row=15, column=0,padx=40,pady=10)
                printc1 = Label(tgui, text="|" * APoll,fg='yellow',font='Arial 16 bold',border=5,bg='#2e004d')
                printc1.grid(row=15, column=1,padx=40,pady=10)
                APoll = (str)(APoll)
                printc2 = Label(tgui, text=APoll + " %",fg='yellow',font='Arial 16 bold',border=5,bg='#2e004d')
                printc2.grid(row=15, column=2,padx=40,pady=10)

                if (bactive == 1):
                    printb = Label(tgui, text="B",fg='yellow',font='Arial 16 bold',border=5,bg='#2e004d')
                    printb.grid(row=16, column=0,padx=40,pady=10)
                    printb1 = Label(tgui, text="|" * BPoll,fg='yellow',font='Arial 16 bold',border=5,bg='#2e004d')
                    printb1.grid(row=16, column=1,padx=40,pady=10)
                    BPoll = (str)(BPoll)
                    printb2 = Label(tgui, text=BPoll + " %",fg='yellow',font='Arial 16 bold',border=5,bg='#2e004d')
                    printb2.grid(row=16, column=2,padx=40,pady=10)

                if (aactive == 1):
                    printa = Label(tgui, text="A",fg='yellow',font='Arial 16 bold',border=5,bg='#2e004d')
                    printa.grid(row=16, column=0,padx=40,pady=10)
                    printa1 = Label(tgui, text="|" * BPoll,fg='yellow',font='Arial 16 bold',border=5,bg='#2e004d')
                    printa1.grid(row=16, column=1,padx=40,pady=10)
                    BPoll = (str)(BPoll)
                    printa2 = Label(tgui, text=BPoll + " %",fg='yellow',font='Arial 16 bold',border=5,bg='#2e004d')
                    printa2.grid(row=16, column=2,padx=40,pady=10)

                if (dactive == 1):
                    printd = Label(tgui, text="D",fg='yellow',font='Arial 16 bold',border=5,bg='#2e004d')
                    printd.grid(row=16, column=0,padx=40,pady=10)
                    printd1 = Label(tgui, text="|" * BPoll,fg='yellow',font='Arial 16 bold',border=5,bg='#2e004d')
                    printd1.grid(row=16, column=1,padx=40,pady=10)
                    BPoll = (str)(BPoll)
                    printd2 = Label(tgui, text=BPoll + " %",fg='yellow',font='Arial 16 bold',border=5,bg='#2e004d')
                    printd2.grid(row=16, column=2,padx=40,pady=10)

            if (correct == 'D'):
                printd = Label(tgui, text="D",fg='yellow',font='Arial 16 bold',border=5,bg='#2e004d')
                printd.grid(row=15, column=0,padx=40,pady=10)
                printd1 = Label(tgui, text="|" * APoll,fg='yellow',font='Arial 16 bold',border=5,bg='#2e004d')
                printd1.grid(row=15, column=1,padx=40,pady=10)
                APoll = (str)(APoll)
                printd2 = Label(tgui, text=APoll + " %",fg='yellow',font='Arial 16 bold',border=5,bg='#2e004d')
                printd2.grid(row=15, column=2,padx=40,pady=10)

                if (bactive == 1):
                    printb = Label(tgui, text="B",fg='yellow',font='Arial 16 bold',border=5,bg='#2e004d')
                    printb.grid(row=16, column=0,padx=40,pady=10)
                    printb1 = Label(tgui, text="|" * BPoll,fg='yellow',font='Arial 16 bold',border=5,bg='#2e004d')
                    printb1.grid(row=16, column=1,padx=40,pady=10)
                    BPoll = (str)(BPoll)
                    printb2 = Label(tgui, text=BPoll + " %",fg='yellow',font='Arial 16 bold',border=5,bg='#2e004d')
                    printb2.grid(row=16, column=2,padx=40,pady=10)

                if (cactive == 1):
                    printc = Label(tgui, text="C",fg='yellow',font='Arial 16 bold',border=5,bg='#2e004d')
                    printc.grid(row=16, column=0,padx=40,pady=10)
                    printc1 = Label(tgui, text="|" * BPoll,fg='yellow',font='Arial 16 bold',border=5,bg='#2e004d')
                    printc1.grid(row=16, column=1,padx=40,pady=10)
                    BPoll = (str)(BPoll)
                    printc2 = Label(tgui, text=BPoll + " %",fg='yellow',font='Arial 16 bold',border=5,bg='#2e004d')
                    printc2.grid(row=16, column=2,padx=40,pady=10)

                if (aactive == 1):
                    printa = Label(tgui, text="A",fg='yellow',font='Arial 16 bold',border=5,bg='#2e004d')
                    printa.grid(row=16, column=0,padx=40,pady=10)
                    printa1 = Label(tgui, text="|" * BPoll,fg='yellow',font='Arial 16 bold',border=5,bg='#2e004d')
                    printa1.grid(row=16, column=1,padx=40,pady=10)
                    BPoll = (str)(BPoll)
                    printa2 = Label(tgui, text=BPoll + " %",fg='yellow',font='Arial 16 bold',border=5,bg='#2e004d')
                    printa2.grid(row=16, column=2,padx=40,pady=10)

            OKbutton = Button(tgui, text='  OK  ', font='Arial 22 bold', bg="black", fg='yellow', border=5,
                              command=tgui.destroy)
            OKbutton.grid(row=21, column=1, padx=40, pady=40)

            tgui.mainloop()

        else:
            audiencedone=1
            tgui = Tk()
            tgui.title("Audience Poll")
            tgui.geometry('960x400+300+270')
            tgui.iconbitmap(os.path.join(path, 'Images and icons\kbc_logo.ico'))
            tgui.configure(bg='#2e004d')
            if (denomination < 40001):
                APoll = randint(70, 100)
                ALeft = 100 - APoll
                BPoll = randint(0, ALeft)
                BLeft = ALeft - BPoll
                CPoll = randint(0, BLeft)
                DPoll = BLeft - CPoll

                printa = Label(tgui, text="A",bg='#2e004d',fg='yellow',font='Arial 16 bold',border=5)
                printa.grid(row=15, column=0,padx=40,pady=10)
                printb = Label(tgui, text="B",fg='yellow',font='Arial 16 bold',border=5,bg='#2e004d')
                printb.grid(row=16, column=0,padx=40,pady=10)
                printc = Label(tgui, text="C",fg='yellow',font='Arial 16 bold',border=5,bg='#2e004d')
                printc.grid(row=17, column=0,padx=40,pady=10)
                printd = Label(tgui, text="D",fg='yellow',font='Arial 16 bold',border=5,bg='#2e004d')
                printd.grid(row=18, column=0,padx=40,pady=10)

                if (correct == 'A'):
                    printa1 = Label(tgui, text="|" * APoll,fg='yellow',font='Arial 16 bold',border=5,bg='#2e004d')
                    printa1.grid(row=15, column=1,padx=40,pady=10)
                    printb1 = Label(tgui, text="|" * BPoll,fg='yellow',font='Arial 16 bold',border=5,bg='#2e004d')
                    printb1.grid(row=16, column=1,padx=40,pady=10)
                    printc1 = Label(tgui, text="|" * CPoll,fg='yellow',font='Arial 16 bold',border=5,bg='#2e004d')
                    printc1.grid(row=17, column=1,padx=40,pady=10)
                    printd1 = Label(tgui, text="|" * DPoll,fg='yellow',font='Arial 16 bold',border=5,bg='#2e004d')
                    printd1.grid(row=18, column=1,padx=40,pady=10)

                    APoll = (str)(APoll)
                    BPoll = (str)(BPoll)
                    CPoll = (str)(CPoll)
                    DPoll = (str)(DPoll)

                    printa2 = Label(tgui, text=APoll + " %",fg='yellow',font='Arial 16 bold',border=5,bg='#2e004d')
                    printa2.grid(row=15, column=2,padx=40,pady=10)
                    printb2 = Label(tgui, text=BPoll + " %",fg='yellow',font='Arial 16 bold',border=5,bg='#2e004d')
                    printb2.grid(row=16, column=2,padx=40,pady=10)
                    printc2 = Label(tgui, text=CPoll + " %",fg='yellow',font='Arial 16 bold',border=5,bg='#2e004d')
                    printc2.grid(row=17, column=2,padx=40,pady=10)
                    printd2 = Label(tgui, text=DPoll + " %",fg='yellow',font='Arial 16 bold',border=5,bg='#2e004d')
                    printd2.grid(row=18, column=2,padx=40,pady=10)

                if (correct == 'B'):
                    printa1 = Label(tgui, text="|" * BPoll,fg='yellow',font='Arial 16 bold',border=5,bg='#2e004d')
                    printa1.grid(row=15, column=1,padx=40,pady=10)
                    printb1 = Label(tgui, text="|" * APoll,fg='yellow',font='Arial 16 bold',border=5,bg='#2e004d')
                    printb1.grid(row=16, column=1,padx=40,pady=10)
                    printc1 = Label(tgui, text="|" * CPoll,fg='yellow',font='Arial 16 bold',border=5,bg='#2e004d')
                    printc1.grid(row=17, column=1,padx=40,pady=10)
                    printd1 = Label(tgui, text="|" * DPoll,fg='yellow',font='Arial 16 bold',border=5,bg='#2e004d')
                    printd1.grid(row=18, column=1,padx=40,pady=10)

                    APoll = (str)(APoll)
                    BPoll = (str)(BPoll)
                    CPoll = (str)(CPoll)
                    DPoll = (str)(DPoll)

                    printa2 = Label(tgui, text=BPoll + " %",fg='yellow',font='Arial 16 bold',border=5,bg='#2e004d')
                    printa2.grid(row=15, column=2,padx=40,pady=10)
                    printb2 = Label(tgui, text=APoll + " %",fg='yellow',font='Arial 16 bold',border=5,bg='#2e004d')
                    printb2.grid(row=16, column=2,padx=40,pady=10)
                    printc2 = Label(tgui, text=CPoll + " %",fg='yellow',font='Arial 16 bold',border=5,bg='#2e004d')
                    printc2.grid(row=17, column=2,padx=40,pady=10)
                    printd2 = Label(tgui, text=DPoll + " %",fg='yellow',font='Arial 16 bold',border=5,bg='#2e004d')
                    printd2.grid(row=18, column=2,padx=40,pady=10)

                if (correct == 'C'):
                    printa1 = Label(tgui, text="|" * CPoll,fg='yellow',font='Arial 16 bold',border=5,bg='#2e004d')
                    printa1.grid(row=15, column=1,padx=40,pady=10)
                    printb1 = Label(tgui, text="|" * BPoll,fg='yellow',font='Arial 16 bold',border=5,bg='#2e004d')
                    printb1.grid(row=16, column=1,padx=40,pady=10)
                    printc1 = Label(tgui, text="|" * APoll,fg='yellow',font='Arial 16 bold',border=5,bg='#2e004d')
                    printc1.grid(row=17, column=1,padx=40,pady=10)
                    printd1 = Label(tgui, text="|" * DPoll,fg='yellow',font='Arial 16 bold',border=5,bg='#2e004d')
                    printd1.grid(row=18, column=1,padx=40,pady=10)

                    APoll = (str)(APoll)
                    BPoll = (str)(BPoll)
                    CPoll = (str)(CPoll)
                    DPoll = (str)(DPoll)

                    printa2 = Label(tgui, text=CPoll + " %",fg='yellow',font='Arial 16 bold',border=5,bg='#2e004d')
                    printa2.grid(row=15, column=2,padx=40,pady=10)
                    printb2 = Label(tgui, text=BPoll + " %",fg='yellow',font='Arial 16 bold',border=5,bg='#2e004d')
                    printb2.grid(row=16, column=2,padx=40,pady=10)
                    printc2 = Label(tgui, text=APoll + " %",fg='yellow',font='Arial 16 bold',border=5,bg='#2e004d')
                    printc2.grid(row=17, column=2,padx=40,pady=10)
                    printd2 = Label(tgui, text=DPoll + " %",fg='yellow',font='Arial 16 bold',border=5,bg='#2e004d')
                    printd2.grid(row=18, column=2,padx=40,pady=10)

                if (correct == 'D'):
                    printa1 = Label(tgui, text="|" * DPoll,fg='yellow',font='Arial 16 bold',border=5,bg='#2e004d')
                    printa1.grid(row=15, column=1,padx=40,pady=10)
                    printb1 = Label(tgui, text="|" * BPoll,fg='yellow',font='Arial 16 bold',border=5,bg='#2e004d')
                    printb1.grid(row=16, column=1,padx=40,pady=10)
                    printc1 = Label(tgui, text="|" * CPoll,fg='yellow',font='Arial 16 bold',border=5,bg='#2e004d')
                    printc1.grid(row=17, column=1,padx=40,pady=10)
                    printd1 = Label(tgui, text="|" * APoll,fg='yellow',font='Arial 16 bold',border=5,bg='#2e004d')
                    printd1.grid(row=18, column=1,padx=40,pady=10)

                    APoll = (str)(APoll)
                    BPoll = (str)(BPoll)
                    CPoll = (str)(CPoll)
                    DPoll = (str)(DPoll)

                    printa2 = Label(tgui, text=DPoll + " %",fg='yellow',font='Arial 16 bold',border=5,bg='#2e004d')
                    printa2.grid(row=15, column=2,padx=40,pady=10)
                    printb2 = Label(tgui, text=BPoll + " %",fg='yellow',font='Arial 16 bold',border=5,bg='#2e004d')
                    printb2.grid(row=16, column=2,padx=40,pady=10)
                    printc2 = Label(tgui, text=CPoll + " %",fg='yellow',font='Arial 16 bold',border=5,bg='#2e004d')
                    printc2.grid(row=17, column=2,padx=40,pady=10)
                    printd2 = Label(tgui, text=APoll + " %",fg='yellow',font='Arial 16 bold',border=5,bg='#2e004d')
                    printd2.grid(row=18, column=2,padx=40,pady=10)

            elif (denomination < 640001):
                APoll = randint(50, 70)
                ALeft = 100 - APoll
                BPoll = randint(0, ALeft)
                BLeft = ALeft - BPoll
                CPoll = randint(0, BLeft)
                DPoll = BLeft - CPoll

                printa = Label(tgui, text="A",fg='yellow',font='Arial 16 bold',border=5,bg='#2e004d')
                printa.grid(row=15, column=0,padx=40,pady=10)
                printb = Label(tgui, text="B",fg='yellow',font='Arial 16 bold',border=5,bg='#2e004d')
                printb.grid(row=16, column=0,padx=40,pady=10)
                printc = Label(tgui, text="C",fg='yellow',font='Arial 16 bold',border=5,bg='#2e004d')
                printc.grid(row=17, column=0,padx=40,pady=10)
                printd = Label(tgui, text="D",fg='yellow',font='Arial 16 bold',border=5,bg='#2e004d')
                printd.grid(row=18, column=0,padx=40,pady=10)

                if (correct == 'A'):
                    printa1 = Label(tgui, text="|" * APoll,fg='yellow',font='Arial 16 bold',border=5,bg='#2e004d')
                    printa1.grid(row=15, column=1,padx=40,pady=10)
                    printb1 = Label(tgui, text="|" * BPoll,fg='yellow',font='Arial 16 bold',border=5,bg='#2e004d')
                    printb1.grid(row=16, column=1,padx=40,pady=10)
                    printc1 = Label(tgui, text="|" * CPoll,fg='yellow',font='Arial 16 bold',border=5,bg='#2e004d')
                    printc1.grid(row=17, column=1,padx=40,pady=10)
                    printd1 = Label(tgui, text="|" * DPoll,fg='yellow',font='Arial 16 bold',border=5,bg='#2e004d')
                    printd1.grid(row=18, column=1,padx=40,pady=10)

                    APoll = (str)(APoll)
                    BPoll = (str)(BPoll)
                    CPoll = (str)(CPoll)
                    DPoll = (str)(DPoll)

                    printa2 = Label(tgui, text=APoll + " %",fg='yellow',font='Arial 16 bold',border=5,bg='#2e004d')
                    printa2.grid(row=15, column=2,padx=40,pady=10)
                    printb2 = Label(tgui, text=BPoll + " %",fg='yellow',font='Arial 16 bold',border=5,bg='#2e004d')
                    printb2.grid(row=16, column=2,padx=40,pady=10)
                    printc2 = Label(tgui, text=CPoll + " %",fg='yellow',font='Arial 16 bold',border=5,bg='#2e004d')
                    printc2.grid(row=17, column=2,padx=40,pady=10)
                    printd2 = Label(tgui, text=DPoll + " %",fg='yellow',font='Arial 16 bold',border=5,bg='#2e004d')
                    printd2.grid(row=18, column=2,padx=40,pady=10)

                if (correct == 'B'):
                    printa1 = Label(tgui, text="|" * BPoll,fg='yellow',font='Arial 16 bold',border=5,bg='#2e004d')
                    printa1.grid(row=15, column=1,padx=40,pady=10)
                    printb1 = Label(tgui, text="|" * APoll,fg='yellow',font='Arial 16 bold',border=5,bg='#2e004d')
                    printb1.grid(row=16, column=1,padx=40,pady=10)
                    printc1 = Label(tgui, text="|" * CPoll,fg='yellow',font='Arial 16 bold',border=5,bg='#2e004d')
                    printc1.grid(row=17, column=1,padx=40,pady=10)
                    printd1 = Label(tgui, text="|" * DPoll,fg='yellow',font='Arial 16 bold',border=5,bg='#2e004d')
                    printd1.grid(row=18, column=1,padx=40,pady=10)

                    APoll = (str)(APoll)
                    BPoll = (str)(BPoll)
                    CPoll = (str)(CPoll)
                    DPoll = (str)(DPoll)

                    printa2 = Label(tgui, text=BPoll + " %",fg='yellow',font='Arial 16 bold',border=5,bg='#2e004d')
                    printa2.grid(row=15, column=2,padx=40,pady=10)
                    printb2 = Label(tgui, text=APoll + " %",fg='yellow',font='Arial 16 bold',border=5,bg='#2e004d')
                    printb2.grid(row=16, column=2,padx=40,pady=10)
                    printc2 = Label(tgui, text=CPoll + " %",fg='yellow',font='Arial 16 bold',border=5,bg='#2e004d')
                    printc2.grid(row=17, column=2,padx=40,pady=10)
                    printd2 = Label(tgui, text=DPoll + " %",fg='yellow',font='Arial 16 bold',border=5,bg='#2e004d')
                    printd2.grid(row=18, column=2,padx=40,pady=10)

                if (correct == 'C'):
                    printa1 = Label(tgui, text="|" * CPoll,fg='yellow',font='Arial 16 bold',border=5,bg='#2e004d')
                    printa1.grid(row=15, column=1,padx=40,pady=10)
                    printb1 = Label(tgui, text="|" * BPoll,fg='yellow',font='Arial 16 bold',border=5,bg='#2e004d')
                    printb1.grid(row=16, column=1,padx=40,pady=10)
                    printc1 = Label(tgui, text="|" * APoll,fg='yellow',font='Arial 16 bold',border=5,bg='#2e004d')
                    printc1.grid(row=17, column=1,padx=40,pady=10)
                    printd1 = Label(tgui, text="|" * DPoll,fg='yellow',font='Arial 16 bold',border=5,bg='#2e004d')
                    printd1.grid(row=18, column=1,padx=40,pady=10)

                    APoll = (str)(APoll)
                    BPoll = (str)(BPoll)
                    CPoll = (str)(CPoll)
                    DPoll = (str)(DPoll)

                    printa2 = Label(tgui, text=CPoll + " %",fg='yellow',font='Arial 16 bold',border=5,bg='#2e004d')
                    printa2.grid(row=15, column=2,padx=40,pady=10)
                    printb2 = Label(tgui, text=BPoll + " %",fg='yellow',font='Arial 16 bold',border=5,bg='#2e004d')
                    printb2.grid(row=16, column=2,padx=40,pady=10)
                    printc2 = Label(tgui, text=APoll + " %",fg='yellow',font='Arial 16 bold',border=5,bg='#2e004d')
                    printc2.grid(row=17, column=2,padx=40,pady=10)
                    printd2 = Label(tgui, text=DPoll + " %",fg='yellow',font='Arial 16 bold',border=5,bg='#2e004d')
                    printd2.grid(row=18, column=2,padx=40,pady=10)

                if (correct == 'D'):
                    printa1 = Label(tgui, text="|" * DPoll,fg='yellow',font='Arial 16 bold',border=5,bg='#2e004d')
                    printa1.grid(row=15, column=1,padx=40,pady=10)
                    printb1 = Label(tgui, text="|" * BPoll,fg='yellow',font='Arial 16 bold',border=5,bg='#2e004d')
                    printb1.grid(row=16, column=1,padx=40,pady=10)
                    printc1 = Label(tgui, text="|" * CPoll,fg='yellow',font='Arial 16 bold',border=5,bg='#2e004d')
                    printc1.grid(row=17, column=1,padx=40,pady=10)
                    printd1 = Label(tgui, text="|" * APoll,fg='yellow',font='Arial 16 bold',border=5,bg='#2e004d')
                    printd1.grid(row=18, column=1,padx=40,pady=10)

                    APoll = (str)(APoll)
                    BPoll = (str)(BPoll)
                    CPoll = (str)(CPoll)
                    DPoll = (str)(DPoll)

                    printa2 = Label(tgui, text=DPoll + " %",fg='yellow',font='Arial 16 bold',border=5,bg='#2e004d')
                    printa2.grid(row=15, column=2,padx=40,pady=10)
                    printb2 = Label(tgui, text=BPoll + " %",fg='yellow',font='Arial 16 bold',border=5,bg='#2e004d')
                    printb2.grid(row=16, column=2,padx=40,pady=10)
                    printc2 = Label(tgui, text=CPoll + " %",fg='yellow',font='Arial 16 bold',border=5,bg='#2e004d')
                    printc2.grid(row=17, column=2,padx=40,pady=10)
                    printd2 = Label(tgui, text=APoll + " %",fg='yellow',font='Arial 16 bold',border=5,bg='#2e004d')
                    printd2.grid(row=18, column=2,padx=40,pady=10)

            else:
                APoll = randint(30, 60)
                ALeft = 100 - APoll
                BPoll = randint(0, ALeft)
                BLeft = ALeft - BPoll
                CPoll = randint(0, BLeft)
                DPoll = BLeft - CPoll

                printa = Label(tgui, text="A",fg='yellow',font='Arial 16 bold',border=5,bg='#2e004d')
                printa.grid(row=15, column=0,padx=40,pady=10)
                printb = Label(tgui, text="B",fg='yellow',font='Arial 16 bold',border=5,bg='#2e004d')
                printb.grid(row=16, column=0,padx=40,pady=10)
                printc = Label(tgui, text="C",fg='yellow',font='Arial 16 bold',border=5,bg='#2e004d')
                printc.grid(row=17, column=0,padx=40,pady=10)
                printd = Label(tgui, text="D",fg='yellow',font='Arial 16 bold',border=5,bg='#2e004d')
                printd.grid(row=18, column=0,padx=40,pady=10)

                if (correct == 'A'):
                    printa1 = Label(tgui, text="|" * APoll,fg='yellow',font='Arial 16 bold',border=5,bg='#2e004d')
                    printa1.grid(row=15, column=1,padx=40,pady=10)
                    printb1 = Label(tgui, text="|" * BPoll,fg='yellow',font='Arial 16 bold',border=5,bg='#2e004d')
                    printb1.grid(row=16, column=1,padx=40,pady=10)
                    printc1 = Label(tgui, text="|" * CPoll,fg='yellow',font='Arial 16 bold',border=5,bg='#2e004d')
                    printc1.grid(row=17, column=1,padx=40,pady=10)
                    printd1 = Label(tgui, text="|" * DPoll,fg='yellow',font='Arial 16 bold',border=5,bg='#2e004d')
                    printd1.grid(row=18, column=1,padx=40,pady=10)

                    APoll = (str)(APoll)
                    BPoll = (str)(BPoll)
                    CPoll = (str)(CPoll)
                    DPoll = (str)(DPoll)

                    printa2 = Label(tgui, text=APoll + " %",fg='yellow',font='Arial 16 bold',border=5,bg='#2e004d')
                    printa2.grid(row=15, column=2,padx=40,pady=10)
                    printb2 = Label(tgui, text=BPoll + " %",fg='yellow',font='Arial 16 bold',border=5,bg='#2e004d')
                    printb2.grid(row=16, column=2,padx=40,pady=10)
                    printc2 = Label(tgui, text=CPoll + " %",fg='yellow',font='Arial 16 bold',border=5,bg='#2e004d')
                    printc2.grid(row=17, column=2,padx=40,pady=10)
                    printd2 = Label(tgui, text=DPoll + " %",fg='yellow',font='Arial 16 bold',border=5,bg='#2e004d')
                    printd2.grid(row=18, column=2,padx=40,pady=10)

                if (correct == 'B'):
                    printa1 = Label(tgui, text="|" * BPoll,fg='yellow',font='Arial 16 bold',border=5,bg='#2e004d')
                    printa1.grid(row=15, column=1,padx=40,pady=10)
                    printb1 = Label(tgui, text="|" * APoll,fg='yellow',font='Arial 16 bold',border=5,bg='#2e004d')
                    printb1.grid(row=16, column=1,padx=40,pady=10)
                    printc1 = Label(tgui, text="|" * CPoll,fg='yellow',font='Arial 16 bold',border=5,bg='#2e004d')
                    printc1.grid(row=17, column=1,padx=40,pady=10)
                    printd1 = Label(tgui, text="|" * DPoll,fg='yellow',font='Arial 16 bold',border=5,bg='#2e004d')
                    printd1.grid(row=18, column=1,padx=40,pady=10)

                    APoll = (str)(APoll)
                    BPoll = (str)(BPoll)
                    CPoll = (str)(CPoll)
                    DPoll = (str)(DPoll)

                    printa2 = Label(tgui, text=BPoll + " %",fg='yellow',font='Arial 16 bold',border=5,bg='#2e004d')
                    printa2.grid(row=15, column=2,padx=40,pady=10)
                    printb2 = Label(tgui, text=APoll + " %",fg='yellow',font='Arial 16 bold',border=5,bg='#2e004d')
                    printb2.grid(row=16, column=2,padx=40,pady=10)
                    printc2 = Label(tgui, text=CPoll + " %",fg='yellow',font='Arial 16 bold',border=5,bg='#2e004d')
                    printc2.grid(row=17, column=2,padx=40,pady=10)
                    printd2 = Label(tgui, text=DPoll + " %",fg='yellow',font='Arial 16 bold',border=5,bg='#2e004d')
                    printd2.grid(row=18, column=2,padx=40,pady=10)

                if (correct == 'C'):
                    printa1 = Label(tgui, text="|" * CPoll,fg='yellow',font='Arial 16 bold',border=5,bg='#2e004d')
                    printa1.grid(row=15, column=1,padx=40,pady=10)
                    printb1 = Label(tgui, text="|" * BPoll,fg='yellow',font='Arial 16 bold',border=5,bg='#2e004d')
                    printb1.grid(row=16, column=1,padx=40,pady=10)
                    printc1 = Label(tgui, text="|" * APoll,fg='yellow',font='Arial 16 bold',border=5,bg='#2e004d')
                    printc1.grid(row=17, column=1,padx=40,pady=10)
                    printd1 = Label(tgui, text="|" * DPoll,fg='yellow',font='Arial 16 bold',border=5,bg='#2e004d')
                    printd1.grid(row=18, column=1,padx=40,pady=10)

                    APoll = (str)(APoll)
                    BPoll = (str)(BPoll)
                    CPoll = (str)(CPoll)
                    DPoll = (str)(DPoll)

                    printa2 = Label(tgui, text=CPoll + " %",fg='yellow',font='Arial 16 bold',border=5,bg='#2e004d')
                    printa2.grid(row=15, column=2,padx=40,pady=10)
                    printb2 = Label(tgui, text=BPoll + " %",fg='yellow',font='Arial 16 bold',border=5,bg='#2e004d')
                    printb2.grid(row=16, column=2,padx=40,pady=10)
                    printc2 = Label(tgui, text=APoll + " %",fg='yellow',font='Arial 16 bold',border=5,bg='#2e004d')
                    printc2.grid(row=17, column=2,padx=40,pady=10)
                    printd2 = Label(tgui, text=DPoll + " %",fg='yellow',font='Arial 16 bold',border=5,bg='#2e004d')
                    printd2.grid(row=18, column=2,padx=40,pady=10)

                if (correct == 'D'):
                    printa1 = Label(tgui, text="|" * DPoll,fg='yellow',font='Arial 16 bold',border=5,bg='#2e004d')
                    printa1.grid(row=15, column=1,padx=40,pady=10)
                    printb1 = Label(tgui, text="|" * BPoll,fg='yellow',font='Arial 16 bold',border=5,bg='#2e004d')
                    printb1.grid(row=16, column=1,padx=40,pady=10)
                    printc1 = Label(tgui, text="|" * CPoll,fg='yellow',font='Arial 16 bold',border=5,bg='#2e004d')
                    printc1.grid(row=17, column=1,padx=40,pady=10)
                    printd1 = Label(tgui, text="|" * APoll,fg='yellow',font='Arial 16 bold',border=5,bg='#2e004d')
                    printd1.grid(row=18, column=1,padx=40,pady=10)

                    APoll = (str)(APoll)
                    BPoll = (str)(BPoll)
                    CPoll = (str)(CPoll)
                    DPoll = (str)(DPoll)

                    printa2 = Label(tgui, text=DPoll + " %",fg='yellow',font='Arial 16 bold',border=5,bg='#2e004d')
                    printa2.grid(row=15, column=2,padx=40,pady=10)
                    printb2 = Label(tgui, text=BPoll + " %",fg='yellow',font='Arial 16 bold',border=5,bg='#2e004d')
                    printb2.grid(row=16, column=2,padx=40,pady=10)
                    printc2 = Label(tgui, text=CPoll + " %",fg='yellow',font='Arial 16 bold',border=5,bg='#2e004d')
                    printc2.grid(row=17, column=2,padx=40,pady=10)
                    printd2 = Label(tgui, text=APoll + " %",fg='yellow',font='Arial 16 bold',border=5,bg='#2e004d')
                    printd2.grid(row=18, column=2,padx=40,pady=10)

            OKbutton = Button(tgui, text='  OK  ', font='Arial 22 bold', bg="black", fg='yellow', border=5,
                              command=tgui.destroy)
            OKbutton.grid(row=21,column=1, padx=40, pady=40)

            tgui.mainloop()

def expertadvice(correct):

    global randnumber2a,fiftyfiftydone,expertdone,randnumber3a

    expertanswer1 = ["I am confident the answer is ", "I am sure the correct option is ", "My answer would be "]
    expertanswer2 = ["I am confused between ", "According to me the answer might be ",
                     "Maybe the answer is either  "]
    expertanswer3 = ["I am sorry but I have no idea about this question. ",
                     "I apologize, I don't have any answer for this question. ",
                     "I regret to say that I don't the answer to this question. "]

    if expertdone==0:
        tgui = Tk()
        tgui.title("Expert Advice")
        tgui.geometry('600x400+480+270')
        tgui.iconbitmap(os.path.join(path, 'Images and icons\kbc_logo.ico'))
        tgui.configure(bg='#2e004d')
        correct=str(correct)
        correct=correct.upper()

        expertintro = Label(tgui, text="Hello . My name is Mrs. Kavya Dixit\nand I am the expert for today's game.", bg='#2e004d', fg='yellow', font='Arial 16 bold', border=5)
        expertintro.grid(row=6, columnspan=1, padx=80, pady=20)

        expertdone = 1
        if (denomination < 320001 or (fiftyfiftydone == 1 and sameq_flag==1)):
            randstring = random.choice(expertanswer1)
            expertanswers = Label(tgui, text=randstring + correct+'.',bg='#2e004d',fg='yellow',font='Arial 16 bold',border=5)
            expertanswers.grid(row=10, columnspan=2,padx=80,pady=10)

        elif (denomination < 2500001):
            randnumber2 = randint(1, 2)
            if (randnumber2 == 1):
                randstring = random.choice(expertanswer1)
                expertanswers = Label(tgui, text=randstring + correct+'.',bg='#2e004d',fg='yellow',font='Arial 16 bold',border=5)
                expertanswers.grid(row=10, columnspan=2,padx=80,pady=10)
            if (randnumber2 == 2):
                if (correct == 'A'):
                    randnumber2a = randint(1, 4)
                    while (randnumber2a == 1):
                        randnumber2a = randint(1, 4)

                if (correct == 'B'):
                    randnumber2a = randint(1, 4)
                    while (randnumber2a == 2):
                        randnumber2a = randint(1, 4)

                if (correct == 'C'):
                    randnumber2a = randint(1, 4)
                    while (randnumber2a == 3):
                        randnumber2a = randint(1, 4)

                if (correct == 'D'):
                    randnumber2a = randint(1, 4)
                    while (randnumber2a == 4):
                        randnumber2a = randint(1, 4)

                randstring2a = (str)(randnumber2a)
                if (randstring2a == '1'):
                    randstring2a = 'A'
                if (randstring2a == '2'):
                    randstring2a = 'B'
                if (randstring2a == '3'):
                    randstring2a = 'C'
                if (randstring2a == '4'):
                    randstring2a = 'D'
                randstring = random.choice(expertanswer2)
                expertanswers = Label(tgui, text=randstring + correct + "," + randstring2a,bg='#2e004d',fg='yellow',font='Arial 16 bold',border=5)
                expertanswers.grid(row=10, columnspan=2,padx=80,pady=10)

        else:
            randnumber3 = randint(1, 3)
            if (randnumber3 == 1):
                randstring = random.choice(expertanswer1)
                expertanswers = Label(tgui, text=randstring + correct+'.',bg='#2e004d',fg='yellow',font='Arial 16 bold',border=5)
                expertanswers.grid(row=10, columnspan=1,padx=80,pady=10)
            if (randnumber3 == 2):
                if (correct == 'A'):
                    randnumber3a = randint(1, 4)
                    while (randnumber3a == 1):
                        randnumber3a = randint(1, 4)

                if (correct == 'B'):
                    randnumber3a = randint(1, 4)
                    while (randnumber3a == 2):
                        randnumber3a = randint(1, 4)

                if (correct == 'C'):
                    randnumber3a = randint(1, 4)
                    while (randnumber3a == 3):
                        randnumber3a = randint(1, 4)

                if (correct == 'D'):
                    randnumber3a = randint(1, 4)
                    while (randnumber3a == 4):
                        randnumber3a = randint(1, 4)

                randstring3a = (str)(randnumber3a)
                if (randstring3a == '1'):
                    randstring3a = 'A'
                if (randstring3a == '2'):
                    randstring3a = 'B'
                if (randstring3a == '3'):
                    randstring3a = 'C'
                if (randstring3a == '4'):
                    randstring3a = 'D'
                randstring = random.choice(expertanswer2)
                expertanswers = Label(tgui, text=randstring + correct + "," + randstring3a,bg='#2e004d',fg='yellow',font='Arial 16 bold',border=5)
                expertanswers.grid(row=10, columnspan=2,padx=80,pady=10)
            if (randnumber3 == 3):
                randstring = random.choice(expertanswer3)
                expertanswers = Label(tgui, text=randstring,bg='#2e004d',fg='yellow',font='Arial 16 bold',border=5)
                expertanswers.grid(row=10, columnspan=2,padx=80,pady=10)

        OKbutton = Button(tgui, text='  OK  ', font='Arial 22 bold', bg="black", fg='yellow', border=5,
                          command=tgui.destroy)
        OKbutton.grid(row=15, padx=80, pady=40)

        tgui.mainloop()





startingwindow()
screen.mainloop()
