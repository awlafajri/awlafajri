import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

data = pd.DataFrame(columns = ["x","y"])

#y = x
data["x"]= [1,2,3,4,5,6,7,8,9,10]
data["y"]= [1,1.2,3.6,3.9,4.3,6.8,7,7.3,8.7,10]

#plt.plot(data["x"],data["y"],"bo")
#plt.show()

def loss_function(m,b,titik):
    error = 0
    for indeks in range(len(titik)):
        x = titik.iloc[indeks].x
        y = titik.iloc[indeks].y
        error = error + (y - (m*x + b))**2
    error = error/float(len(titik))
    return error

def gradient_descent(m_sekarang, b_sekarang, titik, eta):
    m_gradien = 0
    b_gradien = 0

    n = len(titik)

    for indeks in range(n):
        x = titik.iloc[indeks].x
        y = titik.iloc[indeks].y

        m_gradien = m_gradien + -(2/n)*x*(y-(m_sekarang*x + b_sekarang))
        b_gradien = b_gradien + -(2/n)*(y-(m_sekarang*x +b_sekarang))

    m_baru = m_sekarang - eta*m_gradien
    b_baru = b_sekarang - eta*b_gradien

    return m_baru,b_baru

m = 0
b = 0
eta = 0.0005 #max 1 min 0
epoch = 200

errorfunc = list()
for indeks in range(epoch):
    errorfunc.append(loss_function(m,b,data))
    m,b = gradient_descent(m,b,data,eta)

    if indeks%20 == 0:
        plt.plot(data["x"],data["y"],"bo")
        plt.plot(data["x"], [m*x+b for x in data["x"]], "r--")
        plt.show()
        plt.close()

plt.plot(range(epoch),errorfunc,"g")
plt.xlabel("epoch")
plt.ylabel("error")
plt.show()
plt.close()

x_coba = input("masukkan x: ")
y_hasil = m*x_coba+b
print("ini hasilnya :"+ str(y_hasil))