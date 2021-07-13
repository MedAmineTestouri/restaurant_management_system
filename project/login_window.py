from tkinter import *
from tkinter import messagebox
import random
import time
#==================================================================================================
                                            #login window#
#=====================================================================================================

#=============================Time====================================================================
localtime=time.asctime(time.localtime(time.time()))
#===============================login window configuration==============================================
login = Tk()
login.geometry("1366x768+0+0")
login.title("Login Restaurant Management System")
sarah = "sarah"
mdp1 = "sarah"
testouri = "testouri"
mdp2 = "testouri"
amira="amira"
mdp3="amira"

#========================= window configuration ==========================================
Topss = Frame(login,width = 1366 ,height=50, bg="powder blue" , relief=SUNKEN )
Topss.pack(side=TOP)


f11 = Frame(login,width = 768 ,height=700,bg="#ffffff" , relief=SUNKEN )
f11.pack(side=LEFT)
#=============================================================================================

User = StringVar()
MDP = StringVar()
Exit = StringVar()
Submit = StringVar()
#=================================Title login window============================================
lblInfo = Label(Topss,font=('lato',50,'bold','italic'),text="Login Restaurant Management Systems",fg="Steel Blue",bd=10,anchor='w')
lblInfo.grid(row=0,column=0)
lblInfo = Label(Topss,font=('lato',17,'bold','italic'),text=localtime,fg="Steel Blue",bd=5,anchor='w')
lblInfo.grid(row=1,column=0)
#=================================user field=======================================
lblUser = Label(f11,font=('arial',20,'bold'), text = "User Name",bd=1 , anchor="w")
lblUser.grid(row=1,column=1)
txtUser=Entry(f11,font=('arial',20,'bold'), textvariable=User,bd=1 , insertwidth=4,
bg="powder blue",justify='right')
txtUser.grid(row=1,column=2)

    
#==================================password field==============================


lblMDP = Label(f11,font=('arial',20,'bold'), text = "Password",bd=1 , anchor="w")
lblMDP.grid(row=2,column=1)
txtMDP=Entry(f11,font=('arial',20,'bold'), textvariable=MDP,bd=1 , insertwidth=4,
bg="powder blue",justify='right',show='*')
txtMDP.grid(row=2,column=2)
#====================================Buttons ( submit & Exit )===========================================
def Exit():
    login.destroy()

    
def Submit():
    user=txtUser.get()
    passwd = txtMDP.get()
    if (user == sarah) and (mdp1 == passwd):
        print('yes')
        messagebox.showinfo("Welcome sarah","welcome sarah and have a nice day !")
        login.destroy()
        import Restooo.py
    elif (user == testouri) and (mdp2 == passwd):
        print('yes')
        messagebox.showinfo("Welcome testouri","welcome testouri and have a nice day !")
        login.destroy()
        import Restooo.py
    elif (user == amira) and (mdp3 == passwd):
        print('yes')
        messagebox.showinfo("Welcome amira","welcome amira and have a nice day !")
        login.destroy()
        import Restooo.py
    else :
        messagebox.showwarning("Warning","Password or User Name is Incorrect Please Try Again :D !!!")
        
        
btnExitt=Button(f11,padx=12 , pady=5,bd=3,fg='red',font=('arial',9,'bold'),width=6,
                    text="EXIT" , bg="powder blue" , command = Exit).grid(row=3,column=2)
btnSub=Button(f11,padx=12 , pady=5,bd=3,fg='green',font=('arial',9,'bold'),width=6,
                    text="SUBMIT" , bg="powder blue" , command = Submit).grid(row=3,column=3)


login.mainloop()

