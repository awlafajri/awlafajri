#Awla Fajri Assalam
#Program tutorial tipe data
#10.29.2020

#a="hello world"
#b= list(a)

#print(b)
#print(a[4])
#print(a[-4])
#print(a[1:3])
#print(a[-5:-1])
#print(a[:3])
#print(a[3:])

#c= """Hello
#      World
#Blabla
#"""

#d= "Hello \nworld"
#e=list(d)

#a="hello"
#b=" world"
#print(a+b)

#print(len(a+b))
#print(dir(str))
#print(a.capitalize())
#print(a.upper())

#c="Nama saya babe saya suka burung perkutut"
#print(c.index("saya"))
#print(c.index("su"))
#print(c)
#c=c.replace("saya","kamu",1)
#print(c)
#c=c[0:5]+"kamu"+c[9:]
#print(c)

#d="  hello,world "
#d=d.strip()
#e=d.split(",")
#print(d)
#print(e)

#z= "nama saya Awla saya" + str(17) +"tahun berat saya "+ str(14.3)

a= "Nama saya {nama} saya {umur} tahun berat saya {berat:.3f}"
a=a.format(nama="a",umur="b",berat=1.2345)
print(a)
