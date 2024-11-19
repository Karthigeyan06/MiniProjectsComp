import turtle  
#EquivalentResistance
def eqres():
    n=int(input("Enter the number of Resistors:"))
    a=[]
    for i in range(1,n+1):
        r=float(input("Enter the value of Resistor {} ".format(i)))
        a.append(r)
    o=int(input("Enter the Connection type: 1. Series 2. Parellel"))
    if o==1:
        an=sum(a)
    elif o==2:
        su=0
        n=len(a)
        j=2
        while j<n:
            su=(a[0]*a[1])/(a[0]+a[1])
            su=(sum*a[j])/(a[j]+su)
            j+=1
        an=su
    else:
        print("Invalid Input :/")
    print("The Value of the Equivalent Resistance is ", an, "ohms")
#Equivalentcapacitance
def eqcap():
    n=int(input("Enter the number of Capacitors:"))
    a=[]
    for i in range(1,n+1):
        r=float(input("Enter the value of Capacitor {} ".format(i)))
        a.append(r)
    o=int(input("Enter the Connection type: 1. Series 2. Parellel"))
    if o==2:
        an=sum(a)
    elif o==1:
        su=0
        n=len(a)
        j=2
        while j<n:
            su=1/((1/a[0])+(1/a[1]))
            su=1/((1/su)+(1/a[j]))
            j+=1
        an=su
    else:
        print("Invalid Input :/")
    print("The Value of the Equivalent Capacitance is ", an, "farad")
#EquivalentInductance
def eqind():
    n=int(input("Enter the number of Inductors:"))
    a=[]
    for i in range(1,n+1):
        r=float(input("Enter the value of Inductor {} ".format(i)))
        a.append(r)
    o=int(input("Enter the Connection type: 1. Series 2. Parellel"))
    if o==1:
        an=sum(a)
    elif o==2:
        su=0
        n=len(a)
        j=2
        while j<n:
            su(a[0]*a[1])/(a[0]+a[1])
            su=(su*a[j])/(a[j]+su)
            j+=1
        an=su
    else:
        print("Invalid Input :/")
    print("The Value of the Equivalent Inductance is ", an, "henry")
#OhmsLaw
def ohmslaw():
    print("Ohms Law --> V=IR")
    n=int(input("Enter the function, To Find 1. Current 2. Resistance 3. Voltage"))
    if n==1:
        v=float(input("Enter the value of Voltage:"))
        r=float(input("Enter the value of Resistance:"))
        i=v/r
        i=round(i,2)
        print("The value of Current is", i, "Amps")
    elif n==2:
        v=float(input("Enter the value of Voltage:"))
        i=float(input("Enter the value of Current:"))
        r=v/i
        r=round(r,2)
        print("The value of Resistance is", r, "Ohms")
    elif n==3:
        i=float(input("Enter the value of Current:"))
        r=float(input("Enter the value of Resistance:"))
        v=i*r
        v=round(v,2)
        print("The value of Voltage is", v, "Volts")
    else:
        print("Invalid Input :/")
#VoltageDivider
def voltd():
    n=int(input("Enter the funtion, To find 1. Output voltage 2. Input voltage 3. 1st Resistor 4. 2nd Resistor(To measure Output)"))
    if n==1:
        vin=float(input("Enter the Input Voltage:"))
        r1=float(input("Enter the first resistance:"))
        r2=float(input("Enter the second resistance:"))
        vout=vin*(r2/(r1+r2))
        vout=round(vout,2)
        i=vin/(r1+r2)
        i=round(i,2)
        print("The value of Output Voltage is", vout, "volts")
        print("The Value of Current is", i, "Amps")
    elif n==2:
        vout=float(input("Enter the Output Voltage:"))
        r1=float(input("Enter the first resistance:"))
        r2=float(input("Enter the second resistance:"))
        vin=vout*((r1+r2)/r2)
        vin=round(vin,2)
        print("The value of Input Voltage is", vin, "volts")
    elif n==3:
        vin=float(input("Enter the Input Voltage:"))
        vout=float(input("Enter the Output Voltage:"))
        r2=float(input("Enter the second resistance:"))
        r1=(r2*(vin-vout))/vout
        r1=round(r1,2)
        print("The value of First Resistor is", r1, "ohms")
    elif n==4:
        vin=float(input("Enter the Input Voltage:"))
        vout=float(input("Enter the Output Voltage:"))
        r1=float(input("Enter the first resistance:"))
        r2=(vout/vin)*(r1+r2)
        r2=round(r2,2)
        print("The value of Second Resistor is", r2, "ohms")
    else:
        print("Invalid Input :/")
#CurrentDivisionRule
def curdiv():
    v=float(input("Enter the value of supply voltage:"))
    r1=float(input("Enter the value of first resistance:"))
    r2=float(input("Enter the value of second resistance:"))
    req=(r1*r2)/(r1+r2)
    i=v/req
    i1=i*(r2/(r1+r2))
    i2=i*(r1/(r1+r2))
    i1=round(i1,2)
    i2=round(i2,2)
    print("By Current Division Rule:")
    print("The value of Current through the 1st Resistor is", i1, "Amps")
    print("The value of Current through the 2nd Resistor is", i2, "Amps")
#ResonantFrequency
def freq():
    x=int(input("Enter the network: 1.RC 2.LC"))
    if x==1:
        r=float(input("Enter the value of Resistance:"))
        c=float(input("Enter the value of capacitance:"))
        f=1/(2*3.14*r*c)
        f=round(f,2)
        print("The frequency of the RC Network is", f, "Hz")
    elif x==2:
        l=float(input("Enter the value of Inductance:"))
        c=float(input("Enter the value of capacitance:"))
        y=((l*c)**0.5)
        f=1/(2*3.14*y)
        f=round(f,2)
        print("The frequency of the LC Network is", f, "Hz")
    else:
        print("Invalid Input :/")
#SineWave
def sine():
    print("Enter any one of the values to calculate: 1. Average voltage 2. Peak Voltage 3. Peak to Peak voltage 4. Vrms ")
    n=int(input("The value to be entered is:"))
    if n==1:
        avg=float(input("Enter the Average value of the sine function:"))
        peak=avg/0.637
        x=2**0.5
        vrms=peak/x
        vpp=2.828*vrms
        peak=round(peak,2)
        vrms=round(vrms,2)
        vpp=round(vpp,2)
        print("Vm=", peak, "V")
        print("Vrms=", vrms, "V")
        print("Vpp=",vpp, "V")
    elif n==2:
        vm=float(input("Enter the value of Peak voltage:"))
        vrms=vm/x
        vpp=2.828*vrms
        avg=0.637*vrms
        print("Vrms=", vrms, "V")
        print("Vpp=", vpp,"V")
        print("Vavg=", avg, "V")
    elif n==3:
        vpp=float(input("Enter the value of Vpp:"))
        vrms=vpp/2.828
        vp=vrms*x
        avg=0.637*vp
        print("Vrms=", vrms, "V")
        print("Vp=", vp,"V")
        print("Vavg=", avg, "V")
    elif n==4:
        vrms=float(input("Enter the value of Vrms:"))
        vpp=2.828*vrms
        vp=vrms*x
        avg=0.637*vp
        print("Vpp=", vpp, "V")
        print("Vp=", vp,"V")
        print("Vavg=", avg, "V")
    else:
        print("Invalid Input :/")
#ResistorColourCoding
def rescol():
    def col_res():
        sum=[]
        list=[]
        m1=input("Enter the 1st line:")
        m2=input("Enter the 2nd line:")
        m3=input("Enter the 3rd line:")
        t=input("Enter the 4th line:")
        list.append(m1)
        list.append(m2)
        list.append(m3)
        list.append(t)
        if m1=='black':
            sum.append(0)
        elif m1=='brown':
            sum.append(1)
        elif m1=='red':
            sum.append(2)
        elif m1=='orange':
            sum.append(3)
        elif m1=='yellow':
            sum.append(4)
        elif m1=='green':
            sum.append(5)
        elif m1=='blue':
            sum.append(6)
        elif m1=='violet':
            sum.append(7)
        elif m1=='grey':
            sum.append(8)
        elif m1=='white':
            sum.append(9)
        if m2=='black':
            sum.append(1)
        elif m2=='brown':
            sum.append(1)
        elif m2=='red':
            sum.append(2)
        elif m2=='orange':
            sum.append(3)
        elif m2=='yellow':
            sum.append(4)
        elif m2=='green':
            sum.append(5)
        elif m2=='blue':
            sum.append(6)
        elif m2=='violet':
            sum.append(7)
        elif m2=='grey':
            sum.append(8)
        elif m2=='white':
            sum.append(9)
        else:
            sum.append(1)
        mm=m3
        if mm=='black':
            sum.append(1)
        elif mm=='brown':
            sum.append(10)
        elif mm=='red':
            sum.append(100)
        elif mm=='orange':
            sum.append(1000)
        elif mm=='yellow':
            sum.append(10000)
        elif mm=='green':
            sum.append(100000)
        elif mm=='blue':
            sum.append(1000000)
        elif mm=='violet':
            sum.append(1)
        elif mm=='grey':
            sum.append(1)
        elif mm=='white':
            sum.append(1)
        else:
            sum.append(1)
        if t=='silver':
            sum.append(0.1)
        elif t=='gold':
            sum.append(0.05)
        else:
            sum.append(1)
        f1=str(sum[0])
        f2=str(sum[1])
        fi=f1+f2
        fin=int(fi)
        mul=sum[2]
        tot=fin*mul
        print(tot,'+',sum[3],'%')
        return(list)
    def res_col():
        val=int(input("Enter the resistance value in whole number:"))
        tel=float(input("Enter the value of tolerance in decimals:"))
        colour=[]
        st=str(val)
        div=st[0]+st[1]
        div=int(div)
        mult=val/div
        cl=['black','brown', 'red','orange','yellow','green','blue','violet','grey','white']
        d11=[0,1,2,3,4,5,6,7,8,9]
        d12=d11
        mul=[1,10,100,1000,10000,100000,1000000,1,1,1]
        div=str(div)
        d1=div[0]
        d2=div[1]
        d1=int(d1)
        d2=int(d2)
        if d1 in d11:
            in1=d11.index(d1)
            digit1=cl[in1]
            colour.append(digit1)
        else:
            print("Check your input value...")
        if d2 in d11:
            in2=d11.index(d2)
            digit2=cl[in2]
            colour.append(digit2)
        else:
            print("Check your input value...")
        if mult in mul:
            in3=mul.index(mult)
            digit3=cl[in3]
            colour.append(digit3)
        else:
            print("Check your input value...")
        if tel==0.1:
            colour.append('silver')
        elif tel==0.05:
            colour.append('gold')
        else:
            print()
        for i in colour:
            print(i)
        return colour
    def pen(a,b,c,d):
        t = turtle.Turtle()
        t.speed(10)
        t.color('black')
        t.pensize(3)
        t.penup()
        t.goto(-100, 0)
        t.pendown()
        t.forward(180)
        t.right(90)
        t.forward(50)
        t.right(90)
        t.forward(180)
        t.right(90)
        t.forward(50)
        t.penup()
        t.goto(-70, 0)
        t.pendown()
        t.color(a)
        t.begin_fill()
        t.right(90)
        t.forward(30)
        t.right(90)
        t.forward(50)
        t.right(90)
        t.forward(30)
        t.right(90)
        t.forward(50)
        t.end_fill()
        t.penup()
        t.goto(-40,0)
        t.pendown()
        t.color(b)
        t.begin_fill()
        t.right(90)
        t.forward(30)
        t.right(90)
        t.forward(50)
        t.right(90)
        t.forward(30)
        t.end_fill()
        t.penup()
        t.goto(-10,0)
        t.pendown()
        t.color(c)
        t.begin_fill()
        t.right(180)
        t.forward(30)
        t.right(90)
        t.forward(50)
        t.right(90)
        t.forward(30)
        t.end_fill()
        t.penup()
        t.goto(20,0)
        t.pendown()
        t.color(d)
        t.begin_fill()
        t.right(180)
        t.forward(30)
        t.right(90)
        t.forward(50)
        t.right(90)
        t.forward(30)
        t.end_fill()
        t.penup()
        t.color('black')
        t.goto(-100, 0)
        t.pendown()
        t.right(180)
        t.forward(180)
        t.right(90)
        t.forward(50)
        t.right(90)
        t.forward(180)
        t.right(90)
        t.forward(50)
        t.penup()
        t.goto(-100,-25)
        t.pendown()
        t.left(90)
        t.forward(50)
        t.penup()
        t.goto(80,-25)
        t.right(180)
        t.pendown()
        t.forward(50)
        t.end_fill()
        t.hideturtle()
        turtle.done()
        return()
    p=0
    while p==0:
        print('1. Colour to Resistance\n2.Resistance to Colour')
        op=int(input("Enter the operation:"))
        if op==1:
            f=col_res()
            pen(f[0],f[1],f[2],f[3])
        elif op==2:
            f=res_col()
            pen(f[0],f[1],f[2],f[3])
        else:
            p=1
#SinglePhaseTransformer
def sigtrans():
    print("Enter the function to calculate: 1. Secondary voltage 2. Primary voltage 3. Transformer Ratio 4. Maximum value of flux")
    x=int(input())
    if x==1:
        n1=int(input("Enter the No. of Primary Turns:"))
        n2=int(input("Enter the No. of Seconday Turns:"))
        v1=float(input("Enter Primary Voltage:"))
        tr=float(input("Enter Transformer Rating:"))
        v2=v1*(n2/n1)
        print("Secondary Voltage=", v2, "V")
        i1=tr/v1
        i2=tr/v2
        print("Primary current:", i1, "Amps")
        print("Secondary current:", i2, "Amps")
    elif x==2:
        n1=int(input("Enter the No. of Primary Turns:"))
        n2=int(input("Enter the No. of Seconday Turns:"))
        v2=float(input("Enter Secondary Voltage:"))
        tr=float(input("Enter Transformer Rating:"))
        v1=v2*(n1/n2)
        print("Primary Voltage=", v1, "V")
        i1=tr/v1
        i2=tr/v2
        print("Primary current:", i1, "Amps")
        print("Secondary current:", i2, "Amps")
    elif x==3:
        n1=int(input("Enter the No. of Primary Turns:"))
        n2=int(input("Enter the No. of Seconday Turns:"))
        k=n1/n2
        print("Tranformer Ratio:", k)
    elif x==4:
        n1=int(input("Enter the No. of Primary Turns:"))
        v1=float(input("Enter Primary Voltage:"))
        f=float(input("Enter supply Frequency:"))
        fl=v1/(4.44*f*n1)
        print("Maximum Flux:", fl, "wb")
    else:
        print("Invalid Input :/")
print("ElectroRookie")
print("Available Modules \n 1. Equivalent Resistance \n 2. Equivalent Capacitance \n 3. Equivalent Inductance \n 4. Ohm's Law \n 5. Voltage Divider Rule \n 6. Current Division Rule \n 7. Resonant Frequency \n 8. Sine Wave \n 9. Resistor Colour Coding \n 10. Single Phase Transformer")
print('---------------------------------------------------------------------------------------')
i=1
while i==1:
    c=int(input("Enter Module Number:"))
    if c==1:
        eqres()
    elif c==2:
        eqcap()
    elif c==3:
        eqind()
    elif c==4:
        ohmslaw()
    elif c==5:
        voltd()
    elif c==6:
        curdiv()
    elif c==7:
        freq()
    elif c==8:
        sine()
    elif c==9:
        rescol()
    elif c==10:
        sigtrans()
    else:
        print("Invalid Input:/ \n No Modules Available...")
    print('---------------------------------------------------------------------------------------')
    i=int(input("Do you want to continue: Yes--> 1 | No-->0"))






    









    

    


