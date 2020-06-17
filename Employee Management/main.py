from tkinter import*
from tkinter import ttk
import random
import tkinter.messagebox
import datetime
import time
import tempfile, os
import EmployeeData

#FrontEnd

class Employee:
    def __init__(self,root):
        self.root=root
        self.root.title("Employee Database Management System")
        self.root.geometry("1350x700+0+0")
        self.root.configure(bg="gainsboro")

        bg_color="gainsboro"
        title=Label(self.root,text="Employee Database",bd=12,relief=GROOVE,bg=bg_color,font=("times new roman",30, "bold"),pady=2).pack(fill=X)
          
        mainframe = Frame(self.root,bd = 10, width=1350,height=700, relief=RIDGE)
        mainframe.pack()

        TopFrame1 = Frame(mainframe,bd = 7, width=1340,height=50, relief=RIDGE)
        TopFrame1.grid(row=2, column = 0)

        TopFrame2 = Frame(mainframe,bd = 7, width=1340,height=100, relief=RIDGE)
        TopFrame2.grid(row=1, column = 0)

        TopFrame3 = Frame(mainframe,bd = 7, width=1340,height=500, relief=RIDGE)
        TopFrame3.grid(row=0, column = 0)

        LeftFrame = Frame(TopFrame3,bd = 5, width=1340, height=400,  padx=2, bg="gainsboro", relief=RIDGE)
        LeftFrame.pack(side=LEFT)
        LeftFrame1 = Frame(LeftFrame,bd = 5, width=600, height=180, padx=4,pady=4, bg="gainsboro",relief=RIDGE)
        LeftFrame1.pack(side=TOP)

        LeftFrame2 = Frame(LeftFrame,bd = 5, width=600, height=180,  padx=2, bg="gainsboro", relief=RIDGE)
        LeftFrame2.pack(side=TOP)
        LeftFrame2Left = Frame(LeftFrame2,bd = 5, width=300, height=170, padx=2, bg="gainsboro",relief=RIDGE)
        LeftFrame2Left.pack(side=LEFT)
        LeftFrame2Right = Frame(LeftFrame2,bd = 5, width=300, height=170, padx=2, bg="gainsboro",relief=RIDGE)
        LeftFrame2Right.pack(side=RIGHT)


        RightFrame1 = Frame(TopFrame3,bd = 5, width=320, height=400,  padx=2, bg="gainsboro", relief=RIDGE)
        RightFrame1.pack(side=RIGHT)
        RightFrame1a = Frame(RightFrame1,bd = 5, width=310, height=300, padx=2, bg="gainsboro",relief=RIDGE)
        RightFrame1a.pack(side=TOP)


        RightFrame2 = Frame(TopFrame3,bd = 5, width=300, height=400,  padx=2, bg="gainsboro", relief=RIDGE)
        RightFrame2.pack(side=RIGHT)
        RightFrame2a = Frame(RightFrame2,bd = 5, width=200, height=50, padx=2, bg="gainsboro",relief=RIDGE)
        RightFrame2a.pack(side=TOP)
        RightFrame2b = Frame(RightFrame2,bd = 5, width=180, height=180, padx=2, bg="gainsboro",relief=RIDGE)
        RightFrame2b.pack(side=TOP)
        RightFrame2c = Frame(RightFrame2,bd = 5, width=280, height=100, padx=2, bg="gainsboro",relief=RIDGE)
        RightFrame2c.pack(side=TOP)
        RightFrame2d = Frame(RightFrame2,bd = 5, width=280, height=50, padx=2, bg="gainsboro",relief=RIDGE)
        RightFrame2d.pack(side=TOP)

        
        #------------------------------------------------Variables------------------------------------------------# 
     
        global Ed
        Firstname =StringVar()
        Surname =StringVar()
        Address =StringVar()
        Refrence =StringVar()
        CityWeighting =StringVar()
        Mobile =StringVar()
        BasicSalary =StringVar()
        OverTIme =StringVar()
        GrossPay =StringVar()
        NetPay =StringVar()
        Tax =StringVar()
        Pension =StringVar()
        stdLoan =StringVar()
        NIPayment =StringVar()
        Deduction =StringVar()
        Gender =StringVar()
        Payday =StringVar()
        TaxPeriod =StringVar()
        NINumber =StringVar()
        NICode =StringVar()
        TaxablePay =StringVar()
        PensionablePay =StringVar()
        OtherPaymentDue =StringVar()
        TaxCode =StringVar()

        CityWeighting.get()
        BasicSalary.get()
        OtherPaymentDue.set("0.00")
        
        #------------------------------------------------Functions------------------------------------------------# 

        def Reset():
            Firstname.set("")
            Surname.set("")
            Address.set("")
            Refrence.set("")
            CityWeighting.set("")
            Mobile.set("")
            BasicSalary.set("")
            OverTIme.set("")
            GrossPay.set("")
            NetPay.set("")
            Tax.set("")
            Pension.set("")
            stdLoan.set("")
            NIPayment.set("")
            Deduction.set("")
            Gender.set("")
            Payday.set("")
            TaxPeriod.set("")
            NINumber.set("")
            NICode.set("")
            TaxablePay.set("")
            PensionablePay.set("")
            TaxCode.set("")
            OtherPaymentDue.set("0.00")
            self.txtReceipt.delete("1.0",END)

        def EQuit():
            Equit = tkinter.messagebox.askyesnocancel("Employee Database","Really Want to exit?!!")
            if Equit > 0:
                root.destroy()
                return
        
        def AddNew():
            if(len(Refrence.get()) != 0):
                EmployeeData.addEmployeeRec(Refrence.get(),Firstname.get() , Surname.get() , Address.get() , Gender.get() , Mobile.get() , NINumber.get() ,stdLoan.get() , Tax.get() , Pension.get() , Deduction.get(), NetPay.get() ,GrossPay.get())
                IstEmployee.delete(0,END)  
                IstEmployee.insert(END,(Refrence.get(),Firstname.get(),Surname.get(),Address.get(),Gender.get(),Mobile.get(),NINumber.get(),stdLoan.get(),Tax.get(),Pension.get(), Deduction.get(), NetPay.get(),GrossPay.get()))          
        
        def Print():
            a = self.txtReceipt.get("1.0", "end-1c") # can use END
            filename = tempfile.mktemp(".doc") #can take txt 
            open(filename,"w").write(a)
            os.startfile(filename,"print") 
    
        def Disp():
            IstEmployee.delete(0,END)
            for row in EmployeeData.viewData():
                IstEmployee.insert(END,row,str(""))

        def EmployeeRec(event):
            global Ed
            searchEd = IstEmployee.curselection()[0]
            Ed = IstEmployee.get(searchEd)

            self.txtReference.delete(0,END)
            self.txtReference.insert(END,Ed[1])
            self.txtFirstname.delete(0,END)
            self.txtFirstname.insert(END,Ed[2])
            self.txtSurname.delete(0,END)
            self.txtSurname.insert(END,Ed[3])
            self.txtAddress.delete(0,END)
            self.txtAddress.insert(END,Ed[4])
            self.txtGender.delete(0,END)
            self.txtGender.insert(END,Ed[5])
            self.txtMobile.delete(0,END)
            self.txtMobile.insert(END,Ed[6])
            self.txtNINumber.delete(0,END)
            self.txtNINumber.insert(END,Ed[7])
            self.txtstdLoan.delete(0,END)
            self.txtstdLoan.insert(END,Ed[8])
            self.txtTax.delete(0,END)
            self.txtTax.insert(END,Ed[9])
            self.txtPension.delete(0,END)
            self.txtPension.insert(END,Ed[10])
            self.txtDeduction.delete(0,END)
            self.txtDeduction.insert(END,Ed[11])
            self.txtNetPay.delete(0,END)
            self.txtNetPay.insert(END,Ed[12])
            self.txtGrossPay.delete(0,END)
            self.txtGrossPay.insert(END,Ed[13])



        def Upd():
            if (len(Refrence.get())!=0):
                EmployeeData.DeleteRecord(Ed[0])
            if (len(Refrence.get())!=0):
                EmployeeData.addEmployeeRec(Reference).get(),Firstname.get(),Surname.get(),Address.get(),Gender.get(),Mobile.get(),NINumber.get(),stdLoan.get(),Tax.get(),Pension.get(), Deduction.get(), NetPay.get(),GrossPay.get()
                IstEmployee.delete(0,END)  
                IstEmployee.insert(END,(Reference.get(),Firstname.get(),Surname.get(),Address.get(),Gender.get(),Mobile.get(),NINumber.get(),stdLoan.get(),Tax.get(),Pension.get(), Deduction.get(), NetPay.get(),GrossPay.get()))          

        def Del():
            global Ed
            if (len(Refrence.get())!=0):
                EmployeeData.DeleteRecord(Ed[0])
                Reset()
                Dis()

        def search():
            IstEmployee.delete(0,END)
            for row in EmployeeData.SearchData(Refrence.get(),Firstname.get(),Surname.get(),Address.get(),Gender.get(),Mobile.get(),NINumber.get(),stdLoan.get(),Tax.get(),Pension.get(), Deduction.get(), NetPay.get(),GrossPay.get()):
                IstEmployee.insert(END,row,str(""))
            
        def PayRef():
            Payday.set(time.strftime("%d/%m/%y"))
            RefPay = random.randint(16999,890009)
            RefPaid = ("Ref" +str(RefPay))
            Refrence.set(RefPaid)

            NIpay = random.randint(34050, 400908)
            NIpaid = ("NI" + str(NIpay))
            NINumber.set(NIpay)

            NCode = random.randint(1000, 15000)
            CodeNI = ("NIC" + str(NCode))
            NICode.set(CodeNI)

            iTaxCode = random.randint(7000, 30000)
            PaymentTaxCode = ("TXC" + str(NCode))
            TaxCode.set(PaymentTaxCode)

            iDate = datetime.datetime.now()
            TaxPeriod.set(iDate.month)

        def MontlySal():
            PayRef()

            BS = float(BasicSalary.get())
            CW = float(CityWeighting.get())
            OT = float(OverTIme.get())
            OPD = float(OtherPaymentDue.get())

            MTax = ((BS + CW + OT + OPD) * 0.03)
            TTax = "Rs.",str("%.2f"%(MTax))
            Tax.set(TTax)

            M_Pension = ((BS + CW + OT + OPD) * 0.02)
            MM_Pension = "Rs.",str("%.2f"%(M_Pension))
            Pension.set(MM_Pension)

            M_stdLoan = ((BS + CW + OT + OPD) * 0.012)
            MM_stdLoan = "Rs.",str("%.2f"%(M_stdLoan))
            stdLoan.set(MM_stdLoan)

            M_NIpayment = ((BS + CW + OT + OPD) * 0.011)
            MM_NIpayment = "Rs.",str("%.2f"%(M_NIpayment))
            NIPayment.set(MM_NIpayment)

            Deduct = (MTax + M_Pension + M_stdLoan + M_NIpayment)
            Deduct_Payment = "Rs.",str("%.2f"%(Deduct))
            Deduction.set(Deduct_Payment)

            Gross_Pay = "Rs.",str("%.2f"%(BS +CW + OT + OPD))
            GrossPay.set(Gross_Pay)

            NetPayAfter = (BS + CW + OT + OPD) - Deduct
            MM_stdLoan = "Rs.",str("%.2f"%(NetPayAfter))
            NetPay.set(MM_stdLoan)

            TaxablePay.set(TTax)
            PensionablePay.set(MM_Pension)

            self.txtReceipt.insert(END, "\t  Monthly Pay Slip" + "\n\n")
            self.txtReceipt.insert(END, "***************************************************\n\n")
            self.txtReceipt.insert(END, "Refrence: \t\t\t" + Refrence.get()+"\n\n")
            self.txtReceipt.insert(END, "Pay Day: \t\t\t" + Payday.get()+"\n\n")
            self.txtReceipt.insert(END, "Employer Name: \t\t\t" + Surname.get()+"\n\n")
            self.txtReceipt.insert(END, "Employee Name: \t\t\t" + Firstname.get()+"\n\n")
            self.txtReceipt.insert(END, "Tax:    \t\t\t" + Tax.get()+"\n\n")
            self.txtReceipt.insert(END, "Pension: \t\t\t" + Pension.get()+"\n\n")
            self.txtReceipt.insert(END, "Student Loan: \t\t\t" + stdLoan.get()+"\n\n")
            self.txtReceipt.insert(END, "NI Number: \t\t\t" + NINumber.get()+"\n\n")
            self.txtReceipt.insert(END, "NI Payment: \t\t\t" + NIPayment.get()+"\n\n")
            self.txtReceipt.insert(END, "Deduction: \t\t\t" + Deduction.get()+"\n\n")
            self.txtReceipt.insert(END, "City Weighting: \t\t\t" + "Rs."+str(CityWeighting.get())+"\n\n")

            self.txtReceipt.insert(END, "\nTax Paid: \t\t\t" + "Rs."+str(TaxablePay.get())+"\n\n")
            self.txtReceipt.insert(END, "Over Time: \t\t\t" + OverTIme.get()+"\n\n")
            self.txtReceipt.insert(END, "Net Pay: \t\t\t" + NetPay.get()+"\n\n")
            self.txtReceipt.insert(END, "Gross Pay: \t\t\t" + GrossPay.get()+"\n\n")

            AddNew()
        
        #------------------------------------------Receipt-----------------------------------------------------#
          
        self.txtReceipt = Text(RightFrame1a, height=24, width=37,bd=8,font=('arial',9,'bold'))
        self.txtReceipt.grid(row=0, column=0)

        #------------------------------------------------------------------------------------------------------# 

        self.lalLabel=Label(TopFrame2,font=('arial',10,'bold'),padx=6,pady=2, text="Refrence\tFirst\tSurname\tAddress\t\tGemder\tMobile\tNI Number\tStudent Loan\tTax\tPension \tDeduction\tNet Pay\t\tGross Pay")
        self.lalLabel.grid(row=0,column=0, columnspan=17)

        #---------------------------------------------Listbox and Scrollbar------------------------------------# 

        

        scrollbar = Scrollbar(TopFrame2)
        scrollbar.grid(row=1,column=1,sticky='ns')

        IstEmployee = Listbox(TopFrame2,width=145,height=5,font=('arial',12,'bold'),yscrollcommand=scrollbar.set)
        IstEmployee.bind('<<ListbosSelect>>',EmployeeRec)
        IstEmployee.grid(row=1,column=0,padx=1,sticky='nsew')
        scrollbar.config(command = IstEmployee.xview)

        
        #--------------------------------------------Widget----------------------------------------------------# 

        self.lblReference= Label(LeftFrame1,font=('arial',12,'bold'),text="Refrence",bg="gainsboro",bd=7, anchor='w')
        self.lblReference.grid(row=0,column=0)
        self.txtReference= Entry(LeftFrame1,font=('arial',12,'bold'),textvariable=Refrence,bd=5, width = 65, justify='left')
        self.txtReference.grid(row=0,column=1)

        self.lblFirstname= Label(LeftFrame1,font=('arial',12,'bold'),text="Firstname",bg="gainsboro",bd=7, anchor='w')
        self.lblFirstname.grid(row=1,column=0)
        self.txtFirstname= Entry(LeftFrame1,font=('arial',12,'bold'),textvariable=Firstname,bd=5, width = 65, justify='left')
        self.txtFirstname.grid(row=1,column=1)

        self.lblSurname= Label(LeftFrame1,font=('arial',12,'bold'),text="Surname",bg="gainsboro",bd=7, anchor='w')
        self.lblSurname.grid(row=2,column=0)
        self.txtSurname= Entry(LeftFrame1,font=('arial',12,'bold'),textvariable=Surname,bd=5, width = 65, justify='left')
        self.txtSurname.grid(row=2,column=1)

        self.lblAddress= Label(LeftFrame1,font=('arial',12,'bold'),text="Address",bg="gainsboro",bd=7, anchor='w')
        self.lblAddress.grid(row=3,column=0)
        self.txtAddress= Entry(LeftFrame1,font=('arial',12,'bold'),textvariable=Address,bd=5, width = 65, justify='left')
        self.txtAddress.grid(row=3,column=1)

        self.lblGender= Label(LeftFrame1,font=('arial',12,'bold'),text="Gender",bg="gainsboro",bd=7, anchor='w')
        self.lblGender.grid(row=4,column=0)
        self.txtGender= Entry(LeftFrame1,font=('arial',12,'bold'),textvariable=Gender,bd=5, width = 65, justify='left')
        self.txtGender.grid(row=4,column=1)

        self.lblMobile= Label(LeftFrame1,font=('arial',12,'bold'),text="Mobile",bg="gainsboro",bd=7, anchor='w')
        self.lblMobile.grid(row=5,column=0)
        self.txtMobile= Entry(LeftFrame1,font=('arial',12,'bold'),textvariable=Mobile,bd=5, width = 65, justify='left')
        self.txtMobile.grid(row=5,column=1)
 
        #------------------------------------------------------------------------------------------------------# 
        
        self.lblCityWeighting= Label(LeftFrame2Left,font=('arial',12,'bold'),text="CityWeighting",bg="gainsboro",bd=7, anchor='e')
        self.lblCityWeighting.grid(row=0,column=0,sticky=W)
        self.txtCityWeighting= Entry(LeftFrame2Left,font=('arial',12,'bold'),textvariable=CityWeighting,bd=5, width = 20, justify='left')
        self.txtCityWeighting.grid(row=0,column=1)

        self.lblBasicSalary= Label(LeftFrame2Left,font=('arial',12,'bold'),text="Basic Salary",bg="gainsboro",bd=7, anchor='w', justify=LEFT)
        self.lblBasicSalary.grid(row=1,column=0,sticky=W)
        self.txtBasicSalary= Entry(LeftFrame2Left,font=('arial',12,'bold'),textvariable=BasicSalary,bd=5, width = 20, justify='left')
        self.txtBasicSalary.grid(row=1,column=1)

        self.lblOverTIme= Label(LeftFrame2Left,font=('arial',12,'bold'),text="Over TIme",bg="gainsboro",bd=7, anchor='w')
        self.lblOverTIme.grid(row=2,column=0,sticky=W)
        self.txtOverTIme= Entry(LeftFrame2Left,font=('arial',12,'bold'),textvariable=OverTIme,bd=5, width = 20, justify='left')
        self.txtOverTIme.grid(row=2,column=1)

        self.lblOtherPaymentDue= Label(LeftFrame2Left,font=('arial',12,'bold'),text="Other Payment Due",bg="gainsboro",bd=7, anchor='w')
        self.lblOtherPaymentDue.grid(row=3,column=0,sticky=W)
        self.txtOtherPaymentDue= Entry(LeftFrame2Left,font=('arial',12,'bold'),textvariable=OtherPaymentDue,bd=5, width = 20, justify='left')
        self.txtOtherPaymentDue.grid(row=3,column=1)        

        #------------------------------------------------------------------------------------------------------# 

        self.lblTax= Label(LeftFrame2Right,font=('arial',12,'bold'),text="Tax",bg="gainsboro",bd=7, anchor='e')
        self.lblTax.grid(row=0,column=0,sticky=W)
        self.txtTax= Entry(LeftFrame2Right,font=('arial',12,'bold'),textvariable=Tax,bd=5, width = 20, justify='left')
        self.txtTax.grid(row=0,column=1)

        self.lblPension= Label(LeftFrame2Right,font=('arial',12,'bold'),text="Pension",bg="gainsboro",bd=7, anchor='e')
        self.lblPension.grid(row=1,column=0,sticky=W)
        self.txtPension= Entry(LeftFrame2Right,font=('arial',12,'bold'),textvariable=Pension,bd=5, width = 20, justify='left')
        self.txtPension.grid(row=1,column=1)

        self.lblStudentLoan= Label(LeftFrame2Right,font=('arial',12,'bold'),text="Student Loan",bg="gainsboro",bd=7, anchor='e')
        self.lblStudentLoan.grid(row=2,column=0,sticky=W)
        self.txtStudentLoan= Entry(LeftFrame2Right,font=('arial',12,'bold'),textvariable=stdLoan ,bd=5, width = 20, justify='left')
        self.txtStudentLoan.grid(row=2,column=1)

        self.lblNIPayment= Label(LeftFrame2Right,font=('arial',12,'bold'),text="NI Payment",bg="gainsboro",bd=7, anchor='e')
        self.lblNIPayment.grid(row=3,column=0,sticky=W)
        self.txtNIPayment= Entry(LeftFrame2Right,font=('arial',12,'bold'),textvariable=NIPayment,bd=5, width = 20, justify='left')
        self.txtNIPayment.grid(row=3,column=1)


        #------------------------------------------------------------------------------------------------------# 
        
        self.lblPayday= Label(RightFrame2a,font=('arial',12,'bold'),text="Payday",bg="gainsboro",bd=7, anchor='e')
        self.lblPayday.grid(row=0,column=0,sticky=W)
        self.txtPayday= Entry(RightFrame2a,font=('arial',12,'bold'),textvariable=Payday,bd=5, width = 20, justify='left')
        self.txtPayday.grid(row=0,column=1)

        self.lblTaxPeriod= Label(RightFrame2b,font=('arial',12,'bold'),text="Tax Period",bg="gainsboro",bd=7, anchor='e')
        self.lblTaxPeriod.grid(row=0,column=0,sticky=W)
        self.txtTaxPeriod= Entry(RightFrame2b,font=('arial',12,'bold'),textvariable=TaxPeriod,bd=5, width = 17, justify='left')
        self.txtTaxPeriod.grid(row=0,column=1)

        self.lblTaxCode= Label(RightFrame2b,font=('arial',12,'bold'),text="Tax Code",bg="gainsboro",bd=7, anchor='e')
        self.lblTaxCode.grid(row=1,column=0,sticky=W)
        self.txtTaxCode= Entry(RightFrame2b,font=('arial',12,'bold'),textvariable=TaxCode,bd=5, width = 17, justify='left')
        self.txtTaxCode.grid(row=1,column=1)

        self.lblNINumber= Label(RightFrame2b,font=('arial',12,'bold'),text="NI Number",bg="gainsboro",bd=7, anchor='e')
        self.lblNINumber.grid(row=2,column=0,sticky=W)
        self.txtNINumber= Entry(RightFrame2b,font=('arial',12,'bold'),textvariable=NINumber,bd=5, width = 17, justify='left')
        self.txtNINumber.grid(row=2,column=1)

        self.lblNICode= Label(RightFrame2b,font=('arial',12,'bold'),text="NICode",bg="gainsboro",bd=7, anchor='e')
        self.lblNICode.grid(row=3,column=0,sticky=W)
        self.txtNICode= Entry(RightFrame2b,font=('arial',12,'bold'),textvariable=NICode,bd=5, width = 17, justify='left')
        self.txtNICode.grid(row=3,column=1)

        self.lblTaxablePay= Label(RightFrame2c,font=('arial',12,'bold'),text="Taxable Pay",bg="gainsboro",bd=7, anchor='e')
        self.lblTaxablePay.grid(row=0,column=0,sticky=W)
        self.txtTaxablePay= Entry(RightFrame2c,font=('arial',12,'bold'),textvariable=TaxablePay,bd=5, width = 12, justify='left')
        self.txtTaxablePay.grid(row=0,column=1)

        self.lblPensionablePay= Label(RightFrame2c,font=('arial',12,'bold'),text="Pensionable Pay",bg="gainsboro",bd=7, anchor='e')
        self.lblPensionablePay.grid(row=1,column=0,sticky=W)
        self.txtPensionablePay= Entry(RightFrame2c,font=('arial',12,'bold'),textvariable=PensionablePay,bd=5, width = 12, justify='left')
        self.txtPensionablePay.grid(row=1,column=1)


        self.lblNetPay= Label(RightFrame2d,font=('arial',12,'bold'),text="Net Pay",bg="gainsboro",bd=7, anchor='e')
        self.lblNetPay.grid(row=0,column=0,sticky=W)
        self.txtNetPay= Entry(RightFrame2d,font=('arial',12,'bold'),textvariable=NetPay,bd=5, width = 17, justify='left')
        self.txtNetPay.grid(row=0,column=1)


        self.lblGrossPay= Label(RightFrame2d,font=('arial',12,'bold'),text="Gross Pay",bg="gainsboro",bd=7, anchor='e')
        self.lblGrossPay.grid(row=1,column=0,sticky=W)
        self.txtGrossPay= Entry(RightFrame2d,font=('arial',12,'bold'),textvariable=GrossPay,bd=5, width = 17, justify='left')
        self.txtGrossPay.grid(row=1,column=1)


        self.lblDeduction= Label(RightFrame2d,font=('arial',12,'bold'),text="Deduction",bg="gainsboro",bd=7, anchor='e')
        self.lblDeduction.grid(row=2,column=0,sticky=W)
        self.txtDeduction= Entry(RightFrame2d,font=('arial',12,'bold'),textvariable=Deduction,bd=5, width = 17, justify='left')
        self.txtDeduction.grid(row=2,column=1)

        #-----------------------------------------------Buttons-------------------------------------------------------# 
        
        self.btnAddNewTotal=Button(TopFrame1,pady=1,bd=4,fg="black",command = MontlySal, font=('arial', 16,'bold'), padx=24, width=8,text="AddNew/Total").grid(row=0,column=0,padx=1)

        self.btnPrint=Button(TopFrame1,pady=1,bd=4,fg="black", command=Print, font=('arial', 16,'bold'), padx=24, width=8,text="Print").grid(row=0,column=1,padx=1)

        self.btnDisplay=Button(TopFrame1,pady=1,bd=4,fg="black", command = Disp,font=('arial', 16,'bold'), padx=24, width=8,text="Display").grid(row=0,column=2,padx=1)

        self.btnUpdate=Button(TopFrame1,pady=1,bd=4,fg="black", command=Upd, font=('arial', 16,'bold'), padx=24, width=8,text="Update").grid(row=0,column=3,padx=1)

        self.btnDelete=Button(TopFrame1,pady=1,bd=4,fg="black",command=Del, font=('arial', 16,'bold'), padx=24, width=8,text="Delete").grid(row=0,column=4,padx=1)

        self.btnSearch=Button(TopFrame1,pady=1,bd=4,fg="black",command=search, font=('arial', 16,'bold'), padx=24, width=8,text="Search").grid(row=0,column=5,padx=1)

        self.btnReset=Button(TopFrame1,pady=1,bd=4,fg="black",command=Reset, font=('arial', 16,'bold'), padx=24, width=8,text="Reset").grid(row=0,column=6,padx=1)

        self.btnExit=Button(TopFrame1,pady=1,bd=4,fg="black", command=EQuit, font=('arial', 16,'bold'), padx=24, width=8,text="Exit").grid(row=0,column=7,padx=1)        

        #------------------------------------------------------------------------------------------------------# 

if __name__=='__main__':
    root=Tk()
    app=Employee(root)
    root.mainloop()
