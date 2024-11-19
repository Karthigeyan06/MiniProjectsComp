import sqlite3
con=sqlite3.connect("Dbase_bank.db")
cr=con.cursor()
com="""CREATE TABLE CUSTOMER(
        NAME CHAR,
        PLACE CHAR,
        BALANCE INTEGER,
        PHONE_NO INTEGER(10),
        ADDRESS VARCHAR(20),
        PASSWORD VARCHAR(4));"""

cr.execute(com)
