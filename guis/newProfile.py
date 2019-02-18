import tkinter as tk
# import Pizzas as p1
root=tk.Tk()
root.title("Profile")
root.geometry("1200x740")
root.config(bg="#F2F2F2")

#-----------------Hero Image------------
hero = tk.PhotoImage(file="F:/projects/PDS/images/PIZZAS3.png")
heroLabel = tk.Label(root,image = hero,borderwidth=0)
heroLabel.pack(side="top",fill="both")

#----------------Profilecard----------------
profileFrame = tk.Frame(root,height="230",width="280",bg="#ffffff")
profileFrame.place(x=80,y=454)

#-----------------ProfileCardImage-----------
profileImage = tk.PhotoImage(file="F:/projects/PDS/images/face.png")
profileLabel = tk.Label(root,image=profileImage,borderwidth=0,bg="#f2f2f2")
profileLabel.place(x=80,y=350)

#---------------- Orders-------------
orders = tk.Frame(root,height="320",width="600",bg="#ffffff")
orders.place(x=440,y=364)

#----------order Border---------------
orderBorImage = tk.PhotoImage(file="F:/projects/PDS/images/orderBorder.png")
borderImageLabel = tk.Label(root,image=orderBorImage,borderwidth=0)
borderImageLabel.place(x=440,y=364)
#-----------track button--------------
trackImage = tk.PhotoImage(file="F:/projects/PDS/images/track.png")
trackImageLabel = tk.Label(root,image=trackImage,borderwidth=0)
trackImageLabel.place(x=1105,y=485)
#-----------------add button------------


# def temp():
#     p1.run(root)


addImage = tk.PhotoImage(file="F:/projects/PDS/images/add1.png")
addImageLabel = tk.Label(root,image=addImage,borderwidth=0)  #command=temp
addImageLabel.place(x=1080,y=585)
# def run():
#     root.mainloop()



root.mainloop()