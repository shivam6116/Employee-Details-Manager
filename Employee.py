from tkinter import *

class Employee:
    def __init__(self, a, b, c, d):
        self.ID = a
        self.firstname = b
        self.lastname = c
        self.salary = d

    def getid(self):
        print(self.ID)

    def getlname(self):
        print( self.lastname)

    def getfirstname(self):
        print( self.firstname)

    def name(self):
        print(self.firstname, self.lastname)

    def getsalary(self):
        print( self.salary)


    def setsalary(self, x):
        self.salary = x

    def anuall(self):
        print(self.salary * 12)

    def raisesalary(self):
        y = int(input("Enter per to raise salary="))
        a = y / 100 * self.salary
        self.salary = self.salary + a
        return self.salary

#main for class
E1 = Employee(6945, "shivam", "mishra", 1000)

# main for GUI
root=Tk()
root.title("Employee")
pro=Label(root,text=" Welcome to Employee Details ",bg="white",fg="red",font="8,bold",relief=SUNKEN)
pro.pack()

root.geometry("444x345")
bt=Button(root, text="First name",fg="red",command=E1.getfirstname)
bt.pack(side=LEFT)
bt1=Button(root, text="last name",fg="purple",command=E1.getlname)
bt1.pack(side=LEFT)
bt5=Button(root, text="Full name",fg="orange",command=E1.name)
bt5.pack(side=LEFT)
bt2=Button(root, text="salary details",fg="blue",command=E1.getsalary)
bt2.pack(side=LEFT)
bt3=Button(root, text="Get id",fg="brown",command=E1.getid)
bt3.pack(side=LEFT)
bt4=Button(root, text="Anuall salary",fg="green",command=E1.anuall)
bt4.pack(side=LEFT)

root.mainloop()