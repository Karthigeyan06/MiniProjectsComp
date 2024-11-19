import sqlite3
con=sqlite3.connect("Fruit_shop.db")
cr=con.cursor()
cr.execute(''' CREATE TABLE Details( Bill_no int, date str, time str, name str, total int)''')
con.commit()
con.close()