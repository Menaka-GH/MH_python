from tkinter import *
import pyodbc
from tkinter import messagebox
from AddCustomer import *
from UpdateCustomer import *
from DeleteCustomer import *
# Add database name 

conn = pyodbc.connect('Driver={SQL Server};'
                          'Server=LAPTOP-E87J5PNF\SQLEXPRESS;'
                          'Database=BikeStores;'
                          'Trusted_Connection=yes;')

cur = conn.cursor()
root = Tk()
root.title("Sales")
root.minsize(width=400,height=800)
root.geometry("600x500")
headingFrame1 = Frame(root,bg="#FFBB00",bd=5)
headingFrame1.place(relx=0.2,rely=0.1,relwidth=0.6,relheight=0.16)

headingLabel = Label(headingFrame1, text="Welcome to \n Customers Database System", bg='black', fg='white', font=('Courier',15))
headingLabel.place(relx=0,rely=0, relwidth=1, relheight=1)

btn1 = Button(root,text="Add Customer Details",bg='black', fg='white', command=addCustomer)
btn1.place(relx=0.28,rely=0.4, relwidth=0.45,relheight=0.1)

    
btn2 = Button(root,text="Delete Customer",bg='black', fg='white', command=delete)
btn2.place(relx=0.28,rely=0.5, relwidth=0.45,relheight=0.1)
    
btn3 = Button(root,text="Update Customer List",bg='black', fg='white', command=updateCustomer)
btn3.place(relx=0.28,rely=0.6, relwidth=0.45,relheight=0.1)    

root.mainloop()