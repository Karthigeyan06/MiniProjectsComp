import datetime
import sqlite3
con=sqlite3.connect("Fruit_shop.db")
cr=con.cursor()
now=datetime.datetime.now()
billdet=[]
date=now.strftime("%d-%m-%Y")
time=now.strftime("%H:%M:%S")
cr=con.execute("SELECT Bill_no FROM Details WHERE name='nil' ")
bno=cr.fetchone()
bnom=bno[0]+1
billdet.append(bnom)
billdet.append(date)
billdet.append(time)


    

F1001 = 'Apple'
F1002 = 'Banana'
F1003 = 'Mango'
F1004 = 'Orange'

fruit = ['Apple', 'Banana', 'Mango', 'Orange']
Rate = [100,60,90,75]
proCode = [F1001,F1002,F1003,F1004]
prod = []
weight = []
sno = []
name = []
rate = []
num=int(input("Enter the no. of products:"))

for x in range(1,num+1):
    sno.append(x)


for i in range(1,num+1):
    pro=input('Enter the product code:')
    prod.append(pro)
    kg=float(input("Enter the weight of product in kg :"))

    weight.append(kg)

    if pro=='F1001' :
        a='Apple'
        name.append(a)
        rate.append(100)
    elif pro=='F1002' :
        b='Banana'
        name.append(b)
        rate.append(60)
    elif pro=='F1003' :
        c='Mango'
        name.append(c)
        rate.append(90)
    elif pro=='F1004' :
        d='Orange'
        name.append(d)
        rate.append(75)

    else:
        e=0





am = []

for K in range(0,num):
    aP=weight[K]*rate[K]
    am.append(aP)

s=sum(am)
cname=input("Enter Customer name:")
billdet.append(cname)
billdet.append(s)

print('==============================================================================================================================================================')
print()
print()    
    



print('                                                                           FRUITS   SHOP')
print()
print('                                                                         INVOICE RECEIPT')
print()
print("Bill no:",bnom)
print("Date:",date                                                                                       ,"Time:",time)
print("Name:", cname)
print('---------------------------------------------------------------------------------------------------------------------------------------------------')
print(' \t S.no \t\t Product Name \t Product Code \t Quantity \t \tRate \t\t Amount ')
print('---------------------------------------------------------------------------------------------------------------------------------------------------')

for y in range(0,num):
    print('\t ', sno[y], '\t\t',  name[y], '\t\t',  prod[y], '\t\t', weight[y], '\t\t', rate[y], '\t\t', weight[y]*rate[y])
print()
print('---------------------------------------------------------------------------------------------------------------------------------------------------')
print('                                                                                                                 Total Amount : Rs.', s)
print()
print('                                                           THANKS    FOR  SHOPPING !!!    HAVE   A  NICE  DAY !!!')


    
    
print()
print()
print('==============================================================================================================================================================')
print()
e1=billdet[0]
e2=billdet[1]
e3=billdet[2]
e4=billdet[3]
e5=billdet[4]
tuple=tuple(billdet)
list=[]
list.append(tuple)

cr.execute("UPDATE Details SET Bill_no=? WHERE name='nil'",[e1])
for i in list:
    cr.execute("INSERT INTO Details VALUES(?,?,?,?,?)",i)
con.commit()
cr.close()

