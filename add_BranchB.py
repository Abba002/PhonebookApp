from tkinter import *
from tkinter import messagebox
import sqlite3
import queries2

conn = sqlite3.connect("employeeapp.sqlite3")
cur = conn.cursor()


class AddEmployee(Toplevel):
    def __init__(self):
        Toplevel.__init__(self)

        self.geometry("650x650+600+200")
        self.title("Add New Employee")

        self.top = Frame(self, height=150, bg='white')
        self.top.pack(fill=X)

        self.bottom = Frame(self, height=500, bg='tan')
        self.bottom.pack(fill=X)

        # top frame design
        self.top_image = PhotoImage(file='icons/user.png')
        self.top_image_label = Label(self.top, image=self.top_image)
        self.top_image_label.place(x=120, y=35)

        self.heading = Label(self.top, text='Add New Employee',
                             font='arial 28 bold', bg='white', fg='black')
        self.heading.place(x=230, y=50)

        # firstName
        self.label_firstname = Label(self.bottom, text='First Name', font='arial 15 bold', fg='black', bg='white')
        self.label_firstname.place(x=40, y=40)

        self.entry_firstname = Entry(self.bottom, width=30, bd=4)
        self.entry_firstname.place(x=150, y=40)

        # lastName
        self.label_lastname = Label(self.bottom, text='Last Name', font='arial 15 bold', fg='black', bg='white')
        self.label_lastname.place(x=40, y=80)

        self.entry_lastname = Entry(self.bottom, width=30, bd=4)
        self.entry_lastname.place(x=150, y=80)

        # email
        self.label_email = Label(self.bottom, text='Email', font='arial 15 bold', fg='black', bg='white')
        self.label_email.place(x=40, y=120)

        self.entry_email = Entry(self.bottom, width=30, bd=4)
        self.entry_email.place(x=150, y=120)

        # phone number
        self.label_phone = Label(self.bottom, text='Phone No.', font='arial 15 bold', fg='black', bg='white')
        self.label_phone.place(x=40, y=160)

        self.entry_phone = Entry(self.bottom, width=30, bd=4)
        self.entry_phone.place(x=150, y=160)

        # address
        self.label_address = Label(self.bottom, text="Address", font='arial 15 bold', fg='black', bg='white')
        self.label_address.place(x=40, y=200)

        self.entry_address = Entry(self.bottom, width=30, bd=4)
        self.entry_address.place(x=150, y=200)

        #salary
        self.label_salary = Label(self.bottom, text="Salary", font='arial 15 bold', fg='black', bg='white')
        self.label_salary.place(x=40, y=240)

        self.entry_salary = Entry(self.bottom, width=30, bd=4)
        self.entry_salary.place(x=150, y=240)

        # button
        button = Button(self.bottom, text='Add Employee', command=self.add_employee)
        button.place(x=250, y=280)

    def add_employee(self):
        first_name: str = self.entry_firstname.get()
        last_name: str = self.entry_lastname.get()
        number = self.entry_phone.get()
        email: str = self.entry_email.get()
        address: str = self.entry_address.get()
        salary: int = self.entry_salary.get()

        if len(first_name)>30:
            messagebox.showerror('Error', 'first name is too long')
            return
        if len(last_name)>30:
            messagebox.showerror('Error', 'last name is too long')
            return
        if first_name and last_name and number and email and address != "":
            try:
                number = int(number)
            except:
                messagebox.showerror('Error', 'phone number is not valid')
                return
            try:
                salary = int(salary)
            except:
                messagebox.showerror('Error', 'salary is not valid')
                return
            try:
                cur.execute(queries2.INSERT, (first_name, last_name, number, email, address,salary))
                conn.commit()
                messagebox.showinfo('Success', "Employee added successfully")
                self.destroy()
                return

            except EXCEPTION as e:
                messagebox.showerror("Error", str(e))
        else:
            messagebox.showerror('Error', "All fields must be filled", icon='warning')
