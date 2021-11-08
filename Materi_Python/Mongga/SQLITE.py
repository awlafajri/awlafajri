import sqlite3

conn = sqlite3.connect('customer.db')

c=conn.cursor()

#c.execute("""CREATE TABLE customers (
#        first_name text,
#        last_name text,
#        email text
#)""")

banyak = [
    ('Awla','Fajri','aryunaji.kbc81@gmail.com')
]
c.execute("INSERT INTO customers VALUES ('Mary','Smith','aryunaji.kbc81@gmail.com')")
c.executemany("INSERT INTO customers VALUES (?,?,?)", banyak)

c.execute("SELECT rowid,* FROM customers WHERE email LIKE '%gmail.com' ORDER BY rowid DESC")
c.execute("""UPDATE customers SET first_name = "BOB"
        WHERE last_name="ELDER"
""")
c.execute("""DELETE FROM customers WHERE rowid=6
""")

items= c.fetchall()
for item in items:
    print(item[0])
