from tkinter import *
#from PIL import ImageTk,Image
from tkinter import messagebox
import pyodbc
import logging


def customerRegister():
    
    ID = custid.get()
    NAME = name.get()

    AGE= age.get()
    ADDRESS = address.get()
    SALARY= salary.get()
    

    insertBooks = "insert into "+customerTable+" values('"+ID+"','"+NAME+"','"+AGE+"','"+ADDRESS+"','"+SALARY+"')"
    
    try:
        cur.execute(insertBooks)
        conn.commit()
        messagebox.showinfo('Success',"customers added successfully")
    except ValueError:
        logging.debug(custid)
        messagebox.showinfo("Error","Can't add data into Database")
    
    
    root.destroy()
    
def addCustomer():
    
    global custid,name,age,address,salary,conn,customerTable,cur,root
    
    root = Tk()
    root.title("Sales_Customers")
    root.minsize(width=400,height=800)
    root.geometry("800x700")

    # Add your own database name and password here to reflect in the code
    #mypass = "root"
    #mydatabase="db"

    conn = pyodbc.connect('Driver={SQL Server};'
                          'Server=LAPTOP-E87J5PNF\SQLEXPRESS;'
                          'Database=BikeStores;'
                          'Trusted_Connection=yes;')


    cur = conn.cursor()
    #cur.execute('SELECT * FROM BikeStores.sales.customers')

    #for row in cur:
       # print(row)

    # Enter Table Names here
    customerTable = "BikeStores.dbo.CUSTOMERS" # Book Table

    Canvas1 = Canvas(root)
    
    Canvas1.config(bg="#ff6e11")
    Canvas1.pack(expand=True,fill=BOTH)
        
    headingFrame1 = Frame(root,bg="#BBBB40",bd=5)
    headingFrame1.place(x=100,y=40,relwidth=0.5,relheight=0.13)

    headingLabel = Label(headingFrame1, text="Add customers", bg='black', fg='white', font=('Courier',15))
    headingLabel.place(relx=0,rely=0, relwidth=1, relheight=1)


    labelFrame = Frame(root,bg='black')
    labelFrame.place(x=70,y=300,relwidth=0.8,relheight=0.7)

    # Customer ID
    lb1 = Label(labelFrame,text="Customer ID : ", bg='black', fg='white')
    lb1.place(x=20,y=20, relheight=0.08)
        
    custid = Entry(labelFrame)
    custid.place(x=100,y=30, relwidth=0.3, relheight=0.09)
     
        
    # name
    lb3 = Label(labelFrame,text="Name: ", bg='black', fg='white')
    lb3.place(x=20,y=150, relheight=0.08)
        
    name = Entry(labelFrame)
    name.place(x=100,y=150, relwidth=0.3, relheight=0.08)
        
    #age
    lb4 = Label(labelFrame,text="Age: ", bg='black', fg='white')
    lb4.place(x=320,y=150, relheight=0.08)
        
    age = Entry(labelFrame)
    age.place(x=400,y=150, relwidth=0.3, relheight=0.08)

   
    
    # city
    lb4 = Label(labelFrame, text="Address: ", bg='black', fg='white')
    lb4.place(x=20, y=340, relheight=0.08)

    address = Entry(labelFrame)
    address.place(x=100, y=340, relwidth=0.3, relheight=0.08)

    # salary
    lb4 = Label(labelFrame, text="Salary: ", bg='black', fg='white')
    lb4.place(x=320, y=340, relheight=0.08)

    salary = Entry(labelFrame)
    salary.place(x=400, y=340, relwidth=0.3, relheight=0.08)

    
        
    #Submit Button
    SubmitBtn = Button(root,text="SUBMIT",bg='#d1ccc0', fg='black',command=customerRegister)
    SubmitBtn.place(relx=0.28,rely=0.9, relwidth=0.18,relheight=0.03)
    
    quitBtn = Button(root,text="Quit",bg='#f7f1e3', fg='black', command=root.destroy)
    quitBtn.place(relx=0.53,rely=0.9, relwidth=0.18,relheight=0.03)
    
    root.mainloop()