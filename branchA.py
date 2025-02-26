from tkinter import *
import sqlite3
import queries
from add_BranchA import AddEmployee
from update_branchA import Update
from display_branchA import Display
from tkinter import messagebox
from searchA import Search


conn = sqlite3.connect("employeeapp.sqlite3")
cur = conn.cursor()

cur.execute(queries.CREATE_TABLE)
conn.commit()


class BranchA(Toplevel):
    def __init__(self):
        Toplevel.__init__(self)

        self.geometry("650x650+600+200")
        self.title("Branch A")

        self.top = Frame(self, height=150, bg='white')
        self.top.pack(fill=X)

        self.bottom = Frame(self, height=500, bg='plum')
        self.bottom.pack(fill=X)

        self.top_image = PhotoImage(file='icons/user.png')
        self.top_image_label = Label(self.top, image=self.top_image)
        self.top_image_label.place(x=120, y=27)

        self.heading = Label(self.top, text='Branch A Employees',
                             font='arial 34 bold', bg='white', fg='black')
        self.heading.place(x=230, y=40)

        self.scroll = Scrollbar(self.bottom, orient=VERTICAL)

        self.listBox = Listbox(self.bottom, width=40, height=27)
        self.listBox.grid(row=0, column=0, padx=(40, 0))
        self.scroll.config(command=self.listBox.yview)
        self.listBox.config(yscrollcommand=self.scroll.set)

        employees = cur.execute(queries.FETCH_ALL).fetchall()
        count = 0
        for employee in employees:
            self.listBox.insert(count, str(employee[0]) + ". " + employee[1] + " " + employee[2])
            count += 1

        self.scroll.grid(row=0, column=1, sticky=N+S)

        # buttons

        button_add = Button(self.bottom, text='Add', width=12, font='Sans 12 bold', command=self.add_employee)
        button_add.grid(row=0, column=2, padx=20, pady=10, sticky=N)

        button_update = Button(self.bottom, text='Update', width=12, font='Sans 12 bold',
                               command=self.update_employee)
        button_update.grid(row=0, column=2, padx=20, pady=50, sticky=N)

        button_display = Button(self.bottom, text='Display', width=12, font='Sans 12 bold',
                                command=self.display_employee)
        button_display.grid(row=0, column=2, padx=20, pady=90, sticky=N)

        button_delete = Button(self.bottom, text='Delete', width=12, font='Sans 12 bold',
                               command=self.delete_employee)
        button_delete.grid(row=0, column=2, padx=20, pady=130, sticky=N)

        button_search = Button(self.bottom, text='Search', width=12, font='Sans 12 bold',
                               command=self.search_employee)
        button_search.grid(row=0, column=2, padx=20, pady=170, sticky=N)

    def add_employee(self):
        AddEmployee()
        self.destroy()
        return

    def update_employee(self):
        selected_item = self.listBox.curselection()
        employee = self.listBox.get(selected_item)
        employee_id = employee.split(".")[0]
        Update(employee_id)
        self.destroy()
        return

    def display_employee(self):
        selected_item = self.listBox.curselection()
        employee = self.listBox.get(selected_item)
        employee_id = employee.split(".")[0]
        Display(employee_id)
        self.destroy()
        return

    def delete_employee(self):
        selected_item = self.listBox.curselection()
        employee = self.listBox.get(selected_item)
        employee_id = employee.split(".")[0]

        employee_ID = employee_id
        answer = messagebox.askquestion('Warning', 'Are you sure you want to delete? ')
        if answer == 'yes':
            try:
                cur.execute(queries.DELETE, employee_ID)
                conn.commit()
                messagebox.showinfo("Success", "Employee deleted successfully")
                self.destroy()

            except Exception as e:
                messagebox.showinfo("Info", str(e))

    def search_employee(self):
        Search()
        self.destroy()
        return
