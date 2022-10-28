

import mysql.connector 
connect=mysql.connector.connect(host="localhost",user="root",password="112001",database=" bank5")

def deposit ():
    ACCNO=input("ENTER THE ACCOUNT NUMBER: ")
    NAME=input("ENTER THE NAME: ")
    AMOUNT=int(input("ENTER THE AMOUNT: "))
    res=connect.cursor()
    sql="select AMOUNT from users where ACCNO=%s" #select account
    user=(ACCNO,)
    res.execute(sql,user)
    result=res.fetchone() #using fetchone we are taking res tuple ino result
    total=result[0]+AMOUNT

    sql="update users set AMOUNT=%s where ACCNO=%s"
    totals=(total,ACCNO)
    res.execute(sql,totals)
    connect.commit()
    print("MONEY DEPOSITED SUCCESFULLY")
    pass

def withdraw ():
    ACCNO=input("ENTER THE ACCOUNT NUMBER: ")
    NAME=input("ENTER THE NAME: ")
    AMOUNT=int(input("ENTER THE AMOUNT: "))
    res=connect.cursor()
    sql="select AMOUNT from users where ACCNO=%s"
    user=(ACCNO,)
    res.execute(sql,user)
    result=res.fetchone()
    total=result[0]-AMOUNT

    sql="update users set AMOUNT=%s where ACCNO=%s"
    totals=(total,ACCNO)
    res.execute(sql,totals)
    connect.commit()
    print("MONEY WITHDRAWED SUCCESFULLY")

    sql="select AMOUNT from users where ACCNO=%s"
    user=(ACCNO,)
    res=connect.cursor()
    res.execute(sql,user)
    result=res.fetchone()
    print("BALANCE FOR ",NAME, "IS", result[0] )
    pass

def balance():
    ACCNO=input("ENTER THE ACCOUNT NUMBER: ")
    NAME=input("ENTER THE NAME: ")
    sql="select AMOUNT from users where ACCNO=%s"
    user=(ACCNO,)
    res=connect.cursor()
    res.execute(sql,user)
    result=res.fetchone()
    print("BALANCE FOR ",NAME, "IS", result[0] )
    pass

def admin(USERNAME,PASSWORD):
    q=(USERNAME,PASSWORD)
    pass


def accreate(ACCNO,NAME,PHNO,AMOUNT):
    res=connect.cursor()
    sql="insert into users(ACCNO,NAME,PHNO,AMOUNT) values (%s,%s,%s,%s)"
    user=(ACCNO,NAME,PHNO,AMOUNT)
    res.execute(sql,user)
    connect.commit()
    print("ACCOUNT CREATED SUCCESSFULLY")
    pass

def admincreate(USERNAME,NAME,PASS):
    res=connect.cursor()
    sql="insert into admins(USERNAME,NAME,PASS) values (%s,%s,%s)"
    admins=(USERNAME,NAME,PASS)
    res.execute(sql,admins)
    connect.commit()
    print("ACCOUNT CREATED SUCCESSFULLY")
    pass

def closeacc(ACCNO):
    res=connect.cursor()
    sql= "delete from users WHERE ACCNO=%s"
    user=(ACCNO,)
    res.execute(sql,user)
    connect.commit()
    print("ACCOUNT DELETED SUCCESSFULLY")
    pass

    



        
# start of the program
ch=''


while ch != 9:
    
    print("************************************************************")
    print("========== WELCOME TO FERGUSSON COLLEGE BANK ==========")
    print("************************************************************")
    print("==========      (1). DEPOSIT AMOUNT      ============")
    print("==========      (2). WITHDRAW AMOUNT     ============")
    print("==========      (3). BALANCE ENQUIRY     ============")
    print("==========      (4). ADMIN CONSOLE       ============")
    print("==========      (5). Quit                ============")
    print("==========     Select Your Option (1-5)  ============")
    print("************************************************************")
    ch = input("Enter your choice : ")
    
    
    if ch == '1':
        deposit()
        
    elif ch =='2':
        withdraw()
        
    elif ch == '3':
        balance()
        
    elif ch == '4':
        USERNAME=input("ENTER THE USER NAME: ")
        PASSWORD=input("ENTER THE PASSWORD: ")
        admin(USERNAME,PASSWORD)
        
        ac=''
        if ch=='4':
            
            while ac!=5:
                print("\t_________________ADMIN CONSOLE___________________")
                print("\t1. NEW ACCOUNT CREATION")
                print("\t2. CLOSE AN ACCOUNT")
                print("\t3. ADMIN CREATION")
                print("\t4. EXIT")
                print("\tSelect Your Option (1-3) : ")
                ac = input("Enter your choice : ")

                if ac=='1':
                    ACCNO=int(input("ENTER ACCOUNT NUMBER: "))
                    NAME=input("ENTER NAME: ")
                    PHNO=int(input("ENTER PHONE NUMBER: "))
                    AMOUNT=int(input("ENTER THE AMOUNT: "))
                    accreate(ACCNO,NAME,PHNO,AMOUNT)
                   
            
                elif ac=='2':
                    ACCNO=int(input("ENTER ACCOUNT NUMBER: "))
                    closeacc(ACCNO)
                
                elif ac == '3':
                    USERNAME=input("ENTER USER NAME: ")
                    NAME=input("ENTER NAME: ")
                    PASS=input("ENTER PASSWORD: ")
                    admincreate(USERNAME,NAME,PASS)
           
                elif ac=='4':
                    break
                else:
                    print("Invalid choice...PLEASE ENTER FORM(1-3)")
                    
    
    elif ch == '5':
        print("\t************* THANKS FOR VISITING FERGUSSON COLLEGE BANK *************")
        break
    else :
        print("Invalid choice...PLEASE ENTER FORM(1-5)")
    
   
    


