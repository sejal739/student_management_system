def addstudent():
    def submitadd():
        id = idval.get()
        name = nameval.get()
        mobile = mobileval.get()
        email = emailval.get()
        dob = dobval.get()
        addeddate = time.strftime("%d/%m/%Y")
        try:
            strr = 'insert into studentdata1 values(%s,%s,%s,%s,%s,%s)'
            mycursor.execute(strr,(id,name,mobile,email,dob,addeddate))
            con.commit()
            res = messagebox.askyesnocancel('Notification','Id {} Name {} added successfully..and want to clear the form'.format(id,name), parent=addroot)
            if(res == True):
                idval.set('')
                nameval.set('')
                mobileval.set('')
                emailval.set('')
                dobval.set('')

        except:
            messagebox.showerror('notifications','Id already exist try another id...',parent=addroot)
        strr = 'select * from studentdata1'
        mycursor.execute(strr)
        datas = mycursor.fetchall()
        studenttable.delete(*studenttable.get_children())
        for i in datas:
            vv = [i[0], i[1], i[2], i[3], i[4], i[5]]
            studenttable.insert('',END,values=vv)

    addroot = Toplevel(master=DataEntryFrame)
    addroot.grab_set()
    addroot.geometry('470x450+220+200')
    addroot.title('student management system')
    addroot.config(bg='blue')
    addroot.resizable(False,False)
    ###########----------------------
    idlable = Label(addroot, text="Enter ID : ", bg='gold2', font=('times', 20, 'bold'), relief=GROOVE, borderwidth=3,
                    width=12, anchor='w')
    idlable.place(x=10, y=10)
    namelable = Label(addroot, text="Enter Name : ", bg='gold2', font=('times', 20, 'bold'), relief=GROOVE, borderwidth=3,
                    width=12, anchor='w')
    namelable.place(x=10, y=70)
    phnlable = Label(addroot, text="Enter mobile no. : ", bg='gold2', font=('times', 20, 'bold'), relief=GROOVE, borderwidth=3,
                    width=12, anchor='w')
    phnlable.place(x=10, y=130)
    emaillable = Label(addroot, text="Enter email : ", bg='gold2', font=('times', 20, 'bold'), relief=GROOVE, borderwidth=3,
                    width=12, anchor='w')
    emaillable.place(x=10, y=190)
    doblable = Label(addroot, text="Enter D.O.B : ", bg='gold2', font=('times', 20, 'bold'), relief=GROOVE, borderwidth=3,
                    width=12, anchor='w')
    doblable.place(x=10, y=250)
    #############3-----------------------ADD STUDENT ENTRY
    idval = StringVar()
    nameval = StringVar()
    mobileval = StringVar()
    emailval = StringVar()
    dobval = StringVar()
    identry = Entry(addroot,font=('roman',15,'bold'),bd=5,textvariable=idval)
    identry.place(x=250,y=10)

    nameentry = Entry(addroot, font=('roman', 15, 'bold'), bd=5, textvariable=nameval)
    nameentry.place(x=250, y=70)

    mobileentry = Entry(addroot, font=('roman', 15, 'bold'), bd=5, textvariable=mobileval)
    mobileentry.place(x=250, y=130)

    emailentry = Entry(addroot, font=('roman', 15, 'bold'), bd=5, textvariable=emailval)
    emailentry.place(x=250, y=190)

    dobentry = Entry(addroot, font=('roman', 15, 'bold'), bd=5, textvariable=dobval)
    dobentry.place(x=250, y=250)

    submitbtn = Button(addroot,text='submit',font=('roman', 15, 'bold'),bg ='red', bd=5, width =20,
                       activebackground ='blue',activeforeground ='white',command=submitadd)
    submitbtn.place(x=150,y=380)
    addroot.mainloop()
def searchstudent():
    def search():
        id = idval.get()
        name = nameval.get()
        mobile = mobileval.get()
        email = emailval.get()
        dob = dobval.get()
        addeddate = time.strftime("%d/%m/%y")
        if(id != ''):
            strr = 'select * from studentdata1 where id=%s'
            mycursor.execute(strr,(id))
            datas = mycursor.fetchall()
            studenttable.delete(*studenttable.get_children())
            for i in datas:
                vv = [i[0],i[1],i[2],i[3],i[4],i[5]]
                studenttable.insert('',END,values=vv)
        if (name != ''):
            strr = 'select * from studentdata1 where name=%s'
            mycursor.execute(strr, (name))
            datas = mycursor.fetchall()
            studenttable.delete(*studenttable.get_children())
            for i in datas:
                vv = [i[0], i[1], i[2], i[3], i[4], i[5]]
                studenttable.insert('', END, values=vv)
        if (mobile != ''):
            strr = 'select * from studentdata1 where mobile=%s'
            mycursor.execute(strr, (mobile))
            datas = mycursor.fetchall()
            studenttable.delete(*studenttable.get_children())
            for i in datas:
                vv = [i[0], i[1], i[2], i[3], i[4], i[5]]
                studenttable.insert('', END, values=vv)
        if (email != ''):
            strr = 'select * from studentdata1 where email=%s'
            mycursor.execute(strr, (email))
            datas = mycursor.fetchall()
            studenttable.delete(*studenttable.get_children())
            for i in datas:
                vv = [i[0], i[1], i[2], i[3], i[4], i[5]]
                studenttable.insert('', END, values=vv)
        if (dob != ''):
            strr = 'select * from studentdata1 where dob=%s'
            mycursor.execute(strr, (dob))
            datas = mycursor.fetchall()
            studenttable.delete(*studenttable.get_children())
            for i in datas:
                vv = [i[0], i[1], i[2], i[3], i[4], i[5]]
                studenttable.insert('', END, values=vv)


    searchroot = Toplevel(master=DataEntryFrame)
    searchroot.grab_set()
    searchroot.geometry('470x490+220+200')
    searchroot.title('student management system')
    searchroot.config(bg='firebrick1')
    searchroot.resizable(False,False)
    ###########----------------------
    idlable = Label(searchroot, text="Enter ID : ", bg='gold2', font=('times', 20, 'bold'), relief=GROOVE, borderwidth=3,
                    width=12, anchor='w')
    idlable.place(x=10, y=10)
    namelable = Label(searchroot, text="Enter Name : ", bg='gold2', font=('times', 20, 'bold'), relief=GROOVE, borderwidth=3,
                    width=12, anchor='w')
    namelable.place(x=10, y=70)
    phnlable = Label(searchroot, text="Enter mobile no. : ", bg='gold2', font=('times', 20, 'bold'), relief=GROOVE, borderwidth=3,
                    width=12, anchor='w')
    phnlable.place(x=10, y=130)
    emaillable = Label(searchroot, text="Enter email : ", bg='gold2', font=('times', 20, 'bold'), relief=GROOVE, borderwidth=3,
                    width=12, anchor='w')
    emaillable.place(x=10, y=190)

    doblable = Label(searchroot, text="Enter D.O.B : ", bg='gold2', font=('times', 20, 'bold'), relief=GROOVE,
                     borderwidth=3,
                     width=12, anchor='w')
    doblable.place(x=10, y=250)
    datelable = Label(searchroot, text="Enter Date: ", bg='gold2', font=('times', 20, 'bold'), relief=GROOVE,
                     borderwidth=3,
                     width=12, anchor='w')
    datelable.place(x=10, y=310)
    #############3-----------------------ADD STUDENT ENTRY
    idval = StringVar()
    nameval = StringVar()
    mobileval = StringVar()
    emailval = StringVar()
    dobval = StringVar()
    dateval = StringVar()
    identry = Entry(searchroot,font=('roman',15,'bold'),bd=5,textvariable=idval)
    identry.place(x=250,y=10)

    nameentry = Entry(searchroot, font=('roman', 15, 'bold'), bd=5, textvariable=nameval)
    nameentry.place(x=250, y=70)

    mobileentry = Entry(searchroot, font=('roman', 15, 'bold'), bd=5, textvariable=mobileval)
    mobileentry.place(x=250, y=130)

    emailentry = Entry(searchroot, font=('roman', 15, 'bold'), bd=5, textvariable=emailval)
    emailentry.place(x=250, y=190)

    dobentry = Entry(searchroot, font=('roman', 15, 'bold'), bd=5, textvariable=dobval)
    dobentry.place(x=250, y=250)
    dateentry = Entry(searchroot, font=('roman', 15, 'bold'), bd=5, textvariable=dateval)
    dateentry.place(x=250, y=310)

    submitbtn = Button(searchroot,text='search',font=('roman', 15, 'bold'),bg ='red', bd=5, width =20,
                       activebackground ='blue',activeforeground ='white',command=search)
    submitbtn.place(x=150,y=380)
    searchroot.mainloop()

def deletestudent():
    cc = studenttable.focus()
    content = studenttable.item(cc)
    pp = content['values'][0]
    strr = 'delete from studentdata1 where id=%s'
    mycursor.execute(strr,(pp))
    con.commit()
    messagebox.showinfo('Notifications','Id {} deleted successfully..'.format(pp) )
    strr = 'select * from studentdata1'
    mycursor.execute(strr)
    datas = mycursor.fetchall()
    studenttable.delete(*studenttable.get_children())
    for i in datas:
        vv = [i[0], i[1], i[2], i[3], i[4], i[5]]
        studenttable.insert('', END, values=vv)

def updatestudent():
    def update():
        id = idval.get()
        name = nameval.get()
        mobile = mobileval.get()
        email = emailval.get()
        dob = dobval.get()
        date = dateval.get()

        strr = 'update studentdata1 set name=%s,mobile=%s,email=%s,dob=%s,date=%s where id=%s'
        mycursor.execute(strr,(name,mobile,email,dob,date,id))
        con.commit()
        messagebox.showinfo('notifications','Id {} Modified successfully...'.format(id),parent=updateroot)
        strr = 'select * from studentdata1'
        mycursor.execute(strr)
        datas = mycursor.fetchall()
        studenttable.delete(*studenttable.get_children())
        for i in datas:
            vv = [i[0], i[1], i[2], i[3], i[4], i[5]]
            studenttable.insert('', END, values=vv)
    updateroot = Toplevel(master=DataEntryFrame)
    updateroot.grab_set()
    updateroot.geometry('470x490+220+200')
    updateroot.title('student management system')
    updateroot.config(bg='lawn green')
    updateroot.resizable()
    ###########----------------------
    idlable = Label(updateroot, text="Update ID : ", bg='gold2', font=('times', 20, 'bold'), relief=GROOVE, borderwidth=3,
                    width=12, anchor='w')
    idlable.place(x=10, y=10)
    namelable = Label(updateroot, text="UpdateName : ", bg='gold2', font=('times', 20, 'bold'), relief=GROOVE, borderwidth=3,
                    width=12, anchor='w')
    namelable.place(x=10, y=70)
    phnlable = Label(updateroot, text="Update mobile no. : ", bg='gold2', font=('times', 20, 'bold'), relief=GROOVE, borderwidth=3,
                    width=12, anchor='w')
    phnlable.place(x=10, y=130)
    emaillable = Label(updateroot, text="Update email : ", bg='gold2', font=('times', 20, 'bold'), relief=GROOVE, borderwidth=3,
                    width=12, anchor='w')
    emaillable.place(x=10, y=190)

    doblable = Label(updateroot, text="Update D.O.B : ", bg='gold2', font=('times', 20, 'bold'), relief=GROOVE,
                     borderwidth=3,
                     width=12, anchor='w')
    doblable.place(x=10, y=250)
    datelable = Label(updateroot, text="Update Date: ", bg='gold2', font=('times', 20, 'bold'), relief=GROOVE,
                     borderwidth=3,
                     width=12, anchor='w')
    datelable.place(x=10, y=310)
    #############3-----------------------ADD STUDENT ENTRY
    idval = StringVar()
    nameval = StringVar()
    mobileval = StringVar()
    emailval = StringVar()
    dobval = StringVar()
    dateval = StringVar()
    identry = Entry(updateroot,font=('roman',15,'bold'),bd=5,textvariable=idval)
    identry.place(x=250,y=10)

    nameentry = Entry(updateroot, font=('roman', 15, 'bold'), bd=5, textvariable=nameval)
    nameentry.place(x=250, y=70)

    mobileentry = Entry(updateroot, font=('roman', 15, 'bold'), bd=5, textvariable=mobileval)
    mobileentry.place(x=250, y=130)

    emailentry = Entry(updateroot, font=('roman', 15, 'bold'), bd=5, textvariable=emailval)
    emailentry.place(x=250, y=190)

    dobentry = Entry(updateroot, font=('roman', 15, 'bold'), bd=5, textvariable=dobval)
    dobentry.place(x=250, y=250)
    dateentry = Entry(updateroot, font=('roman', 15, 'bold'), bd=5, textvariable=dateval)
    dateentry.place(x=250, y=310)

    submitbtn = Button(updateroot,text='Update student',font=('roman', 15, 'bold'),bg ='red', bd=5, width =20,
                       activebackground ='blue',activeforeground ='white',command=update)
    submitbtn.place(x=150,y=380)
    cc = studenttable.focus()
    content = studenttable.item(cc)
    pp = content['values']
    if(len(pp) != 0):
        idval.set(pp[0])
        nameval.set(pp[1])
        mobileval.set(pp[2])
        emailval.set(pp[3])
        dobval.set(pp[4])
        dateval.set(pp[5])

    updateroot.mainloop()


def showstudent():
    strr = 'select * from studentdata1'
    mycursor.execute(strr)
    datas = mycursor.fetchall()
    studenttable.delete(*studenttable.get_children())
    for i in datas:
        vv = [i[0], i[1], i[2], i[3], i[4], i[5]]
        studenttable.insert('', END, values=vv)
def exitstudent():
    res = messagebox.askyesnocancel('notification','do you want to exit?')
    if(res==True):
        root.destroy()
#############CONNETTO DATABASE
def connectdb():
    def submitdb():
        global con,mycursor
        host = hostval.get()
        user = userval.get()
        password = passwordval.get()
        try:
            con = pymysql.connect(host=host,user=user,password=password)
            mycursor =con.cursor()
        except:
            messagebox.showerror('Notifications','data is incorrect please enter again',parent = dbroot)
            return
        try:
            strr = 'create database stumanagementsys'
            mycursor.execute(strr)
            strr = 'use stumanagementsys'
            mycursor.execute(strr)
            strr = 'create table studentdata1(id int,name varchar(20),mobile varchar(12),email varchar(30),dob varchar(40),date varchar(40))'
            mycursor.execute(strr)
            strr = 'alter table studentdata1 modify column id int primary key'
            mycursor.execute(strr)
            messagebox.showinfo('notification', 'Database is created and now you are connected to database...', parent=dbroot)
        except:
            strr = 'use stumanagementsys'
            mycursor.execute(strr)
            messagebox.showinfo('notification','now you are connected to database...',parent = dbroot)
        dbroot.destroy()
    dbroot = Toplevel()
    dbroot.grab_set()
    dbroot.geometry('470x250+800+230')
    dbroot.resizable(False,False)
    dbroot.config(bg='blue')
    idlable = Label(dbroot,text = "enter Host : ",bg='gold2',font=('times',20,'bold'),relief=GROOVE,borderwidth=3,width=12,anchor = 'w')
    idlable.place(x=10,y=10)
    namelable = Label(dbroot, text="enter username : ", bg='gold2', font=('times', 20, 'bold'), relief=GROOVE, borderwidth=3,
                    width=12, anchor='w')
    namelable.place(x=10, y=70)
    passwordlable = Label(dbroot, text="enter password : ", bg='gold2', font=('times', 20, 'bold'), relief=GROOVE, borderwidth=3,
                    width=12, anchor='w')
    passwordlable.place(x=10, y=130)

    ########################### entrybox
    hostval = StringVar()
    userval = StringVar()
    passwordval = StringVar()
    hostentry = Entry(dbroot,font=('roman',15,'bold'),bd=5,textvariable=hostval)
    hostentry.place(x=250,y=10)
    userentry = Entry(dbroot, font=('roman', 15, 'bold'), bd=5, textvariable=userval)
    userentry.place(x=250, y=70)
    passwordentry = Entry(dbroot, font=('roman', 15, 'bold'), bd=5, textvariable=passwordval)
    passwordentry.place(x=250, y=130)
    #############submitbutton
    submitbutton = Button(dbroot,text='submit', font=('roman', 15, 'bold'),bg ='red', bd=5, width =20,
                          activebackground ='blue',activeforeground ='white',command = submitdb)
    submitbutton.place(x=150,y=190)

    dbroot.mainloop()

##############
def Tick():
    global text
    time_string = time.strftime("%H:%M:%S")
    date_string = time.strftime("%d:%m:%y")
    clock.config(text='date : '+date_string+"\n"+'time : '+time_string)
    clock.after(200,Tick)
import random
colors =['red','green','blue','pink','red2']
def IntroLableColortick():
    fg = random.choice(colors)
    SliderLable.config(fg=fg)
    SliderLable.after(5,IntroLableColortick)
def introlabeltick():
    global count,text
    if(count>=len(ss)):
        count = 0
        text = ''
        SliderLable.config(text=text)
    else:
        text = text+ss[count]
        SliderLable.config(text = text)
        count +=1
    SliderLable.after(100,introlabeltick)
from tkinter import *
from tkinter import Toplevel,messagebox
from tkinter.ttk import Treeview
from tkinter import ttk
import pymysql
import time
root = Tk()
root.title('Student management system')
root.config(bg='gold2')
root.geometry('1144x700+200+50')
#root.iconbitmap('mana.ico')
root.resizable(False,False)
################### frames
DataEntryFrame = Frame(root,bg ='gold2', relief=GROOVE,borderwidth=2)
DataEntryFrame.place(x=10,y=80,width=500,height=600)
##############################################frames
frontlable = Label(DataEntryFrame,text='---------------WELCOME---------------',font=('arial',30,'italic bold'),width=30,bg='gold2')
frontlable.pack(side=TOP,expand=TRUE)
#############BUTTONS
addbtn =Button(DataEntryFrame,text='1. Add student',font=('chiller',20,' bold'),width=25,bd=6,bg='skyblue3',activebackground ='blue',
               relief=RIDGE,activeforeground ='white',command =addstudent)
addbtn.pack(side=TOP,expand=TRUE)
searchbtn =Button(DataEntryFrame,text='2. Seach student',font=('chiller',20,' bold'),width=25,bd=6,bg='skyblue3',activebackground ='blue',
               relief=RIDGE,activeforeground ='white',command = searchstudent)
searchbtn.pack(side=TOP,expand=TRUE)
updatebtn =Button(DataEntryFrame,text='2. update student',font=('chiller',20,' bold'),width=25,bd=6,bg='skyblue3',activebackground ='blue',
               relief=RIDGE,activeforeground ='white',comm
                  =updatestudent)
updatebtn.pack(side=TOP,expand=TRUE)
deletebtn =Button(DataEntryFrame,text='4. delete student',font=('chiller',20,' bold'),width=25,bd=6,bg='skyblue3',activebackground ='blue',
               relief=RIDGE,activeforeground ='white',command=deletestudent)
deletebtn.pack(side=TOP,expand=TRUE)
showbtn =Button(DataEntryFrame,text='5. show All',font=('chiller',20,' bold'),width=25,bd=6,bg='skyblue3',activebackground ='blue',
               relief=RIDGE,activeforeground ='white',command=showstudent)
showbtn.pack(side=TOP,expand=TRUE)
exitbtn =Button(DataEntryFrame,text='6. Exit',font=('chiller',20,' bold'),width=25,bd=6,bg='skyblue3',activebackground ='blue',
               relief=RIDGE,activeforeground ='white',command = exitstudent)
exitbtn.pack(side=TOP,expand=TRUE)

#######################################-------------
ShowDataFrame = Frame(root,bg ='gold2', relief=GROOVE,borderwidth=2)
ShowDataFrame.place(x=550,y=80,width=620,height=600)
##############slider
style = ttk.Style()
style.configure('Treeview.Heading',font=('chiller',20,'bold'),foreground='blue')
scroll_x = Scrollbar(ShowDataFrame,orient = HORIZONTAL)
scroll_y = Scrollbar(ShowDataFrame,orient = VERTICAL)
studenttable = Treeview(ShowDataFrame,columns=('Id','Name','Mobile No.','Email','D.O.B','Added Date'),
                        yscrollcommand=scroll_y.set,xscrollcommand=scroll_x.set)
scroll_x.pack(side=BOTTOM,fill=X)
scroll_y.pack(side=RIGHT,fill=Y)
scroll_x.config(command=studenttable.xview)
scroll_y.config(command=studenttable.yview)
studenttable.heading('Id',text='Id')
studenttable.heading('Name',text='Name')
studenttable.heading('Mobile No.',text='Moblie No.')
studenttable.heading('Email',text='Email')
studenttable.heading('D.O.B',text='D.O.B')
studenttable.heading('Added Date',text='Date')
studenttable['show'] = 'headings'
studenttable.column('Id',width=100)
studenttable.column('Name',width=200)
studenttable.column('Mobile No.',width=200)
studenttable.column('Email',width=300)
studenttable.column('D.O.B',width=150)
studenttable.column('Added Date',width=150)
studenttable.pack(fill=BOTH,expand =1)
###############################
ss = 'welcome to student management system'
count = 0
text = ''
SliderLable = Label(root,text=ss,font=('chiller',30,'italic bold'),relief=RIDGE,borderwidth=4,width=35,bg='cyan')
SliderLable.place(x=260,y=0)
introlabeltick()
IntroLableColortick()
#################################################
clock =Label(root,text=ss,font=('times',14,'bold'),relief=RIDGE,borderwidth=14,bg='lawn green')
clock.place(x=0,y=0)
Tick()
######################connecttodatabase
connectbutton = Button(root,text='Administrator Login',font=('chiller',19,'italic bold'),width=23,relief=RIDGE,borderwidth=4,
                       bg='green2',activebackground ='blue',activeforeground ='white',command = connectdb)
connectbutton.place(x=930,y=0)
root.mainloop()