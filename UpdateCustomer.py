from tkinter import *

from tkinter import messagebox
import pyodbc



conn = pyodbc.connect('Driver={SQL Server};'
                          'Server=LAPTOP-E87J5PNF\SQLEXPRESS;'
                          'Database=BikeStores;'
                          'Trusted_Connection=yes;')


cur = conn.cursor()

# Enter Table Names here
customerTable = "BikeStores.dbo.CUSTOMERS"  # Book Table


# logging.basicConfig(filename='customer.log', level=logging.DEBUG)
def update():
    ID= custid.get()
    NAME = name.get()
    updateBooks = "UPDATE " + customerTable + " SET name = '" + NAME + "' where ID = '" + ID+ "'"
    try:
        cur.execute(updateBooks)
        conn.commit()
        messagebox.showinfo('Success', "customers info updated successfully")
    except ValueError:
        # logging.debug(custid)
        messagebox.showinfo("Error", "Can't update data into Database")


    
def updateCustomer():
    
    global updateBtn, labelFrame, lb1, quitBtn, root, Canvas1, custid,name, conn
    
    root = Tk()
    root.title("Customers")
    root.minsize(width=400,height=400)
    root.geometry("600x500")
    
    Canvas1 = Canvas(root)
    Canvas1.config(bg="#D6ED99")
    Canvas1.pack(expand=True,fill=BOTH)

    headingFrame1 = Frame(root,bg="#FBBB55",bd=5)
    headingFrame1.place(relx=0.25,rely=0.1,relwidth=0.5,relheight=0.13)
        
    headingLabel = Label(headingFrame1, text="Update Customers", bg='black', fg='white', font=('Courier',15))
    headingLabel.place(relx=0,rely=0, relwidth=1, relheight=1)
    
    labelFrame = Frame(root,bg='black')
    labelFrame.place(relx=0.1,rely=0.3,relwidth=0.8,relheight=0.5)  
        
    # Customer ID
    lb1 = Label(labelFrame, text="Customer ID : ", bg='black', fg='white')
    lb1.place(x=20, y=20, relheight=0.28)

    custid = Entry(labelFrame)
    custid.place(x=100, y=30, relwidth=0.3, relheight=0.09)
    # first name
    lb2 = Label(labelFrame, text="Name : ", bg='black', fg='white')
    lb2.place(x=120, y=120, relheight=0.28)

    name = Entry(labelFrame)
    name.place(x=200, y=130, relwidth=0.3, relheight=0.09)

    
    #update Button
    updateBtn = Button(root, text="Update",bg='#d1ccc0', fg='black',command=update)
    updateBtn.place(relx=0.28, rely=0.9, relwidth=0.18,relheight=0.08)
    
    quitBtn = Button(root,text="Quit",bg='#aaa69d', fg='black', command=root.destroy)
    quitBtn.place(relx=0.53,rely=0.9, relwidth=0.18,relheight=0.08)
    
    root.mainloop()