dict= {
    "Nama" : "Awla",
    "Usia" : 20,
    "Teman":["ldoni","ba"]
}
dict["hewan kesukaan"]="Burung"

#print(dict)
#print(dict.keys())
#print(dict.items())
#print(dict.values())

print(dict["Nama"])
print(dict.get("Usia2",0))

#list = [1,2,3,4,5]
#list.append(6)
#print(list)

#f(x) dari x= 0 sampai x=5
#f(x)=x^2+3+1

f =list()
for x in range(0,6):
    f.append(x**2 + 3 + 1)

#print(f)


#print(dict.values())
#for f in dict.values():
#    print(f)

#for a in "Saya manusia":
#    if a in ["a","i","u","e","o"]:
#        print(a)

kata="Saya manusia"
tes2=list(kata)
#print(tes2)

#print(len(kata))

#for g in range(len(kata)):
#    print(kata[g])

indeks = 0
while indeks < len(kata):
#    print(kata[indeks])
    indeks+=1

for a in range(10):
    print("a")
    for b in range(5):
        print("b")
        if b == 2:
            break

