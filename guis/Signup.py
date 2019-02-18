import tkinter as tk
import tkinter.messagebox
import sqlite3
root=tk.Tk()
root.config(bg="#fff")
root.geometry("1200x740")

#--------------Database---------
db=sqlite3.connect("pizzadb.db")
pointer=db.cursor()
def clickSignup():
    usn=usernamesignEntry.get()
    psn=phoneNumEntry.get()
    for ads in addressEntry:
        ads=ads+addressEntry.get(0,END)
    pas=signPasswordEntry.get()
    cpass=signConfirmPasswordEntry.get()
    if(pas==cpass):
        pointer.execute("insert into users values(?,?,?,?)",(usn,psn,ads,pas))
    else:
        tkinter.messagebox.showerror("wrong attempt","your password didn't match ")





#------------------functions----------




#-----------background---------------
bgImage=tk.PhotoImage(file="F:/projects/PDS/images/signup.png")
bgImageLabel = tk.Label(root,image=bgImage,borderwidth=0)
bgImageLabel.pack(fill="both")

#--------------Signup Label-------
loginAsk = tk.Label(root,text="Sign Up",font=("Sans-Serif",16),fg="#ff1744",bg="#fff")
loginAsk.place(x=740,y=100)
#--------------username---------
usernamesignFrame = tk.Frame(root,bg="#fff",borderwidth=2)
usernamesignFrame.place(x=600,y=160)  #pack(side="top",padx=20,pady=10)
usernamesignLabel = tk.Label(usernamesignFrame,text="Username :",font=("Sans-Serif",12),fg="#000",bg="#fff")
usernamesignLabel.pack(side="left")
usernamesignEntry = tk.Entry(usernamesignFrame,width=28)
usernamesignEntry.pack(side="right",padx=64)

#-----------phone number-----------
phoneNumFrame = tk.Frame(root,bg="#fff",borderwidth=2)
phoneNumFrame.place(x=600,y=200)  #pack(side="top",padx=20,pady=10)
phoneNumLabel = tk.Label(phoneNumFrame,text="Phone Number :",font=("Sans-Serif",12),fg="#000",bg="#fff")
phoneNumLabel.pack(side="left")
phoneNumEntry = tk.Entry(phoneNumFrame,width=28)
phoneNumEntry.pack(side="right",padx=32)

# #-----------Address---------------
addressFrame = tk.Frame(root,bg="#fff",borderwidth=2)
addressFrame.place(x=600,y=240)   #pack(side="top",padx=20,pady=10)
addressLabel = tk.Label(addressFrame,text="address :",font=("Sans-Serif",12),fg="#000",bg="#fff")
addressLabel.place(x=0,y=0)
addressEntry = tk.Text(addressFrame,width=28,height=8)
addressEntry.pack(side="right",padx=150)
#-----------password----------
signPasswordFrame = tk.Frame(root,bg="#fff",borderwidth=2)
signPasswordFrame.place(x=600,y=390)  #pack(side="top",padx=20,pady=10)
signPasswordLabel = tk.Label(signPasswordFrame,text="Password :",font=("Sans-Serif",12),fg="#000",bg="#fff")
signPasswordLabel.pack(side="left")
signPasswordEntry = tk.Entry(signPasswordFrame,width=28,show="*️⃣")
signPasswordEntry.pack(side="right",padx=68)

# #-----------password----------
signConfirmPasswordFrame = tk.Frame(root,bg="#fff",borderwidth=2)
signConfirmPasswordFrame.place(x=600,y=430)
signConfirmPasswordLabel = tk.Label(signConfirmPasswordFrame,text="Confirm password :",font=("Sans-Serif",12),fg="#000",bg="#fff")
signConfirmPasswordLabel.pack(side="left")
signConfirmPasswordEntry = tk.Entry(signConfirmPasswordFrame,width=28,show="*️⃣")
signConfirmPasswordEntry.pack(side="right",padx=10)

#--------------aks login-----------
loginAsk = tk.Label(root,text="Already registered..? Login",font=("Sans-Serif",10),fg="blue",bg="#fff")
loginAsk.place(x=680,y=470)



# #---------------button--------
signupButtonImage = tk.PhotoImage(file="F:/projects/PDS/images/signupButton.png")
signupButton = tk.Button(root,image=signupButtonImage,bg="#fff",borderwidth=0,activebackground="#ffffff",command=clickSignup)
signupButton.place(x=700,y=510)   #pack(side="bottom")





root.mainloop()