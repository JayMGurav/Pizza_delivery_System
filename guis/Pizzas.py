import tkinter as tk
# import time
root=tk.Tk()
root.title("Pizzas")
root.geometry("1200x740")
root.config(bg="#f2f2f2")
#----------------------------------------------functions------------------------------------
#------------check functions-----
def Checkclick1(event):
    prs=str(p.get())
    amount= "Now at "+prs+" Rs only!"
    textField=tk.Text(root,height=1,width=18,borderwidth=0,font=("Sans-Serif",12))
    textField.place(x=150,y=284)
    textField.insert(tk.END,amount)

def Checkclick2(event):
    frs=str(f.get())
    amount= "Now at "+frs+" Rs only!"
    textField=tk.Text(root,height=1,width=18,borderwidth=0,font=("Sans-Serif",12))
    textField.place(x=545,y=284)
    textField.insert(tk.END,amount)

def Checkclick3(event):
    vrs=str(v.get())
    amount= "Now at "+vrs+" Rs only!"
    textField=tk.Text(root,height=1,width=18,borderwidth=0,font=("Sans-Serif",12))
    textField.place(x=930,y=284)
    textField.insert(tk.END,amount)



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
        textField=tk.Text(root,height=1,width=18,borderwidth=0,font=("Sans-Serif",12))
        textField.place(x=880,y=620)
        textField.insert(tk.END,totalbill)
    
    def displayBill(self,pizzaVal,val):
        self.bill =str(self.bill) + pizzaVal+"                  "+str(val)+"Rs" +'\n'
        textFieldBill =tk.Text(root,height=8,width=25,font=("Sans-Serif",12),borderwidth=0)
        textFieldBill.place(x=880,y=450)
        textFieldBill.insert(tk.END,self.bill)
       
    


#-----------creating instance of totaling---------

ob2=totaling
#---------order button on clink functions------
def callp(event,ob1):
        ob1.up(ob1)
        ob1.display(ob1)
        ob1.displayBill(ob1,'peppy-paneer',p.get())

def callf(event,ob1):
        ob1.uf(ob1)
        ob1.display(ob1)
        ob1.displayBill(ob1,'Five-Pepper     ',f.get())

def callv(event,ob1):
        ob1.uv(ob1)
        ob1.display(ob1)
        ob1.displayBill(ob1,'Veg-Extra         ',v.get())

#-------------------------------------------Pizzas Card--------
pizzaList = [r"F:/projects/PDS/images/p1.png",r"F:/projects/PDS/images/p2.png",r"F:/projects/PDS/images/p3.png"]
p = tk.StringVar()
p.set(150) # initialize
f = tk.StringVar()
f.set(300) 
v = tk.StringVar()
v.set(200) 

# ------------P1 Card---------
pizzaImage = tk.PhotoImage(file=pizzaList[0])     
p1 = tk.Label(root,image=pizzaImage,borderwidth=0,bg="#e4e4e4")
p1.grid(row=0,column=1,padx=90,pady=20)
#------radiobutton for P1-----
radioLabel=tk.Label(root,borderwidth=0,bg="#ffffff")
radioLabel.place(x=155,y=250)
a=tk.Radiobutton(radioLabel,text="S",variable=p,value=90,bg="#ffffff")
a.pack(side="left",padx=2)
b=tk.Radiobutton(radioLabel,text="M",variable=p,value=150,bg="#ffffff")
b.pack(side="left",padx=4)
c=tk.Radiobutton(radioLabel,text="L",variable=p,value=300,bg="#ffffff")
c.pack(side="left",padx=2)
#------------check 1 button----------------
check1 = tk.PhotoImage(file="F:/projects/PDS/images/check.png")
check1Label = tk.Label(root,image=check1,borderwidth=0,width=40,height=40,bg="#ffffff")
check1Label.bind("<Button-1>",Checkclick1)  #checkBox1--
check1Label.place(x=285,y=246)
#--------------OrderButton----------------
order1 = tk.PhotoImage(file="F:/projects/PDS/images/order.png")
buttonOrder1 = tk.Button(root,image=order1,borderwidth=0,bg="#ffffff",activebackground="#ffffff")
buttonOrder1.bind("<Button-1>",lambda event,arg=ob2: callp(event,arg))
buttonOrder1.place(x=155,y=312)

# buttonOrder1.



# ------------P2 Card---------
pizzaImage2 = tk.PhotoImage(file=pizzaList[1])     
p2 = tk.Label(root,image=pizzaImage2,borderwidth=0,bg="#e4e4e4")
p2.grid(row=0,column=2,padx=40,pady=20)
#------radiobutton for P2-----
radioLabel=tk.Label(root,borderwidth=0,bg="#ffffff")
radioLabel.place(x=545,y=250)
d=tk.Radiobutton(radioLabel,text="S",variable=f,value=120,bg="#ffffff")
d.pack(side="left",padx=2)
e=tk.Radiobutton(radioLabel,text="M",variable=f,value=300,bg="#ffffff")
e.pack(side="left",padx=4)
g=tk.Radiobutton(radioLabel,text="L",variable=f,value=450,bg="#ffffff")
g.pack(side="left",padx=2)
#------------check 2 button----------------
check2Label = tk.Label(root,image=check1,borderwidth=0,width=40,height=40,bg="#ffffff")
check2Label.bind("<Button-1>",Checkclick2)  #checkBox2--
check2Label.place(x=670,y=246)
#------------order Button-------------------
buttonOrder2 = tk.Button(root,image=order1,borderwidth=0,bg="#ffffff",activebackground="#ffffff")   
buttonOrder2.bind("<Button-1>",lambda event,arg=ob2: callf(event,arg))
buttonOrder2.place(x=550,y=312)





# ------------P3 Card---------
pizzaImage3 = tk.PhotoImage(file=pizzaList[2])     
p3 = tk.Label(root,image=pizzaImage3,borderwidth=0,bg="#e4e4e4")
p3.grid(row=0,column=3,padx=90,pady=20)
#------radiobutton for P3-----
radioLabel=tk.Label(root,borderwidth=0,bg="#ffffff")
radioLabel.place(x=935,y=250)
h=tk.Radiobutton(radioLabel,text="S",variable=v,value=200,bg="#ffffff")
h.pack(side="left",padx=2)
i=tk.Radiobutton(radioLabel,text="M",variable=v,value=300,bg="#ffffff")
i.pack(side="left",padx=4)
j=tk.Radiobutton(radioLabel,text="L",variable=v,value=450,bg="#ffffff")
j.pack(side="left",padx=2)
#------------check 3 button----------------
check3Label = tk.Label(root,image=check1,borderwidth=0,width=40,height=40,bg="#ffffff")
check3Label.bind("<Button-1>",Checkclick3)  #checkBox3--
check3Label.place(x=1060,y=246)
#------------order Button-------------------
buttonOrder3 = tk.Button(root,image=order1,borderwidth=0,bg="#ffffff",activebackground="#ffffff")  
buttonOrder3.bind("<Button-1>",lambda event,arg=ob2: callv(event,arg))
buttonOrder3.place(x=935,y=312)



#----------------------bill Card-----------
billImage = tk.PhotoImage(file="F:/projects/PDS/images/bill.png")
billLabel = tk.Label(root,image=billImage,borderwidth=0)
billLabel.place(x=850,y=400)


#------------------checkoutButon---------------
checkButton = tk.PhotoImage(file="F:/projects/PDS/images/checkout.png")
checkOutButtLabel = tk.Button(root,image=checkButton,bg="#ffffff",activebackground="#ffffff")
checkOutButtLabel.place(x=930,y=660)
    
# ------------------advertisement------------
# addImages=["F:/projects/PDS/images/pepsiAdd1.png","F:/projects/PDS/images/pizzaAdd2.png","F:/projects/PDS/images/pizzaAdd3.png","F:/projects/PDS/images/pizzaAdd4.png"]
# # while(1):
# for i in range(3):
pepsiAdd = tk.PhotoImage(file="F:/projects/PDS/images/pepsiAdd1.png")
pepsiAddLabel = tk.Label(root,image=pepsiAdd)
pepsiAddLabel.place(x="120",y="500")
    # if(i==2):
    #     i=0
    # time.sleep(2)






root.mainloop()