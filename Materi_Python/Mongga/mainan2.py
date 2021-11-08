kalimat = input("Masukkan kalimat : \n")
jumlah_kata = {}

kata_kata = kalimat.split(" ")
print(kata_kata)

for kata in kata_kata:
    jumlah_kata[kata.lower()]= jumlah_kata.get(kata.lower(),0) + 1
#    print(jumlah_kata)

print(jumlah_kata)
majority = str()
jumlah = 0

for kata in jumlah_kata.keys():
    if jumlah_kata[kata]> jumlah:
        majority = kata
        jumlah=jumlah_kata[kata]

print(majority)
print(jumlah)