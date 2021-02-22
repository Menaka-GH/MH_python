from tkinter import *
#from PIL import ImageTk,Image
from tkinter import messagebox
import pyodbc
import logging

#logging.basicConfig(filename='customer.log', level=logging.DEBUG)
def customerRegister():
    
    customer_id = custid.get()
    first_name = firstname.get()
    last_name = lastname.get()
    phone = phone_no.get()
    email = email_id.get()
    street = street_name.get()
    city = city_name.get()
    state = state_name.get()
    zip_code = zipcode.get()

    insertBooks = "insert into "+customerTable+" values('"+customer_id+"','"+first_name+"','"+last_name+"','"+phone+"','"+email+"','"+street+"','"+city+"','"+state+"','"+zip_code+"')"
    # insertBooks = ("INSERT INTO BikeStores.sales.customers(customer_id, firstname, lastname, phone_no, email_id, street_name, city_name, state_name, zipcode) VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?)")
    #values = [customer_id, first_name, last_name, phone, email, street, city, state, zip_code]
    try:
        cur.execute(insertBooks)
        conn.commit()
        messagebox.showinfo('Success',"customers added successfully")
    except ValueError:
        logging.debug(custid)
        messagebox.showinfo("Error","Can't add data into Database")
    
    # print(custid)
    #print(firstname)
    #print(lastname)
    #print(phone_no)
    #print(email_id)
    #print(street_name)
    #print(city_name)
    #print(state_name)
    #print(zipcode)
    root.destroy()
    
def addCustomer():
    
    global custid,firstname,lastname,phone_no,email_id,street_name, city_name, state_name, zipcode,conn,customerTable,cur,root
    
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
    customerTable = "BikeStores.dbo.customer" # Book Table

    Canvas1 = Canvas(root)
    
    Canvas1.config(bg="#ff6e40")
    Canvas1.pack(expand=True,fill=BOTH)
        
    headingFrame1 = Frame(root,bg="#FFBB00",bd=5)
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
     # first name
    lb2 = Label(labelFrame,text="First Name : ", bg='black', fg='white')
    lb2.place(x=300,y=20, relheight=0.08)
        
    firstname = Entry(labelFrame)
    firstname.place(x=400,y=30, relwidth=0.3, relheight=0.09)
        
    # Last name
    lb3 = Label(labelFrame,text="Last Name: ", bg='black', fg='white')
    lb3.place(x=20,y=150, relheight=0.08)
        
    lastname = Entry(labelFrame)
    lastname.place(x=100,y=150, relwidth=0.3, relheight=0.08)
        
    # phone
    lb4 = Label(labelFrame,text="Phone: ", bg='black', fg='white')
    lb4.place(x=320,y=150, relheight=0.08)
        
    phone_no = Entry(labelFrame)
    phone_no.place(x=400,y=150, relwidth=0.3, relheight=0.08)

    # email
    lb4 = Label(labelFrame, text="Email: ", bg='black', fg='white')
    lb4.place(x=20, y=270, relheight=0.08)

    email_id = Entry(labelFrame)
    email_id.place(x=100, y=270, relwidth=0.3, relheight=0.08)

    # street
    lb4 = Label(labelFrame, text="Street: ", bg='black', fg='white')
    lb4.place(x=320, y=270, relheight=0.08)

    street_name = Entry(labelFrame)
    street_name.place(x=400, y=270, relwidth=0.3, relheight=0.08)

    # city
    lb4 = Label(labelFrame, text="City: ", bg='black', fg='white')
    lb4.place(x=20, y=340, relheight=0.08)

    city_name = Entry(labelFrame)
    city_name.place(x=100, y=340, relwidth=0.3, relheight=0.08)

    # state
    lb4 = Label(labelFrame, text="State: ", bg='black', fg='white')
    lb4.place(x=320, y=340, relheight=0.08)

    state_name = Entry(labelFrame)
    state_name.place(x=400, y=340, relwidth=0.3, relheight=0.08)

    # Zipcode
    lb4 = Label(labelFrame, text="Zip Code: ", bg='black', fg='white')
    lb4.place(x=20, y=400, relheight=0.08)

    zipcode = Entry(labelFrame)
    zipcode.place(x=100, y=400, relwidth=0.3, relheight=0.08)
        
    #Submit Button
    SubmitBtn = Button(root,text="SUBMIT",bg='#d1ccc0', fg='black',command=customerRegister)
    SubmitBtn.place(relx=0.28,rely=0.9, relwidth=0.18,relheight=0.03)
    
    quitBtn = Button(root,text="Quit",bg='#f7f1e3', fg='black', command=root.destroy)
    quitBtn.place(relx=0.53,rely=0.9, relwidth=0.18,relheight=0.03)
    
    root.mainloop()