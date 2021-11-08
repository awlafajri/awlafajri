import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv("datamainanrev.csv")

fruit_name_onehot = list()

for data in df["fruit_name"]:
    if data == "orange":
        fruit_name_onehot.append(1)
    else:
        fruit_name_onehot.append(-1)

df["fruit_name_onehot"]=fruit_name_onehot

w = [0,0,0]
b = 1
eta = 0.5
epoch = 10000
banyakdata = len(df)


databaru1 = df.loc[df["fruit_name_onehot"]==1]
databaru2 = df.loc[df["fruit_name_onehot"]==-1]

#plt.plot(databaru1["height"] ,databaru1["width"],"ro")
#plt.plot(databaru2["height"] ,databaru2["width"],"bo")
#plt.show()

for iterasi in range(epoch):
    z = list()
    for indeks in range(banyakdata):
        x1 = df["height"][indeks]
        x2 = df["width"][indeks]
        x3 = df["mass"][indeks]
        dum = w[0]*x1 + w[1]*x2 +w[2]*x3 #z = w1x + w2y
        z.append(dum)

    pi = list()
    for z_n in z:
        if z_n + b >= 0:
            pi.append(1)
        else:
            pi.append(-1)


    for n in range(banyakdata):
        deltaw1 =  eta*(df["fruit_name_onehot"][n]-pi[n])*df["height"][n] # eta * k1 * x1
        deltaw2 = eta*(df["fruit_name_onehot"][n] - pi[n]) * df["width"][n] # eta * k2 * x2
        deltaw3 = eta * (df["fruit_name_onehot"][n] - pi[n]) * df["mass"][n]
        w[0] = w[0]+deltaw1
        w[1] = w[1]+deltaw2
        w[2] = w[2]+deltaw3


#    x_model = range(int(min(df["height"]-1)),int(max(df["height"]+2)))
#    y_model = (1/w[1])*(-w[0]*x_model-b)

#    if iterasi%20 == 0:
#        plt.plot(databaru1["height"] ,databaru1["width"],"ro")
#        plt.plot(databaru2["height"] ,databaru2["width"],"bo")
#        plt.plot(x_model,y_model,"g--")
#        plt.show()
#        plt.close()


sb_x1_coba = float(input("masukkan tinggi buah:"))
sb_x2_coba = float(input("masukkan lebar buah:"))
sb_x3_coba = float(input("masukkan berat buah:"))

if w[0]*sb_x1_coba + w[1]*sb_x2_coba + w[2]*sb_x3_coba + b >= 0:
    print("Buah ini adalah Orange")
else:
    print("Buah ini adalah Lemon")