import tkinter as tk
import tkinter.messagebox
import sqlite3 
root=tk.Tk()
root.title("Pizzas")
root.geometry("1200x740")
root.config(bg="#ffffff")
#------------------entry restrict------
var = tk.StringVar()
max_len = 9
def on_write(*args):
    s = var.get()
    if len(s) > max_len:
        var.set(s[:max_len])
var.trace_variable("w", on_write)
#---------------DAtabase-----------
db=sqlite3.connect("pizzadb.db")
pointer=db.cursor()
# pointer.execute("create table users(username varchar,phoneNumber int,address varchar,password varchar)")
# pointer.execute("insert into users values('Jay',8762290119,'punjab LPU','12345678')")
# db.commit()
def login1(event):
    userGname=userName.get()
    passGword=password.get()
    pointer.execute("select * from users where username=? and password=? ",(userGname,passGword,))
    r=pointer.fetchone()
    if r is not None:
        print('wow!! you just loged in')
    else:
        tkinter.messagebox.showerror("Data not found","wrong Username or Password, Please enter correct details")
        




    



#---------------background Frame----------
rootImage = tk.PhotoImage(file="F:/projects/PDS/images/loginBack.png")
rootFrame = tk.Label(root,image=rootImage,borderwidth=0)
rootFrame.pack(fill="both")

#--------------entry for login details---------
loginFrame = tk.Frame(root,bg="#ffffff")
loginFrame.place(x=640,y=280)
loginFrame.config(highlightbackground="#ff1744",highlightthickness=2)
#--------------username---------
userNameFrame = tk.Frame(loginFrame,bg="#fff",borderwidth=2)
userNameFrame.pack(side="top",padx=10,pady=28)
userNameLabel = tk.Label(userNameFrame,text="User name :",width=10,font=("Sans-Serif",12),fg="#ff1744",bg="#fff")
userNameLabel.pack(side="left",padx=16)
userName = tk.Entry(userNameFrame,width=28)
userName.pack(side="right",padx=4)
#--------------password--------
passwordFrame = tk.Frame(loginFrame,bg="#fff",borderwidth=2)
passwordFrame.pack(side="top",padx=10,pady=0)
passwordLabel = tk.Label(passwordFrame,text="Password :",width=10,font=("Sans-Serif",12),fg="#ff1744",bg="#fff")
passwordLabel.pack(side="left",padx=16)
password = tk.Entry(passwordFrame,width=28,show="*️⃣",textvariable=var)
password.pack(side="right",padx=4)
#-----------Sign Up link-------------
signUpLink = tk.Label(loginFrame,text="Not yet Registered..? Sign-Up ",font=("Sans-Serif",10),fg="blue",bg="#fff")
signUpLink.pack(side="top",pady=8)


#----------------login Button------
login=tk.PhotoImage(file="F:/projects/PDS/images/loginButton.png")
loginButton = tk.Button(loginFrame,image=login,borderwidth=0,bg="#ffffff",height=40,activebackground="#ffffff")
loginButton.bind("<Button-1>",login1)
loginButton.pack(side="bottom",pady=28)

root.mainloop()