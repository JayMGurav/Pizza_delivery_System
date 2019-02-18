from tkinter import *
import tkinter.messagebox
import sqlite3 
import time
root=Tk()
db=sqlite3.connect("pizzadb.db")
pointer=db.cursor()
# pointer.execute("create table users(u_id INTEGER PRIMARY KEY AUTOINCREMENT,username varchar,phoneNumber int,address varchar,password varchar)")
# pointer.execute("insert into users values(1,'Jay',8762290119,'punjab LPU','123')")
# db.commit()
#-------------------logut Terminate-----
def clicklogout(event):
    profile_p.withdraw()
    profile_p.destroy()
    root.destroy()
    # exit()

#----------------------------loginPage----------
def loginpage():
    root.withdraw()
    global login_p
    login_p=Toplevel()
    login_p.title("Pizzas")
    login_p.geometry("1200x740")
    login_p.config(bg="#ffffff")
    #------setting entry restriction------
    var =StringVar()
    max_len = 9
    def on_write(*args):
        s = var.get()
        if len(s) > max_len:
            var.set(s[:max_len])
    var.trace_variable("w", on_write)
    #---------------DAtabase-----------
    # db=sqlite3.connect("pizzadb.db")
    # pointer=db.cursor()
    # pointer.execute("create table users(u_id INTEGER PRIMARY KEY AUTOINCREMENT,username varchar,phoneNumber int,address varchar,password varchar)")
    # pointer.execute("insert into users values(1,'Jay',8762290119,'punjab LPU','123')")
    # db.commit()
    def login1(event):
        userGname=userName.get()
        passGword=password.get()
        pointer.execute("select * from users where username=? and password=? ",(userGname,passGword,))
        r=pointer.fetchone()
        # print(r)
        if r is not None:
            callprofilepage(event,'login',r)
        else:
            tkinter.messagebox.showerror("Data not found","wrong Username or Password, Please enter correct details")
             
    #---------------background Frame----------
    rootImage =PhotoImage(file="loginBack.png")
    rootFrame =Label(login_p,image=rootImage,borderwidth=0)
    rootFrame.pack(fill="both")

    #--------------entry for login details---------
    loginFrame =Frame(login_p,bg="#ffffff")
    loginFrame.place(x=640,y=280)
    loginFrame.config(highlightbackground="#ff1744",highlightthickness=2)
    #--------------username---------
    userNameFrame =Frame(loginFrame,bg="#fff",borderwidth=2)
    userNameFrame.pack(side="top",padx=10,pady=28)
    userNameLabel =Label(userNameFrame,text="User name :",width=10,font=("Sans-Serif",12),fg="#ff1744",bg="#fff")
    userNameLabel.pack(side="left",padx=16)
    userName =Entry(userNameFrame,width=28)
    userName.pack(side="right",padx=4)
    #--------------password--------
    passwordFrame =Frame(loginFrame,bg="#fff",borderwidth=2)
    passwordFrame.pack(side="top",padx=10,pady=0)
    passwordLabel =Label(passwordFrame,text="Password :",width=10,font=("Sans-Serif",12),fg="#ff1744",bg="#fff")
    passwordLabel.pack(side="left",padx=16)
    password =Entry(passwordFrame,width=28,show="*️⃣",textvariable=var)
    password.pack(side="right",padx=4)
    #-----------Sign Up link-------------
    signUpLink =Label(loginFrame,text="Not yet Registered..? Sign-Up ",font=("Sans-Serif",10),fg="blue",bg="#fff")#,COMMAND=signuppage())
    signUpLink.bind("<Button-1>",signuppage)
    signUpLink.pack(side="top",pady=8)


    #----------------login Button------
    login=PhotoImage(file="loginButton.png")
    loginButton =Button(loginFrame,image=login,borderwidth=0,bg="#ffffff",height=40,activebackground="#ffffff")
    loginButton.bind("<Button-1>",login1)
    loginButton.pack(side="bottom",pady=28)    
    login_p.mainloop()
#-------------------function-call Login Page in signup-----
def callLoginpage(Event):
    signup_p.withdraw()
    signup_p.destroy()
    loginpage()
#----------------------------Signup_Page---------
def signuppage(Event):
    login_p.withdraw()
    login_p.destroy()
    global signup_p  
    signup_p=Toplevel()
    signup_p.geometry("1200x458")
    signup_p.config(bg="#fff")
    signup_p.geometry("1200x740")
      #--------database---------
    # db=sqlite3.connect("pizzadb.db")
    # pointer=db.cursor()
    def clickSignup(event):
        usn=str(usernamesignEntry.get())
        psn=int(phoneNumEntry.get())
        # for ads in addressEntry:
        ads=str(addressEntry.get('1.0','end-1c'))
        pas=str(signPasswordEntry.get())
        cpass=str(signConfirmPasswordEntry.get())
        if(pas==cpass):
            pointer.execute("insert into users(username,phoneNumber,address,password) values(?,?,?,?)",(usn,psn,ads,pas,))
            db.commit()
            pointer.execute("select * from users where username=? and password=?",(usn,pas,))
            r=pointer.fetchone()
            # print(r)
            callprofilepage(event,'sign',r)

        else:
            tkinter.messagebox.showerror("wrong attempt","your password didn't match ")
        

    #------------------functions----------
    #-----------background---------------
    bgImage=PhotoImage(file="signup.png")
    bgImageLabel =Label(signup_p,image=bgImage,borderwidth=0)
    bgImageLabel.pack(fill="both")

    #--------------Signup Label-------
    loginAsk =Label(signup_p,text="Sign Up",font=("Sans-Serif",16),fg="#ff1744",bg="#fff")
    loginAsk.place(x=740,y=100)
    #--------------username---------
    usernamesignFrame =Frame(signup_p,bg="#fff",borderwidth=2)
    usernamesignFrame.place(x=600,y=160)  #pack(side="top",padx=20,pady=10)
    usernamesignLabel =Label(usernamesignFrame,text="Username :",font=("Sans-Serif",12),fg="#000",bg="#fff")
    usernamesignLabel.pack(side="left")
    usernamesignEntry =Entry(usernamesignFrame,width=28)
    usernamesignEntry.pack(side="right",padx=64)

    #-----------phone number-----------
    phoneNumFrame =Frame(signup_p,bg="#fff",borderwidth=2)
    phoneNumFrame.place(x=600,y=200)  #pack(side="top",padx=20,pady=10)
    phoneNumLabel =Label(phoneNumFrame,text="Phone Number :",font=("Sans-Serif",12),fg="#000",bg="#fff")
    phoneNumLabel.pack(side="left")
    phoneNumEntry =Entry(phoneNumFrame,width=28)
    phoneNumEntry.pack(side="right",padx=32)

    # #-----------Address---------------
    addressFrame =Frame(signup_p,bg="#fff",borderwidth=2)
    addressFrame.place(x=600,y=240)   #pack(side="top",padx=20,pady=10)
    addressLabel =Label(addressFrame,text="address :",font=("Sans-Serif",12),fg="#000",bg="#fff")
    addressLabel.place(x=0,y=0)
    addressEntry =Text(addressFrame,width=28,height=8)
    addressEntry.pack(side="right",padx=150)
    #-----------password----------
    signPasswordFrame =Frame(signup_p,bg="#fff",borderwidth=2)
    signPasswordFrame.place(x=600,y=390)  #pack(side="top",padx=20,pady=10)
    signPasswordLabel =Label(signPasswordFrame,text="Password :",font=("Sans-Serif",12),fg="#000",bg="#fff")
    signPasswordLabel.pack(side="left")
    signPasswordEntry =Entry(signPasswordFrame,width=28,show="*️⃣")
    signPasswordEntry.pack(side="right",padx=68)

    # #-----------password----------
    signConfirmPasswordFrame =Frame(signup_p,bg="#fff",borderwidth=2)
    signConfirmPasswordFrame.place(x=600,y=430)
    signConfirmPasswordLabel =Label(signConfirmPasswordFrame,text="Confirm password :",font=("Sans-Serif",12),fg="#000",bg="#fff")
    signConfirmPasswordLabel.pack(side="left")
    signConfirmPasswordEntry =Entry(signConfirmPasswordFrame,width=28,show="*️⃣")
    signConfirmPasswordEntry.pack(side="right",padx=10)

    #--------------aks login-----------
    loginAsk =Label(signup_p,text="Already registered..? Login",font=("Sans-Serif",10),fg="blue",bg="#fff")
    loginAsk.bind("<Button-1>",callLoginpage)
    loginAsk.place(x=680,y=470)
    # #---------------button--------
    signupButtonImage =PhotoImage(file="signupButton.png")
    signupButton =Button(signup_p,image=signupButtonImage,bg="#fff",borderwidth=0,activebackground="#ffffff")#,command=clickSignup)
    signupButton.bind("<Button-1>",clickSignup)
    signupButton.place(x=700,y=510)   #pack(side="bottom")
    signup_p.mainloop()
#----------------------------profile Page--------
#------------------function for profilePage call---
def callprofilepage(event,fromPage,r):
    if fromPage=='login':
        login_p.withdraw()
        login_p.destroy()
    elif fromPage=='order' :
        pizza_p.withdraw()
        pizza_p.destroy()
    elif fromPage=='sign':
        signup_p.withdraw()
        signup_p.destroy()
    elif fromPage=='track':
        track_p.withdraw()
        track_p.destroy()
    profilepage(r)

def profilepage(r):

    global profile_p
    profile_p=Toplevel()
    profile_p.title("Profile")
    profile_p.geometry("1200x740")
    profile_p.config(bg="#F2F2F2")
    #------------------function----------
    #----------delete Pizza------
    def deletePizza(event,uid):
        d=orderNo.get()
        pointer.execute("select * from orders where order_id=? and u_id=?",(d,uid,))
        x=pointer.fetchone()
        if x is not None:
            pointer.execute("delete from orders where order_id=? and u_id=?",(d,uid,))
            # pointer.execute("select * from orders where u_id=?",(uid,))
            db.commit()
        else:
            tkinter.messagebox.showerror("Data not found","Wrong details, Please Enter Correct Order Id.")


    #-----------------Hero Image------------
    hero =PhotoImage(file="PIZZAS3.png")
    heroLabel =Label(profile_p,image = hero,borderwidth=0)
    heroLabel.pack(side="top",fill="both")

    #----------------Profilecard----------------
    profileFrame =Frame(profile_p,height="230",width="280",bg="#ffffff")
    profileFrame.place(x=80,y=454)

    #-----------------ProfileCardImage-----------
    profileImage =PhotoImage(file="face.png")
    profileLabel =Label(profile_p,image=profileImage,borderwidth=0,bg="#f2f2f2")
    profileLabel.place(x=80,y=350)
    #-------------------profile--Details----------
    # print(r)
    text='Name : '+ str(r[1])
    profileDetails = Text(profile_p,height=1,width=16,bg="#fff",borderwidth=0,cursor="arrow",font=("Sans-Serif",12))
    profileDetails.place(x=164,y=480)
    profileDetails.configure(state='normal')
    profileDetails.insert(END,text)
    profileDetails.configure(state='disabled')

    text2='Phone number : '+str(r[2])
    profileDetails2 = Text(profile_p,height=1,width=24,bg="#fff",borderwidth=0,cursor="arrow",font=("Sans-Serif",12))
    profileDetails2.place(x=114,y=506)
    profileDetails2.configure(state='normal')
    profileDetails2.insert(END,text2)
    profileDetails2.configure(state='disabled')

    text3='Address : '+r[3]
    profileDetails3 = Text(profile_p,height=4,width=22,bg="#fff",borderwidth=0,cursor="arrow",font=("Sans-Serif",12))
    profileDetails3.place(x=120,y=532)
    profileDetails3.configure(state='normal')
    profileDetails3.insert(END,text3)
    profileDetails3.configure(state='disabled')
    #----------------logut Button--------
    logutImage=PhotoImage(file="logout.png")
    logutButton=Button(profile_p,image=logutImage,borderwidth=0,activebackground="#F2F2F2")
    logutButton.bind("<Button-1>",clicklogout)
    logutButton.place(x=180,y=636)
    #---------------- Orders-------------
    orders =Frame(profile_p,height="320",width="600",bg="#ffffff")
    orders.place(x=440,y=364)
    #------------------order Details---------
    pointer.execute("select * from orders where u_id=?",(r[0],))
    orders=pointer.fetchall()
    n=1
    for x in orders:
        pointer.execute("select * from pizzas where p_id=?",(x[2],))
        d=pointer.fetchone()
        ordertext=str(x[0])+'\t\t\t'+str(d[1])+'\t\t\t\t'+str(d[2])
        orderDetails = Text(profile_p,height=2,width=64,bg="#fff",borderwidth=0,cursor="arrow",font=("Sans-Serif",12))
        orderDetails.place(x=456,y=418+n)
        orderDetails.configure(state='normal')
        orderDetails.insert(END,ordertext)
        orderDetails.configure(state='disabled')
        n=n+40
    #-------------------------delete order------
    deleteFrame = Frame(profile_p,width=100,bg="#fff")
    deleteFrame.place(x=459,y=640)
    deleteLabel=Label(deleteFrame,text="Order Number :",bg="#fff",borderwidth=0,font=("Sans-Serif",12))
    deleteLabel.pack(side="left",padx=4)
    orderNo=Entry(deleteFrame,width=8,borderwidth=1)
    orderNo.pack(side="left",)
    deleteImg=PhotoImage(file="delete1.png")
    deleteButton=Button(deleteFrame,image=deleteImg,borderwidth=0,bg="#fff",activebackground="#fff",width=40,height=40)
    deleteButton.bind("<Button-1>",lambda event,arg2=r[0]: deletePizza(event,arg2))  
    deleteButton.pack(side="right",padx=8)

    #----------order Border---------------
    orderBorImage =PhotoImage(file="orderBorder.png")
    borderImageLabel =Label(profile_p,image=orderBorImage,borderwidth=0)
    borderImageLabel.place(x=440,y=364)
    #-----------track button--------------
    trackImage =PhotoImage(file="track.png")
    trackImageLabel =Button(profile_p,image=trackImage,borderwidth=0,activebackground="#F2F2F2")
    trackImageLabel.bind("<Button-1>",lambda event,arg=r : trackpage(event,arg))  
    trackImageLabel.place(x=1105,y=485)
    #-----------------add button------------
    addImage =PhotoImage(file="add1.png")
    addImageButton =Button(profile_p,image=addImage,borderwidth=0,activebackground="#F2F2F2")
    addImageButton.bind("<Button-1>",lambda event,arg=r: orderpizzapage(event,arg))  
    addImageButton.place(x=1080,y=585)
   
    profile_p.mainloop()
#----------------------------order pizza page---------------------
def orderpizzapage(Event,r):
    profile_p.withdraw()
    profile_p.destroy()
    global pizza_p
    pizza_p=Toplevel()
    pizza_p.title("Pizzas")
    pizza_p.geometry("1200x740")
    pizza_p.config(bg="#f2f2f2")

    #------------check functions-----
    def Checkclick1(event):
        prs=str(p.get())
        amount= "Now at "+prs+" Rs only!"
        textField=Text(pizza_p,height=1,width=18,borderwidth=0,font=("Sans-Serif",12),cursor="arrow")
        textField.place(x=150,y=284)
        textField.configure(state='normal')
        textField.insert(END,amount)
        textField.configure(state='disabled')

    def Checkclick2(event):
        frs=str(f.get())
        amount= "Now at "+frs+" Rs only!"
        textField=Text(pizza_p,height=1,width=18,borderwidth=0,font=("Sans-Serif",12),cursor="arrow")
        textField.place(x=545,y=284)
        textField.configure(state='normal')
        textField.insert(END,amount)
        textField.configure(state='disabled')

    def Checkclick3(event):
        vrs=str(v.get())
        amount= "Now at "+vrs+" Rs only!"
        textField=Text(pizza_p,height=1,width=18,borderwidth=0,font=("Sans-Serif",12),cursor="arrow")
        textField.place(x=930,y=284)
        textField.configure(state='normal')
        textField.insert(END,amount)
        textField.configure(state='disabled')



    #----------order Bill Total------------
    class totaling:
        total=0
        bill=0
        def up(self):
            self.total=self.total+int(p.get())
        def uf(self):
            self.total=self.total+int(f.get())
        def uv(self):
            self.total=self.total+int(v.get())       
        def display(self):
            totalbill = "Total :    "+str(self.total)+" Rs"
            textField=Text(pizza_p,height=1,width=18,borderwidth=0,font=("Sans-Serif",12),cursor="arrow")
            textField.place(x=880,y=620)
            textField.configure(state='normal')
            textField.insert(END,totalbill)
            textField.configure(state='disabled')
        
        def displayBill(self,pizzaVal,val):
            if self.bill==0:
                self.bill=pizzaVal+"                  "+str(val)+"Rs" +'\n'
            else:
                self.bill =str(self.bill) + pizzaVal+"                  "+str(val)+"Rs" +'\n'
            textFieldBill =Text(pizza_p,height=8,width=25,font=("Sans-Serif",12),borderwidth=0,cursor="arrow")
            textFieldBill.place(x=880,y=450)
            textFieldBill.configure(state='normal')
            textFieldBill.insert(END,self.bill) 
            textFieldBill.configure(state='disabled')   

    #-----------creating instance of totaling---------
    ob2=totaling
    #---------order button on clink functions------
    def callp(event,ob1):
            ob1.up(ob1)
            ob1.display(ob1)
            ob1.displayBill(ob1,'peppy-paneer',p.get())
            y=time.time()
            pizzaType=p.get()
            if pizzaType =='90':
                piz_id = 1
            elif pizzaType =='150':
                piz_id=2
            elif pizzaType =='300':
                piz_id = 3
            us=r[0]
            pointer.execute("insert into orders(u_id,p_id,time) values(?,?,?)",(us,piz_id,y,) )

    def callf(event,ob1):
            ob1.uf(ob1)
            ob1.display(ob1)
            ob1.displayBill(ob1,'Five-Pepper     ',f.get())
            y=time.time()
            pizzaType=f.get()
            if pizzaType =='120':
                piz_id = 4
            elif pizzaType =='300':
                piz_id=5
            elif pizzaType =='450':
                piz_id = 6
            us=r[0]
            pointer.execute("insert into orders(u_id,p_id,time) values(?,?,?)",(us,piz_id,y,) )

    def callv(event,ob1):
            ob1.uv(ob1)
            ob1.display(ob1)
            ob1.displayBill(ob1,'Veg-Extra         ',v.get())
            y=time.time()
            pizzaType=v.get()
            if pizzaType =='200':
                piz_id = 7
            elif pizzaType =='300':
                piz_id=8
            elif pizzaType =='450':
                piz_id = 9
            us=r[0]
            pointer.execute("insert into orders(u_id,p_id,time) values(?,?,?)",(us,piz_id,y,) )

    #------------------check out Butoon function-----------------
    def checkOut(Event):
        tkinter.messagebox.showinfo("Check Out","Order placed..!! Hope you enjoy your pizza")
        db.commit()
    #-------------------------------------------Pizzas Card--------
    pizzaList = [r"p1.png",r"p2.png",r"p3.png"]
    p =StringVar()
    p.set(150) # initialize
    f =StringVar()
    f.set(300) 
    v =StringVar()
    v.set(200) 

    # ------------P1 Card---------
    pizzaImage =PhotoImage(file=pizzaList[0])     
    p1 =Label(pizza_p,image=pizzaImage,borderwidth=0,bg="#e4e4e4")
    p1.grid(row=0,column=1,padx=90,pady=20)
    #------radiobutton for P1-----
    radioLabel=Label(pizza_p,borderwidth=0,bg="#ffffff")
    radioLabel.place(x=155,y=250)
    a=Radiobutton(radioLabel,text="S",variable=p,value=90,bg="#ffffff")
    a.pack(side="left",padx=2)
    b=Radiobutton(radioLabel,text="M",variable=p,value=150,bg="#ffffff")
    b.pack(side="left",padx=4)
    c=Radiobutton(radioLabel,text="L",variable=p,value=300,bg="#ffffff")
    c.pack(side="left",padx=2)
    #------------check 1 button----------------
    check1 =PhotoImage(file="check.png")
    check1Label =Label(pizza_p,image=check1,borderwidth=0,width=40,height=40,bg="#ffffff")
    check1Label.bind("<Button-1>",Checkclick1)  #checkBox1--
    check1Label.place(x=285,y=246)
    #--------------OrderButton----------------
    order1 =PhotoImage(file="order.png")
    buttonOrder1 =Button(pizza_p,image=order1,borderwidth=0,bg="#ffffff",activebackground="#ffffff")
    buttonOrder1.bind("<Button-1>",lambda event,arg=ob2: callp(event,arg))
    buttonOrder1.place(x=155,y=312)

    # ------------P2 Card---------
    pizzaImage2 =PhotoImage(file=pizzaList[1])     
    p2 =Label(pizza_p,image=pizzaImage2,borderwidth=0,bg="#e4e4e4")
    p2.grid(row=0,column=2,padx=40,pady=20)
    #------radiobutton for P2-----
    radioLabel=Label(pizza_p,borderwidth=0,bg="#ffffff")
    radioLabel.place(x=545,y=250)
    d=Radiobutton(radioLabel,text="S",variable=f,value=120,bg="#ffffff")
    d.pack(side="left",padx=2)
    e=Radiobutton(radioLabel,text="M",variable=f,value=300,bg="#ffffff")
    e.pack(side="left",padx=4)
    g=Radiobutton(radioLabel,text="L",variable=f,value=450,bg="#ffffff")
    g.pack(side="left",padx=2)
    #------------check 2 button----------------
    check2Label =Label(pizza_p,image=check1,borderwidth=0,width=40,height=40,bg="#ffffff")
    check2Label.bind("<Button-1>",Checkclick2)  #checkBox2--
    check2Label.place(x=670,y=246)
    #------------order Button-------------------
    buttonOrder2 =Button(pizza_p,image=order1,borderwidth=0,bg="#ffffff",activebackground="#ffffff")   
    buttonOrder2.bind("<Button-1>",lambda event,arg=ob2: callf(event,arg))
    buttonOrder2.place(x=550,y=312)

    # ------------P3 Card---------
    pizzaImage3 =PhotoImage(file=pizzaList[2])     
    p3 =Label(pizza_p,image=pizzaImage3,borderwidth=0,bg="#e4e4e4")
    p3.grid(row=0,column=3,padx=90,pady=20)
    #------radiobutton for P3-----
    radioLabel=Label(pizza_p,borderwidth=0,bg="#ffffff")
    radioLabel.place(x=935,y=250)
    h=Radiobutton(radioLabel,text="S",variable=v,value=200,bg="#ffffff")
    h.pack(side="left",padx=2)
    i=Radiobutton(radioLabel,text="M",variable=v,value=300,bg="#ffffff")
    i.pack(side="left",padx=4)
    j=Radiobutton(radioLabel,text="L",variable=v,value=450,bg="#ffffff")
    j.pack(side="left",padx=2)
    #------------check 3 button----------------
    check3Label =Label(pizza_p,image=check1,borderwidth=0,width=40,height=40,bg="#ffffff")
    check3Label.bind("<Button-1>",Checkclick3)  #checkBox3--
    check3Label.place(x=1060,y=246)
    #------------order Button-------------------
    buttonOrder3 = Button(pizza_p,image=order1,borderwidth=0,bg="#ffffff",activebackground="#ffffff")  
    buttonOrder3.bind("<Button-1>",lambda event,arg=ob2: callv(event,arg))
    buttonOrder3.place(x=935,y=312)

    #----------------------Back Button-------
    backImage=PhotoImage(file="back.png")
    backButton=Button(pizza_p,image=backImage,borderwidth=0,activebackground="#f2f2f2")
    backButton.bind("<Button-1>",lambda event,arg='order',arg2=r : callprofilepage(event,arg,arg2))
    backButton.place(x=80,y=400)
    #----------------------bill Card-----------
    billImage =PhotoImage(file="bill.png")
    billLabel =Label(pizza_p,image=billImage,borderwidth=0)
    billLabel.place(x=850,y=400)


    #------------------checkoutButon---------------
    checkButton =PhotoImage(file="checkout.png")
    checkOutButtButton =Button(pizza_p,image=checkButton,bg="#ffffff",activebackground="#ffffff",borderwidth=0)
    checkOutButtButton.bind("<Button-1>",checkOut)#lambda event,arg='order': callprofilepage(event,arg))
    checkOutButtButton.place(x=930,y=660)
        
    # ------------------advertisement------------
    pepsiAdd =PhotoImage(file="pepsiAdd1.png")
    pepsiAddLabel =Label(pizza_p,image=pepsiAdd)
    pepsiAddLabel.place(x="100",y="490")

    pizza_p.mainloop()


    #---------------pizza database-----------

#=============track==page====
def trackpage(event,r):
    profile_p.withdraw()
    profile_p.destroy()
    global track_p
    track_p=Toplevel()
    track_p.title("Track")
    track_p.geometry("1200x740")
    track_p.config(bg="#ffffff")
    x=time.time()
    #------Background image------
    bgTrackImage=PhotoImage(file="trackImg.png")
    bgTrackImageLabel =Label(track_p,image=bgTrackImage,borderwidth=0)
    bgTrackImageLabel.pack(fill="both")
    #==========backButton----
    backImage=PhotoImage(file="back.png")
    backButton=Button(track_p,image=backImage,borderwidth=0,activebackground="#f2f2f2",bg="#fff")
    backButton.bind("<Button-1>",lambda event,arg='track',arg2=r : callprofilepage(event,arg,arg2))
    backButton.place(x=80,y=40)
    #----------time------
    pointer.execute("select * from orders where u_id=?",(r[0],))
    timevalrow=pointer.fetchone()
    if timevalrow is not None:
        timeval=timevalrow[3]
        print(timeval)    
        print(x)
        z=x-timeval    
        if z<6000:
            timeText="Your order is on our list"+'\n'+'will be delivered in 25 min'
        elif z<12000:
            timeText="Your order is on delivery"+'\n'+'will be delivered in 10 min'
        elif z<18000:
            timeText="your order will be delivered in few minutes"
        else:
            timeText="Order Deivered !!"

    else:
        timeText="NO orders to be delivered"
    displayTimeText=Text(track_p,height=4,width=38,bg="#fff",borderwidth=0,font=("Sans-Serif",18),cursor="arrow")
    displayTimeText.place(x=480,y=300)
    displayTimeText.configure(state='normal')
    displayTimeText.insert(END,timeText)
    displayTimeText.configure(state='disabled')

    track_p.mainloop()


loginpage()
# pointer.execute("delete from users where u_id= 2 or u_id=3")
# trackpage()
# pointer.execute("drop table users")
# pointer.execute("drop table orders")
# db.commit()
# pointer.execute("create table pizzas(p_id INTEGER PRIMARY KEY AUTOINCREMENT,pizzaName varchar,cost int) ")
# pointer.execute("insert into pizzas(pizzaName,cost) values('PeppyPaneer S',90)")
# pointer.execute("insert into pizzas(pizzaName,cost) values('PeppyPaneer M',150)")
# pointer.execute("insert into pizzas(pizzaName,cost) values('PeppyPaneer L',300)")
# pointer.execute("insert into pizzas(pizzaName,cost) values('Five-Pepper S',120)")
# pointer.execute("insert into pizzas(pizzaName,cost) values('Five-Pepper M',300)")
# pointer.execute("insert into pizzas(pizzaName,cost) values('Five-Pepper L',450)")
# pointer.execute("insert into pizzas(pizzaName,cost) values('Veg-Extra S',200)")
# pointer.execute("insert into pizzas(pizzaName,cost) values('Veg-Extra M',300)")
# pointer.execute("insert into pizzas(pizzaName,cost) values('Veg-Extra L',450)")
# db.commit()
# pointer.execute("select * from orders")
# x=pointer.fetchall()
# for d in x:
#     print('\n',d)
#----------------------order table-----------
# pointer.execute("create table orders(order_id INTEGER PRIMARY KEY AUTOINCREMENT,u_id integer,p_id integer,time float, FOREIGN KEY(p_id) REFERENCES pizzas(p_id),FOREIGN KEY(u_id) REFERENCES users(u_id) )")
# db.commit()
# pointer.execute("drop table orders")
# db.commit()
#-------------------------------------------------------------------------------------------
# pointer.execute("drop table orders")
# db.commit()
# pointer.execute("select * from orders")
# x=pointer.fetchall()
# print(x)
# pointer.execute("delete from orders where u_id=2")
# db.commit()

# pointer.execute("drop table users")
# pointer.execute("drop table orders")
# db.commit()