
import tkinter as tk

from tkinter import messagebox,Canvas
# from tkinter.ttk import *
import sqlite3
from tkinter import IntVar
# from random import choice
import customtkinter as ctk
from tkinter import TclError,messagebox,Canvas
import sqlite3
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
from matplotlib.figure import Figure 
from matplotlib.backends.backend_tkagg import (FigureCanvasTkAgg,  NavigationToolbar2Tk) 
import pandas as pd
import customtkinter as ctk

 
 
 
class Restaurant:
 def __init__(self):
        
        ##################General############################
        self.UserId = ""
        self. Password=""
        self. Phone=""
        self.Email=""
        self.CashierData=[['Ali Ahmed','Cashier1'],['Ahmed Abid','Cashier2'],['Aleesha Ahmed','Cashier3']]
        self.con = sqlite3.Connection('RestaurantDb')
        self.c=self.con.cursor()
        
        self.con.execute('''CREATE TABLE IF NOT EXISTS UserCredentials2 (
                                ID INTEGER PRIMARY KEY AUTOINCREMENT,
                                 
                                NAME VARCHAR(30),
                                EMAIL VARCHAR(30),
                                PHONE_NUMBER VARCHAR(12),
                                PASSWORD VARCHAR(20)
                            );''')
        self.con.commit()

        # self.c.execute("SELECT NAME, PASSWORD FROM UserCredentials2 WHERE NAME = ? AND PASSWORD = ?", (useridVal, passwordVal))
        # ExistingUser=self.c.fetchone()
        # print('Existing Customers:',ExistingUser)
        # self.con.execute("DELETE FROM UserCredentials2  WHERE ID = (SELECT MAX(ID) FROM UserCredentials2 );")
        self.con.execute('''CREATE TABLE IF NOT EXISTS CashierNames3 (
                                ID INTEGER PRIMARY KEY AUTOINCREMENT,
                                NAME VARCHAR(30),
                                PASSWORD VARCHAR(12)
                            );''')
        self.con.commit()
         
        # for nameC,passwordC in self.CashierData:
        #  self.con.execute('INSERT INTO CashierNames3 (NAME,PASSWORD) VALUES (?,?)', (nameC,passwordC))
        #  self.con.commit()
        self.c.execute("SELECT * FROM CashierNames3")
        self.ExistingCashier = self.c.fetchall()
        
        print(self.ExistingCashier)


         #################################
        
        
        ##############################Customer##############################
        self. NameTableCust = ''
        self. PhoneNumberTableCust = ''
        self.TnumberCust = 0
        
        self.con.execute('''CREATE TABLE IF NOT EXISTS TableStatus8Cust (
                                ID INTEGER PRIMARY KEY AUTOINCREMENT,
                                TABLE_NUMBER INTEGER,
                                NAME VARCHAR(30),
                                PHONE_NUMBER VARCHAR(12)
                            );''')
        self.con.commit()

        self.IcecreamVariablesCustomer = []
        self.SundaeVariablesCustomer = []
        self.BeveragesVariablesCustomer = []
         
        self. SelectedItemsCust= []
        self. SelectedItems1Cust= []
        self. SumCust=0
        self. SumGrandCust=0
         
######################Menu for Customer portal ###################
        self. CategoriesOrderCust = ['Ice Cream', 'Sundae', 'Beverages']
        self. IcecreamItemCust = ['Chocolate', 'Mango', 'Stawberry']
        self.IcecreamPriceCust=['10','13','14']
        self. SundaeItemCust = ['Peanut Butter', 'Hot Fudge', 'Dino ']
        self.SundaePriceCust=['12','17','21']
        self. BeveargeItemCust = ['Cold Coffee', 'Milk shake', 'Mint margarita', 'Iced Tea']
        self.BeveragePriceCust=['12','12','10','5']
        self.TotalSumCust=0
         
        self.con.execute('''CREATE Table IF NOT EXISTS ICECREAMCUST42 (
                                ID INTEGER PRIMARY KEY AUTOINCREMENT,
                                 
                                 
                                ITEM VARCHAR(30),
                                PRICE VARCHAR(30)
                                
                            );''')
        self.con.commit()

        # for i in range (len(self.IcecreamPriceCust)):
        #    self.c.execute("INSERT INTO ICECREAMCUST42 (ITEM,PRICE) VALUES (?, ?)", (self.IcecreamItemCust[i],self.IcecreamPriceCust[i]))
        #    self.con.commit()

        self.con.execute('''CREATE Table IF NOT EXISTS BEVERAGECUST4 (
                                ID INTEGER PRIMARY KEY AUTOINCREMENT,
                                 
                                 
                                ITEM VARCHAR(30),
                                PRICE VARCHAR(30)
                                
                            );''')
        self.con.commit()

        # for i in range (len(self.BeveragePriceCust)):
        #    self.c.execute("INSERT INTO BEVERAGECUST4 (ITEM,PRICE) VALUES (?, ?)", (self.BeveargeItemCust[i],self.BeveragePriceCust[i]))
        #    self.con.commit()
    
        self.con.execute('''CREATE Table IF NOT EXISTS SUNDAECUST4 (
                                ID INTEGER PRIMARY KEY AUTOINCREMENT,
                                 
                                 
                                ITEM VARCHAR(30),
                                PRICE VARCHAR(30)
                                
                            );''')
        self.con.commit()
        
        # for i in range (len(self.SundaePriceCust)):
        #    self.c.execute("INSERT INTO SUNDAECUST4 (ITEM,PRICE) VALUES (?, ?)",(self.SundaeItemCust[i],self.SundaePriceCust[i]))
        #    self.con.commit()



         #############Cashier###########################
         # self.FoodMenu = tk.Toplevel()
        # self.FoodMenu.title("Food Ordering System")
        self.IcecreamVariablesCashier = []
        self.SundaeVariablesCashier = []
        self.BeveragesVariablesCashier = []
        self. SelectedItemsCashier= []
        self. SelectedItemsCashier1= []
        self. SumCashier=0
        self. SumGrandCashier=0
        self.SumOfOrdersCashier=0
        self.EntriesCashier=0
        self.LatestIDCashier=0
        self.TotalSumCashier=0
        
        # self.con = sqlite3.Connection('CashierDb')
        self.NAMECashier = ''
        self.PHONENUMBERCashier = ''
        self.TnumberCashier = 0
        self.NAMECartCashier =''
 
        
        self.c=self.con.cursor()
         

        
        self.con.execute('''CREATE Table IF NOT EXISTS TableStatusFTF10 (
                                ID INTEGER PRIMARY KEY AUTOINCREMENT,
                                Table_NUMBER INTEGER,
                                NAME VARCHAR(30),
                                PHONE_NUMBER VARCHAR(12)
                            );''')
        self.con.commit()
        

        self.con.execute('''CREATE Table IF NOT EXISTS OrderFTF8 (
                                ID INTEGER PRIMARY KEY AUTOINCREMENT,
                                 
                                NAME VARCHAR(30),
                                BILL INTEGER
                                
                            );''')
        self.con.commit()
        
        self. CategoriesOrderCashier = ['Ice Cream', 'Sundae', 'Beverages']
        self. IcecreamItemCashier = ['Chocolate', 'Mango', 'Stawberry']
        self.IcecreamPriceCashier=['10','13','14']
        self. SundaeItemCashier = ['Peanut Butter', 'Hot Fudge', 'Dino ']
        self.SundaePriceCashier=['12','17','21']
        self. BeveargeItemCashier = ['Cold Coffee', 'Milk shake', 'Mint margarita', 'Iced Tea']
        self.BeveragePriceCashier=['12','12','10','5']
         
        self.con.execute('''CREATE Table IF NOT EXISTS ICECREAM41 (
                                ID INTEGER PRIMARY KEY AUTOINCREMENT,
                                 
                                 
                                ITEM VARCHAR(30),
                                PRICE VARCHAR(30)
                                
                            );''')
        self.con.commit()

      #   for i in range (len(self.IcecreamPriceCashier)):
      #      self.c.execute("INSERT INTO ICECREAM41 (ITEM,PRICE) VALUES (?, ?)", (self.IcecreamItemCashier[i],self.IcecreamPriceCashier[i]))
      #      self.con.commit()

        self.con.execute('''CREATE Table IF NOT EXISTS BEVERAGE3 (
                                ID INTEGER PRIMARY KEY AUTOINCREMENT,
                                 
                                 
                                ITEM VARCHAR(30),
                                PRICE VARCHAR(30)
                                
                            );''')
        self.con.commit()

      #   for i in range (len(self.BeveragePriceCashier)):
      #      self.c.execute("INSERT INTO BEVERAGE3 (ITEM,PRICE) VALUES (?, ?)", (self.BeveargeItemCashier[i],self.BeveragePriceCashier[i]))
      #      self.con.commit()
    
        self.con.execute('''CREATE Table IF NOT EXISTS SUNDAE3 (
                                ID INTEGER PRIMARY KEY AUTOINCREMENT,
                                 
                                 
                                ITEM VARCHAR(30),
                                PRICE VARCHAR(30)
                                
                            );''')
        self.con.commit()
        
      #   for i in range (len(self.SundaePriceCashier)):
      #      self.c.execute("INSERT INTO SUNDAE3 (ITEM,PRICE) VALUES (?, ?)",(self.SundaeItemCashier[i],self.SundaePriceCashier[i]))
      #      self.con.commit()
        self.LatestOrderArrayCashier=[]
        self.LatestOrderArrayCashier=[]

        ########### Admin ################
        self.AVar=[]
        self.PVar=[]

        # self.con.execute("DELETE FROM SUNDAE3  WHERE ID = (SELECT MAX(ID) FROM SUNDAE3 );")
  ########################################Welcome Page############################
        self.welcome = ctk.CTk()
        # self.welcome.geometry('580x200')
        self.welcome.title('Welcome Page')
        self.welcome.config(bg='#FC3588')
        
    
        welcomeLab1 = tk.Label(self.welcome, text="Welcome to the  3 in 1 Ice Cream Parlor management application!", font=("Times New Roman", 16),bg='#FC3588')
        welcomeLab1.grid(row=1, column=0,columnspan=5, padx=10, pady=5)

        welcomeLab2 = tk.Label(self.welcome, text="Project By:\nTehreem Javed\nMuddasar Khan\nMuhammad Hashir Malik", font=("Times New Roman", 13),justify='center',bg='#FC3588')
        welcomeLab2.grid(row=2 ,column=2, padx=10, pady=5, sticky='w')
        button1 = ctk.CTkButton(self.welcome, text="Login", command=self.LoginPage,text_color='white',fg_color=('#FC35B8','#FC35B8'),hover_color='#bd3e91' ,corner_radius=10)
        button1.grid(row=10,column=1, padx=10, pady=5, sticky='s')

 
        button2 = ctk.CTkButton(self.welcome, text="SignUp",text_color='white',fg_color=('#FC35B8','#FC35B8'),hover_color='#bd3e91' ,corner_radius=10, command=self.SignupPage)
        # button2 = ctk.CTkButton(self.welcome, text="SignUp", command=self.AttendenceFunction,fg='white',bg='#FC35B8' )

        button2.grid(row=10,column=3, padx=10, pady=5, sticky='s')
        
        self.LoginPage=None
        self.SignupPage=None
        # self.MainPageCustomer=None
        self.welcome.mainloop()
        
 def Admin(self):
     
    useridVal = self.UserId.get()
    passwordVal = self. Password .get()
    
    if( useridVal == "HassanAli1" and passwordVal == "admin1" or useridVal ==
        "AyeshaAli2" and passwordVal== "admin2" 
    or useridVal == "AhmedAli3" and passwordVal== "admin3"):
        messagebox.showinfo("Login Successful", "Welcome admin")
        self.MainPageAdminFunction()
    else:
        messagebox.showerror("Login Failed", " you are not registered as Admin  or perhaps you forgot your username")


 def  Cashier(self):
    useridVal = self.UserId.get()
    passwordVal = self. Password.get()
    for entries in self.ExistingCashier:
     if  useridVal==entries[1] and passwordVal==entries[2]:
         messagebox.showinfo("Login Successful", "Welcome Cashier")
         self.MainPageCashierFunction()
         return 
     
    messagebox.showerror("Login Failed ", 
                             "you are not registered as Cashier or perhaps you forgot your username")

 def  Customer(self):
    useridVal = self.UserId.get()
    passwordVal = self. Password .get()
    self.c.execute("SELECT NAME, PASSWORD FROM UserCredentials2 WHERE NAME = ? AND PASSWORD = ?",
                    (useridVal, passwordVal))
    ExistingUser=self.c.fetchone()
    print('Existing Customers:',ExistingUser)
    if  ExistingUser:
        messagebox.showinfo(f'Success Login',"Login  Successful, Welcome")
        self.MainPageCustomer()
       
    else:
        messagebox.showerror('Error',"You are not registered,Sign Up instead ")
        # self.SignupPage()
 def SignupPage(self):
    self.signup=tk.Toplevel()
    # self.signup.geometry('550x550')
    self.signup.title('SignUp_Window')
    self.signup.config(bg='#FC3588')
    SignupLabel=tk.Label(self.signup,text='Sign Up',font=('Times New Roman',16,'bold'),justify='center',bg='#FC3588')
    SignupLabel.grid(row=0,column=0,columnspan=3)
    # signupLab=tk.Label(self.signup, text="Signup",font=(20,'bold'))
    # signupLab.grid(row=0,column=0,columnspan=4, padx=10, pady=5, sticky='w')
    useridLab = tk.Label(self.signup, text="Name",bg='#FC3588')
    useridLab.grid(row=2,column=0, padx=10, pady=5, sticky='w')
    self.UserId = ctk.CTkEntry(self.signup)
    self.UserId.grid(row=2,column=1, padx=10, pady=5, sticky='w')

    

    emailLab = tk.Label(self.signup, text="Email",bg='#FC3588')
    emailLab.grid(row=3,column=0, padx=10, pady=5, sticky='w')
    default='you@example.com'
    self.Email = ctk.CTkEntry(self.signup)
    self.Email.insert(0, default)
    self.Email.grid(row=3,column=1, padx=10, pady=5, sticky='w')

    
    phoneLab = tk.Label(self.signup, text="Phone Number",bg="#FC3588")
    phoneLab.grid(row=4,column=0, padx=10, pady=5, sticky='w')
    self. Phone = ctk.CTkEntry(self.signup)
    self. Phone.grid(row=4,column=1, padx=10, pady=5, sticky='w')

    passwordLab = tk.Label(self.signup, text="Password",bg='#FC3588')
    passwordLab.grid(row=5,column=0, padx=10, pady=5, sticky='w')
    self. Password = ctk.CTkEntry( self.signup, show=".")   
    self. Password.grid(row=5,column=1, padx=10, pady=5, sticky='w')

    
    signupButton= ctk.CTkButton(self.signup, text="SignUp",command=self.SavedStatusSignup,fg_color='white',hover_color='#bd3e91',text_color='black')
    signupButton.grid(row=6,column=0,columnspan=2,pady=30)


 def LoginPage(self): 
    self.login = ctk.CTkToplevel()
    self.login.title('login_Window')
    LoginLabel = tk.Label(self.login, text='Login', font=('Times New Roman', 16, 'bold'), justify='center')
    LoginLabel.grid(row=0, column=0, columnspan=6)
    LoginLabel.grid_propagate(False)
    
    FrameLogin = ctk.CTkFrame(self.login, fg_color=('#FC35B8', '#FC35B8'))
    FrameLogin.grid(row=1, rowspan=8, column=0, columnspan=8, padx=20, pady=20)
    FrameLogin.grid_propagate(False)
    
    useridLab = tk.Label(FrameLogin, text="Name:", justify='center', bg='#FC35B8')
    useridLab.grid(row=1, column=0, padx=10, pady=10, sticky='w')

    self.UserId = ctk.CTkEntry(FrameLogin,width=100)
    self.UserId.grid(row=1, column=1, sticky='w', pady=10)

    passwordLab = tk.Label(FrameLogin, text="Password:", justify='center', bg='#FC35B8')
    passwordLab.grid(row=2, column=0, padx=10, pady=2, sticky='w')

    self.Password = ctk.CTkEntry(FrameLogin, show=".",width=100)
    self.Password.grid(row=2, column=1, sticky='w', pady=2)

    LoginAsLab = tk.Label(FrameLogin, text="Login as", font=("Times New Roman", 12),bg=('#FC35B8'))
    LoginAsLab.grid(row=3, column=0, columnspan=2,pady=2)

    loginAdmin = ctk.CTkButton(FrameLogin, text="Admin", command=self.Admin, font=("Times New Roman", 12),
                                fg_color='white', hover_color='#bd3e91', text_color='black', width=5)
    loginAdmin.grid(row=4, column=0, columnspan=2,pady=2)

    loginCashier = ctk.CTkButton(FrameLogin, text="Cashier", command=self.Cashier, font=("Times New Roman", 12),
                                  fg_color='white', hover_color='#bd3e91', text_color='black', width=5)
    loginCashier.grid(row=5, column=0, columnspan=2,pady=2)

    loginCustomer = ctk.CTkButton(FrameLogin, text="Customer", command=self.Customer, font=("Times New Roman", 12),
                                   fg_color='white', hover_color='#bd3e91', text_color='black', width=5)
    loginCustomer.grid(row=6, column=0, columnspan=2,pady=2)
 def SavedStatusSignup(self):
   self.c.execute("SELECT NAME,EMAIL,PHONE_NUMBER, PASSWORD FROM UserCredentials2 WHERE NAME = ? AND EMAIL=? AND PHONE_NUMBER =? AND PASSWORD = ?",
                    (self.UserId.get(), self.Email.get(),self. Phone.get(),self. Password.get()))
   existingUser=self.c.fetchone()
   print('existing;',existingUser)
   if  existingUser:
        messagebox.showerror('Error SignUp'," This user already exist,Login instead " )
        self.LoginPage()
   elif self.UserId.get() and self. Password.get() and self. Phone.get() and self.Email.get():
            data = (self.UserId.get() , self.Email.get() , self. Phone.get() ,self. Password.get()  )
            self.con.execute("INSERT INTO UserCredentials2 (NAME ,EMAIL ,PHONE_NUMBER,PASSWORD ) VALUES (?, ?, ?,?)", data)
            self.con.commit()
            self.c.execute('SELECT * FROM UserCredentials2 ')
            data = self.c.fetchall()
            print('\n\nRegistered Customers:',data)
            # self.SucccessSignup()
            messagebox.showinfo('Success Signup',"Signed Up Successfully")
            self.MainPageCustomer()
 
   else:
     messagebox.showerror('Error SignUp','Enter complete details please')
    #  self.ErrorSignup()

  
 def MainPageCustomer(self):   
       self.MainPage=tk.Toplevel()
      #  MainPage.geometry('650x550')
       self.MainPage.title('Main Page Customer')
       self.MainPage.configure(bg='#FC3588')
        
        
       
    #  self.ErrorSignup()
       Logo=tk.Label(self.MainPage,text='Berrilicious',fg='white',font=('Helvetica',20),bg='#FC3588')
       Logo.grid(row=2,column=0,sticky='w')
       Home = ctk.CTkButton(self.MainPage, text="Home",font=('Helvetica',15),width=30,fg_color=('#FC35B8','#FC35B8'),hover_color='#bd3e91',text_color='black' )
       Home.grid(row=2,column=5, padx=5, pady=5,sticky='ne')
       Aboutus = ctk.CTkButton(self.MainPage, text="About Us",font=('Helvetica',15),width=30,fg_color=('#FC35B8','#FC35B8'),hover_color='#bd3e91',text_color='black',command=self.AboutUsFunction )
       Aboutus.grid(row=2,column=6, padx=5, pady=5,sticky='ne')
       Menu = ctk.CTkButton(self.MainPage, text="Menu",command=self.MenuDisplayFunctionCustomer,font=('Helvetica',15),width=30,fg_color=('#FC35B8','#FC35B8'),hover_color='#bd3e91',text_color='black')
       Menu.grid(row=2,column=7, padx=5, pady=5,sticky='ne')
       BookTable = ctk.CTkButton(self.MainPage, text="Book a Table",command=self.TableReservationFunctionCustomer,font=('Helvetica',15),width=30,fg_color=('#FC35B8','#FC35B8'),hover_color='#bd3e91',text_color='black' )
       BookTable.grid(row=2,column=8, padx=5, pady=5,sticky='ne')
       Feedback = ctk.CTkButton(self.MainPage, text="Feedback",command=self.FeedbackFunction ,font=('Helvetica',15),width=30,fg_color=('#FC35B8','#FC35B8'),hover_color='#bd3e91',text_color='black')
       Feedback.grid(row=2,column=9, padx=5, pady=5,sticky='ne')
       LogOutButtonCustomer = ctk.CTkButton(self.MainPage, text="Logout" ,font=('Helvetica',15),width=30,fg_color=('#FC35B8','#FC35B8'),hover_color='#bd3e91',text_color='black',command=self.LogoutFunctionCustomer)
       LogOutButtonCustomer.grid(row=2,column=10, padx=5, pady=5,sticky='ne')
       WelcomeCustomer=tk.Label(self.MainPage,text='Welcome to Berrilicious',font=('Helvetica',16),bg='#FC3588')
       WelcomeCustomer.grid(row=3,column=3,columnspan=7,pady=20 )
      #  WelcomeCustomer1=tk.Label(MainPage,text='Berrilicious is a professional ice cream parlour website.\n We will offer you variety of icecreams,sundaes and beverages on a very reasonable prices.',font=('Helvetica',15),bg='#FC3588')
      #  WelcomeCustomer1.grid(row=4,column=3,columnspan=7,pady=5 )
       Order=ctk.CTkButton(self.MainPage, text="Order Online" ,font=('Helvetica',20),command=self.FoodMenuFunctionCustomer ,fg_color=('#FC35B8','#FC35B8'),hover_color='#bd3e91',text_color='white')
       Order.grid(row=5,column=3,columnspan=7 ,padx=10, pady=5 )
  
 def FeedbackFunction(self):
     self.FeedbackPage=tk.Toplevel()
    #  self.FeedbackPage.geometry('650x550')
     self.FeedbackPage.title('Feedback')
     self.FeedbackPage.title("Feedback Form")
     self.FeedbackPage.configure(bg="#FC3588")

     canvas = Canvas(self.FeedbackPage)
        # self.canvas.grid(row=1)
     BorderFrame = tk.Frame(self.FeedbackPage, relief=tk.RIDGE, borderwidth=2,bg='white')
     BorderFrame.grid(row=3, column=0,columnspan=4)
  
     Logo = tk.Label(self.FeedbackPage, text="Berrilicious", font=('Helvetica', 17 ),fg='white',bg="#FC3588")
     Logo.grid(row=0, column=0, sticky='w', padx=10, pady=10)

     Survey = tk.Label(self.FeedbackPage, text="Customer survey form", font=('The Nautigal', 17, 'italic', 'underline'),fg='white',bg="#FC3588")
     Survey.grid(row=0, column=1, sticky='e', padx=15, pady=10)

     RateLabel = tk.Label(self.FeedbackPage, text="Rate from scale of 1 to 5", font=('The Nautigal', 13),bg="#FC3588")
     RateLabel.grid(row=1, column=0, columnspan=3, padx=10, pady=5, sticky='w')

     ValueLabel = tk.Label(self.FeedbackPage, text="1.Highly Satisfied  2.Satisfied   3.Neutral    4.Disatisfied   5.Highly Dissatisfied", font=('The Nautigal', 10, 'bold'),bg="#FC3588")
     ValueLabel.grid(row=2, column=0, columnspan=4, padx=10, pady=5, sticky='w')

     FoodTaste = tk.Label(BorderFrame, text="The taste of food", font=('The Nautigal', 13),bg='white')
     FoodTaste.grid(row=3, column=0, padx=10, pady=5, sticky='w')

     FoodTasteScale = tk.Scale(BorderFrame, from_=1, to=5, orient=tk.HORIZONTAL,bg='white',troughcolor="#FC35B8", activebackground		="#e173fa")
     FoodTasteScale.grid(row=3, column=1, padx=10, pady=5, sticky='w')
      
     FoodQuality = tk.Label(BorderFrame, text="The quality of food", font=('The Nautigal', 13),bg='white')
     FoodQuality.grid(row=4, column=0, padx=10, pady=5, sticky='w')

     FoodQualityScale = tk.Scale(BorderFrame, from_=1, to=5, orient=tk.HORIZONTAL,bg='white',troughcolor="#FC35B8", activebackground		="#e173fa")
     FoodQualityScale.grid(row=4, column=1, padx=10, pady=5, sticky='w')

     Attitude = tk.Label(BorderFrame, text="The attitude of staff", font=('The Nautigal', 13),bg='white')
     Attitude.grid(row=5, column=0, padx=10, pady=5, sticky='w')

     AttitudeScale = tk.Scale(BorderFrame, from_=1, to=5, orient=tk.HORIZONTAL,bg='white',troughcolor="#FC35B8", activebackground		="#e173fa")
     AttitudeScale.grid(row=5, column=1, padx=10, pady=5, sticky='w')

     OrderAccuracy = tk.Label(BorderFrame, text="The accuracy of order", font=('The Nautigal', 13),bg='white')
     OrderAccuracy.grid(row=6, column=0, padx=10, pady=5, sticky='w')

     OrderAccuracyScale = tk.Scale(BorderFrame, from_=1, to=5, orient=tk.HORIZONTAL,bg='white',troughcolor="#FC35B8", activebackground		="#FC9435")
     OrderAccuracyScale.grid(row=6, column=1, padx=10, pady=5, sticky='w')

     ServiceSpeed = tk.Label(BorderFrame, text="The speed of Service", font=('The Nautigal', 13),bg='white')
     ServiceSpeed.grid(row=7, column=0, padx=10, pady=5, sticky='w')

     ServiceSpeedScale = tk.Scale(BorderFrame, from_=1, to=5, orient=tk.HORIZONTAL,bg='white',troughcolor="#FC35B8", activebackground		="#FC9435")
     ServiceSpeedScale.grid(row=7, column=1, padx=10, pady=5, sticky='w')

     SubmitFeedback = ctk.CTkButton(self.FeedbackPage, text="Submit Feedback", font=("Times New Roman", 16),fg_color=('#FC35B8','#FC35B8'),hover_color='#bd3e91',text_color='white',command=self.SubmitFeedbackButton)
     SubmitFeedback.grid(row=8, column=0, columnspan=2, padx=10, pady=10)

 def SubmitFeedbackButton(self):
         
        messagebox.showinfo('Success','Feedback Submitted Succesfully')   

 def TableReservationFunctionCustomer(self):
       






           self.TableReservationPageCustomer = tk.Toplevel()
           self.TableReservationPageCustomer .title("Table Reservation")
         #   self.TableBookingFTF.geometry('600x300')
         #   self.TableBookingFTF.rowconfigure(0,weight=1)
         #   self.TableBookingFTF.columnconfigure(0,weight=1)

           EnterNumberCustomer=tk.Label(self.TableReservationPageCustomer,text="Select Table Number to view details")
           EnterNumberCustomer.grid(row=0,column=0)
           self.TableNumberCustomer = ctk.CTkButton(self.TableReservationPageCustomer, text="1", command=lambda:self.TableButtonClickCustomer(1),fg_color='#FC3588',text_color='black',hover_color='#bd3e91')
           self.TableNumberCustomer.grid(row=1, column=0, pady=10)
 
           self.TableNumberCustomer = ctk.CTkButton(self.TableReservationPageCustomer, text="2", command=lambda:self.TableButtonClickCustomer(2),fg_color='#FC3588',text_color='black',hover_color='#bd3e91')
           self.TableNumberCustomer.grid(row=1, column=1, pady=10)

           self.TableNumberCustomer = ctk.CTkButton(self.TableReservationPageCustomer, text="3", command=lambda:self.TableButtonClickCustomer(3),fg_color='#FC3588',text_color='black',hover_color='#bd3e91')
           self.TableNumberCustomer.grid(row=1, column=2, pady=10)

           self.TableNumberCustomer = ctk.CTkButton(self.TableReservationPageCustomer, text="4", command=lambda:self.TableButtonClickCustomer(4),fg_color='#FC3588',text_color='black',hover_color='#bd3e91')
           self.TableNumberCustomer.grid(row=2, column=0, pady=10)

           self.TableNumberCustomer = ctk.CTkButton(self.TableReservationPageCustomer, text="5", command=lambda:self.TableButtonClickCustomer(5),fg_color='#FC3588',text_color='black',hover_color='#bd3e91')
           self.TableNumberCustomer.grid(row=2, column=1, pady=10)

           self.TableNumberCustomer = ctk.CTkButton(self.TableReservationPageCustomer, text="6", command=lambda:self.TableButtonClickCustomer(6),fg_color='#FC3588',text_color='black',hover_color='#bd3e91')
           self.TableNumberCustomer.grid(row=2, column=2, pady=10)

           self.TableNumberCustomer = ctk.CTkButton(self.TableReservationPageCustomer, text="7", command=lambda:self.TableButtonClickCustomer(7),fg_color='#FC3588',text_color='black',hover_color='#bd3e91')
           self.TableNumberCustomer.grid(row=3, column=0, pady=10)

           self.TableNumberCustomer = ctk.CTkButton(self.TableReservationPageCustomer, text="8", command=lambda:self.TableButtonClickCustomer(8),fg_color='#FC3588',text_color='black',hover_color='#bd3e91')
           self.TableNumberCustomer.grid(row=3, column=1, pady=10)

           self.TableNumberCustomer = ctk.CTkButton(self.TableReservationPageCustomer, text="9", command=lambda:self.TableButtonClickCustomer(9),fg_color='#FC3588',text_color='black',hover_color='#bd3e91')
           self.TableNumberCustomer.grid(row=3, column=2, pady=10, padx=10)
    
           Namelab = tk.Label(self.TableReservationPageCustomer, text="Name:")
           Namelab.grid(row=4, column=0, pady=10)
           self. NameTableCust  = ctk.CTkEntry(self.TableReservationPageCustomer,fg_color='white',border_color='#FC3588',border_width=3)
           self. NameTableCust .grid(row=4, column=1, pady=10)
        
           Phonenolab = tk.Label(self.TableReservationPageCustomer, text="Phone Number:")
           Phonenolab.grid(row=5, column=0,  pady=10)
           self. PhoneNumberTableCust  = ctk.CTkEntry(self.TableReservationPageCustomer,fg_color='white',border_color='#FC3588',border_width=3)
           self. PhoneNumberTableCust .grid(row=5, column=1, pady=10)

           bookCustomer= ctk.CTkButton(self.TableReservationPageCustomer, text="Book Reservation", command=self.SaveCredentialsTableCustomer,fg_color=('#FC35B8','#FC35B8'),hover_color='#bd3e91',text_color='white')
           bookCustomer.grid(row=6, column=1)
 def TableButtonClickCustomer(self, number):

        self.TnumberCust = number
        self.c.execute("SELECT * FROM TableStatus8Cust WHERE TABLE_NUMBER = ?", (number,))
        ExistingTable=self.c.fetchone() 
        print(ExistingTable)
        if ExistingTable:
         messagebox.showerror("Error",f"Table number {number} already reserved")
        else:
           return self.TnumberCust

#  def DetailsTableCustomer(self):
#         NameLab = tk.Label( self.TableReservationPageCustomer, text="Name:",font=("Times New Roman", 16))
#         NameLab.grid(row=4, column=0, padx=10, pady=10)
#         self. NameTableCust = ctk.CTkEntry( self.TableReservationPageCustomer)
#         self. NameTableCust.grid(row=4, column=1, pady=10)
        
#         PhoneLab = tk.Label( self.TableReservationPageCustomer, text="Phone Number:",font=("Times New Roman", 16))
#         PhoneLab.grid(row=5, column=0, padx=10, pady=10)
#         self. PhoneNumberTableCust = ctk.CTkEntry( self.TableReservationPageCustomer)
#         self. PhoneNumberTableCust.grid(row=5, column=1, pady=10)

 def SaveCredentialsTableCustomer(self):
        if self. NameTableCust.get() and self. PhoneNumberTableCust.get():
            data = (self.TnumberCust, self. NameTableCust.get(), self. PhoneNumberTableCust.get())
            self.con.execute("INSERT INTO TableStatus8Cust (TABLE_NUMBER, NAME, PHONE_NUMBER) VALUES (?, ?, ?)", data)
            self.con.commit()
            self.c.execute('SELECT * FROM TableStatus8Cust ')
            data = self.c.fetchall()
            print(data)
            # self.SuccessTable()
            messagebox.showinfo('Success','Table Reserved Succesfully')
        else:
            # self.ErrorMessageTable()
            messagebox.showerror('Error','Enter Complete details please')
            
 def  MenuDisplayFunctionCustomer(self):
         self.MenuDisplayCustomer = ctk.CTkToplevel()
         self.MenuDisplayCustomer.title('Menu Display')
         self.MenuDisplayCustomer.config(bg='#FC3588')

         MenuLab1Customer = tk.Label(self.MenuDisplayCustomer, text="Food Menu", font=("Times New Roman",16),bg='#FC3588',fg='black')
         MenuLab1Customer.pack(pady=20)
         varsCust=[]
         aCust=tk.Label(self.MenuDisplayCustomer, text='Ice Cream', font=("Times New Roman", 16,'bold'),fg='black',bg='#FC3588').pack() 
   
         self.c.execute("SELECT ID FROM ICECREAMCUST42")
         IDIcecreamCust=self.c.fetchall()
      # print(CountIcecream)
         ItemIceCreamCust=self.c.execute("SELECT  ITEM FROM ICECREAMCUST42")
         ItemIcecream1Cust=self.c.fetchall()
         print(len(ItemIcecream1Cust))
         PriceIceCreamCust=self.c.execute("SELECT  PRICE FROM ICECREAMCUST42")
         PriceIcecreamCust=self.c.fetchall()

         for  i in range(len(IDIcecreamCust)):
              var = tk.StringVar()
              text = f"{ItemIcecream1Cust[i]} - ${PriceIcecreamCust[i]}"
              text=text.replace("(","")
              text=text.replace(")","")
              text=text.replace(",","")
              text=text.replace("''","")
              text=text.replace("'", "")
              MenuLab2Cust = tk.Label(self.MenuDisplayCustomer, text=text, font=("Times New Roman", 13),bg='#FC3588',fg='black')
              MenuLab2Cust.pack(pady=10)
         

         bCust=tk.Label(self.MenuDisplayCustomer, text='Beverages', font=("Times New Roman", 16,'bold'),fg='black',bg='#FC3588').pack() 
         self.c.execute("SELECT ID FROM BEVERAGECUST4")
         IDBeverageCust=self.c.fetchall()
      # print(CountIcecream)
         self.c.execute("SELECT  ITEM FROM BEVERAGECUST4")
         ItemBeverageCust=self.c.fetchall()
      # print(len(ItemIcecream1))
         self.c.execute("SELECT  PRICE FROM BEVERAGECUST4")
         PriceBeverageCust=self.c.fetchall()

         for  i in range(len(IDBeverageCust)):
           var = tk.StringVar()
           text = f"{ItemBeverageCust[i]} - ${PriceBeverageCust[i]}"
           text=text.replace("(","")
           text=text.replace(")","")
           text=text.replace(",","")
           text=text.replace("''","")
           text=text.replace("'", "")
           MenuLab2Cust = tk.Label(self.MenuDisplayCustomer, text=text, font=("Times New Roman", 13),bg='#FC3588',fg='black')
           MenuLab2Cust.pack(pady=10)
         
    


         cCust=tk.Label(self.MenuDisplayCustomer, text='Sundae', font=("Times New Roman", 16,'bold'),fg='black',bg='#FC3588').pack() 
         self.c.execute("SELECT ID FROM SUNDAECUST4")
         IDSundaeCust=self.c.fetchall()
      # print(CountIcecream)
         self.c.execute("SELECT  ITEM FROM SUNDAECUST4")
         ItemSundaeCust=self.c.fetchall()
      # print(len(ItemIcecream1))
         self.c.execute("SELECT  PRICE FROM SUNDAECUST4")
         PriceSundaeCust=self.c.fetchall()

         for  i in range(len(IDSundaeCust)):
           
           text = f"{ItemSundaeCust[i]} - ${PriceSundaeCust[i]}"
           text=text.replace("(","")
           text=text.replace(")","")
           text=text.replace(",","")
           text=text.replace("''","")
           text=text.replace("'", "")
           MenuLab2Cust = tk.Label(self.MenuDisplayCustomer, text=text, font=("Times New Roman", 13),bg='#FC3588',fg='black')
           MenuLab2Cust.pack(pady=10)

        
             
 def OnClickMenuCustomer(self,varsCust):
         
        
        self.SelectedItemsCust = [var.get() for var in varsCust if var.get()]
        if self.SelectedItemsCust==[]:#if Menu item not selected
            messagebox.showinfo('Error','Select Menu item first')
        else:#if menu item selected 
         messagebox.showinfo("Status ","Items added to cart succesfully")
        
        print(self.SelectedItemsCust)
        return  self.SelectedItemsCust

        # for item, Variable, price in zip(self.appetizer_list, self.SundaeVariables):
        #  if Variable.get():
        #    self. SelectedItems.append(item)
        #     SelectedItemsListbox.insert(tk.END, f"Appetizers: {item} - ${price}")
     

         
 def FoodMenuFunctionCustomer(self):
      self.MenuCust = tk.Toplevel()
      self.MenuCust.title('Menu')
      self.MenuCust.config(bg='#FC3588')


      MenuLab1Customer = tk.Label(self.MenuCust, text="Food Menu", font=("Times New Roman", 16),bg='#FC3588')
      MenuLab1Customer.pack(pady=20)
      varsCust=[]

     
      aCust=tk.Label(self.MenuCust, text='Ice Cream', font=("Times New Roman", 16),fg='black',bg='#FC3588').pack() 
   
      self.c.execute("SELECT ID FROM ICECREAMCUST42")
      IDIcecreamCust=self.c.fetchall()
      # print(CountIcecream)
      ItemIceCreamCust=self.c.execute("SELECT  ITEM FROM ICECREAMCUST42")
      ItemIcecream1Cust=self.c.fetchall()
      PriceIceCreamCust=self.c.execute("SELECT  PRICE FROM ICECREAMCUST42")
      PriceIcecreamCust=self.c.fetchall()

      for  i in range(len(IDIcecreamCust)):
        var = tk.StringVar()
        text = f"{ItemIcecream1Cust[i]} - ${PriceIcecreamCust[i]}"
        text=text.replace("(","")
        text=text.replace(")","")
        text=text.replace(",","")
        text=text.replace("''","")
        text=text.replace("'", "")

        chkCust = tk.Checkbutton(self.MenuCust, text=text, variable=var , onvalue=text,  offvalue="",bg='#FC3588')
        chkCust.pack()
        varsCust.append(var)

      bCust=tk.Label(self.MenuCust, text='Beverages', font=("Times New Roman", 16),fg='black',bg='#FC3588').pack() 
      self.c.execute("SELECT ID FROM BEVERAGECUST4")
      IDBeverageCust=self.c.fetchall()
      # print(CountIcecream)
      self.c.execute("SELECT  ITEM FROM BEVERAGECUST4")
      ItemBeverageCust=self.c.fetchall()
      # print(len(ItemIcecream1))
      self.c.execute("SELECT  PRICE FROM BEVERAGECUST4")
      PriceBeverageCust=self.c.fetchall()

      for  i in range(len(IDBeverageCust)):
        var = tk.StringVar()
        text = f"{ItemBeverageCust[i]} - ${PriceBeverageCust[i]}"
        text=text.replace("(","")
        text=text.replace(")","")
        text=text.replace(",","")
        text=text.replace("''","")
        text=text.replace("'", "")

        chkCust= tk.Checkbutton(self.MenuCust, text=text, variable=var , onvalue=text,  offvalue="",bg='#FC3588')
        chkCust.pack()
        varsCust.append(var)
    



      cCust=tk.Label(self.MenuCust, text='Sundae', font=("Times New Roman", 16),fg='black',bg='#FC3588').pack() 
      self.c.execute("SELECT ID FROM SUNDAECUST4")
      IDSundaeCust=self.c.fetchall()
      # print(CountIcecream)
      self.c.execute("SELECT  ITEM FROM SUNDAECUST4")
      ItemSundaeCust=self.c.fetchall()
      # print(len(ItemIcecream1))
      self.c.execute("SELECT  PRICE FROM SUNDAECUST4")
      PriceSundaeCust=self.c.fetchall()

      for  i in range(len(IDSundaeCust)):
        var = tk.StringVar()
        text = f"{ItemSundaeCust[i]} - ${PriceSundaeCust[i]}"
        text=text.replace("(","")
        text=text.replace(")","")
        text=text.replace(",","")
        text=text.replace("''","")
        text=text.replace("'", "")


        chkCust = tk.Checkbutton(self.MenuCust, text=text, variable=var , onvalue=text,  offvalue="",bg='#FC3588')
        chkCust.pack()
        varsCust.append(var)
        self.SelectedItemsCust = [var.get() for var in varsCust if var.get()]

      self.SubmitMenuButton = ctk.CTkButton(self.MenuCust, text="Submit", command=lambda: self.OnClickMenuCustomer(varsCust),fg_color=('#FC35B8','#FC35B8'),hover_color='#FC35B8')
      self.SubmitMenuButton.pack(pady=20)
      self.GotoCartButton = ctk.CTkButton(self.MenuCust, text="Goto Cart", command=self. ShoppingCartCustomer,fg_color=('#FC35B8','#FC35B8'),hover_color='#FC35B8')
      self.GotoCartButton .pack(pady=20)
 def ShoppingCartCustomer(self):
      # self.Menu.destroy()

      self.CartCustomer = tk.Toplevel()
      self.CartCustomer.title('Shopping cart')

      YourCartLab1Cust = tk.Label(self.CartCustomer, text="Your cart", font=("Times New Roman", 16),fg='white',bg='#FC3588')
      YourCartLab1Cust.pack(anchor=tk.NW)
      EmptyCartLab1Cust = ctk.CTkButton(self.CartCustomer, text="EmptyCart", font=("Times New Roman", 16), command=self.EmptyCartCustomer,fg_color=('#FC35B8','#FC35B8'),hover_color='#bd3e91',text_color='white',corner_radius=0)
      EmptyCartLab1Cust.pack(anchor=tk.NE)

      self. SelectedItemsListbox1Cust = tk.Listbox(self.CartCustomer, height=10, width=100,font=("Times New Roman", 13))
      self. SelectedItemsListbox1Cust.pack(pady=10)
     
      self.TotalSumCust=0
      for item in self.SelectedItemsCust:
        PriceStrCust = item.split(' - $')[-1].replace("'", "")
        ItemPriceCust = int (PriceStrCust)
        # print(item_price)
        self.TotalSumCust += ItemPriceCust
    #   self.SelectedItems1=self.SelectedItems.strip('{}')
      self.SelectedItemsListbox1Cust.insert(tk.END, self.SelectedItemsCust)
      # print("Selected items:",SelectedItems)
      print("Total sum:",  self.TotalSumCust)

      self. TotalVariableCust = ctk.IntVar()
      self. TotalVariableCust.set(self.TotalSumCust)
      self. SumCust= 0
      self. SumGrandCust=0
      self. TotalVariable1Cust = ctk.IntVar()
      self. SumGrandCust=self. TotalVariableCust.get()+200
      self. TotalVariable1Cust.set(self.SumGrandCust)
      DefaultCartCust='0'
      SubtotalLabCust = tk.Label(self.CartCustomer, text="Subtotal:")
      SubtotalLabCust.pack(anchor=tk.S)
      self.SubtotalCust = ctk.CTkEntry(self.CartCustomer, textvariable=self.TotalVariableCust)
      self.SubtotalCust.pack(anchor=tk.S)
      self.deliveryvar = tk.IntVar(value=200)   

      if  (self.TotalVariableCust).get() >10: #if items selected are more than 10 dollars then free delivery 
         self.FreeLabCust = tk.Label(self.CartCustomer, text="You have got Free delivery")
         self.FreeLabCust.pack(anchor=tk.S)
         DeliveryLabCust = tk.Label(self.CartCustomer, text="Delivery Charges:")
         DeliveryLabCust.pack(anchor=tk.S)
         self.DeliveryCust = ctk.CTkEntry(self.CartCustomer)
         self.DeliveryCust.insert(0,DefaultCartCust)
         self.DeliveryCust.pack(anchor=tk.S)
          
         TotalLabCust = tk.Label(self.CartCustomer, text="Grand Total:")
         TotalLabCust.pack(anchor=tk.S)
         self.TotalCust = ctk.CTkEntry(self.CartCustomer, textvariable=self.TotalVariableCust)
          
         self.TotalCust.pack(anchor=tk.S)
      else: #if items selected are less than 10 dollars then delivery charges=200 
         DeliveryLabCust = tk.Label(self.CartCustomer, text="Delivery Charges:")
         DeliveryLabCust.pack(anchor=tk.S)
         self.DeliveryCust = ctk.CTkEntry(self.CartCustomer, textvariable=self.deliveryvar)

         
         self.DeliveryCust.pack(anchor=tk.S)
         TotalLabCust = tk.Label(self.CartCustomer, text="Grand Total:")
         TotalLabCust.pack(anchor=tk.S)
         self.TotalCust = ctk.CTkEntry(self.CartCustomer, textvariable=self.TotalVariable1Cust)
         
         self.TotalCust.pack(anchor=tk.S)
      

 
 def EmptyCartCustomer(self):
     self. SelectedItemsCust = []   
     self. SelectedItemsListbox1Cust.delete(0, ctk.END)
     self.DeliveryCust.delete(0,ctk.END)
     self.SubtotalCust.delete(0,ctk.END)
     self.TotalCust.delete(0,ctk.END) 
     self.FreeLabCust.configure('') 
 def AboutUsFunction(self):
      self.AboutUsWindow = tk.Toplevel()
      self.AboutUsWindow.title('About Us')
      self.AboutUsWindow.configure(bg='#FC3588')
 
      AboutUsLab= tk.Label(self.AboutUsWindow, text="About Us!\nGreetings From Berrilicious\n Berrilicious is a professional ice cream parlour website. We will offer you variety of icecreams,sundaes and beverages on a very reasonable pries.\n. With an emphasis on reliability and the sale of ice cream, beverages, and sundaes, we're committed to giving you the greatest possible ice cream parlour experience. \n As much as we like serving you, we hope you enjoy our ice cream parlour.\n Please provide your love and support.\nWe Appreciate You Viewing Our Website.\nI hope you have a pleasant day!",font=("Times New Roman", 16),fg='Black',bg='#FC3588')

 
      AboutUsLab.pack()
      
      
 def MainPageCashierFunction(self):
       self.MainPageCashier = ctk.CTkToplevel()
       self.MainPageCashier.title('Main Page Cashier')

       canvas = Canvas(self.MainPageCashier)
       LogOutButtonCashier=ctk.CTkButton(self.MainPageCashier,text='Log out', font=("Times New Roman", 16),fg_color=('#FC35B8','#FC35B8'),hover_color='#FC35B8',command=self.LogoutFunctionCashier)
       LogOutButtonCashier.grid(row=0,column=7)
         
       Logo=tk.Label(self.MainPageCashier,text='Berrilicious', font=("The Nautigal", 16))
       Logo.grid(row=0,column=0,sticky='w',padx=10)
       
       BorderFrameDashboard = ctk.CTkFrame(self.MainPageCashier,border_color='black',fg_color=('#FC35B8','#FC35B8'))
       BorderFrameDashboard.grid(row=2,rowspan=10, column=0,columnspan=3,pady=20)
       DashboardButton = ctk.CTkButton(BorderFrameDashboard, text="Dashboard", font=("Times New Roman", 16),fg_color=('#FC35B8','#FC35B8'),hover_color='#bd3e91',text_color='white')
       DashboardButton.grid(row=3,column=0,columnspan=2,pady=10)
       MenuButton = ctk.CTkButton(BorderFrameDashboard, text="Menu", font=("Times New Roman", 16),fg_color=('#FC35B8','#FC35B8'),hover_color='#bd3e91',text_color='white',command=self.MenuDisplayCashierFunction)
       MenuButton.grid(row=4,column=0,columnspan=2,pady=10)
       TableBookingButton = ctk.CTkButton(BorderFrameDashboard, text="Table Booking", font=("Times New Roman", 16),fg_color=('#FC35B8','#FC35B8'),hover_color='#bd3e91',text_color='white',command=self.TableFunctionCashier)
       TableBookingButton.grid(row=5,column=0,columnspan=2,pady=10)
       OrderButton = ctk.CTkButton(BorderFrameDashboard, text="Order", font=("Times New Roman", 16),fg_color=('#FC35B8','#FC35B8'),hover_color='#bd3e91',text_color='white',command=self.MenuCashier)
       OrderButton.grid(row=6,column=0,columnspan=2,pady=10)
    #    logoutButton= ctk.CTkButton(BorderFrameDashboard, text="Logout", font=("Times New Roman", 16),fg_color='white',command=self.LogoutFunctionCashier)
    #    logoutButton.grid(row=7,column=0,columnspan=2,pady=10)
       
       DefaultNumber=0
       DefaultStr='0'
      
       FrameNewOrder= ctk.CTkFrame(self.MainPageCashier,fg_color=('#FC35B8','#FC35B8'))
       FrameNewOrder.grid(row=2, column=5,columnspan=3,padx=20,pady=20)
       NewOrderLabel= tk.Label(FrameNewOrder, text="New Orders", font=("Times New Roman", 16),justify='center')
       NewOrderLabel.grid(row=2,column=6,pady=10)
       self.NewOrderEntry= ctk.CTkEntry(FrameNewOrder , font=("Times New Roman", 16),justify='center')
       self.NewOrderEntry.insert(0,DefaultNumber)
       self.NewOrderEntry.grid(row=3,column=6,pady=10)
      

       FrameTotalOrder= ctk.CTkFrame(self.MainPageCashier,fg_color=('#FC35B8','#FC35B8'))
       FrameTotalOrder.grid(row=4, column=5,columnspan=3,padx=20,pady=20)
       TotalOrderLabel= tk.Label(FrameTotalOrder, text="Total Orders", font=("Times New Roman", 16),justify='center')
       TotalOrderLabel.grid(row=4,column=6,pady=10)
       self.TotalOrderEntry= ctk.CTkEntry(FrameTotalOrder , font=("Times New Roman", 16),justify='center')
       self.TotalOrderEntry.insert(0,DefaultNumber)
       self.TotalOrderEntry.grid(row=5,column=6,pady=10)

       FrameInProgress= ctk.CTkFrame(self.MainPageCashier ,fg_color=('#FC35B8','#FC35B8'))
       FrameInProgress.grid(row=6, column=5,columnspan=3,padx=20,pady=20)
       InProgressLabel= tk.Label(FrameInProgress, text="In Progress", font=("Times New Roman", 16),justify='center')
       InProgressLabel.grid(row=6,column=6,pady=10)
       self.InProgressEntry= ctk.CTkEntry(FrameInProgress,  font=("Times New Roman", 16),justify='center')
       self.InProgressEntry.insert(0,DefaultStr)
       self.InProgressEntry.grid(row=7,column=6,pady=10)
       InProgressButton= ctk.CTkButton(FrameInProgress, text="In Progress Update", font=("Times New Roman", 16),fg_color=('#FC35B8','#FC35B8'),hover_color='#bd3e91',text_color='white',command=self.InProgressUpdate)
       InProgressButton.grid(row=8,column=6,pady=10)
 def OnClickMenuCashier(self,vars):
        
        self.SelectedItems = [var.get() for var in vars if var.get()] #items selected by Cashier for customer
        if self.SelectedItems==[]: #if no item selected
            messagebox.showerror("Error "," Select Menu item first")
        else: # if items selected
            
         messagebox.showinfo("Status ","Items added to cart succesfully")

        
        print(self.SelectedItems)
        return self.SelectedItems
     

    # def MenuCashier(self):
    #   self.Menu = ctk.CTkToplevel()
    #   self.Menu.title('Menu')
    #   self.Menu.config(bg='#FC3588')
    #   MenuLab1 = tk.Label(self.Menu, text="Food Menu", font=("Times New Roman", 13),fg='white',bg='#FC35B8')
    #   MenuLab1.pack(pady=20)
    #   vars = []
     
    #   for category in self.categories_order:
    #    tk.Label(self.Menu, text=category, font=("Times New Roman", 13),fg='black',bg='#FC3588').pack() 
    #    items = self.Item1Cashier[category]
  
    #    for item, price in items.items():
    #     var = tk.StringVar()
    #     text = f"{item} - ${price}"
    #     chk = tk.Checkbutton(self.Menu, text=text, variable=var , onvalue=text,  offvalue="",bg='#FC3588')
    #     chk.pack()
    #     vars.append(var)
    #    self.SelectedItems = [var.get() for var in vars if var.get()]
    
    #   self.SubmitMenuButton = ctk.CTkButton(self.Menu, text="Submit",fg_color=('#FC35B8','#FC35B8'),hover_color='#FC35B8', command=lambda: self.OnClickMenuCashier(vars))
    #   self.SubmitMenuButton.pack(pady=20)
    #   self.GotoCartButton = ctk.CTkButton(self.Menu, text="Goto Cart",fg_color=('#FC35B8','#FC35B8'),hover_color='#FC35B8', command=self. ShoppingCartCashier)
    #   self.GotoCartButton .pack(pady=20)

 def MenuCashier(self):
      self.Menu = ctk.CTkToplevel()
      self.Menu.title('Menu')
      self.Menu.config(bg='#FC3588')
      MenuLab1 = tk.Label(self.Menu, text="Food Menu", font=("Times New Roman", 20),fg='white',bg='#FC35B8')
      MenuLab1.pack(pady=20)
      vars = []
     
       
      a=tk.Label(self.Menu, text='Ice Cream', font=("Times New Roman", 16),fg='black',bg='#FC3588').pack() 
   
      self.c.execute("SELECT ID FROM ICECREAM41")
      IDIcecream=self.c.fetchall()
      # print(CountIcecream)
      ItemIceCream=self.c.execute("SELECT  ITEM FROM ICECREAM41")
      ItemIcecream1=self.c.fetchall()
      print(len(ItemIcecream1))
      PriceIceCream=self.c.execute("SELECT  PRICE FROM ICECREAM41")
      PriceIcecream=self.c.fetchall()

      for  i in range(len(IDIcecream)):
        var = tk.StringVar()
        text = f"{ItemIcecream1[i]} - ${PriceIcecream[i]}"
        text=text.replace("(","")
        text=text.replace(")","")
        text=text.replace(",","")
        text=text.replace("''","")
        text=text.replace("'", "")

        chk = tk.Checkbutton(self.Menu, text=text, variable=var , onvalue=text,  offvalue="",bg='#FC3588')
        chk.pack()
        vars.append(var)

      b=tk.Label(self.Menu, text='Beverages', font=("Times New Roman", 16),fg='black',bg='#FC3588').pack() 
      self.c.execute("SELECT ID FROM BEVERAGE3")
      IDBeverage=self.c.fetchall()
      # print(CountIcecream)
      self.c.execute("SELECT  ITEM FROM BEVERAGE3")
      ItemBeverage=self.c.fetchall()
      # print(len(ItemIcecream1))
      self.c.execute("SELECT  PRICE FROM BEVERAGE3")
      PriceBeverage=self.c.fetchall()

      for  i in range(len(IDBeverage)):
        var = tk.StringVar()
        text = f"{ItemBeverage[i]} - ${PriceBeverage[i]}"
        text=text.replace("(","")
        text=text.replace(")","")
        text=text.replace(",","")
        text=text.replace("''","")
        text=text.replace("'", "")

        chk = tk.Checkbutton(self.Menu, text=text, variable=var , onvalue=text,  offvalue="",bg='#FC3588')
        chk.pack()
        vars.append(var)
    



      c=tk.Label(self.Menu, text='Sundae', font=("Times New Roman", 16),fg='black',bg='#FC3588').pack() 
      self.c.execute("SELECT ID FROM SUNDAE3")
      IDSundae=self.c.fetchall()
      # print(CountIcecream)
      self.c.execute("SELECT  ITEM FROM SUNDAE3")
      ItemSundae=self.c.fetchall()
      # print(len(ItemIcecream1))
      self.c.execute("SELECT  PRICE FROM SUNDAE3")
      PriceSundae=self.c.fetchall()

      for  i in range(len(IDSundae)):
        var = tk.StringVar()
        text = f"{ItemSundae[i]} - ${PriceSundae[i]}"
        text=text.replace("(","")
        text=text.replace(")","")
        text=text.replace(",","")
        text=text.replace("''","")
        text=text.replace("'", "")


        chk = tk.Checkbutton(self.Menu, text=text, variable=var , onvalue=text,  offvalue="",bg='#FC3588')
        chk.pack()
        vars.append(var)
      self.SelectedItems = [var.get() for var in vars if var.get()]
    
      self.SubmitMenuButton = ctk.CTkButton(self.Menu, text="Submit",fg_color=('#FC35B8','#FC35B8'),hover_color='#FC35B8', command=lambda: self.OnClickMenuCashier(vars))
      self.SubmitMenuButton.pack(pady=20)
      self.GotoCartButton = ctk.CTkButton(self.Menu, text="Goto Cart",fg_color=('#FC35B8','#FC35B8'),hover_color='#FC35B8', command=self. ShoppingCartCashier)
      self.GotoCartButton .pack(pady=20)


     
#  def SelectMenuItem(self):
#      if self
 def  ShoppingCartCashier(self):
       
      self.Cart = ctk.CTkToplevel()
      self.Cart.title('Shopping cart')
      self.Cart.config(bg='#FC3588')
     
       
      YourCartLab1 = tk.Label(self.Cart, text="Your cart", font=("Times New Roman", 16),fg='white',bg='#FC3588')
      YourCartLab1.pack(anchor=tk.NW,padx=20)
      EmptyCartLab1 = ctk.CTkButton(self.Cart, text="Clear Cart", font=("Times New Roman", 16), command=self.EmptyCartCashier,fg_color=('#FC35B8','#FC35B8'),hover_color='#bd3e91',text_color='white',corner_radius=0)
      EmptyCartLab1.pack(anchor=tk.NE)

      self. SelectedItemsCashierListbox1 = tk.Listbox(self.Cart, height=10, width=100,font=("Times New Roman", 13))
      self. SelectedItemsCashierListbox1.pack(pady=10)
     
      print(self.SelectedItems)
      self.TotalSumCashier = 0
      
      for item in self.SelectedItems:
        PriceStr = item.split(' - $')[-1].replace("'", "")
        item_price = int (PriceStr)
        # print(item_price)
        self.TotalSumCashier += item_price
      # self.SelectedItems1=self.SelectedItems.('{}')
      self.SelectedItemsCashierListbox1.insert(tk.END, f'{self.SelectedItems}\n')
             
      # print("Selected items:",SelectedItems)
      print("Total sum:",  self.TotalSumCashier)
     

      self. TotalVariable = tk.IntVar()
      self. TotalVariable.set(self.TotalSumCashier)
      self. SumCashier = 0
      self. SumGrandCashier=0
      
      # DefaultCart='0'
      NameLabCart= tk.Label(self.Cart, text="Name of customer:",bg='#FC3588')
      NameLabCart.pack(anchor=tk.S)
      self.NAMECartCashier= ctk.CTkEntry(self.Cart,border_color='#FC3588')
      self.NAMECartCashier.pack(anchor=tk.S)
      SubtotalLab = tk.Label(self.Cart, text="Subtotal:",bg='#FC3588')
      SubtotalLab.pack(anchor=tk.S)
      self.Subtotal = ctk.CTkEntry(self.Cart, textvariable=self.TotalVariable,border_color='#FC3588')
      # self.Subtotal.insert(0, DefaultCart)
      self.Subtotal.pack(anchor=tk.S)
       
          
      TotalLab = tk.Label(self.Cart, text="Grand Total:",bg='#FC3588')
      TotalLab.pack(anchor=tk.S)
      self.Total = ctk.CTkEntry(self.Cart, textvariable=self.TotalVariable,border_color='#FC3588')
      # self.Total.insert(0, DefaultCart)
      self.Total.pack(anchor=tk.S)
       
         
         
      self.SubmitOrder = ctk.CTkButton(self.Cart,  text='Submit Order',command=self.TotalOrdersFunctionCashier,fg_color=('#FC35B8','#FC35B8'),hover_color='#bd3e91',text_color='white',corner_radius=0)
      self.SubmitOrder.pack(anchor=tk.S,pady=10)
      
      
 def EmptyCartCashier(self):
      self. SelectedItemsCashier = []   
      self. SelectedItemsCashierListbox1.delete(0, ctk.END)
    #  self.SelectedItemsListbox.delete(0,tk.END)
      self.Subtotal.delete(0,ctk.END)
      self.Total.delete(0,ctk.END)  
      self.NAMECartCashier.delete(0,ctk.END)
      self.SelectedItems=[]




 def MenuDisplayCashierFunction(self):
         self.MenuDisplay = ctk.CTkToplevel()
         self.MenuDisplay.title('Menu Display')
         self.MenuDisplay.config(bg='#FC3588')

         MenuLab1 = tk.Label(self.MenuDisplay, text="Food Menu", font=("Times New Roman",20,'bold'),bg='#FC3588',fg='white')
         MenuLab1.pack(pady=20)

         a=tk.Label(self.MenuDisplay, text='Ice Cream', font=("Times New Roman", 16,'bold'),fg='black',bg='#FC3588').pack() 
   
         self.c.execute("SELECT ID FROM ICECREAM41")
         IDIcecream=self.c.fetchall()
      # print(CountIcecream)
         ItemIceCream=self.c.execute("SELECT  ITEM FROM ICECREAM41")
         ItemIcecream1=self.c.fetchall()
         print(len(ItemIcecream1))
         PriceIceCream=self.c.execute("SELECT  PRICE FROM ICECREAM41")
         PriceIcecream=self.c.fetchall()

         for  i in range(len(IDIcecream)):
              var = tk.StringVar()
              text = f"{ItemIcecream1[i]} - ${PriceIcecream[i]}"
              text=text.replace("(","")
              text=text.replace(")","")
              text=text.replace(",","")
              text=text.replace("''","")
              text=text.replace("'", "")
              MenuLab2 = tk.Label(self.MenuDisplay, text=text, font=("Times New Roman", 13),bg='#FC3588',fg='black')
              MenuLab2.pack(pady=10)
         

         b=tk.Label(self.MenuDisplay, text='Beverages', font=("Times New Roman", 16,'bold'),fg='black',bg='#FC3588').pack() 
         self.c.execute("SELECT ID FROM BEVERAGE3")
         IDBeverage=self.c.fetchall()
      # print(CountIcecream)
         self.c.execute("SELECT  ITEM FROM BEVERAGE3")
         ItemBeverage=self.c.fetchall()
      # print(len(ItemIcecream1))
         self.c.execute("SELECT  PRICE FROM BEVERAGE3")
         PriceBeverage=self.c.fetchall()

         for  i in range(len(IDBeverage)):
           var = tk.StringVar()
           text = f"{ItemBeverage[i]} - ${PriceBeverage[i]}"
           text=text.replace("(","")
           text=text.replace(")","")
           text=text.replace(",","")
           text=text.replace("''","")
           text=text.replace("'", "")
           MenuLab2 = tk.Label(self.MenuDisplay, text=text, font=("Times New Roman", 13),bg='#FC3588',fg='black')
           MenuLab2.pack(pady=10)
         
    


         c=tk.Label(self.MenuDisplay, text='Sundae', font=("Times New Roman", 16,'bold'),fg='black',bg='#FC3588').pack() 
         self.c.execute("SELECT ID FROM SUNDAE3")
         IDSundae=self.c.fetchall()
      # print(CountIcecream)
         self.c.execute("SELECT  ITEM FROM SUNDAE3")
         ItemSundae=self.c.fetchall()
      # print(len(ItemIcecream1))
         self.c.execute("SELECT  PRICE FROM SUNDAE3")
         PriceSundae=self.c.fetchall()

         for  i in range(len(IDSundae)):
           
           text = f"{ItemSundae[i]} - ${PriceSundae[i]}"
           text=text.replace("(","")
           text=text.replace(")","")
           text=text.replace(",","")
           text=text.replace("''","")
           text=text.replace("'", "")
           MenuLab2 = tk.Label(self.MenuDisplay, text=text, font=("Times New Roman", 13),bg='#FC3588',fg='black')
           MenuLab2.pack(pady=10)

        
        
        

 def TableFunctionCashier(self):
           self.TableBookingFTF = ctk.CTkToplevel()
           self.TableBookingFTF.title("Table Reservation")
         #   self.TableBookingFTF.geometry('600x300')
         #   self.TableBookingFTF.rowconfigure(0,weight=1)
         #   self.TableBookingFTF.columnconfigure(0,weight=1)

           Enter_number=tk.Label(self.TableBookingFTF,text="Select Table Number to view details")
           Enter_number.grid(row=0,column=0)
           self.TableNumber = ctk.CTkButton(self.TableBookingFTF, text="1", command=lambda:self.TableButtonClickCashier(1),fg_color='#FC3588',text_color='black',hover_color='#bd3e91')
           self.TableNumber.grid(row=1, column=0, pady=10)
 
           self.TableNumber = ctk.CTkButton(self.TableBookingFTF, text="2", command=lambda:self.TableButtonClickCashier(2),fg_color='#FC3588',text_color='black',hover_color='#bd3e91')
           self.TableNumber.grid(row=1, column=1, pady=10)

           self.TableNumber = ctk.CTkButton(self.TableBookingFTF, text="3", command=lambda:self.TableButtonClickCashier(3),fg_color='#FC3588',text_color='black',hover_color='#bd3e91')
           self.TableNumber.grid(row=1, column=2, pady=10)

           self.TableNumber = ctk.CTkButton(self.TableBookingFTF, text="4", command=lambda:self.TableButtonClickCashier(4),fg_color='#FC3588',text_color='black',hover_color='#bd3e91')
           self.TableNumber.grid(row=2, column=0, pady=10)

           self.TableNumber = ctk.CTkButton(self.TableBookingFTF, text="5", command=lambda:self.TableButtonClickCashier(5),fg_color='#FC3588',text_color='black',hover_color='#bd3e91')
           self.TableNumber.grid(row=2, column=1, pady=10)

           self.TableNumber = ctk.CTkButton(self.TableBookingFTF, text="6", command=lambda:self.TableButtonClickCashier(6),fg_color='#FC3588',text_color='black',hover_color='#bd3e91')
           self.TableNumber.grid(row=2, column=2, pady=10)

           self.TableNumber = ctk.CTkButton(self.TableBookingFTF, text="7", command=lambda:self.TableButtonClickCashier(7),fg_color='#FC3588',text_color='black',hover_color='#bd3e91')
           self.TableNumber.grid(row=3, column=0, pady=10)

           self.TableNumber = ctk.CTkButton(self.TableBookingFTF, text="8", command=lambda:self.TableButtonClickCashier(8),fg_color='#FC3588',text_color='black',hover_color='#bd3e91')
           self.TableNumber.grid(row=3, column=1, pady=10)

           self.TableNumber = ctk.CTkButton(self.TableBookingFTF, text="9", command=lambda:self.TableButtonClickCashier(9),fg_color='#FC3588',text_color='black',hover_color='#bd3e91')
           self.TableNumber.grid(row=3, column=2, pady=10, padx=10)
    
           Name_lab = tk.Label(self.TableBookingFTF, text="Name:")
           Name_lab.grid(row=4, column=0, pady=10)
           self.NAMECashier = ctk.CTkEntry(self.TableBookingFTF,fg_color='white',border_color='#FC3588',border_width=3)
           self.NAMECashier.grid(row=4, column=1, pady=10)
        
           Phone_no_lab = tk.Label(self.TableBookingFTF, text="Phone Number:")
           Phone_no_lab.grid(row=5, column=0,  pady=10)
           self.PHONENUMBERCashier = ctk.CTkEntry(self.TableBookingFTF,fg_color='white',border_color='#FC3588',border_width=3)
           self.PHONENUMBERCashier.grid(row=5, column=1, pady=10)

           book = ctk.CTkButton(self.TableBookingFTF, text="Book Reservation", command=self.SaveTableCredentialsCashier,fg_color=('#FC35B8','#FC35B8'),hover_color='#bd3e91',text_color='white')
           book.grid(row=6, column=1)

 def TableButtonClickCashier(self, number):

        self.TnumberCashier = number
        self.c.execute("SELECT Table_NUMBER FROM TableStatusFTF10 WHERE Table_NUMBER = ?", (number,))
        ExistingTable=self.c.fetchone()
        
        if ExistingTable:
         messagebox.showerror("Error",f"Table number {number} already reserved")
        else:
         return self.TnumberCashier
        
 def SaveTableCredentialsCashier(self):
        self.c.execute("SELECT Table_NUMBER FROM TableStatusFTF10 ")
        ExistingTable=self.c.fetchone()
        print('\n\nReserved Tables:',ExistingTable)
        if self.NAMECashier.get() and self.PHONENUMBERCashier.get():
            data = (self.TnumberCashier, self.NAMECashier.get(), self.PHONENUMBERCashier.get())
            self.con.execute("INSERT INTO TableStatusFTF10 (Table_NUMBER, NAME, PHONE_NUMBER) VALUES (?, ?, ?)", data)
            self.con.commit()
            self.c.execute('SELECT * FROM TableStatusFTF10 ')
            data = self.c.fetchall()
            print(data)
            
            messagebox.showinfo('Success Window','Table Reserved Successfully')
        else:
            messagebox.showerror ('Error Window',"Enter complete details please") 

     
    
 def LogoutFunctionAdmin(self):
       self.MainPageAdmin.destroy()
 def LogoutFunctionCustomer(self):
     self.MainPage.destroy()
 def LogoutFunctionCashier(self):
   self.MainPageCashier.destroy()

    

    
 def TotalOrdersFunctionCashier(self):
      if (self.SelectedItems==[]):#if no items in cart
       messagebox.showerror('Error','Select Menu item first')
      elif(self.NAMECartCashier.get() and self.Total.get()  ): #if Name is not empty and Total bill is not empty
      
       self.c.execute("INSERT INTO OrderFTF8 (NAME,BILL) VALUES (?,?)", (self.NAMECartCashier.get(),self.Total.get()))
       self.con.commit()
       self.c.execute("SELECT LAST_INSERT_ROWID() FROM  OrderFTF8")
       self.NewOrderEntryUpdate=self.c.fetchone()
       self.NewOrderEntryUpdate=str(self.NewOrderEntryUpdate).replace(',','')
       self.NewOrderEntryUpdate=str(self.NewOrderEntryUpdate).replace('(','')
       self.NewOrderEntryUpdate=str(self.NewOrderEntryUpdate).replace(')','')
       self.LatestOrderArrayCashier.append('Order#'+str(self.NewOrderEntryUpdate ))
       self.LatestOrderArray1Cashier=','.join(self.LatestOrderArrayCashier)
    #    self.SumOfOrdersCashier=self.SumOfOrdersCashier+1
       self.c.execute("SELECT COUNT (*) FROM OrderFTF8")
       self.EntriesCashier=self.c.fetchall()
       self.con.commit()
    #    print(self.EntriesCashier)
       self.NewOrderEntry.delete(0,tk.END)
       self.NewOrderEntry.insert(0,self.LatestOrderArray1Cashier)
       self.TotalOrderEntry.delete(0,tk.END)
       self.TotalOrderEntry.insert(0,self.EntriesCashier)
       messagebox.showinfo('Success Window','Order Submitted')

      else: #if Name of customer not entered by cashier
        messagebox.showerror('Error Window','Enter Name of Customer please')


 def InProgressUpdate(self):
     if(self.NAMECartCashier.get() and self.Total.get()  ):

       self.c.execute("SELECT LAST_INSERT_ROWID() FROM  OrderFTF8")
    #    self.c.execute("SELECT ID FROM  OrderFTF8 ORDER BY ID DESC LIMIT 1 OFFSET 1")

       
       self.LatestIDCashier=self.c.fetchone()
    #    self.LatestIDCashier=self.LatestIDCashier[:-1]
    #    print(self.LatestIDCashier)
       self.InProgressEntry.delete(0,tk.END)
      
       InProgressstr=f'Order#{self.LatestIDCashier}'
       InProgressstr=InProgressstr.replace(',','')
       InProgressstr=InProgressstr.replace('(','')
       InProgressstr=InProgressstr.replace(')','')
       self.InProgressEntry.insert(0,InProgressstr)
   

####################### Admin #####################################
       
 def MainPageAdminFunction(self):
       self.MainPageAdmin = ctk.CTkToplevel()
       self.MainPageAdmin.title('Main Page Admin')
       self.MainPageAdmin.config(bg='#FC3588')
       DefaultNumber=0
       DefaultStr='$0'
       
       canvas = Canvas(self.MainPageAdmin)
       LogoutAdmin=ctk.CTkButton(self.MainPageAdmin,text='Logout', font=("Times New Roman", 16),fg_color=('#FC35B8','#FC35B8'),hover_color='#bd3e91',text_color='white',corner_radius=0,command=self.LogoutFunctionAdmin)
       LogoutAdmin.grid(row=0,column=7)
         
       Logo=tk.Label(self.MainPageAdmin,text='Berrilicious', font=("Times New Roman", 16),fg='white',bg='#FC3588')
       Logo.grid(row=0,column=0,sticky='w',padx=10)
       
       BorderFrameDashboard = ctk.CTkFrame(self.MainPageAdmin,fg_color='white',border_color='black',border_width=3,corner_radius=0,width=130,height=250)
       BorderFrameDashboard.grid(row=1,rowspan=7, column=0,columnspan=2,pady=20)
       BorderFrameDashboard.grid_propagate(False)


       DashboardButton = ctk.CTkButton(BorderFrameDashboard, text="Dashboard", font=("Times New Roman", 16),fg_color=('#FC35B8','#FC35B8'),hover_color='#bd3e91',width=10)
       DashboardButton.grid(row=3,column=0,columnspan=3,pady=10)
       Salary = ctk.CTkButton(BorderFrameDashboard, text="Salary", font=("Times New Roman", 16),fg_color=('#FC35B8','#FC35B8'),hover_color='#bd3e91',width=10,command=self.SalaryFunction)
       Salary.grid(row=4,column=0, columnspan=2,pady=10)
       Attendence = ctk.CTkButton(BorderFrameDashboard, text="Attendence", font=("Times New Roman", 16),fg_color=('#FC35B8','#FC35B8'),hover_color='#bd3e91' ,width=10,command=self.AttendenceFunction)
       Attendence.grid(row=5,column=0,columnspan=2,pady=10)
       AddEmployees = ctk.CTkButton(BorderFrameDashboard, text="Add Employees", font=("Times New Roman", 16),fg_color=('#FC35B8','#FC35B8'),hover_color='#bd3e91',width=10,corner_radius=0,command=self.AddEmployeesFunctiontest)
       AddEmployees.grid(row=6,column=0,columnspan=2,pady=10,padx=10)#done on customer module
       AddMenu= ctk.CTkButton(BorderFrameDashboard, text="Add Menu", font=("Times New Roman", 16),fg_color=('#FC35B8','#FC35B8'),hover_color='#bd3e91',width=10,command=self.AddMenuFunction)
       AddMenu.grid(row=7,column=0,columnspan=2,pady=10)
       
      
      
       FrameOrders= ctk.CTkFrame(self.MainPageAdmin,fg_color=('#FC35B8','#FC35B8'),border_color='black',border_width=3,corner_radius=0)
       FrameOrders.grid(row=2, column=5,padx=20,pady=20)
       self.OrderEntry= ctk.CTkEntry(FrameOrders , font=("Times New Roman", 16),justify='center')
       self.OrderEntry.insert(0,DefaultNumber)
       self.OrderEntry.grid(row=3,column=5,pady=10)
       OrderLabel= tk.Label(FrameOrders, text="Orders", font=("Times New Roman", 12),justify='center',bg=('#FC35B8'))
       OrderLabel.grid(row=4,column=5,pady=10)

       FrameRevenue= ctk.CTkFrame(self.MainPageAdmin,fg_color=('#FC35B8','#FC35B8'),border_color='black',border_width=3,corner_radius=0)
       FrameRevenue.grid(row=2, column=6,padx=20,pady=20)
       self.RevenueEntry= ctk.CTkEntry(FrameRevenue , font=("Times New Roman", 16),justify='center' )
       self.RevenueEntry.insert(0,DefaultStr)
       self.RevenueEntry.grid(row=3,column=6,pady=10)
       RevenueLabel= tk.Label(FrameRevenue, text="Revenue", font=("Times New Roman", 12),justify='center',bg=('#FC35B8'))
       RevenueLabel.grid(row=4,column=6,pady=10)

       FrameCustomers= ctk.CTkFrame(self.MainPageAdmin,fg_color=('#FC35B8','#FC35B8'),border_color='black',border_width=3,corner_radius=0)
       FrameCustomers.grid(row=2, column=7,padx=20,pady=20)
       self.CustomerEntry= ctk.CTkEntry( FrameCustomers , font=("Times New Roman", 16))
       self.CustomerEntry.insert(0,DefaultNumber)
       self.CustomerEntry.grid(row=3,column=7,pady=10)
       CustomerLabel= tk.Label( FrameCustomers, text="Customers", font=("Times New Roman", 12),justify='center',bg=('#FC35B8'))
       CustomerLabel.grid(row=4,column=7,pady=10)
       self.ProfitGraph,self.ax= plt.subplots()
       canvas = FigureCanvasTkAgg(self.ProfitGraph, 
                               self.MainPageAdmin)   
       canvas.get_tk_widget().grid(row=7,column=5,columnspan=3,pady=10) 
       self.GraphButton = ctk.CTkButton(self.MainPageAdmin, text="Visualize Graph" ,fg_color=('#FC35B8','#FC35B8'),hover_color='#bd3e91',border_color='#FC3588',border_width=3,command=self.ProfitGraphFunction)
       self.GraphButton.grid(row=8, column=6, pady=10)
    
       self.c.execute('Select BILL from OrderFTF8')
       SumAll=self.c.fetchall()
       self.con.commit()
       TotalBill=0
       for LastColumn in SumAll:
          TotalBill += LastColumn[0]
      #  print(totalbill)
       TotalBillStr=f'${TotalBill}'
       self.RevenueEntry.delete(0,tk.END)
       self.RevenueEntry.insert(0,TotalBillStr)

       self.c.execute("SELECT ID FROM  OrderFTF8 ORDER BY ID DESC LIMIT 1 OFFSET 1")
       self.LatestIDAdmin=self.c.fetchone()
       print(self.LatestIDAdmin)
       self.con.commit()
       self.RevenueEntry.delete(0,tk.END)
       self.RevenueEntry.insert(0,TotalBillStr)
       self.CustomerEntry.delete(0,tk.END)
       self.CustomerEntry.insert(0,self.LatestIDAdmin)
       self.OrderEntry.delete(0,tk.END)
       self.OrderEntry.insert(0,self.LatestIDAdmin)
 def  ProfitGraphFunction(self):
       

       self.c.execute('Select BILL from OrderFTF8')
       SumAll=self.c.fetchall()
       self.con.commit()
       Y1=0 
       Y1=SumAll[0]+SumAll[1]
       YDay1=Y1[0]+Y1[1]
       Y2=0 
       Y2=SumAll[2]+SumAll[3]+SumAll[4]
       YDay2=Y2[0]+Y2[1]+Y2[2]
       Y3=0 
       Y3=SumAll[5]+SumAll[6]
       YDay3=Y3[0]+Y3[1]
       Y4=0 
       Y4=SumAll[7]+SumAll[8]+SumAll[9]
       YDay4=Y4[0]+Y4[1]+Y4[2]
       Y5=0 
       Y5=SumAll[10]+SumAll[11]+SumAll[12]+SumAll[13]+SumAll[14]
       YDay5=Y5[0]+Y5[1]+Y5[2]+Y5[3]+Y5[4]
       Y6=0 
       Y6=SumAll[15]+SumAll[16]+SumAll[17]
       YDay6=Y6[0]+Y6[1]+Y6[2]
       Y7=0 
       Y7=SumAll[18]+SumAll[19]+SumAll[20]+SumAll[21]
       YDay7=Y7[0]+Y7[1]+Y7[2]+Y7[3]
      

       Y=[YDay1,YDay2,YDay3,YDay4,YDay5,YDay6,YDay7]
       X=['Day1','Day2','Day3','Day4','Day5','Day6','Day7']
       Profit, axis = plt.subplots()

       axis.plot(X,Y,marker='o',linestyle='-',color='#FC3588')
       axis.set_title('Profit Graph')
       Profitgraph = FigureCanvasTkAgg(Profit, self.MainPageAdmin)
       Profitgraph.get_tk_widget().grid(row=7,column=5,columnspan=3,pady=10)
       
 def SalaryUpdateFunction(self):
         GetDesignation=self.DesignationEntry.get()
         print(f'designation: {GetDesignation}')
         GetSalary= self.UpdateSalaryEntry.get()

         if GetDesignation==self.DesignationList[0]:#Cashier selected
            self.SalaryLabel1.config(text=str(GetSalary))
            
            self.c.execute("UPDATE Salaries1 SET Salary = ? WHERE ID = 1;", (str(GetSalary),))
            self.con.commit()


            self.c.execute("SELECT Salary  FROM  Salaries1")
            self.SalaryDbsal=self.c.fetchall()
            print(self.SalaryDbsal)
            messagebox.showinfo('Success','Salary Updated')
            # print(self.SalaryList)
         elif GetDesignation==self.DesignationList[1]:#Chef selected
             self.SalaryLabel2.config(text=str(GetSalary))
             self.c.execute("UPDATE Salaries1 SET Salary = ? WHERE ID = 2;", (str(GetSalary),))
             self.con.commit()


             self.c.execute("SELECT Salary  FROM  Salaries1")
             self.SalaryDbsal=self.c.fetchall()
             print(self.SalaryDbsal)
             messagebox.showinfo('Success','Salary Updated')
         elif GetDesignation==self.DesignationList[2]:#Waiter selected
             self.SalaryLabel3.config(text=str(GetSalary))
             self.c.execute("UPDATE Salaries1 SET Salary = ? WHERE ID = 3;", (str(GetSalary),))
             self.con.commit()


             self.c.execute("SELECT Salary  FROM  Salaries1")
             self.SalaryDbsal=self.c.fetchall()
             print(self.SalaryDbsal)
             messagebox.showinfo('Success','Salary Updated')
         elif GetDesignation==self.DesignationList[3]:#sweeper selected
             self.SalaryLabel4.config(text=str(GetSalary))
             self.c.execute("UPDATE Salaries1 SET Salary = ? WHERE ID = 4;", (str(GetSalary),))
             self.con.commit()


             self.c.execute("SELECT Salary  FROM  Salaries1")
             self.SalaryDbsal=self.c.fetchall()
             print(self.SalaryDbsal)
             messagebox.showinfo('Success','Salary Updated')
         elif GetDesignation=='' or GetSalary=='': #No designation or salary entered in entry widget
             messagebox.showerror('Error',' Designation or salary not entered ')
         else:#Incorrect designation entered
          messagebox.showerror('Error','Incorrect designation or salary entered ')
         
         
         
 def SalaryFunction(self):
      self.con.execute('''CREATE Table IF NOT EXISTS  Salaries1 (
                                ID INTEGER PRIMARY KEY AUTOINCREMENT,
                                 
                                Designation VARCHAR(30),
                                Salary VARCHAR(8)
                                
                            );''')
      self.con.commit()
      self.DesignationList=['Cashier','Chef','Waiter','Sweeper']
      self.SalaryList=['2000','2000','1000','500']
      # for i in range(len(self.SalaryList)):
      #  self.c.execute("INSERT INTO Salaries1 (Designation,Salary) VALUES (?,?)", (self.DesignationList[i],self.SalaryList[i]))
      #  self.con.commit()


      self.c.execute("SELECT  COUNT (*)  FROM  Salaries1")
      self.SalaryDb=self.c.fetchall()
      print(self.SalaryDb)

      self.SalaryWindow = ctk.CTkToplevel()
      self.SalaryWindow.title('Salary')
      self.SalaryWindow.config(bg='#FC3588')
      FrameSalary= ctk.CTkFrame(self.SalaryWindow,fg_color=('#FC35B8','#FC35B8'),border_color='black',border_width=3,corner_radius=0)
      FrameSalary.grid(row=1, column=0,columnspan=3,padx=20,pady=20)
      SalaryLabel=tk.Label(self.SalaryWindow,text='Salaries' ,font=('Times New Roman',17,'bold'),fg='white',bg='#FC3588')
      SalaryLabel.grid(row=0,column=0,columnspan=3)
      HeaderDesignation=tk.Label(FrameSalary,text='Designation',font=('Times New Roman',15,'bold'),fg='white',bg='#FC35B8')
      HeaderDesignation.grid(row=1,column=0,padx=10,pady=10)
      HeaderSalary=tk.Label(FrameSalary,text='Salary',font=('Times New Roman',15,'bold'),fg='white',bg='#FC35B8')
      HeaderSalary.grid(row=1,column=1,padx=10,pady=10)
      
      
      for i in range (len(self.DesignationList)):
         self.DesignationLabel=tk.Label(FrameSalary,text=self.DesignationList[i] ,font=('Times New Roman',13),fg='white',bg='#FC35B8')
         self.DesignationLabel.grid(row=i+2,column=0,padx=10,pady=10)

      self.c.execute("SELECT Salary FROM Salaries1")
      Salary0 = self.c.fetchall()

      self.SalaryLabel1=tk.Label(FrameSalary,text=(Salary0[0]) ,font=('Times New Roman',13),fg='white',bg='#FC35B8')
      self.SalaryLabel1.grid(row=2,column=1,padx=10,pady=10)
      
      self.SalaryLabel2=tk.Label(FrameSalary,text=(Salary0[1]) ,font=('Times New Roman',13),fg='white',bg='#FC35B8')
      self.SalaryLabel2.grid(row=3,column=1,padx=10,pady=10)

     
      self.SalaryLabel3=tk.Label(FrameSalary,text=(Salary0[2]) ,font=('Times New Roman',13),fg='white',bg='#FC35B8')
      self.SalaryLabel3.grid(row=4,column=1,padx=10,pady=10)

      
      self.SalaryLabel4=tk.Label(FrameSalary,text=(Salary0[3]) ,font=('Times New Roman',13),fg='white',bg='#FC35B8')
      self.SalaryLabel4.grid(row=5,column=1,padx=10,pady=10)
      
      DesignationLbl=tk.Label(self.SalaryWindow,text='Designation',font=('Times New Roman',13,'bold'),fg='white',bg='#FC3588')
      DesignationLbl.grid(row=7,column=0,padx=10,pady=10)
      self.DesignationEntry=ctk.CTkEntry(self.SalaryWindow , font=("Times New Roman", 13))
      self.DesignationEntry.grid(row=7,column=1,padx=10,pady=10)
      UpdateSalaryLbl=tk.Label(self.SalaryWindow,text= 'Salary' ,font=('Times New Roman',13,'bold'),fg='white',bg='#FC3588')
      UpdateSalaryLbl.grid(row=8,column=0,padx=10,pady=10)
      self.UpdateSalaryEntry=ctk.CTkEntry( self.SalaryWindow , font=("Times New Roman", 13))
      self.UpdateSalaryEntry.grid(row=8,column=1,padx=10,pady=10)
      UpdateSalary= ctk.CTkButton(self.SalaryWindow, text="Update Salary", font=("Times New Roman", 16),fg_color=('#FC35B8','#FC35B8'),hover_color='#bd3e91',width=10,command=self.SalaryUpdateFunction)
      UpdateSalary.grid(row=10,column=0,columnspan=2,pady=10)
    

 def AddMenuFunction(self):
      self.AddMenuWindow = ctk.CTkToplevel()
      self.AddMenuWindow.title('Add Menu')
      self.AddMenuWindow.config(bg='#FC3588')
      AddMenuLabel=tk.Label(self.AddMenuWindow,text='Add Menu' ,font=('Times New Roman',17,'bold'),fg='white',bg='#FC3588')
      AddMenuLabel.grid(row=0,column=0,columnspan=3)

      FrameAddMenu= ctk.CTkFrame(self.AddMenuWindow,fg_color=('#FC35B8','#FC35B8'),border_color='black',border_width=3,corner_radius=0)
      FrameAddMenu.grid(row=1,rowspan=4, column=0,columnspan=3,padx=20,pady=20)

      CategoryLbl=tk.Label(FrameAddMenu,text='Category:',font=('Times New Roman',13,'bold'),fg='white',bg='#FC35B8')
      CategoryLbl.grid(row=1,column=0,padx=10,pady=10)
      self.CategoryEntry=ctk.CTkEntry(FrameAddMenu , font=("Times New Roman", 13))
      self.CategoryEntry.grid(row=1,column=1,padx=10,pady=10)
      ItemLbl=tk.Label(FrameAddMenu,text= 'Item:' ,font=('Times New Roman',13,'bold'),fg='white',bg='#FC35B8')
      ItemLbl.grid(row=2,column=0,padx=10,pady=10)
      self.ItemEntry=ctk.CTkEntry( FrameAddMenu, font=("Times New Roman", 13))
      self.ItemEntry.grid(row=2,column=1,padx=10,pady=10)
      PriceLbl=tk.Label(FrameAddMenu,text= 'Price:' ,font=('Times New Roman',13,'bold'),fg='white',bg='#FC35B8')
      PriceLbl.grid(row=3,column=0,padx=10,pady=10)
      self. PriceEntry=ctk.CTkEntry( FrameAddMenu , font=("Times New Roman", 13))
      self.PriceEntry.grid(row=3,column=1,padx=10,pady=10)

        
      AddMenuButton= ctk.CTkButton(self.AddMenuWindow, text=" Add Item", font=("Times New Roman", 16),fg_color=('#FC35B8','#FC35B8'),hover_color='#bd3e91',width=10,command=self.UpdateMenuFunction)
      AddMenuButton.grid(row=5,column=0,columnspan=3,pady=10)
 def UpdateMenuFunction(self):
        if self.CategoryEntry.get()=='Icecream'  : #if admin selected Ice cream category
            DataMenu= (self.ItemEntry.get(),self.PriceEntry.get())
            self.c.execute("INSERT INTO ICECREAM41 (ITEM,PRICE) VALUES (?, ?)",DataMenu )
            self.con.commit()
            self.c.execute("INSERT INTO ICECREAMCUST42 (ITEM,PRICE) VALUES (?, ?)",DataMenu )
            self.con.commit()
            self.c.execute('SELECT * FROM ICECREAM41 ')
            data = self.c.fetchall()
            print(data)
            messagebox.showinfo('Success','Item added')
             
        elif self.CategoryEntry.get()=='Beverage'  : #if admin selected Beverage category
            DataMenu= (self.ItemEntry.get(),self.PriceEntry.get())
            self.c.execute("INSERT INTO BEVERAGE3 (ITEM,PRICE) VALUES (?, ?)",DataMenu )
            self.con.commit()
            self.c.execute("INSERT INTO BEVERAGECUST4 (ITEM,PRICE) VALUES (?, ?)",DataMenu )
            self.con.commit()
            self.c.execute('SELECT * FROM BEVERAGE3 ')
            data = self.c.fetchall()
            print(data)
            messagebox.showinfo('Success','Item added')

        elif self.CategoryEntry.get()=='Sundae'  :#if admin selected Sundae category
            DataMenu= (self.ItemEntry.get(),self.PriceEntry.get())
            self.c.execute("INSERT INTO SUNDAE3 (ITEM,PRICE) VALUES (?, ?)",DataMenu )
            self.con.commit()
            self.c.execute("INSERT INTO SUNDAECUST4 (ITEM,PRICE) VALUES (?, ?)",DataMenu )
            self.con.commit()
            self.c.execute('SELECT * FROM SUNDAE3 ')
            data = self.c.fetchall()
            print(data)
            messagebox.showinfo('Success','Item added')
            
        elif  self.CategoryEntry.get()==''or self.ItemEntry.get()=='' or self.PriceEntry.get()=='':#if admin  did not select any category 
            # self.ErrorMessageTable()
            messagebox.showerror('Error','Enter Category please')
        else:#any other exception 
            messagebox.showinfo('Error','Incorrect details entered')
    
       
 def AddEmployeesFunctiontest(self):
      self.AddEmployeesWindow = tk.Toplevel()
      self.AddEmployeesWindow.title('Add Employee')
      ENameLab = tk.Label(self.AddEmployeesWindow, text="Name:")
      ENameLab.pack(anchor=tk.S)
      self.EName = ctk.CTkEntry(self.AddEmployeesWindow)
    #   self.EName.insert(0, '')
      self.EName.pack(anchor=tk.S)
      EPasswordLab = tk.Label(self.AddEmployeesWindow, text="Password:")
      EPasswordLab.pack(anchor=tk.S)
      self.EPassword = ctk.CTkEntry(self.AddEmployeesWindow, show='.')
    #   self.EPassword.insert(0, show='.')
      self.EPassword.pack(anchor=tk.S)
      AddEmployeeButton = ctk.CTkButton(self.AddEmployeesWindow, text="Add Employee", command=self.AddEmployeesFunction, font=("Times New Roman", 16),fg_color=('#FC35B8','#FC35B8'),hover_color='#bd3e91',width=10,border_color='#FC3588')
      AddEmployeeButton.pack(anchor=tk.S,pady=10)
 def AddEmployeesFunction(self):
        nameC=self.EName.get()
        passwordC=self.EPassword.get()
        if(nameC and passwordC): #if Name and password entered
         self.con.execute('INSERT INTO CashierNames (NAME,PASSWORD) VALUES (?,?)', (nameC,passwordC))
         self.con.commit()
         self.c.execute("SELECT LAST_INSERT_ROWID() FROM CashierNames  ")
         self.NewCashier=self.c.fetchone()
         print(self.NewCashier)
         messagebox.showinfo('Success Window','Employee Added Succesfully')
        else:#if Name and password left empty
            messagebox.showerror('Error Window','Enter Name and Password please')

 def AttendenceFunction(self):
  self.AttendenceWindow = ctk.CTkToplevel()
  self.AttendenceWindow.title('Attendence')
  #Function to select either present or absent not both
  def Absent(n):
      if self.AVar[n].get() == 1:
            self.PVar[n].set(0)
  def Present(n):
       if self.AVar[n].get() == 1:
            self.PVar[n].set(0)
#   self.AVar=tk.IntVar()
#   self.PVar=tk.IntVar()
  self.c.execute("SELECT COUNT (*) FROM CashierNames") #Cashier names from databse
  self.CountCashier=self.c.fetchall()
  self.con.commit()
  self.c.execute("SELECT ID FROM CashierNames LIMIT 4")
  self.IDCashier=self.c.fetchall()
  self.con.commit()
  self.c.execute("SELECT NAME FROM CashierNames LIMIT 4")
  self.NameCashier=self.c.fetchall()
  self.con.commit()
  WaitersList=[(1,'Latif Ahmed'),(2,'Misbah Ali'),(3,'Usama Sidique')] #Waiters name list
  AttendenceLabel=tk.Label(self.AttendenceWindow,text='Attendence',font=('Times New Roman',16,'bold'))
  AttendenceLabel.grid(row=0,column=0)
  headerID=tk.Label(self.AttendenceWindow,text='ID')
  headerID.grid(row=1,column=0)
  headerName=tk.Label(self.AttendenceWindow,text='Name')
  headerName.grid(row=1,column=1)
  headerDesignation=tk.Label(self.AttendenceWindow,text='Designation')
  headerDesignation.grid(row=1,column=2)
  headerStatus=tk.Label(self.AttendenceWindow,text='Status')
  headerStatus.grid(row=1,column=3)
   

    
  self.W1 = tk.Entry(self.AttendenceWindow, width=20, fg='black')
  self.W1.grid(row=2, column=0)
  self.W1.insert(tk.END,WaitersList[0][0])
  self.W2 = tk.Entry(self.AttendenceWindow, width=20, fg='black')
  self.W2.grid(row=3, column=0)
  self.W2.insert(tk.END,WaitersList[1][0])
  self.W3 = tk.Entry(self.AttendenceWindow, width=20, fg='black')
  self.W3.grid(row=4, column=0)
  self.W3.insert(tk.END,WaitersList[2][0])

  self.W1Name = tk.Entry(self.AttendenceWindow, width=20, fg='black')
  self.W1Name.grid(row=2, column=1)
  self.W1Name.insert(tk.END,WaitersList[0][1])
  self.W2Name = tk.Entry(self.AttendenceWindow, width=20, fg='black')
  self.W2Name.grid(row=3, column=1)
  self.W2Name.insert(tk.END,WaitersList[1][1])
  self.W3Name = tk.Entry(self.AttendenceWindow, width=20, fg='black')
  self.W3Name.grid(row=4, column=1)
  self.W3Name.insert(tk.END,WaitersList[2][1])


  self.W1Designation = tk.Entry(self.AttendenceWindow, width=20, fg='black')
  self.W1Designation.grid(row=2, column=2)
  self.W1Designation.insert(tk.END, 'Waiter')
  self.W2Designation = tk.Entry(self.AttendenceWindow, width=20, fg='black')
  self.W2Designation.grid(row=3, column=2)
  self.W2Designation.insert(tk.END,'Waiter')
  self.W3Designation = tk.Entry(self.AttendenceWindow, width=20, fg='black')
  self.W3Designation.grid(row=4, column=2)
  self.W3Designation.insert(tk.END,'Waiter')
  AVar1,AVar2,AVar3,AVar4,AVar5,AVar6,AVar7,PVar1,PVar2,PVar3,PVar4,PVar5,PVar6,PVar7=0,0,0,0,0,0,0,0,0,0,0,0,0,0
  self.AVar=[ AVar1,AVar2,AVar3,AVar4,AVar5,AVar6,AVar7]
  self.AVar = [tk.IntVar() for _ in range(7)]   
  self.PVar=[ PVar1,PVar2,PVar3,PVar4,PVar5,PVar6,PVar7 ]
  self.PVar = [tk.IntVar() for _ in range(7)]
   
  self.W1A = tk.Checkbutton(self.AttendenceWindow,text='Absent', width=10, fg='black',bg='red',variable=self.AVar[0],command=lambda:Absent(0))
  self.W1A.grid(row=2, column=3)
  
  self.W2A = tk.Checkbutton(self.AttendenceWindow,text='Absent', width=10, fg='black',bg='red',variable=self.AVar[1],command=lambda:Absent(1))
  self.W2A.grid(row=3, column=3)
   
  self.W3A= tk.Checkbutton(self.AttendenceWindow,text='Absent', width=10, fg='black',bg='red',variable=self.AVar[2],command=lambda:Absent(2))
  self.W3A.grid(row=4, column=3)

  self.W1P = tk.Checkbutton(self.AttendenceWindow,text='Present', width=10, fg='black',bg='green',variable=self.PVar[0],command=lambda:Present(0))
  self.W1P.grid(row=2, column=4)
  
  self.W2P = tk.Checkbutton(self.AttendenceWindow,text='Present', width=10, fg='black',bg='green',variable=self.PVar[1],command=lambda:Present(1))
  self.W2P.grid(row=3, column=4)
   
  self.W3P= tk.Checkbutton(self.AttendenceWindow,text='Present', width=10, fg='black',bg='green',variable=self.PVar[2],command=lambda:Present(2))
  self.W3P.grid(row=4,column=4)

  print(self.NameCashier[0])
  print(self.IDCashier)
  name=''
  for i in range (len(self.IDCashier)):
   name=str(self.NameCashier[i])
   name.strip('{}')
   print(name)

  
  for i in range (len(self.IDCashier)):
        self.CID = tk.Entry(self.AttendenceWindow, width=20, fg='black')
        self.CID.grid(row=5+i, column=0,pady=5)
        self.CID.insert(tk.END,self.IDCashier[i][0])

  for i in range (len(self.IDCashier)):
        # self.NameCashier[i].replace('{','')
        Name=str(self.NameCashier[i]).strip('('',)')
        self.CName = tk.Entry(self.AttendenceWindow, width=20, fg='black')
        self.CName.grid(row=5+i, column=1,pady=5)
        self.CName.insert(tk.END,Name.replace("'",''))
  for i in range (len(self.IDCashier)):
       
        self.CDesig = tk.Entry(self.AttendenceWindow, width=20, fg='black')
        self.CDesig.grid(row=5+i, column=2,pady=5)
        self.CDesig.insert(tk.END,'Cashier')

  
   
  
  self.CA1 = tk.Checkbutton(self.AttendenceWindow, width=10, fg='black',bg='red',text='Absent',variable= self.AVar[3],command=lambda:Absent(3))
  self.CA1.grid(row=5, column=3)
  self.CA2 = tk.Checkbutton(self.AttendenceWindow, width=10, fg='black',bg='red',text='Absent',variable= self.AVar[4],command=lambda:Absent(4))
  self.CA2.grid(row=6, column=3)
  self.CA3 = tk.Checkbutton(self.AttendenceWindow, width=10, fg='black',bg='red',text='Absent',variable= self.AVar[5],command=lambda:Absent(5))
  self.CA3.grid(row=7, column=3)
  self.CA4 = tk.Checkbutton(self.AttendenceWindow, width=10, fg='black',bg='red',text='Absent',variable= self.AVar[6],command=lambda:Absent(6))
  self.CA4.grid(row=8, column=3)

  self.CP1 = tk.Checkbutton(self.AttendenceWindow, width=10, fg='black',bg='green',text='Present',variable= self.PVar[3],command=lambda:Present(3))
  self.CP1.grid(row=5, column=4)
  self.CP2 = tk.Checkbutton(self.AttendenceWindow, width=10, fg='black',bg='green',text='Present',variable= self.PVar[4],command=lambda:Present(4))
  self.CP2.grid(row=6, column=4)
  self.CP3 = tk.Checkbutton(self.AttendenceWindow, width=10, fg='black',bg='green',text='Present',variable= self.PVar[5],command=lambda:Present(5))
  self.CP3.grid(row=7, column=4)
  self.CP4 = tk.Checkbutton(self.AttendenceWindow, width=10, fg='black',bg='green',text='Present',variable= self.PVar[6],command=lambda:Present(6))
  self.CP4.grid(row=8, column=4)

  
  self.SubmitAttendence = tk.Button(self.AttendenceWindow, width=20, fg='black',bg='#27b356',text='Save',justify='center',command=self.AttendenceSave)
  self.SubmitAttendence.grid(row=12,column=2,columnspan=1,pady=0)

 def AttendenceSave(self):
       if (self.PVar[0].get() or self.AVar[0].get() and self.PVar[1].get() or self.AVar[1].get() and self.PVar[2].get() or self.AVar[2].get() and self.PVar[3].get() or self.AVar[3].get() and self.PVar[4].get() or self.AVar[4].get() and self.PVar[5].get() or self.AVar[5].get() and self.PVar[6].get() or self.AVar[6].get()   ) :
       
        messagebox.showinfo('Success','Attendence marked')
       else:
          messagebox.showerror('Error','Attendence not marked')
 
 

if __name__ == "__main__":
 application=Restaurant()