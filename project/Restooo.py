from tkinter import *
from tkinter import messagebox
import random 
import time



#=====================================================================================================

#==================================================================================================
                                        #Menue Window#
#=====================================================================================================

#======================================================================================================

root = Tk()
root.geometry("1366x768+0+0")
root.title("Resto Management System")


#==========================================================
text_input=StringVar()
operator=""
Les_commandes = {}


#====================================================================
Tops = Frame(root,width = 1366 ,height=50, bg="powder blue" , relief=SUNKEN )
Tops.pack(side=TOP)

f1 = Frame(root,width = 768 ,height=700, relief=SUNKEN )
f1.pack(side=LEFT)

f2 = Frame(root,width = 300 ,height=700, bg="powder blue" , relief=SUNKEN )
f2.pack(side=RIGHT)
#=============================Time============================
localtime=time.asctime(time.localtime(time.time()))

#=============================Info============================
lblInfo = Label(Tops,font=('lato',50,'bold','italic'),text="Restaurant Management Systems",fg="Steel Blue",bd=10,anchor='w')
lblInfo.grid(row=0,column=0)
lblInfo = Label(Tops,font=('lato',17,'bold','italic'),text=localtime,fg="Steel Blue",bd=5,anchor='w')
lblInfo.grid(row=1,column=0)
#=============================Calculator=========================
def btnClick(numbers):
    global operator
    operator=operator + str(numbers)
    text_input.set(operator)
def btnClearDisplay():
    global operator
    operator=""
    text_input.set('')

def btnEqualsInput():
    global operator
    sumup=str(eval(operator))
    text_input.set(sumup)
    operator=""

def Ref():
    global refacture
    x = random.randint(12908,525986)
    randomRef = str(x)
    rand.set(randomRef)
    refacture=randomRef
    print(refacture)
    
 
    Coef_of_Escalope = float(Escalope_grie.get() or "0")
    Coef_of_Suplement = float(Suplement.get()or "0")
    Coef_of_filet = float(filet_boeuf.get()or "0")
    Coef_of_patte = float(patte.get()or "0")
    Coef_of_poulet = float(poulet.get()or "0")
    Coef_of_fruit_de_mer= float(fruit_de_mer.get()or "0")
    Coef_of_Special_chef1= float(Special_chef1.get()or "0")
    Coef_of_Special_chef2 = float(Special_chef2.get()or "0")
    Coef_of_Special_chef3 = float(Special_chef3.get()or "0")
    Coef_of_Drinks = float(Drinks.get()or "0")
    Coef_of_Water = float(Water.get()or "0")
    Coef_of_Salad = float(Salad.get()or "0")

    

    Les_commandes["cost_of_Escalope_grie"] = Coef_of_Escalope * 16.600
    Les_commandes["cost_of_Suplement"] = Coef_of_Suplement * 3.300
    Les_commandes["cost_of_filet_boeuf"] = Coef_of_filet * 23.700
    Les_commandes["cost_of_patte"] = Coef_of_patte * 8.200
    Les_commandes["cost_of_poulet"] = Coef_of_poulet * 7.700
    Les_commandes["cost_of_fruit_de_mer"]= Coef_of_fruit_de_mer * 12.800
    Les_commandes["cost_of_Special_chef1"] = Coef_of_Special_chef1 * 52.500
    Les_commandes["cost_of_Special_chef2"] = Coef_of_Special_chef2 * 48.400
    Les_commandes["cost_of_Special_chef3"] = Coef_of_Special_chef3 * 37.400
    Les_commandes["cost_of_Drinks"] = Coef_of_Drinks * 3500
    Les_commandes["cost_of_Water"] = Coef_of_Water * 2000
    Les_commandes["cost_of_Salad"] = Coef_of_Salad * 9700
    print(Les_commandes)
    
    

    cost=(Les_commandes.get("cost_of_Escalope_grie") + Les_commandes.get("cost_of_Suplement") + Les_commandes.get("cost_of_filet_boeuf") + Les_commandes.get("cost_of_patte") +
                                                                                                                                                     
         Les_commandes.get("cost_of_fruit_de_mer") + Les_commandes.get("cost_of_Special_chef1") +Les_commandes.get("cost_of_Special_chef2") +
        Les_commandes.get("cost_of_Special_chef3") +Les_commandes.get("cost_of_Drinks") + Les_commandes.get("cost_of_Water") + Les_commandes.get("cost_of_Salad"))
                                     
    
    Ser = 3
    
    costof_Meal = "DT",str('%.2f' % (cost))
    
    Service_cost = "DT",str('%.2f' % 3)
                           
    Total_cost =  "DT",str('%.2f' % (cost + Ser  ))

    Cost.set(costof_Meal)
    Service.set(Service_cost)
    SubTotal.set(Total_cost)
    
                           
    return refacture
    

def qExit():
    root.destroy()

def Reset():
    rand.set("") 
    Escalope_grie.set("")
    Suplement.set("")
    filet_boeuf.set("")
    patte.set("")
    poulet.set("")
    fruit_de_mer.set("")
    Special_chef1.set("")
    Special_chef2.set("")
    Special_chef3.set("")
    Drinks.set("")
    Water.set("")
    Cost.set("")
    Service.set("")
    SubTotal.set("")
    Salad.set("")
def Save():
    texte=""
    
    for cle,valeur in Les_commandes.items():
        if (valeur!=0.0) :
            texte = texte , cle , valeur
    print(texte)
    f= open(str(refacture)+".txt","w+")
    f.write("reference facture  : "+str(refacture)+" \r\ndate facture : "+ localtime +"  "+"Les Commandes : "+ str(texte))
            
            
#====================================calculator=======================
    
    
txtDisplay = Entry(f2,font=('lato',20,'bold'),
                   textvariable=text_input,bd=30,insertwidth=4,bg="#e1d89f",justify='right')
txtDisplay.grid(columnspan=4)
#=====================================================
btn7=Button(f2,padx=16,pady=16,bd=8,fg="black",font=('arial',20,'bold'),
            text="7",bg="powder blue",
            command=lambda:btnClick(7)).grid(row=2,column=0)
btn8=Button(f2,padx=16,pady=16,bd=8,fg="black",font=('arial',20,'bold'),
            text="8",bg="powder blue",
            command=lambda:btnClick(8)).grid(row=2,column=1)
btn9=Button(f2,padx=16,pady=16,bd=8,fg="black",font=('arial',20,'bold'),
            text="9",bg="powder blue",
            command=lambda:btnClick(9)).grid(row=2,column=2)
Addition=Button(f2,padx=16,pady=16,bd=8,fg="black",font=('arial',20,'bold'),
            text="+",bg="powder blue",
            command=lambda:btnClick("+")).grid(row=2,column=3)
#========================================================
btn4=Button(f2,padx=16,pady=16,bd=8,fg="black",font=('arial',20,'bold'),
            text="4",bg="powder blue",
            command=lambda:btnClick(4)).grid(row=3,column=0)
btn5=Button(f2,padx=16,pady=16,bd=8,fg="black",font=('arial',20,'bold'),
            text="5",bg="powder blue",
            command=lambda:btnClick(5)).grid(row=3,column=1)
btn6=Button(f2,padx=16,pady=16,bd=8,fg="black",font=('arial',20,'bold'),
            text="6",bg="powder blue",
            command=lambda:btnClick(6)).grid(row=3,column=2)
Subtraction=Button(f2,padx=16,pady=16,bd=8,fg="black",font=('arial',20,'bold'),
            text="-",bg="powder blue",
            command=lambda:btnClick("-")).grid(row=3,column=3)
#====================================================================
btn1=Button(f2,padx=16,pady=16,bd=8,fg="black",font=('arial',20,'bold'),
            text="1",bg="powder blue",
            command=lambda:btnClick(1)).grid(row=4,column=0)
btn2=Button(f2,padx=16,pady=16,bd=8,fg="black",font=('arial',20,'bold'),
            text="2",bg="powder blue",
            command=lambda:btnClick(2)).grid(row=4,column=1)
btn3=Button(f2,padx=16,pady=16,bd=8,fg="black",font=('arial',20,'bold'),
            text="3",bg="powder blue",
            command=lambda:btnClick(3)).grid(row=4,column=2)
Multiply=Button(f2,padx=16,pady=16,bd=8,fg="black",font=('arial',20,'bold'),
            text="x",bg="powder blue",
            command=lambda:btnClick("*")).grid(row=4,column=3)
#=======================================================================
btn0=Button(f2,padx=16,pady=16,bd=8,fg="black",font=('arial',20,'bold'),
            text="0",bg="powder blue",
            command=lambda:btnClick(0)).grid(row=5,column=0)
btnClear=Button(f2,padx=16,pady=16,bd=8,fg="black",font=('arial',20,'bold'),
            text="c",bg="powder blue",
            command=lambda:btnClearDisplay()).grid(row=5,column=1)
btnEquals=Button(f2,padx=16,pady=16,bd=8,fg="black",font=('arial',20,'bold'),
            text="=",bg="powder blue",
            command=lambda:btnEqualsInput()).grid(row=5,column=2)
Division=Button(f2,padx=16,pady=16,bd=8,fg="black",font=('arial',20,'bold'),
            text="/",bg="powder blue",
            command=lambda:btnClick('/')).grid(row=5,column=3)
#===================================variables=======================================
rand = StringVar()
Escalope_grie = StringVar()
Suplement = StringVar()
filet_boeuf = StringVar()
patte = StringVar()
poulet = StringVar()
fruit_de_mer = StringVar()
Special_chef1 = StringVar()
Special_chef2 = StringVar()
Special_chef3 = StringVar()
Drinks = StringVar()
Water = StringVar()
Cost = StringVar()
Service = StringVar()
SubTotal = StringVar()
Salad = StringVar()
#===============================menue=================================
lblReference = Label(f1,font=('arial',13,'bold'), text = "Reference",bd=13 , anchor="w")
lblReference.grid(row=0,column=0)
txtReference=Entry(f1,font=('arial',13,'bold'), textvariable=rand,bd=13 , insertwidth=4,
                   bg="powder blue",justify='right')
txtReference.grid(row=0,column=1)
#====================================================================
lblPlat_Escalope_grie = Label(f1,font=('arial',13,'bold'), text = "Escalope grié",bd=13 , anchor="w")
lblPlat_Escalope_grie.grid(row=1,column=0)
txt_Escalope_grie=Entry(f1,font=('arial',13,'bold'), textvariable=Escalope_grie,bd=13 , insertwidth=4,
                   bg="powder blue",justify='right')
txt_Escalope_grie.grid(row=1,column=1)
#===========================================================================
lblPlat_Suplement = Label(f1,font=('arial',13,'bold'), text = "Suplement(frite,sauce,fromage)",bd=13 , anchor="w")
lblPlat_Suplement.grid(row=2,column=0)
txt_Suplement=Entry(f1,font=('arial',13,'bold'), textvariable=Suplement,bd=13 , insertwidth=4,
                   bg="powder blue",justify='right')
txt_Suplement.grid(row=2,column=1)
#===============================================================================
lblPlat_filet_boeuf = Label(f1,font=('arial',13,'bold'), text = "filet_boeuf",bd=13 , anchor="w")
lblPlat_filet_boeuf.grid(row=3,column=0)
txt_filet_boeuf=Entry(f1,font=('arial',13,'bold'), textvariable=filet_boeuf,bd=13 , insertwidth=4,
                   bg="powder blue",justify='right')
txt_filet_boeuf.grid(row=3,column=1)
#===============================================================================
lblPlat_patte = Label(f1,font=('arial',13,'bold'), text = "patte",bd=13 , anchor="w")
lblPlat_patte.grid(row=4,column=0)
txt_patte=Entry(f1,font=('arial',13,'bold'), textvariable=patte,bd=13 , insertwidth=4,
                   bg="powder blue",justify='right')
txt_patte.grid(row=4,column=1)
#================================================================================
lblPlat_poulet = Label(f1,font=('arial',13,'bold'), text = "poulet",bd=13 , anchor="w")
lblPlat_poulet.grid(row=5,column=0)
txt_poulet=Entry(f1,font=('arial',13,'bold'), textvariable=poulet,bd=13 , insertwidth=4,
                   bg="powder blue",justify='right')
txt_poulet.grid(row=5,column=1)
#==================================================================================
lblPlat_fruit_de_mer = Label(f1,font=('arial',13,'bold'), text = "fruit de mer",bd=13 , anchor="w")
lblPlat_fruit_de_mer.grid(row=6,column=0)
txt_fruit_de_mer=Entry(f1,font=('arial',13,'bold'), textvariable=fruit_de_mer,bd=13 , insertwidth=4,
                   bg="powder blue",justify='right')
txt_fruit_de_mer.grid(row=6,column=1)
#===============================================================================================
lblPlat_Special_chef1 = Label(f1,font=('arial',13,'bold'), text = "Special chef (Viandes)",bd=13 , anchor="w")
lblPlat_Special_chef1.grid(row=7,column=0)
txt_Special_chef1=Entry(f1,font=('arial',13,'bold'), textvariable=Special_chef1,bd=13 , insertwidth=4,
                   bg="powder blue",justify='right')
txt_Special_chef1.grid(row=7,column=1)
#=====================================================================================
lblPlat_Special_chef2 = Label(f1,font=('arial',13,'bold'), text = "Special chef (Volaille)",bd=13 , anchor="w")
lblPlat_Special_chef2.grid(row=0,column=2)
txt_Special_chef2=Entry(f1,font=('arial',13,'bold'), textvariable=Special_chef2,bd=13 , insertwidth=4,
                   bg="powder blue",justify='right')
txt_Special_chef2.grid(row=0,column=3)
#=================================================================================
lblPlat_Special_chef3 = Label(f1,font=('arial',13,'bold'), text = "Special chef (Fruit De Mer)",bd=13 , anchor="w")
lblPlat_Special_chef3.grid(row=1,column=2)
txt_Special_chef3=Entry(f1,font=('arial',13,'bold'), textvariable=Special_chef3,bd=13 , insertwidth=4,
                   bg="powder blue",justify='right')
txt_Special_chef3.grid(row=1,column=3)
#===============================================================================
lblPlat_salad= Label(f1,font=('arial',13,'bold'), text = "Salade",bd=13 , anchor="w")
lblPlat_salad.grid(row=2,column=2)
txt_salad=Entry(f1,font=('arial',13,'bold'), textvariable=Salad,bd=13 , insertwidth=4,
                   bg="powder blue",justify='right')
txt_salad.grid(row=2,column=3)
#=================================================================================
lblPlat_Drinks = Label(f1,font=('arial',13,'bold'), text = "boissons",bd=13 , anchor="w")
lblPlat_Drinks.grid(row=3,column=2)
txt_Drinks=Entry(f1,font=('arial',13,'bold'), textvariable=Drinks,bd=13 , insertwidth=4,
                   bg="powder blue",justify='right')
txt_Drinks.grid(row=3,column=3)
#===================================================================================
lblPlat_Water = Label(f1,font=('arial',13,'bold'), text = "Eau Minérale",bd=13 , anchor="w")
lblPlat_Water.grid(row=4,column=2)
txt_Water=Entry(f1,font=('arial',13,'bold'), textvariable=Water,bd=13 , insertwidth=4,
                   bg="powder blue",justify='right')
txt_Water.grid(row=4,column=3)
#==================================================================================
lblPlat_Cost = Label(f1,font=('arial',13,'bold'), text = "Cost Of Meal",bd=13 , anchor="w")
lblPlat_Cost.grid(row=5,column=2)
txt_Cost=Entry(f1,font=('arial',13,'bold'), textvariable=Cost,bd=13 , insertwidth=4,
                   bg="#ffffff",justify='right')
txt_Cost.grid(row=5,column=3)
#===================================================================================
lblPlat_Service = Label(f1,font=('arial',13,'bold'), text = "Service Charge",bd=13 , anchor="w")
lblPlat_Service.grid(row=6,column=2)
txt_Service=Entry(f1,font=('arial',13,'bold'), textvariable=Service,bd=13 , insertwidth=4,
                   bg="#ffffff",justify='right')
txt_Service.grid(row=6,column=3)
#==========================================================================================
lblPlat_Total= Label(f1,font=('arial',13,'bold'), text = "Total",bd=13 , anchor="w")
lblPlat_Total.grid(row=7,column=2)
txt_Total=Entry(f1,font=('arial',13,'bold'), textvariable=SubTotal,bd=13 , insertwidth=4,
                   bg="#ffffff",justify='right')
txt_Total.grid(row=7,column=3)
#=========================================================================================

#=========================================Buttons==================================
btnTotal=Button(f1,padx=16 , pady=8,bd=16,fg='black',font=('arial',16,'bold'),width=10,
                text="TOTAL" , bg="powder blue" , command = Ref).grid(row=8,column=1)
btnReset=Button(f1,padx=16 , pady=8,bd=16,fg='black',font=('arial',16,'bold'),width=10,
                text="RESET" , bg="powder blue" , command = Reset).grid(row=8,column=2)
btnExit=Button(f1,padx=16 , pady=8,bd=16,fg='black',font=('arial',16,'bold'),width=10,
                text="EXIT" , bg="powder blue" , command = qExit).grid(row=8,column=3)
btnSave=Button(f1,padx=16 , pady=8,bd=16,fg='green',font=('arial',16,'bold'),width=10,
                text="SAVE" , bg="powder blue" , command = Save).grid(row=9,column=2)

root.mainloop()




