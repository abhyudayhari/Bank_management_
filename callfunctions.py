from allfunctions import *
import os
from playsound import playsound
def photo(x):
    from colorama import Fore
    if x=="log":
        print(Fore.BLUE+">>MAIN MENU")
    elif x=="view":
        print("MAIN MENU>>"+Fore.BLUE+"VIEW ACCOUNT DETAILS")
    elif x=="with":
        print("MAIN MENU>>"+Fore.BLUE+"WITHDRAW MONEY")
    elif x=="acc":
        print("MAIN MENU>>"+Fore.BLUE+"TRANSFER MONEY")
    elif x=="dep":
        print("MAIN MENU>>"+Fore.BLUE+"DEPOSIT MONEY")
    elif x=="app":
        print("MAIN MENU>>"+Fore.BLUE+"APPLICATION FOR LOAN")
    elif x=="lp":
        print("MAIN MENU>>"+Fore.BLUE+"LOAN REPAYMENT")
    elif x=="not":
        print("MAIN MENU>>"+Fore.BLUE+"NOTIFICATIONS")
    elif x=="man":
        print("MAIN MENU>>"+Fore.BLUE+"MANAGE ACCOUNT")
    elif x=="bs":
        print("MAIN MENU>>"+Fore.BLUE+"BANK STATEMENT")
    elif x=="cl":
        print("MAIN MENU>>"+Fore.BLUE+"STATUS OF LOAN")
    elif x=="raise":
        print("MAIN MENU>>"+Fore.BLUE+"RAISE ISSUE")
    elif x=="iss":
        print("MAIN MENU>>"+Fore.BLUE+"ISSUES")
    print(Fore.WHITE+(""))
    print("\n")

def login(accno,pwd):
    from os import system

    if accountcheck(accno,pwd)==True:
        
        playsound1("Hi there user, login successfull")
        print("\t\t\t\tLOGIN SUCCESSFULL")
        print("\n\n")
        ans="y"
        while ans=="y":
            photo("log")
            x=input('''Please enter code for appropriate functions
                     VIEW ACCOUNT DETAILS         1
                     WITHDRAW MONEY               2
                     ACCOUNT TRANSFER             3
                    DEPOSIT MONEY                 4
                    APPLICATION FOR LOAN          5
                    LOAN REPAYMENT                6
                    NOTIFICATION PAGE             7
                    MANAGE ACCOUNT                8
                    BANK STATEMENT                9
                    CHECK STATUS OF LOAN          10
                    DELETE ACCOUNT                11
                    RAISE ISSUE                   12
                    SEE RAISED ISSUES AND STATUS  13
                    LOGOUT                        14

                    \n\n''')
            x=integer(x)
            system("cls")
            if x==1:
                photo("view")
                viewspecific(accno)
                playsound1("The particulars of your account are")
            elif x==2:
                photo("with")
                playsound1("You have opted for cash withdrawal")
                cashwithdrawal(accno)

            elif x==3:
                photo("acc")
                playsound1("You have opted for account transfer")
                accounttransfer(accno)

            elif x==4:
                photo("dep")
                deposit(accno)
            elif x==5:
                if os.path.isfile('./loan.dat')==True:
                    photo("app")
                    playsound1("Welcome user to the loan portal")
                    loanpage(accno)

                else:

                    print("No interest of loan table has been created")
                    playsound1("No interest of loan table has been created")

            elif x==6:
                if os.path.isfile('./appr.dat')==True:
                   photo("lp")
                   loanpayment(accno)
                else:

                    print("No approval table has been created")
                    playsound1("No approval table has been created")

            elif x==7:
                photo("not")
                notificationuser(accno)
                playsound1("The notifications for your account are:")

            elif x==8:
                photo("man")
                manageaccount(accno)
            elif x==9:
                photo("bs")
                print("THe particulars of your account are: ")
                viewspecific(accno)
                if os.path.isfile('./ref.dat')==True:
                    bankstatement(accno)
                else:
                    print("NO transaction table has been created")


            elif x==10:
                if os.path.isfile('./appr.dat')==True:
                   photo("cl")
                   checkloanstatus(accno)
                else:
                    print("No approval table has been created")

            elif x==11:
                deleteaccount(accno)
                break
            elif x==12:
                photo("raise")
                raiseissueuser(accno)
            elif x==13:
                if os.path.isfile('./issues.dat')==True:
                    photo("iss")
                    seemyissue(accno)
                else:
                    print("NO issue table has been created")
            elif x==14:

                print("Logout successfull Thank you for using our banking system")
                playsound1("Logout Successfull")
                return None
            else:
                print("PLease enter a valid code")
            ans=input("Want to Go back to the account  page(y/n)")
            system("cls")
    playsound1("Thank you for banking with us")
    print("THANK YOU FOR BANKING WITH US!!!")
def user():
    from os import system
    ab=input('''Please enter code for appropriate functions
             1 CREATE ACCOUNT
             2 LOGIN ACCOUNT   ''')
    ab=integer(ab)
    system("cls")
    if ab==1:
        type1=input('''Input the type of account
                    BUSINESS ACCOUNT ----C
                    SAVINGS ACCOUNT  ----S  ''')
        [z,ad]=createaccount(type1)
        if z!=None:
            login(z,ad)

    elif ab==2:
        if os.path.isfile('./accounts.dat')==True:
            accno=input("Enter the account number: ")
            from getpass import getpass
            pwd=getpass("Enter the password: ")
            login(accno,pwd)
        else:
            print("No database for account has been created please create a account first")
    else:
        print("Please enter a valid code")
        playsound1("Please enter a valid code")
    system("cls")
def admin():
    from os import system
    from getpass import getpass
    x=getpass("Enter the password: ")
    if x=="admin":
        
        playsound1("Welcome Admin")
        print("Welcome Admin")
        ans="y"
        while ans=="y":
            ab=input('''Please enter code for appropriate functions
             1 VIEW ALL CUSTOMERS PARTICULARS
             2 VIEW SPECIFIC CUSTOMER PARTICULAR
             3 DRAFT A NOTIFICATION
             4 SEE ALL DRAFTED NOTIFICATIONS
             5 CHANGE INTEREST RATES
             6 TRANSACTIONS SUMMARY
             7 CHECK THE HISTORY OF INTEREST RATE CHANGES
             8 APPROVAL FOR LOAN
             9 ALL TRANSACTIONS
             10 APPROVED AND DISAPPROVED LOANS
             11 SEE ALL DELETED ACCOUNTS
             12 SEE RAISED ISSUES AND REPLY THEM
             13 CHECK THE LOAN DUE OF CUSTOMERS
             14 LOGOUT\n\n''')
            ab=integer(ab)
            system("cls")
            if ab==1:
                if os.path.isfile('./accounts.dat')==True:
                    viewall()
                else:
                    print("No database for account has been created please create a account first")

            elif ab==2:
                if  os.path.isfile('./accounts.dat')==True :
                    import pickle
                    import datetime

                    from tabulate import tabulate
                    f = open("accounts.dat", "rb+")
                    found = False
                    try:

                        z = []
                        d = []
                        a = []
                        c = []

                        while True:

                            x = pickle.load(f)
                            y = [str(x["accno"])]
                            z += [y]
                            a = ["Account Number"]
                            found = True
                            print("\t\tThe accounts present in the system are\n\n")
                            z.insert(0, a)

                    except EOFError:
                        if found == False:
                            print("NO accounts registeBLUE other than yours.")
                        else:
                            print(tabulate(z, headers="firstrow", tablefmt="grid", showindex=True))
                    accno=input("Enter the account number: ")
                    f = open("accounts.dat", "rb")
                    found = False
                    try:
                        while True:
                            x = pickle.load(f)
                            if x["accno"] == accno:
                                found = True
                    except EOFError:
                        if found == False:
                            print("Invalid Account number")


                    f.close()

                viewspecific(accno)
                if os.path.isfile('./ref.dat') == True:
                    bankstatement1(accno)
                else:
                    print("NO transaction table has been created")
                if os.path.isfile('./appr.dat')==True:
                    print("The loan application from the customer are: ")
                    checkloanstatus(accno)
                else:
                    print("NO loan application table has been created")
                if os.path.isfile('./issues.dat') == True:
                    print("The issues from the customer are: ")
                    seemyissue(accno)
                else:
                    print("NO issue table has been created")
                print("The notifications for the account are: ")
                notificationuser(accno)


            elif ab==3:
                notificationadmin()
            elif ab==4:
                if os.path.isfile('./notification.dat')==True:
                    notificationsee()
                else:
                    print("No notification table has been created")
            elif ab==5:
                changeinterest()
            elif ab==6:
                if os.path.isfile('./ref.dat')==True:
                    systransaction()
                else:
                    print("NO transaction table has been created")
            elif ab==7:
                if os.path.isfile('./histloan.dat')==True:
                    interehist()
                else:
                    print("No interest of loan table has been created")
            elif ab==8:
                if os.path.isfile('./appr.dat')==True:
                    approvalpage()
                else:
                    print("No approval table has been created")
            elif ab==9:
                if os.path.isfile('./ref.dat')==True:
                    alltrans()
                else:
                    print("NO transaction table has been created")

            elif ab==10:
                if os.path.isfile('./appr.dat')==True:
                    approvedanddisapproved()
                else:
                    print("No approval table has been created")

            elif ab==11:
                if os.path.isfile('./deletedaccount.dat')==True:
                    seedeleteaccounts()
                else:
                    print("NO deleted account table has been created")

            elif ab==12:
                if os.path.isfile('./issues.dat')==True:
                    issueadmin()
                else:
                    print('NO issue table has been created')
            elif ab==13:
                if os.path.isfile('./appr.dat')==True:
                    loandue()
                else:
                    print("No approval table has been created")
            elif ab==14:
                print("\n\nLOGOUT SUCCESSFULL")
                playsound1("logout successfull")

                return None
            else:

                print("Please enter a valid code")
                playsound1("Please enter a valid code")
            ans=input("Go back (y/n) ")
            system("cls")
        print("Thank you admin")
    else:
        print("The password entered is wrong")
        playsound1("Invalid password")

def about():

    print("\t\t\t\t\tBANKING SYSTEM \n\n\nThis BANKING PROJECT is jointly made by Abhyuday Hari Prasad and Vilakshan Saini.It took about 2 months \nto make and about 15 days more for debugging.This project is a great example of binary file formation in python which has brought this project working.\n We are very thankful to our computer teacher MS SAAKSHI MAAM for constant support guidance, motivation and helped us to make this project.\nWe are also thankful to our Principal sir Mr Sandeep Pant sir for their support due to which we could complete this project successfully. ")
    playsound1("BANKING PROJECT is jointly made by Abhyuday Hari Prasad and Vilakshan Saini.It took about 2 months to make and about 15 days more for debugging.This project is a great example of MYSQL and python integration which has brought this project working.We are very thankful to our computer teacher Miss SAAKSHI MAAM for constant support guidance, motivation and helped us to make this project.We are also thankful to our Principal sir Mr Sandeep Pant sir for their support due to which we could complete this project successfully.")
def main():
        from os import system
        logo()
        print("\t\t\t\t\t\t\tBANK MANAGEMENT SYSTEM\n")
        print('\tNOTE: Everything in this program is case sensitive and the password will not be shown in the terminal. Please be aware of that ')
        playsound1("NOTE: Everything in this program is case sensitive and the password will not be shown in the terminal. Please be aware of that ")
        X=int(input('''Enter the appropriate code for the functions
                    FOR USER 1
                    FOR ADMIN 2
                    ABOUT THE PROJECT 3
                    \n\n'''))
        system("cls")
        if X==1:
                user()
        elif X==2:
                admin()
        elif X==3:
                logo()
                about()

        else:
                playsound1("Please enter a valid code")
                print("Please enter a valid code")
main()
