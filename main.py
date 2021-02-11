from tkinter import *
import pyodbc
from tkinter import messagebox
from AddCustomer import *
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