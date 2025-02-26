from tkinter import *
from tkinter import messagebox
import sqlite3
import queries2


conn = sqlite3.connect("employeeapp.sqlite3")
cur = conn.cursor()


class Update(Toplevel):
    def __init__(self, employee_id):
        Toplevel.__init__(self)

        self.geometry("650x650+600+200")
        self.title("Update Employee Details")

        query = "select * from BranchB where id ='{}'".format(employee_id)
        result = cur.execute(query).fetchone()
        self.employee_id = employee_id
        employee_firstname = result[1]
        employee_lastname = result[2]
        employee_number = result[3]
        employee_email = result[4]
        employee_address = result[5]
        employee_salary = result[6]

        self.top = Frame(self, height=150, bg='white')
        self.top.pack(fill=X)

        self.bottom = Frame(self, height=500, bg='tan')
        self.bottom.pack(fill=X)

        # top frame design
        self.top_image = PhotoImage(file='icons/user.png')
        self.top_image_label = Label(self.top, image=self.top_image)
        self.top_image_label.place(x=120, y=20)

        self.heading = Label(self.top, text='Update Employee',
                             font='arial 28 bold', bg='white', fg='black')
        self.heading.place(x=270, y=40)

        # firstName
        self.label_firstname = Label(self.bottom, text='First Name', font='arial 15 bold', fg='black', bg='white')
        self.label_firstname.place(x=40, y=40)

        self.entry_firstname = Entry(self.bottom, width=30, bd=4)
        self.entry_firstname.insert(0, employee_firstname)
        self.entry_firstname.place(x=150, y=40)

        # lastName
        self.label_lastname = Label(self.bottom, text='Last Name', font='arial 15 bold', fg='black', bg='white')
        self.label_lastname.place(x=40, y=80)

        self.entry_lastname = Entry(self.bottom, width=30, bd=4)
        self.entry_lastname.insert(0, employee_lastname)
        self.entry_lastname.place(x=150, y=80)

        # phone number
        self.label_phone = Label(self.bottom, text='Phone No.', font='arial 15 bold', fg='black', bg='white')
        self.label_phone.place(x=40, y=160)

        self.entry_phone = Entry(self.bottom, width=30, bd=4)
        self.entry_phone.insert(0, employee_number)
        self.entry_phone.place(x=150, y=160)

        # email
        self.label_email = Label(self.bottom, text='Email', font='arial 15 bold', fg='black', bg='white')
        self.label_email.place(x=40, y=120)

        self.entry_email = Entry(self.bottom, width=30, bd=4)
        self.entry_email.insert(0, employee_email)
        self.entry_email.place(x=150, y=120)

        # address
        self.label_address = Label(self.bottom, text="Address", font='arial 15 bold', fg='black', bg='white')
        self.label_address.place(x=40, y=200)

        self.entry_address = Entry(self.bottom, width=30, bd=4)
        self.entry_address.insert(0, employee_address)
        self.entry_address.place(x=150, y=200)

        #salary
        self.label_salary = Label(self.bottom, text="Salary", font='arial 15 bold', fg='black', bg='white')
        self.label_salary.place(x=40, y=240)

        self.entry_salary = Entry(self.bottom, width=30, bd=4)
        self.entry_salary.insert(0, employee_salary)
        self.entry_salary.place(x=150, y=240)

        # button
        button = Button(self.bottom, text='Update', command=self.update_employee)
        button.place(x=250, y=280)

    def update_employee(self):
        employee_id = self.employee_id
        first_name = self.entry_firstname.get()
        last_name = self.entry_lastname.get()
        number = self.entry_phone.get()
        email = self.entry_email.get()
        address = self.entry_address.get()
        salary = self.entry_salary.get()
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
                cur.execute(queries2.UPDATE, (first_name, last_name, number, email, address,salary, employee_id))
                conn.commit()
                messagebox.showinfo('Success', "Details updated successfully")
                self.destroy()
                return

            except Exception as e:
                messagebox.showerror("Error", str(e))

        else:
            messagebox.showerror('Error', "All fields must be filled", icon='warning')