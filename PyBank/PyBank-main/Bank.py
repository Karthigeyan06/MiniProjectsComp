def bank():

    import sqlite3
    con=sqlite3.connect("bank_database.db")
    cr=con.cursor()

    PB000 = ['NAME', 'PLACE', 'BALANCE', 'PHONE NO', 'ADDRESS', 'PASSWORD']
    PB1001 = ['Mr. AAA', 'Chennai', 10000, 1111111111, 'AAAAAA' , 1001]
    PB1002 = ['Mr. BBB', 'MADURAI', 230000, 2222222222, 'BBBBBB' , 2002]
    PB1003 = ['Mr. CCC', 'Chennai', 15000, 3333333333, 'CCCCCC', 3003 ]
    PB1004 = ['Mr. DDD', 'KANCHIPURAM', 30000, 4444444444, 'DDDDDD' , 4004]
    PB1005 = ['Mr. EEE', 'Chennai', 20000, 5555555555, 'EEEEE' , 5005]

    cr=con.execute("SELECT BALANCE FROM CUSTOMER WHERE A_NO='PB1001'")
    bal=cr.fetchone()
    PB1001[2]=bal[0]
    
    cr=con.execute("SELECT BALANCE FROM CUSTOMER WHERE A_NO='PB1002'")
    bal=cr.fetchone()
    PB1002[2]=bal[0]

    cr=con.execute("SELECT BALANCE FROM CUSTOMER WHERE A_NO='PB1003'")
    bal=cr.fetchone()
    PB1003[2]=bal[0]

    cr=con.execute("SELECT BALANCE FROM CUSTOMER WHERE A_NO='PB1004'")
    bal=cr.fetchone()
    PB1004[2]=bal[0]

    cr=con.execute("SELECT BALANCE FROM CUSTOMER WHERE A_NO='PB1005'")
    bal=cr.fetchone()
    PB1005[2]=bal[0]


    


    

 
   
    

    print('         PYTHON BANK   ')
    n=input('Enter your a/c number :')

    def exe(a):

        
        print('Welcome ', a[0])

        P= int(input('Enter your password:'))
        if a[5]==P:
            o=0
            while o<=4:
                print('--------------------------------------------------------------------------------------------')

                print('How can we help you !!!', '\n', '1. Profile \n 2. Credit \n 3. Withdraw \n 4. Check Balance \n 5. Exit ')
                o=int(input("Enter the Operation:"))
                print('--------------------------------------------------------------------------------------------')
                
                if o==1:
                    print("a/c number:", n)
                    print("Name: ", a[0])
                    print('Place:', a[1])
                    print('Phone no:', a[3])
                    print('Address:', a[4])

                elif o==2:
                    
                    print("Your current Balance: Rs.", a[2])
                    am=int(input("Enter the amount to credit :"))
                    a[2]=a[2]+am
                    print("Your amount  Rs.", am , "/-  has been successfully credited to your account")
                    print("Your updated Balance: Rs.", a[2])

                elif o==3:

                    pp=int(input("Enter your password:"))
                    if pp==a[5]:
                        print("Your current balance:", a[2])
                        wi=int(input('Enter the amount to withdraw:'))
                        if wi<= a[2]:
                            a[2]=a[2]-wi
                            print("Your amount  Rs.", wi , "/-  has been successfully withdrawn from your account")
                            print("Your updated Balance: Rs.", a[2])

                        else:
                            print("Insufficient Balance....")
                            print("Process failed....")
                        
                    else:
                        print("Incorrect Password...")
                        print("Process Failed with Error...")

                elif o==4:
                    print("Your Current Balance: Rs.",a[2], "/-")

                else:
                    print('  Press ENTER to exit ')
                    EXIT=input()


            else:
                print('  ')

        else:
            print("Invalid Password....")
            print("Login Again...")
            if n=='PB1001':
                print(exe(PB1001))
            elif n=='PB002':
                print(exe(PB1002))
            elif n=="PB003":
                print(exe(PB1003))
            elif n=='PB004':

                print(exe(PB1004))

            elif n=="PB1005":
                print(exe(PB1005))    
            else:
                print("Invalid Input...")
            

        return '   '


    if n=='PB1001':
        print(exe(PB1001))
    elif n=='PB1002':
        print(exe(PB1002))
    elif n=="PB1003":
        print(exe(PB1003))
    elif n=='PB1004':

        print(exe(PB1004))

    elif n=="PB1005":
        print(exe(PB1005))    
    else:
        print("Invalid Input...")


    C1=PB1001[2]
    C2=PB1002[2]
    C3=PB1003[2]
    C4=PB1004[2]
    C5=PB1005[2]
    cr=con.execute("UPDATE CUSTOMER SET BALANCE=? WHERE A_NO='PB1001'", [C1])
    cr=con.execute("UPDATE CUSTOMER SET BALANCE=? WHERE A_NO='PB1002'", [C2])
    cr=con.execute("UPDATE CUSTOMER SET BALANCE=? WHERE A_NO='PB1003'", [C3])
    cr=con.execute("UPDATE CUSTOMER SET BALANCE=? WHERE A_NO='PB1004'", [C4])
    cr=con.execute("UPDATE CUSTOMER SET BALANCE=? WHERE A_NO='PB1005'", [C5])
    con.commit() 


    return '  '



print(bank())


        

            
                
