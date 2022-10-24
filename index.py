from tkinter import ttk
from tkinter import *

import sqlite3

class Product:
    db_name  = 'database.db'
    
    def __init__(self, window):
        self.wind = window
        self.wind.title( "Product Application")

        # Creating a Frame Container
        frame = LabelFrame( self.wind, text = "Register a new product")
        frame.grid(row = 0, column = 0 ,columnspan=3, pady=20)

        # Name Input
        Label(frame, text = "Name: ").grid(row=1, column=0)
        self.name = Entry(frame)
        self.name.focus()
        self.name.grid(row=1, column=1)

        # Price Input
        Label(frame, text = "Price: ").grid(row=2, column=0)
        self.price = Entry(frame)
        self.price.grid(row=2, column=1)
        
        # Button add product
        ttk.Button(frame, text='Save Product', command=self.add_product).grid(row=3, columnspan=2, sticky= W + E)

        # Output Messages
        self.message = Label(text='', fg='red')
        self.message.grid(row=3,column=0,columnspan=2,sticky=W+E)

        # Table
        self.tree = ttk.Treeview(height=10, columns=2)
        self.tree.grid(row=4, column=0, columnspan=2)
        self.tree.heading('#0', text='Name', anchor=CENTER)
        self.tree.heading('#1', text='Price', anchor=CENTER)

        # Buttons
        ttk.Button(text='DELETE', command= self.delete_product).grid(row=5, column=0,sticky=W+E)
        ttk.Button(text='EDIT', command= self.edit_product).grid(row=5, column=1,sticky=W+E)

        # Obtenemos datos 
        self.get_products()

    def run_query(self, query, parameters = ()):
        with sqlite3.connect(self.db_name) as conn:
            cursor = conn.cursor()
            result = cursor.execute(query,parameters)
            conn.commit()
        return result

    def get_products(self):
        # cleaning table
        records = self.tree.get_children()
        for element in records:
            self.tree.delete(element)

        # quering data         
        myquery = 'SELECT * FROM Product ORDER BY name DESC'
        db_row = self.run_query(myquery)

        # filling data
        for row in db_row:
            # print(row)
            self.tree.insert('',0, text = row[1], values= row[2])

    def validation(self):
        return len(self.name.get()) != 0 and len(self.price.get()) != 0 

    def add_product(self):
        if self.validation():
            # print(self.name.get())
            # print(self.price.get())
            query = 'INSERT INTO Product VALUES(NULL, ?,?)'
            parameters = (self.name.get(), self.price.get())
            self.run_query(query, parameters)
            print('Data saved')
            self.message['text'] = 'Product {} added Successfully'.format(self.name.get())
            self.name.delete(0, END)
            self.price.delete(0, END)
        else:
            self.message['text'] = 'Name and Price is requiered'
            print('Name and Price is requiered')
        self.get_products()

    def delete_product(self):
        self.message['text'] = ''
        try:
            print(self.tree.selection())
            self.tree.item(self.tree.selection())['text'][0]
        except IndexError as e:
            self.message['text'] = 'Please Select a Record'
            return
        self.message['text'] = ''
        name =  self.tree.item(self.tree.selection())['text']
        myquery = 'DELETE FROM Product WHERE name = ?'
        myparameters = (name,)
        self.run_query(myquery, myparameters)
        self.message['text'] = 'Record {} deleted successfully'.format(name)
        self.get_products()

    def edit_product(self):
        self.message['text'] = ''
        try:
            print(self.tree.selection())
            print(self.tree.item(self.tree.selection()))
            self.tree.item(self.tree.selection())['text'][0]
        except IndexError as e:
            self.message['text'] = 'Please Select a Record'
            return
        name =  self.tree.item(self.tree.selection())['text']
        old_price = self.tree.item(self.tree.selection())['values'][0]
        self.edit_wind = Toplevel()
        self.edit_wind.title = 'Edit Product'

        # Old Name 
        Label(self.edit_wind, text='Old Name: ').grid( row = 0, column = 1)
        Entry(self.edit_wind, textvariable= StringVar(self.edit_wind, value = name),\
              state = 'readonly').grid(row=0, column=2)

        # New Name
        Label(self.edit_wind, text='New Name: ').grid( row = 1, column = 1)
        new_name = Entry(self.edit_wind)
        new_name.grid(row = 1, column = 2)

        # Old Price
        Label(self.edit_wind, text='Old Price: ').grid( row = 2, column = 1)
        Entry(self.edit_wind, textvariable= StringVar(self.edit_wind, value = \
            old_price), state = 'readonly').grid(row = 2, column = 2)

        # New Price
        Label(self.edit_wind, text='New Price: ').grid( row = 3, column = 1)
        new_price = Entry(self.edit_wind)
        new_price.grid(row = 3, column = 2)

        Button(self.edit_wind, text = 'Update', command = lambda: self.edit_records(\
            new_name.get(),name, new_price.get(), old_price)).grid(row = 4, \
            column = 2, sticky = W)

    def edit_records(self, new_name, name, new_price, old_price):
        myquery = 'UPDATE Product SET name= ?, price = ? WHERE name = ? AND price = ?'
        myparameters = (new_name, new_price, name, old_price)
        self.run_query(myquery, myparameters)
        self.edit_wind.destroy()
        self.message['text'] = 'Record {} updated Successfully'.format(name)
        self.get_products()

if __name__ == '__main__':
    mywindow = Tk()
    application = Product(mywindow)
    mywindow.mainloop()