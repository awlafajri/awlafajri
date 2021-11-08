

try:
    x=int(input("penyebut : "))
    y=int(input("pembilang : "))
    result=y/x
except ValueError:
    print("salah tipe data mas!")
except ZeroDivisionError:
    print("masukkin penyebut mikir mas!")
finally:
    print("program selesai")

if y>3:
    raise Exception("Pembilangnya banyak mas!")

print(result)