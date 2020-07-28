from tkinter import *
import sqlite3

root =Tk()

#Create a DB or connect to one
conn = sqlite3.connect('F:/Python Codes/TKINTER/address_book.db')

#Create Cursor
c= conn.cursor()

#Create table
'''
CREATE TABLE adresses(
            first_name text,
            last_name text,
            address text,
            city text,
            state text,
            zipcode integer)""") 
'''

#Create Submit Fun
def submit():
    # Create a DB or connect to one
    conn = sqlite3.connect('F:/Python Codes/TKINTER/address_book.db')

    # Create Cursor
    c = conn.cursor()

    #Insert into table
    c.execute("INSERT INTO adresses VALUES (:f_name, :l_name, :address, :city, :state, :zipcode )",
              {
                    'f_name': f_name.get(),
                    'l_name': l_name.get(),
                    'address': address.get(),
                    'city': city.get(),
                    'state': state.get(),
                    'zipcode': zipcode.get()
              })


    # Commit Changes
    conn.commit()

    # Close Connection
    conn.close()

    #Clear text boxes
    f_name.delete(0, END)
    l_name.delete(0, END)
    address.delete(0, END)
    city.delete(0, END)
    state.delete(0, END)
    zipcode.delete(0, END)

#Craete Query Fun
def query():
    # Create a DB or connect to one
    conn = sqlite3.connect('F:/Python Codes/TKINTER/address_book.db')

    # Create Cursor
    c = conn.cursor()

    #Query the DB
    c.execute("SELECT *, oid FROM adresses")
    records = c.fetchall()   #fetchone, fetchmany(50)
    print(records)

    #Loop through reslts
    print_records = ''
    for record in records:
        print_records += str(record) + "\n"

    query_label = Label(root, text=print_records)
    query_label.grid(row=8,column=0, columnspan=2)

    # Commit Changes
    conn.commit()

    # Close Connection
    conn.close()


#Create Text Boxes
f_name = Entry(root, width=30)
f_name.grid(row=0, column=1, padx =20)

l_name = Entry(root, width=30)
l_name.grid(row=1, column=1, padx =20)

address = Entry(root, width=30)
address.grid(row=2, column=1, padx =20)

city = Entry(root, width=30)
city.grid(row=3, column=1, padx =20)

state = Entry(root, width=30)
state.grid(row=4, column=1, padx =20)

zipcode = Entry(root, width=30)
zipcode.grid(row=5, column=1, padx =20)

#Create text Labels
f_name_label = Label(root, text="First Name")
f_name_label.grid(row=0, column=0)
l_name_label = Label(root, text="Last Name")
l_name_label.grid(row=1, column=0)
address_label = Label(root, text="Address")
address_label.grid(row=2, column=0)
city_label = Label(root, text="City")
city_label.grid(row=3, column=0)
state_label = Label(root, text="State")
state_label.grid(row=4, column=0)
zipcode_label = Label(root, text="Zipcode")
zipcode_label.grid(row=5, column=0)

#Create Submit Button
submit_btn = Button(root, text="Add Record to DB", command=submit)
submit_btn.grid(row=6, column=0, columnspan= 2, pady=10, padx=10, ipadx=100)

#Create a Query Button
query_btn = Button(root, text="Show Records", command=query)
query_btn.grid(row=7, column=0, columnspan=2,pady=10, padx=10, ipadx=137)

#Commit Changes
conn.commit()

#Close Connection
conn.close()

root.mainloop()