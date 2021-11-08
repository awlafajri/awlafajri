import sqlite3

conn = sqlite3.connect("db.db")
c = conn.cursor()



c.execute("DROP TABLE IF EXISTS tab")
c.execute("""CREATE TABLE tab
        (nama text,
        usia INT(255),
        email text)  
""")



#c.execute("INSERT INTO tab VALUES ('Awla',12,'aryunaji.kbc81@gmail.com')")
listdata=[
    ('nana',22,'nini@gmail.com'),
    ("hahah",31,'hahah@yahoo.co.id'),
    ('nico',23,'nicoivander@google.com'),
    ('humam',32,'humam@gmail.com'),
    ('fawwaz',31,'fawwaz@yahoo.co.id')
]

c.executemany("INSERT INTO tab VALUES (?,?,?)",listdata)

#c.execute("SELECT rowid,* FROM tab ORDER BY nama DESC")
#order by DESC dari besar ke kecil, order by ASC dari kecil ke besar

#c.execute("SELECT rowid,* FROM tab WHERE usia==22 ORDER BY nama")
c.execute("UPDATE tab SET nama='fawaz', usia=31 WHERE rowid=5")
c.execute("DELETE FROM tab WHERE rowid==5")
c.execute("SELECT rowid,* FROM tab")


items = c.fetchall()

for f in items:
   print(f)

#for f in items:
#    print(f[1])

#print(items[2][2])

c.execute("""CREATE TABLE gambar
        (gambar BLOB)
"""
)

c.execute("DROP TABLE IF EXISTS gambar")

gambar = open("depresiface.jpg","rb")
gambar2 = gambar.read()
gambarbaru= open("gambarbaru.jpg","wb")

gambarsimpen = sqlite3.Binary(gambar2)
c.execute("INSERT INTO gambar VALUES (?)", (gambarsimpen,))
c.execute("SELECT * FROM GAMBAR")
gambarbaru.write(c.fetchone()[0])

gambar.close()
gambarbaru.close()
c.close()