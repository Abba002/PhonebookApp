from tkinter import *
from tkinter import messagebox
import sqlite3
import queries


class Search(Toplevel):

    def __init__(self):
        Toplevel.__init__(self)

        self.geometry("500x400+550+150")
        self.title("Employee Search")

        self.top = Frame(self, height=100, bg='white')
        self.top.pack(fill=X)

        self.bottom = Frame(self, height=300, bg='plum')
        self.bottom.pack(fill=X)

        # top frame design
        self.top_image = PhotoImage(file='icons/user.png')
        self.top_image_label = Label(self.top, image=self.top_image)
        self.top_image_label.place(x=120, y=15)

        self.heading = Label(self.top, text='Employee Search',
                             font='arial 28 bold', bg='white', fg='black')
        self.heading.place(x=230, y=30)

        # firstName
        self.label_firstname = Label(self.bottom, text='Enter a name', font='arial 15 bold', fg='black', bg='white')
        self.label_firstname.place(x=40, y=40)

        self.entry_firstname = Entry(self.bottom, width=30, bd=4)
        self.entry_firstname.place(x=150, y=40)

        # button
        button = Button(self.bottom, text='Search', command=self.search_employee)
        button.place(x=250, y=180)

    def search_employee(self):

        try:
            conn = sqlite3.connect("employeeapp.sqlite3")
            cur = conn.cursor()
            query = "select * from BranchA where firstName= '"+employee_firstname+"'"
            cur.execute(query)
            result = cur.execute(query).fetchall()


        except:
            messagebox.showinfo('No data', 'No such data available')