import pickle
from tabulate import tabulate
import os
import colorama
from colorama import Fore
colorama.init(autoreset=True)
def playsound1(text):
    import os
    from playsound import playsound
    from gtts import gTTS
    audio=gTTS(text)
    audio.save("1.mp3")
    playsound("1.mp3")
    os.remove("1.mp3")
def receipt(accno,time,credit,debit,transactionid,Description):
    from tabulate import tabulate

    x="\n\n\n Transaction id "+"\n\n\n Time"+"\n\n\n Account number"+"\n\n\n Description"+"\n\n\n Credit"+"\n\n\n Debit"
    y="\n\n\n"+transactionid+"\n\n\n"+time+'\n\n\n'+accno+"\n\n\n"+Description+"\n\n\n"+credit+'\n\n\n'+debit
    z=[[x,y]]
    print("****************BANKING SYSTEM****************\n\n")
    print(tabulate(z,tablefmt="grid"))

    ans=input("Do you want to save this receipt in txt file?(y/n)")
    if ans=="y":
        print("The receipt is saved with the transaction id")
        playsound1("The receipt is saved with the transaction id")
        f=open(transactionid+".txt","w")
        f.write("****************BANKING SYSTEM****************\n\n")

        f.writelines(tabulate(z,tablefmt="grid"))
        f.close()
    else:
        print("Receipt wil not be saved")
def logo():
    for i in range(0,5):
        z=i+5

        j=10-z
        print("\t\t\t\t\t\t\t","*"*z," "*2*j,"*"*z)
    print("\t\t\t\t\t\t\t","*"*22)
    for i in range(5,-1,-1):
        z=i+5
        j=10-z
        print("\t\t\t\t\t\t\t","*"*z," "*2*j,"*"*z)
def integer(x):
     if x.isnumeric() and int(x)>0:
         x=int(x)
         return x
     else:
        print("Please enter a valid integer only input and greater than 0")
        x=input("Enter again")
        x=integer(x)
        return x

def strings(x):

    if x.isalpha():
        return x
    else:
         print("Please enter a valid Alphabet only input")
         x=input("Enter again")
         x=strings(x)
         return x
def number(state,city,type,operation,accno):
        import random
        if operation=="LOANAM":

                number=str(accno)+"LC"+str(random.randint(0,10000))
                return number

        elif operation=="LOANPAY":
                number=str(accno)+"LPAY"+str(random.randint(0,10000))
                return number
        elif operation=="ACCB":
                number=str(state)+str(city)+"B"+str(random.randint(0,10000))
                return number
        elif operation=="ACCS":
                number=str(state)+str(city)+"S"+str(random.randint(0,10000))
                return number
        elif operation=="WITHC":
                number=str(accno)+"WC"+str(random.randint(0,10000))
                return number
        elif operation=="ACCTRANS":
                number=str(accno)+"WA"+str(random.randint(0,10000))
                return number
        elif operation=="DEP":
                number=str(accno)+"DEP"+str(random.randint(0,10000))
                return number
        elif operation=="LOAN":
                number=str(accno)+"L"+str(random.randint(0,10000))
                return number
        elif operation=="NOTI":
                number="admNOTIF"+str(random.randint(0,10000))
                return number
        elif operation=="APPR":
                number=str(accno)+"APPR"+str(random.randint(0,10000))
                return number
        elif operation=="INT":
                number="admINTECHANGE"+str(random.randint(0,10000))
                return number
        elif operation=="ISSUE":
                number=str(accno)+"ISSUE"+str(random.randint(0,10000))
                return number
def state():
   stat=input('''Enter the state code against the state
Andaman and Nicobar Islands        AN
Andhra Pradesh                     AP
Arunachal Pradesh                  AR
Assam                              AS
Bihar                              BR
Chandigarh                         CH
Chhattisgarh                       CT
Dadra and Nagar Haveli             DN
Daman and Diu                      DD
Delhi                              DL
Goa                                GA
Gujarat                            GJ
Haryana                            HR
Himachal Pradesh                   HP
Jammu and Kashmir                  JK
Jharkhand                          JH
Karnataka                          KA
Kerala                             KL
Lakshadweep                        LD
Madhya Pradesh                     MP
Maharashtra                        MH
Manipur                            MN
Meghalaya                          ML
Mizoram                            MZ
Nagaland                           NL
Odisha                             OR
Puducherry                         PY
Punjab                             PB
Rajasthan                          RJ
Sikkim                             SK
Tamil Nadu                         TN
Telangana                          TG
Tripura                            TR
Uttar Pradesh                      UP
Uttarakhand                        UT
West Bengal                        WB
                             ''')
   if stat in(["AP","AR","AS","BR","CH","CT","DN","DD","DL","GA","GJ","HR","HP","JK","JH","KA","KL","LD","MP","MH","ML","NL","PY","RJ","TN","TG","TR",'UP','UT','WB']):
       return stat
   else:
       print("Please enter a valid state code")
       return None
def accountcheck1(accno):
    f=open("accounts.dat","rb")
    found=False
    try:
        while True:
            x=pickle.load(f)
            if x["accno"]==accno:
                found=True
                return found
    except EOFError:
        if found==False:
            print("Invalid Account number")
            return None
        else:
            return True
    f.close()
def businessid():
    z = input("Enter the Business ID(5 digit integer): ")
    if len(z)==5:
        z = integer(z)
        return z
    else:
        print("Your Business ID is not of the specified condition")
        return None
def createaccount(type1):
    from getpass import getpass
    infileacc=open("accounts.dat","ab+")
    import datetime
    if type1=="C":
        x=input("Enter the Name of Buisness: ")

        y=input("Enter the Business Type: ")

        appa=businessid()
        if appa==None:
            return None
        a=state()
        if a==None:
            return None
        b=input("Enter the City of Operation: ")
        b=b.upper()
        b=strings(b)
        c=input("Enter the Annual Profit: ")
        c=integer(c)
        acc=number(a,b,"C","ACCB","")
    elif type1=="S":
                x=input("Enter your name: ")

                y=input("Enter the Adress: ")
                a=state()
                if a == None:
                    return None
                b=input("Enter the City: ")
                b=b.upper()
                b=strings(b)
                c=input("Enter the Annual Income: ")
                c=integer(c)
                acc=number(a,b,"C","ACCS","")
    else:
        print("Please enter a valid code")
        return None

    d=input("Enter the initial amount: ")
    d=integer(d)
    e=input("Enter the password: ")
    f=input("Confirm Password: ")
    if e==f:
        g=datetime.datetime.now()
        g=str(g)
        print("Your account has been made with account number: "+acc)
        l={}
        l["accno"]=acc
        if type1=="C":
            l["Name_of_Business"]=x
            l["BusinessTYpe"]=y
            l["Business ID"]=appa
            l["Annual Profit"]=c
            l["Type"]="C"
        elif type1=="S":
            l["Name"]=x
            l["Address"]=y

            l["Annual Income"]=c
            l["Type"]="S"
        l["City"]=b
        l["State"]=a
        l["Loan Due"]=0

        l["Balance"]=d
        l["Accountcreated"]=g
        l["pwd"]=e
        pickle.dump(l,infileacc)
        infileacc.close()
        eg=open("notification.dat","ab+")
        ef={}
        x="Thank you for opening an account in our banking system"
        ref = number("", "", "", "NOTI", "")
        ef["ref"] = ref
        ef["Message"]=x
        ef["Target"]=acc
        ef["Time"]=str(datetime.datetime.now())
        pickle.dump(ef,eg)
        eg.close()
        playsound1("Thank you for opening an account in our banking system")
        print("THANK YOU FOR OPENING AN ACCOUNT IN OUR BANKING SYSTEM")
        return [acc,e]

    else:
        playsound1("Invalid confirm password")
        print("confirm password and password are wrong")
        return None

def viewspecific(accno):
    import pickle
    from tabulate import tabulate
    import colorama
    from colorama import Fore
    colorama.init(autoreset=True)
    z=[]
    f=open("accounts.dat","rb")
    found=False
    try:
        print("\t\t \n")
        while True:
            x=pickle.load(f)
            if x["accno"]==accno:
                if x["Loan Due"]>0:
                    x["Loan Due"]=Fore.RED+str(x["Loan Due"])
                    x["Balance"]=Fore.WHITE+str(x["Balance"])
                y=list(x.values())

                del y[10]

                z+=[y]
                a=list(x.keys())
                del a[10]

                found=True
    except EOFError:
       print()
    if found==True:
        z.insert(0,a)
        print("ACCOUNT SUMMARY")
        print(tabulate(z,tablefmt="grid",showindex=True))
    f.close()
def viewall():
    import colorama
    from colorama import Fore
    colorama.init(autoreset=True)
    found=False
    found1=False
    import pickle
    from tabulate import tabulate
    f=open("accounts.dat","rb+")
    try:

        z=[]
        d=[]
        a=[]
        c=[]

        while True:

            x=pickle.load(f)
            if x["Type"]=="C":
                if x["Loan Due"]>0:
                    x["Loan Due"]=Fore.RED+str(x["Loan Due"])
                    x["Balance"]=Fore.WHITE+str(x["Balance"])
                y=list(x.values())
                z+=[y]
                a=list(x.keys())
                found=True
            else:
                if x["Loan Due"]>0:
                    x["Loan Due"]=Fore.RED+str(x["Loan Due"])
                    x["Balance"]=Fore.WHITE+str(x["Balance"])
                b=list(x.values())
                del b[10]
                c+=[b]
                d=list(x.keys())
                del d[10]
                found1=True


    except EOFError:
       print()
    if found==True:
        print("\t\tThe particulars of the Current Type Bank Account holders are\n\n")
        z.insert(0,a)

        print(tabulate(z,headers="firstrow",tablefmt="grid",showindex=True))
    else:
        print("No Current Type Bank Account holder")
    if found1==True:

        print('\t\t\t The particulats of the Savings Account holders are\n\n')
        c.insert(0,d)
        print(tabulate(c,headers="firstrow",tablefmt="grid",showindex=True))
    else:
        print("No Savings Type Bank Account holder")
    f.close()

def notificationadmin():

        import datetime
        d={}

        c=open("notification.dat","ab+")
        x=input("Enter the message: ")
        y=input("Enter the target(ALL,ACCOUNT NUMBER): ")
        ref=number("","","","NOTI","")
        d["ref"]=ref
        d["Message"]=x
        d["Target"]=y
        d["Time"]=str(datetime.datetime.now())
        pickle.dump(d,c)
        print("Notification has successfully sent")
        c.close()
def notificationsee():
    c=open("notification.dat","rb")
    z=[]

    try:
        while True:
            d=pickle.load(c)
            y=list(d.values())
            z+=[y]
            a=list(d.keys())

    except EOFError:
        print()
    z.insert(0,a)
    print(tabulate(z,headers="firstrow",tablefmt="grid",showindex=True))
    c.close()
def notificationuser(accno):
    c=open("notification.dat","rb")
    z=[]
    try:
        while True:
            d=pickle.load(c)
            if d["Target"]==accno or d["Target"]=="ALL":
                 y=list(d.values())
                 z+=[y]
                 a=list(d.keys())
    except EOFError:
        print()
    z.insert(0,a)
    print(tabulate(z,headers="firstrow",tablefmt="grid",showindex=True))
    c.close()
def deposit(accno):
    import datetime
    x=input("Enter the amount: ")
    x=integer(x)
    c=open("accounts.dat","rb+")
    e=open("ref.dat","ab+")
    try:
        while True:
            pos=c.tell()
            d=pickle.load(c)
            if d["accno"]==accno:
                d["Balance"]+=x
                g=d["Balance"]
                c.seek(pos)
                pickle.dump(d,c)
                ref=number("","","","DEP",accno)
                playsound1("Transaction Successfully done ")
                print("Transaction Successfully done with Reference number",ref)
                h=d["Loan Due"]
                print("Your new balance is: ",d["Balance"])

    except EOFError:
        print()

    f={}
    f["Time"]=str(datetime.datetime.today())
    f["REFID"]=ref
    f["Description"]="CASH DEPOSIT"
    f["accno"]=accno

    f["Credit"]=x
    f["Debit"]=0


    f["Credited to"]=""



    f["Credited from"]=""
    f["Balance"]=g
    f["Loan Due"]=h

    f["Transacted Amount"]=x
    f["Identifing accnoo"]=accno
    receipt(accno,str(datetime.datetime.today()),str(x),str(0),ref,"CASH DEPOSIT")
    pickle.dump(f,e)
    c.close()
    e.close()

def cashwithdrawal(accno):
    import datetime
    import pickle
    print("Please be aware that the lower limit is 500 and upper limit is 1,00,000")
    x=input("Enter the amount: ")
    x = integer(x)
    abh=False
    if x>=500 and x<=100000:
        abh=True
    else:
        print("Your amount is less than 500 or greater than 100000")

    if abh==True:
        c=open("accounts.dat","rb+")
        e=open("ref.dat","ab+")
        found=0
        try:
            while True:
                pos=c.tell()
                d=pickle.load(c)
                if d["accno"]==accno:
                    g=d["Balance"]
                    print("Your balance was: ",g)
                    if x<=g:
                        d["Balance"]-=x
                        g=d["Balance"]
                        c.seek(pos)
                        pickle.dump(d,c)
                        ref=number("","","","WITHC",accno)
                        playsound1("Transaction Successfully done ")
                        print("Transaction Successfully done with Reference number",ref)
                        h=d["Loan Due"]

                        found=True
                    else:
                        playsound1("Insufficient Balance")
                        print("Insufficient Balance")
                        return None
                    print("Your balance is: ",g)
        except EOFError:
            print()
        if found== True:
            f={}
            f["Time"]=str(datetime.datetime.today())
            f["REFID"]=ref
            f["Description"]="CASH WITHDRAWAL"
            f["accno"]=accno

            f["Credit"]=0
            f["Debit"]=x

            f["Credited to"]=""
            f["Credited from"]=""
            f["Balance"]=g
            f["Loan Due"]=h

            f["Transacted Amount"]=x
            f["Identifing accnoo"]=accno
            pickle.dump(f,e)
            receipt(accno,str(datetime.datetime.today()),str(0),str(x),ref,"CASH WITHDRAWAL")
        else:
            print()
        c.close()
        e.close()
def changeinterest():
    import datetime
    c=open("histloan.dat","ab+")
    d=open("loan.dat","wb")
    print("Note that every interest rate must be less than 30%")
    x=input("Enter the interest for Home Loan: ")
    x=integer(x)
    y=input("Enter the interest for Personal Loan: ")
    y=integer(y)
    adarsh=input("Enter the interest for Educational Loan: ")
    adarsh=integer(adarsh)
    a=input("Enter the interest for Car loan: ")
    a=integer(a)
    b=input("Enter the interest for Business Account: ")
    b=integer(b)
    if x<30 and y<30 and adarsh<30 and a<30 and b<30:
        ref=number("","","","INT","")

        l={}
        l["ref"]=ref
        l["Home loan"]=x
        l["Personal Loan"]=y
        l["Education Loan"]=adarsh
        l["Car Loan"]=a
        l["Business Loan"]=b
        pickle.dump(l,d)
        l["Time of creation"]=str(datetime.datetime.now())
        pickle.dump(l,c)
        c.close()
        d.close()

        print("The interest rates have successfully been changed")
        g=open("notification.dat","ab+")
        z={}
        z["ref"]=ref
        z["Message"]='The new rates for Home Loan='+str(x)+" ,Personal Loan="+str(y)+" ,Educational Loan="+str(adarsh)+" ,Car Loan="+str(a)+" ,Business Loan="+str(b)
        z["Target"]="ALL"
        z["Time"]=str(datetime.datetime.now())
        pickle.dump(z,g)
        g.close()
    else:
        print("Please enter all the interest rates below 30% only")
def interehist():
     c=open("histloan.dat","rb+")
     z=[]
     a=[]
     try:
         while True:
             x=pickle.load(c)
             y=list(x.values())
             z+=[y]
             a=list(x.keys())
     except EOFError:
        print()
     z.insert(0,a)
     print(tabulate(z,headers="firstrow",tablefmt="grid",showindex=True))
     c.close()
def loanpage(accno):
    import pickle
    import datetime
    abh=False
    h=open("accounts.dat","rb")
    try:
        while True:
            z=pickle.load(h)
            if z["accno"]==accno:
                type1=z["Type"]
    except EOFError:
        print()
    h.close()
    f=open("loan.dat","rb+")
    z=[]
    try:
        while True:
            x=pickle.load(f)
            y=list(x.values())
            z+=[y]
            a=list(x.keys())
            H=x["Home loan"]
            P=x["Personal Loan"]
            E=x["Education Loan"]
            C=x["Car Loan"]
            B=x["Business Loan"]
    except EOFError:
       print()
    z.insert(0,a)
    print(tabulate(z,headers="firstrow",tablefmt="grid",showindex=True))
    if type1=="C":
        playsound1("You have opted for Business loan only loan for Business account")
        print("You have opted for Business loan only loan for Business account")

        op="B"
        inte=B
    else:

        g=input('''Which type of Loan would you want to take
                CAR LOAN : 1
                HOME LOAN : 2
                EDUCATIONAL LOAN : 3
                PERSONAL LOAN : 4
                \n''')
        g=integer(g)
        if g==1:
            playsound1("You have applied for car loan")
            print("You have applied for car loan")
            op="C"
            inte=C
        elif g==2:
            playsound1("You have applied for Home loan")
            print("You have applied for Home loan")
            op="H"
            inte=H
        elif g==3:
            playsound1("You have applied for Educational loan")
            print("You have applied for Educational loan")
            op="E"
            inte=E
        elif g==4:
            playsound1("You have applied for Personal loan")
            print("You have applied for Personal loan")
            op="P"
            inte=P


    g=open("appr.dat","ab+")
    playsound1("Please be aware that the minimum limit of loan is 1000")
    print("Please be aware that the minimum limit of loan is 1000")
    y=input("Enter the amount")
    y=integer(y)
    if y>=1000:
        abh=True
    else:
        print("Your amount is less than 1000 ")
        return None
    if abh==True:
        z=input("Enter the tenure(months)")
        z=integer(z)
        k=inte*y*z/1200
        print("Your interest is ",k)
        ref=number("","","","APPR",accno)
        playsound1("Your application has gone to admin , if it gets approved a notification will come in the notification panel and money will be credited to your account")
        print("Your application has gone to admin , if it gets approved a notification will come in the notification panel and money will be credited to your account")

        print("Your appliation reference number is: ",ref)

        l={}
        l["ref"]=ref
        l["accno"]=accno
        l["Type"]=type1
        l["Type of Loan"]=op
        l["Amount"]=y
        l["Tenure(months)"]=z
        l["Interest"]=k
        l["Approved"]="Pending"
        l["Time"]=str(datetime.datetime.now())
        pickle.dump(l,g)
        g.close()
        f.close()
def checkloanstatus(accno):
    import pickle
    from tabulate import tabulate
    import colorama
    from colorama import Fore
    colorama.init(autoreset=True)
    found=False
    z=[]
    a=[]
    ac=open("appr.dat","rb")
    try:
        while True:
            x=pickle.load(ac)
            if x["accno"]==accno:
                if x["Approved"]=="Yes":

                        x["Approved"] = Fore.GREEN + str(x["Approved"])

                elif x["Approved"]=="NO":

                         x["Approved"] = Fore.RED + str(x["Approved"])
                else:

                        x["Approved"]=Fore.YELLOW+str(x["Approved"])
                x["Time"]=Fore.WHITE+str(x["Time"])
                y=list(x.values())
                z+=[y]
                a=list(x.keys())
                found=True
    except EOFError:
        print()
    if found==True:
        playsound1("The status of your loan applications are")
        print("The status of your loan applications are: \n\n")
        ac.close()
        z.insert(0,a)
        print(tabulate(z,headers="firstrow",tablefmt="grid",showindex=True))
    else:
        print("No loans for your account")
def approvedanddisapproved():
    import pickle
    from tabulate import tabulate
    import colorama
    from colorama import Fore
    colorama.init(autoreset=True)
    z=[]
    a=[]
    ac=open("appr.dat","rb")
    try:
        while True:
            x=pickle.load(ac)

            if x["Approved"]=="Yes":

                    x["Approved"] = Fore.GREEN + str(x["Approved"])

            elif x["Approved"]=="NO":
 
                     x["Approved"] = Fore.RED + str(x["Approved"])
            else:

                    x["Approved"]=Fore.YELLOW+str(x["Approved"])
            x["Time"]=Fore.WHITE+str(x["Time"])
            y=list(x.values())
            z+=[y]
            a=list(x.keys())
    except EOFError:
        print()
    print("The applications and the status of approvals are: \n\n")
    ac.close()
    z.insert(0,a)
    print(tabulate(z,headers="firstrow",tablefmt="grid",showindex=True))
def approvalpage():
    import pickle
    import datetime
    amma=[]
    from tabulate import tabulate
    f=open("appr.dat","rb+")
    z=[]
    try:
        while True:
            x=pickle.load(f)
            amma+=[x]
            if x["Approved"]=="Pending":
                y=list(x.values())
                z+=[y]

                a=list(x.keys())
    except EOFError:
       print()
    f.close()
    z.insert(0,a)
    print(tabulate(z,headers="firstrow",tablefmt="grid",showindex=True))
    z=input("Enter the reference id  which you want to approve the loan from the table ")
    acbd=input("Enter the action for approval (y/n)")
    found=False
    if acbd=="y":
        f=open("appr.dat","wb")
        for abc in amma:
            if abc["ref"]==z and abc["Approved"]=="Pending":
                adarsh=abc["accno"]
                abc["Approved"]="Yes"
                m=x["Amount"]
                p=m+abc["Interest"]
                found=True
        for acd in amma:
            pickle.dump(acd,f)
        f.close()
        if found==False:
            print("Wrong reference id")
            #om sir ne kaafi madad kri!!!
            #vilakshan sir ne bhi kri kaafi madad!!
            return None
        g=open("accounts.dat","rb+")
        try:
            while True:
                pos=g.tell()
                ac=pickle.load(g)
                if ac["accno"]==adarsh:

                    ac["Balance"]+=m
                    o=ac["Balance"]
                    ac["Loan Due"]+=p
                    n=ac["Loan Due"]
                    g.seek(pos)
                    pickle.dump(ac,g)
        except EOFError:
            print()
        g.close()
        ref=number("","","","LOANAM",adarsh)
        h=open("ref.dat","ab+")
        f={}
        f["Time"]=str(datetime.datetime.today())
        f["REFID"]=ref
        f["Description"]="LOAN CREDIT"
        f["accno"]=adarsh

        f["Credit"]=m
        f["Debit"]=0

        f["Credited to"]=''

        f["Credited from"]=""
        f["Balance"]=o
        f["Loan Due"]=n

        f["Transacted Amount"]=m
        f["Identifing accnoo"]=adarsh
        print()
        pickle.dump(f,h)
        h.close()
        ef={}
        eg=open("notification.dat","ab+")

        x="Congratulations your loan has successfully been approved"
        ref = number("", "", "", "NOTI", "")

        ef["ref"]=ref
        ef["Message"]=x
        ef["Target"]=adarsh
        ef["Time"]=str(datetime.datetime.now())
        pickle.dump(ef,eg)
        print("Notification has successfully sent")
        eg.close()
    elif acbd=="n":

        f=open("appr.dat","wb")
        for abc in amma:

            if abc["ref"]==z and abc["Approved"]=="Pending":
                abc["Approved"]="NO"
                adarsh=abc["accno"]
        for acd in amma:
            pickle.dump(acd,f)
        f.close()
        ef={}
        f.close()
        eg=open("notification.dat","ab+")
        ref = number("", "", "", "NOTI", "")
        ef["ref"] = ref
        x="Sorry your loan has not been approved"
        ef["Message"]=x
        ef["Target"]=adarsh
        ef["Time"]=str(datetime.datetime.now())
        pickle.dump(ef,eg)
        print("Notification has successfully sent")
        eg.close()
def systransaction():

    import numpy as np
    import matplotlib.pyplot as plt
    import pickle
    print("THE TRANSACTION SUMMARY IS")
    f=open("ref.dat","rb+")
    z=0
    a=0
    b=0
    try:
        while True:
            x=pickle.load(f)
            b+=x["Transacted Amount"]
            if x["Description"]=="LOAN CREDIT":
                z+=x["Credit"]
            elif x["Description"]=="LOAN REPAYMENT":
                a+=x["Debit"]

    except EOFError:
       print()
    f.close()

    f=open("appr.dat","rb+")
    count=0
    count1=0
    try:
        while True:
            x=pickle.load(f)
            if x["Approved"]=="Yes":
                count1+=1
            count+=1
    except EOFError:
       print()
    f.close()
    if count !=0:
        p=count1/count*100
        print("Loan Approval percentage by the admin",p)
    acc=0
    f=open("accounts.dat","rb+")
    try:
        while True:
            x=pickle.load(f)
            acc+=1
    except EOFError:
       print()
    k=z-a
    if k<=0:
        k=0
    print("Total Transacted Amount through the system is ",b)
    print("Total loan given to the customer is ",z)
    print("Total loan repaid by the customers ",a)
    print("Total Loan due",k)
    data={"Transacted Amount":b,"Loan amount given":z,"Loan repaid":a,"Loan due":k,"Customers":acc}
    category=list(data.keys())
    values=list(data.values())
    fig = plt.figure(figsize = (10, 5))

    # creating the bar plot
    plt.bar(category, values, color ='blue',
            width = 0.4)

    plt.xlabel("category")
    plt.ylabel("Figures")
    plt.title("SYSTEM TRANSACTION SUMMARY")
    plt.show()






def loanpayment(accno):
    import datetime
    import pickle

    c=open("accounts.dat","rb+")
    e=open("ref.dat","ab+")
    found=0
    vilak=False
    try:
        while True:
            pos=c.tell()
            d=pickle.load(c)
            if d["accno"]==accno and d["Loan Due"]>0:
                g=d["Balance"]
                k=d["Loan Due"]
                print("Balance of your account is: ",g)
                print("Loan Due for your account is: ",k)
                if g>=k :
                    z=input('''
                            Since you have balance greater than your loan due please enter the code for the following functions
                            REPAY WHOLE LOAN DUE  1
                            REPAY PARTIAL AMOUNT  2\n\n''')
                    z=integer(z)
                    vilak=True
                if vilak==True:
                    if z==1:
                        print("You have opted for whole loan repayment")
                        x=k
                    elif z==2:
                        x=input("Enter the amount to be repaid: ")
                        x=integer(x)
                    else:
                        print("Please enter a valid code")
                        return None
                else:
                    x=input("Enter the amount to be repaid: ")
                    x=integer(x)
                if x<=g and k!=0 and x<=k:

                    d["Balance"]-=x
                    g=d["Balance"]
                    d["Loan Due"]-=x
                    k=d["Loan Due"]
                    c.seek(pos)
                    pickle.dump(d,c)
                    ref=number("","","","LOANPAY",accno)
                    playsound1("Transaction Successfully done ")
                    print("Transaction Successfully done with Reference number",ref)

                    found=True
                else:
                    print("Insufficient Balance or the Loan Due is 0 or the amount is greater than the loan due")
                    return None
            else:
                print("Either no loan is in your name or your loan due is 0")

    except EOFError:
        print()
    if found==True:
        f={}
        f["Time"]=str(datetime.datetime.today())
        f["REFID"]=ref
        f["Description"]="LOAN REPAYMENT"
        f["accno"]=accno

        f["Credit"]=0
        f["Debit"]=x

        f["Credited to"]=""


        f["Credited from"]=""
        f["Balance"]=g
        f["Loan Due"]=k

        f["Transacted Amount"]=x
        f["Identifing accnoo"]=accno
        pickle.dump(f,e)
        receipt(accno,str(datetime.datetime.today()),str(0),str(x),ref,"LOAN REPAYMENT")
    else:
        print()
    c.close()
    e.close()
def manageaccount(accno):
    import pickle

    f=open("accounts.dat","rb+")
    try:
        while True:
            pos=f.tell()
            x=pickle.load(f)

            if x["accno"]==accno:

                if x["Type"]=="C":
                    z=input('''Please enter value for the appropriate function

                          1 Annual Profit
                          2 Password\n\n''')
                    z=integer(z)
                    a=input("Enter the new value: ")

                    if z==1:
                        x['Annual Profit']=a
                    elif z==2:
                        x['pwd']=a
                    else:
                        print("Please enter a valid code")
                        return None
                else:
                    z=input('''Please enter value for the appropriate function
                          1 Name
                          2 Address
                          3 Annual Income
                          4 Password\n\n''')
                    z=integer(z)
                    a=input("Enter the new value: ")
                    if z==1:
                        x['Name']=a
                    elif z==2:
                        x['Address']=a
                    elif z==3:
                        x['Annual Income']=a
                    elif z==4:
                        x['pwd']=a
                    else:
                        print("Please enter a valid code")
                        return None
                f.seek(pos)
                pickle.dump(x,f)


    except EOFError:
       print()
    f.close()
    print("Successfully updated")
    viewspecific(accno)


def accounttransfer(accno):
    import pickle
    import datetime


    from tabulate import tabulate
    f = open("accounts.dat", "rb+")
    found=False
    try:

        z = []
        d = []
        a = []
        c = []

        while True:

            x = pickle.load(f)


            if x["accno"]!=accno:
                y = [str(x["accno"])]
                z += [y]
                a=["Account Number"]
                found=True

    except EOFError:
        if found==False:
            playsound1("NO accounts registered other than yours")
            print("NO accounts registered other than yours.")
            return None
    print("\t\tThe accounts present in the system are\n\n")
    z.insert(0, a)

    print(tabulate(z, headers="firstrow", tablefmt="grid", showindex=True))

    f.close()

    accno1=input("Enter the target account number")
    a=input("Enter the amount")
    a=integer(a)
    found=0
    e=open("ref.dat","ab+")
    if accountcheck1(accno1)==True:
        c=open("accounts.dat","rb+")

        try:
            while True:
                pos=c.tell()
                d=pickle.load(c)
                if d["accno"]==accno:

                    g=d["Balance"]
                    print("Your balance was: ",g)
                    if a<=g:
                        d["Balance"]-=a
                        g=d["Balance"]
                        c.seek(pos)
                        pickle.dump(d,c)
                        ref=number("","","","ACCTRANS",accno)
                        print("Transaction Successfully done with Reference number",ref)
                        h=d["Loan Due"]
                        found=True
                    else:
                        print("Insufficient Balance")
                        return None
                    print("Your balance is: ",g)

        except EOFError:
            print()
        c.close()

    if found== True:
        dc=open("accounts.dat","rb+")
        try:
            while True:
                posn=dc.tell()
                ab=pickle.load(dc)
                if ab["accno"]==accno1:
                    z=ab["Loan Due"]
                    ab["Balance"]+=a
                    abc=ab["Balance"]
                    dc.seek(posn)
                    pickle.dump(ab,dc)

        except EOFError:
            print()
        dc.close()
        f={}
        f["Time"]=str(datetime.datetime.today())
        f["REFID"]=ref
        f["Description"]="ACC TRANS"
        f["accno"]=accno

        f["Credit"]=0
        f["Debit"]=a

        f["Credited to"]=accno1


        f["Credited from"]=accno
        f["Balance"]=g
        f["Loan Due"]=h

        f["Transacted Amount"]=a
        f["Identifing accnoo"]=accno
        pickle.dump(f,e)
        f={}
        f["Time"]=str(datetime.datetime.today())
        f["REFID"]=ref
        f["Description"]="ACC TRANS"
        f["accno"]=accno1

        f["Credit"]=a
        f["Debit"]=0

        f["Credited to"]=""
        f["Credited from"]=accno
        f["Balance"]=abc

        f["Loan Due"]=z

        f["Transacted Amount"]=a
        f["Identifing accnoo"]=accno1
        pickle.dump(f,e)
        receipt(accno,str(datetime.datetime.today()),str(0),str(a),ref,"ACC TRANS")
    else:
        print()
    e.close()
def deleteaccount(accno):
    import datetime
    import pickle
    f=open("accounts.dat","rb+")
    try:
        while True:
            x=pickle.load(f)
            if x["accno"]==accno:
                if x["Loan Due"]==0:
                    amma=x["Accountcreated"]
                    abc=True
                else:
                    print("Since your loan is due you cannot delete your account")
                    abc=False
    except EOFError:
        print()
    f.close()
    if abc==True:
        f=open("accounts.dat","rb")
        l=[]
        try:
            while True:
                a=pickle.load(f)
                l+=[a]

        except EOFError:
            print()
        for i in l:
            if i["accno"]==accno:
                l.remove(i)
        f.close()
        g=open("accounts.dat","wb")

        for z in l:
            pickle.dump(z,g)
        g.close()
        if os.path.isfile('./notification.dat')==True:
            f=open("notification.dat","rb")
            l=[]
            try:
                while True:
                    a=pickle.load(f)
                    l+=[a]

            except EOFError:
                print()
            for i in l:
                if i['Target']==accno:
                    l.remove(i)
            f.close()
            g=open("notification.dat","wb")

            for z in l:
                pickle.dump(z,g)
            g.close()
        if os.path.isfile('./appr.dat')==True:
            f=open("appr.dat","rb")
            l=[]
            try:
                while True:
                    a=pickle.load(f)
                    l+=[a]

            except EOFError:
                print()
            for i in l:
                if i["accno"]==accno:
                    l.remove(i)
            f.close()
            g=open("appr.dat","wb")

            for z in l:
                pickle.dump(z,g)
            g.close()
        if os.path.isfile('./ref.dat')==True:
            f=open("ref.dat","rb")
            l=[]
            try:
                while True:
                    a=pickle.load(f)
                    l+=[a]

            except EOFError:
                print()
            for i in l:
                if i["accno"]==accno:
                    l.remove(i)
            f.close()
            g=open("ref.dat","wb")

            for z in l:
                pickle.dump(z,g)
            g.close()
        d=open("deletedaccount.dat","ab+")
        z={}
        z["accno"]=accno
        z["creationdate"]=amma
        z["deletiondate"]=str(datetime.datetime.today())
        pickle.dump(z,d)
        d.close()
        print("Your account has successfully been deleted")
        x="n"
        return x
def bankstatement(accno):
    from tabulate import tabulate
    import datetime
    import colorama
    from colorama import Fore
    colorama.init(autoreset=True)
    f=open("ref.dat","rb")
    found=False
    abhyuday=[]
    adarsh=[]
    amma=[]
    z=[]
    try:
        while True:
            x=pickle.load(f)
            abc={}
            if x["Identifing accnoo"]==accno:
                abhyuday=list(x.values())
                del abhyuday[11]
                del abhyuday[10]
                del abhyuday[9]
                del abhyuday[3]
                adarsh+=[abhyuday]

                amma=list(x.keys())
                del amma[11]
                del amma[10]
                del amma[9]
                del amma[3]
                if x["Credit"]>0:


                            x["Credit"]=Fore.GREEN+str(x["Credit"])
                            x["Debit"]=Fore.WHITE+str(x["Debit"])

                elif x["Debit"]>0:


                            x["Debit"]=Fore.YELLOW+str(x["Debit"])
                            x["Credited to"]=Fore.WHITE+str(x["Credited to"])

                y=list(x.values())
                del y[11]
                del y[10]
                del y[9]
                del y[3]


                found=True
                z+=[y]
                a=list(x.keys())
                del a[11]
                del a[10]
                del a[9]
                del a[3]

    except EOFError:
        print()
    if found==False:
        print("NO transaction done")
        return None

    apc=[]
    aca=[]
    adc=open("accounts.dat","rb")
    try:

        while True:
            axc=pickle.load(adc)
            if axc["accno"]==accno:
                ada=list(axc.values())
                aba=list(axc.keys())
                aca+=[ada]
                del ada[10]
                del aba[10]
                if axc["Loan Due"]>0:
                    axc["Loan Due"]=Fore.RED+str(axc["Loan Due"])
                acc=list(axc.values())
                del acc[10]
                apc+=[acc]

                aoc=list(axc.keys())
                del aoc[10]
    except EOFError:
       print()
    apc.insert(0,aoc)
    aca.insert(0,aba)
    view=[tabulate(aca,headers="firstrow",tablefmt="grid",showindex=True)]
    abdad=[]
    print("Bank Statement created at",str(datetime.datetime.now()))
    z.insert(0,a)
    print(tabulate(z,headers="firstrow",tablefmt="grid"))
    anna=[tabulate(z,headers="firstrow",tablefmt="grid")]
    ans=input("Do you want to save the bank statement in a text file(y/n)")
    if ans=="y":
        adarsh.insert(0,amma)
        print("Your bank statement will be saved as a text file with name as your account number")
        abc=[tabulate(adarsh,headers="firstrow",tablefmt="grid",showindex=True)]
        d=open(accno+" BANKSTATEMENT.txt","w")
        d.write("\n\n")
        d.write("Bank Statement is created at: "+str(datetime.datetime.now()))
        d.write("\n\n")
        d.writelines(view)
        d.write("\n\n")
        d.write("The bank statement of account number: "+accno+"\n\n\n")
        d.writelines(abc)
        d.close()
        print("The file is saved")
    else:
        print("The file will not be saved")

def accountcheck(accno,pwd):
    import colorama
    from colorama import Fore
    colorama.init(autoreset=True)
    f=open("accounts.dat","rb")
    found=False
    try:
        while True:
            x=pickle.load(f)
            if x["accno"]==accno and x["pwd"]==pwd:

                found=True
    except EOFError:
        if found==False:
            playsound1("Invalid Account number or password")
            print(Fore.RED+"Invalid Account number or password")
            return None
        else:
            return True
    f.close()
def seedeleteaccounts():
    z=open("deletedaccount.dat","rb")
    d=[]
    aoc=[]
    try:
        while True:
            x=pickle.load(z)
            acc=list(x.values())
            d+=[acc]
            aoc=list(x.keys())
    except EOFError:
        print()
    d.insert(0,aoc)
    print(tabulate(d,headers="firstrow",tablefmt="grid",showindex=True))
def alltrans():
    import colorama
    from colorama import Fore
    from tabulate import tabulate
    colorama.init(autoreset=True)
    f=open("ref.dat","rb")
    z=[]
    try:
        while True:
            x=pickle.load(f)
            if x["Credit"]>0:


                        x["Credit"]=Fore.GREEN+str(x["Credit"])
                        x["Debit"]=Fore.WHITE+str(x["Debit"])

            elif x["Debit"]>0:


                        x["Debit"]=Fore.YELLOW+str(x["Debit"])
                        x["Credited to"]=Fore.WHITE+str(x["Credited to"])

            y=list(x.values())
            del y[11]
            del y[10]
            del y[9]




            z+=[y]
            a=list(x.keys())
            del a[11]
            del a[10]
            del a[9]


    except EOFError:
        print()
    z.insert(0,a)
    print(tabulate(z,headers="firstrow",tablefmt="grid"))
    f.close()


def raiseissueuser(accno):
    import random
    from tabulate import tabulate
    import datetime
    import pickle
    y=input("Enter the reference id for the issue ")
    anna=False
    found=False
    found1=False
    found2=False
    abh=input('''Enter the issue in section
                 BANKSTATEMENT          1
                 INTEREST CHANGES       2
                 APPROVAL FOR LOAN      3

''')
    abh=integer(abh)
    if abh==1 and os.path.isfile('./ref.dat')==True:

        f=open("ref.dat","rb")
        try:
            while True:
                x=pickle.load(f)
                if x["REFID"]==y:
                    #yaha pr
                    Z=x
                    found=True
                    anna=True
        except EOFError:
            print()
        f.close()
    elif abh==2 and os.path.isfile('./histloan.dat')==True:

        f=open("histloan.dat","rb")
        try:
            while True:
                x=pickle.load(f)
                if x["ref"]==y:
                    Z=x
                    found1=True
                    anna=True
        except EOFError:
            print()
        f.close()

    elif abh==3 and os.path.isfile('./appr.dat')==True:

        f=open("appr.dat","rb")
        try:
            while True:
                x=pickle.load(f)
                if x["ref"]==y:
                    Z=x
                    found2=True
                    anna=True
        except EOFError:
            print()
        f.close()
    else:
        print("Please enter a valid input or the table for your particular input is not yet made")
        return None
    for i in [found,found2,found1]:
        if i==True :
            ab=list(Z.keys())
            ad=list(Z.values())
            cd=[ab,ad]

            print(tabulate(cd,headers="firstrow",tablefmt="grid",showindex=True))
            anna=True

    if anna==False:
        print("We couldnt find anything with the referred refid")
    if anna==True:
        f=open("issues.dat","ab+")
        amma={}
        amma["issuerefid"]=str(random.randint(0,10000))
        amma["refid"]=y
        amma["accno"]=accno
        amma["Issue"]=input("Enter the issue")
        amma["Time"]=str(datetime.datetime.today())
        amma["status"]="Yet to be resolved by the admin"
        amma["reply"]="None"
        amma["order"]=abh
        pickle.dump(amma,f)
        f.close()
def seemyissue(accno):
    import pickle
    from tabulate import tabulate
    import colorama
    from colorama import Fore
    colorama.init(autoreset=True)
    z=[]
    a=[]
    found=False
    ac=open("issues.dat","rb")
    try:
        while True:
            x=pickle.load(ac)
            if x["accno"]==accno:
                if x["status"]=="RESOLVED":


                        x["status"]=Fore.GREEN+str(x["status"])
                        x["reply"]=Fore.WHITE+str(x["reply"])

                else:


                        x["status"]=Fore.YELLOW+str(x["status"])
                        x["reply"]=Fore.WHITE+str(x["reply"])
                y=list(x.values())
                del y[7]
                del y[2]
                z+=[y]
                a=list(x.keys())
                del a[7]
                del a[2]
                found=True
    except EOFError:
        print()
    if found==True:
        print("The applications and the status of approvals are: \n\n")
        ac.close()
        z.insert(0,a)
        print(tabulate(z,headers="firstrow",tablefmt="grid",showindex=True))

    else:
        print("No issues found related to your account")
def issueadmin1(ref):
    adarsh=input("Enter the reply")
    amma=[]
    from tabulate import tabulate
    f=open("issues.dat","rb")
    z=[]
    try:
        while True:
            x=pickle.load(f)
            amma+=[x]
    except EOFError:
        print()
    f.close()
    f=open("issues.dat","wb")
    for abc in amma:
        if abc["issuerefid"]==ref:
            abc["status"]="RESOLVED"
            abc["reply"]=adarsh

    for acd in amma:
        pickle.dump(acd,f)
    f.close()

def issueadmin():
    abhyuday=False
    import pickle
    from tabulate import tabulate
    noti=True
    found1=False
    found4=False
    z=[]
    abhy=[]
    a=[]
    found=False
    ac=open("issues.dat","rb")
    try:
        while True:
            x=pickle.load(ac)
            abhy+=[x]
            y=list(x.values())
            z+=[y]
            a=list(x.keys())
            found=True
    except EOFError:
        print()
    if found==True:
        print("The applications and the status of approvals are: \n\n")
        ac.close()
        z.insert(0,a)
        print(tabulate(z,headers="firstrow",tablefmt="grid",showindex=True))
        appa=input("Do you want to reply to some them?(y/n)")
        if appa=="y":
            z=input("Enter the ISSUE REFID  to which you want to respond")
            found4=True
            for i in abhy:
                if i["issuerefid"]==z:
                    vil=i["order"]
                    print(vil)
                    y=i["refid"]
                    abhyuday=True


        else:
            print("Thank you admin")

    else:
        print("No issues admin, have a great day")
    ac.close()
    if abhyuday==False:
        print("PLease enter a valid issue refid")
        return None
    if found4==True:
        found=False
        found1=False
        found2=False
        if vil==1:
            f=open("ref.dat","rb")
            try:
                while True:
                    x=pickle.load(f)
                    if x["REFID"]==y:
                        Z=x
                        found=True
            except EOFError:
                print()
            f.close()
        elif vil==2:

            f=open("histloan.dat","rb")
            try:
                while True:
                    x=pickle.load(f)
                    if x["ref"]==y:
                        Z=x
                        found1=True
            except EOFError:
                print()
            f.close()

        elif vil==4:
            found=True
        elif vil==3:
            f=open("appr.dat","rb")
            try:
                while True:
                    x=pickle.load(f)
                    if x["ref"]==y:
                        Z=x
                        found2=True
            except EOFError:
                print()
            f.close()

        else:
            print("No table there")
        for i in [found,found2,found1]:
            if i==True:
                if i in [found,found2,found1]:
                    ab=list(Z.keys())
                    ad=list(Z.values())
                    cd=[ab,ad]

                    print("The referred item is:\n\n\n")
                    print(tabulate(cd,headers="firstrow",tablefmt="grid",showindex=True))
                issueadmin1(z)
                noti=False
    if noti==True:
        print("We couldnt find anything with the referred refid")
def loandue():
    import pickle
    from tabulate import tabulate
    import colorama
    from colorama import Fore
    colorama.init(autoreset=True)
    f = open("accounts.dat", "rb+")
    found=False

    try:

        z = []
        d = []
        a = []
        c = []

        while True:

            x = pickle.load(f)
            if x["Loan Due"] >0:
                x["Loan Due"]=Fore.RED+str(x["Loan Due"])
                x["Balance"]=Fore.WHITE+str(x["Balance"])
                y = [str(x["accno"]),str(x["Loan Due"]),str(x["Balance"])]
                z += [y]
                a = ["Account Number","Loan Due","Balance"]
                found = True
    except EOFError:
        print()
    if found==True:
        print("\t\tThe accounts with loan due  present in the system are\n\n")
        z.insert(0, a)

        print(tabulate(z, headers="firstrow", tablefmt="grid", showindex=True))


    else:
        print("No account with loan due")
def bankstatement1(accno):
        from tabulate import tabulate
        import datetime

        f = open("ref.dat", "rb")

        z = []
        try:
            while True:
                x = pickle.load(f)
                abc = {}
                if x["Identifing accnoo"] == accno:
                    y = list(x.values())
                    z += [y]
                    a = list(x.keys())
        except EOFError:
            print()

        apc = []
        adc = open("accounts.dat", "rb")
        try:

            while True:
                axc = pickle.load(adc)
                if axc["accno"] == accno:
                    acc = list(axc.values())
                    apc += [acc]
                    aoc = list(axc.keys())
        except EOFError:
            print()
        apc.insert(0, aoc)
        view = [tabulate(apc, headers="firstrow", tablefmt="grid", showindex=True)]
        print("Bank Statement created at", str(datetime.datetime.now()))
        z.insert(0, a)
        print(tabulate(z, headers="firstrow", tablefmt="grid", showindex=True))
