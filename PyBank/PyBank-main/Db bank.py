import sqlite3
con=sqlite3.connect("Dbase_bank.db")
cr=con.cursor()




cr.execute("INSERT INTO CUSTOMER VALUES ('Mr. AAA', 'Chennai', 10000, 1111111111, 'AAAAAA' , 1001)")
cr.execute("INSERT INTO CUSTOMER VALUES ('Mr. BBB', 'MADURAI', 230000, 2222222222, 'BBBBBB' , 2002)")
cr.execute("INSERT INTO CUSTOMER VALUES ('Mr. CCC', 'Chennai', 15000, 3333333333, 'CCCCCC', 3003)")
cr.execute("INSERT INTO CUSTOMER VALUES ('Mr. DDD', 'KANCHIPURAM', 30000, 4444444444, 'DDDDDD' , 4004)")
cr.execute("INSERT INTO CUSTOMER VALUES ('Mr. EEE', 'Chennai', 20000, 5555555555, 'EEEEE' , 5005)")
con.commit()