from tkinter import *
#from PIL import ImageTk,Image
from tkinter import messagebox
import pyodbc



def deleteCustomer():
    
    ID = customer_id.get()
    CUSTOMERS = "BikeStores.dbo.CUSTOMERS"
    deleteSql = "delete from "+CUSTOMERS+" where ID = '"+ID+"'"
    try:
        cur.execute(deleteSql)
        con.commit()
        messagebox.showinfo('Success',"Customer Record Deleted Successfully")
    except:
        messagebox.showinfo("Please check Customer ID")
    


    print(ID)
    customer_id.delete(0, END)
    root.destroy()
    
def delete(): 
    
    global customer_id,name,age,address,salary,Canvas1,con,cur,CUSTOMERS,root
    con = pyodbc.connect('Driver={SQL Server};'
                          'Server=LAPTOP-E87J5PNF\SQLEXPRESS;'
                          'Database=BikeStores;'
                          'Trusted_Connection=yes;')


    cur = con.cursor()
    CUSTOMERS = "BikeStores.dbo.CUSTOMERS"
    root = Tk()
    root.title("Sales_customers")
    root.minsize(width=400,height=400)
    root.geometry("600x500")

    
    Canvas1 = Canvas(root)
    
    Canvas1.config(bg="#006B03")
    Canvas1.pack(expand=True,fill=BOTH)
        
    headingFrame1 = Frame(root,bg="#FFBF60",bd=5)
    headingFrame1.place(relx=0.25,rely=0.1,relwidth=0.5,relheight=0.13)
        
    headingLabel = Label(headingFrame1, text="Delete Customer", bg='black', fg='white', font=('Courier',15))
    headingLabel.place(relx=0,rely=0, relwidth=1, relheight=1)
    
    labelFrame = Frame(root,bg='black')
    labelFrame.place(relx=0.1,rely=0.3,relwidth=0.8,relheight=0.5)   
        
    # Customer ID to Delete
    lb2 = Label(labelFrame,text="Customer ID : ", bg='black', fg='white')
    lb2.place(relx=0.05,rely=0.5)
        
    customer_id = Entry(labelFrame)
    customer_id.place(relx=0.3,rely=0.5, relwidth=0.62)
    
    #Submit Button
    SubmitBtn = Button(root,text="SUBMIT",bg='#d1ccc0', fg='black',command=deleteCustomer)
    SubmitBtn.place(relx=0.28,rely=0.9, relwidth=0.18,relheight=0.08)
    
    quitBtn = Button(root,text="Quit",bg='#f7f1e3', fg='black', command=root.destroy)
    quitBtn.place(relx=0.53,rely=0.9, relwidth=0.18,relheight=0.08)
    
    root.mainloop()