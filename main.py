from tkinter import *
from branchA import BranchA
from branchB import BranchB


class Application(object):
    def __init__(self, master):
        self.master = master
        
        self.top = Frame(master, height=150, bg='white')
        self.top.pack(fill=X)

        self.bottom = Frame(master, height=500, bg='#03befc')
        self.bottom.pack(fill=X)


        self.heading = Label(self.top, text='Employee Application',
                             font='arial 34 bold', bg='white', fg='black')
        self.heading.place(x=160, y=40)

        # button1(Branch A)
        self.branchaButton = Button(self.bottom, text=" Branch A ", fg="#03befc", font='arial 16 bold',
                                     command=self.branch_a)
        self.branchaButton.place(x=270, y=45)

        # button2(Branch B)
        self.branchbButton = Button(self.bottom, text=" Branch B ", fg="#03befc", font='arial 16 bold',
                                command=self.branch_b)
        self.branchbButton.place(x=270, y=95)

    def branch_a(self):
        BranchA()
        return
    def branch_b(self):
        BranchB()
        return

def main():
    root = Tk()
    app = Application(root)
    root.title("Employee App")
    root.geometry("650x650+350+200")
    root.mainloop()


if __name__ == '__main__':
    main()
