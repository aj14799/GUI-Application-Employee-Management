import sqlite3

def EmployeeData():
    con = sqlite3.connect("Employee.db")
    cur = con.cursor()
    cur.execute("CREATE TABLE IF NOT EXISTS Employee (id INTEGER PRIMARY KEY, Refrence text,\
    Firstname text, Surname text, Address text, Gender text, Mobile text, NINumber text, \
    stdLoan text, Tax text, Pension text, Deduction text, NetPay text,GrossPay text)")
    con.commit()
    con.close()
    
def addEmployeeRec(Refrence,Firstname , Surname , Address , Gender , Mobile , NINumber ,stdLoan , Tax , Pension , Deduction, NetPay ,GrossPay):
    con = sqlite3.connect("Employee.db")
    cur = con.cursor()
    cur.execute("INSERT INTO Employee VALUES(NULL,?,?,?,?,?,?,?,?,?,?,?,?,?)",\
    (Refrence,Firstname , Surname , Address , Gender , Mobile , NINumber ,stdLoan , Tax , Pension , Deduction, NetPay ,GrossPay))
    con.commit()
    con.close()


def viewData():
    con = sqlite3.connect("Employee.db")
    cur = con.cursor()
    cur.execute("SELECT * FROM Employee")
    rows = cur.fetchall()
    con.close()
    return rows

def DeleteRecord(id):
    con = sqlite3.connect("Employee.db")
    cur = con.cursor()
    cur.execute("DELETE * FROM Employee WHERE id=?",(id))
    con.close()

def SearchData(Refrence = "",Firstname = "" , Surname = "" , Address = "" , Gender = "" , Mobile = "" , NINumber = "" ,stdLoan = "" , Tax = "" , Pension = "" , Deduction = "", NetPay = "" ,GrossPay = ""):
    con = sqlite3.connect("Employee.db")
    cur = con.cursor()
    cur.execute("SELECT * FROM Employee WHERE  Refrence  = ? OR Firstname  = ? OR  Surname  = ? OR  Address  = ? OR  Gender  = ?  OR  Mobile  = ?  OR NINumber  = ? OR stdLoan  = ? OR Tax  = ? OR Pension  = ? OR  Deduction  = ? OR  NetPay  = ? OR  GrossPay  = ?",(Refrence,Firstname , Surname , Address , Gender , Mobile , NINumber ,stdLoan , Tax , Pension , Deduction, NetPay ,GrossPay))
    rows = cur.fetchall()
    con.close()
    return rows
    con.commit()
    con.close()


def dataUpdate(Refrence = "",Firstname = "" , Surname = "" , Address = "" , Gender = "" , Mobile = "" , NINumber = "" ,stdLoan = "" , Tax = "" , Pension = "" , Deduction = "", NetPay = "" ,GrossPay = ""):
    con = sqlite3.connect("Employee.db")
    cur = con.cursor()
    cur.execute("UPDATE Employee SET  Refrence  = ?  Firstname  = ?   Surname  = ?   Address  = ?   Gender  = ?    Mobile  = ?   NINumber  = ?  stdLoan  = ?  Tax  = ?  Pension  = ?   Deduction  = ?   NetPay  = ?   GrossPay  = ?",(Refrence,Firstname , Surname , Address , Gender , Mobile , NINumber ,stdLoan , Tax , Pension , Deduction, NetPay ,GrossPay,id))
    rows = cur.fetchall()
    con.close()
    return rows
    con.commit()
    con.close()

EmployeeData()
