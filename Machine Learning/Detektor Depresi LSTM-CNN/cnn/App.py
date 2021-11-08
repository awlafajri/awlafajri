import PySimpleGUI as sg
import cv2
import sys

from os.path import basename
from PyQt5 import QtWidgets, QtCore, QtGui
import tkinter as tk
from PIL import ImageGrab
import time
import os

from keras.preprocessing import image
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

file_text = [

    [

        sg.Text("Tahun (Y)")

    ],

    [

        sg.Text("Bulan (M)")

    ],

    [

        sg.Text("Tanggal (D)")

    ],

    [

        sg.Text("Jam")

    ],

    [

        sg.Text("Nama")

    ],



    [

        sg.Text("Bagian ini hanya boleh diisi pribadi")

    ],


    [

        sg.Text("Tolong Jawab Dengan Memasukkan 1-5 (boleh kosong)")

    ],

    [

        sg.Text("1 artinya sangat tidak setuju dan 5 sangat setuju")

    ],


    [

        sg.Text("Saya memikirkan tentang bunuh diri atau menyakiti diri")

    ],

    [

        sg.Text("Saya merasa tidak berguna dan bersalah")

    ],

    [

        sg.Text("Saya tidak bisa konsentrasi")

    ],

    [

        sg.Text("Saya insomnia")

    ],

    [

        sg.Text("Saya kelelahan")

    ],

    [

        sg.Text("Berat badan saya berubah drastis")

    ],

    [sg.Text(size=(12, 1), key="-INF-")]

]

file_input = [

    [

        sg.In(size=(25, 1), enable_events=True, key="-YEAR-"),

    ],

    [

        sg.In(size=(25, 1), enable_events=True, key="-MONTH-"),

    ],

    [

        sg.In(size=(25, 1), enable_events=True, key="-DATE-"),

    ],

    [

        sg.In(size=(25, 1), enable_events=True, key="-TIME-"),

    ],

    [

        sg.In(size=(25, 1), enable_events=True, key="-NAME-"),

    ],

    [sg.Text(size=(12, 1),key="-ANA-")],
    [sg.Text(size=(12, 1))],
    [sg.Text(size=(12, 1))],

    [

        sg.In(size=(25, 1), enable_events=True, key="-Q1-"),

    ],

    [

        sg.In(size=(25, 1), enable_events=True, key="-Q2-"),

    ],

    [

        sg.In(size=(25, 1), enable_events=True, key="-Q3-"),

    ],

    [

        sg.In(size=(25, 1), enable_events=True, key="-Q4-"),

    ],

    [

        sg.In(size=(25, 1), enable_events=True, key="-Q5-"),

    ],

    [

        sg.In(size=(25, 1), enable_events=True, key="-Q6-"),

    ],
    [sg.Text(size=(12, 1), text_color="RED", key="-INFO-")]


]

# For now will only show the name of the file that was chosen

image_viewer_column = [

    [sg.In(size=(25, 1), enable_events=True, key="-PATH-"),

        sg.FileBrowse()],

    [
      sg.Button("Take a Quick Photo", key="-WEB-",)
    ],

    [
        sg.Button("Open Snipping Tool", key="-MED-", )
    ],

    [sg.Text("Image :")],

    [sg.Image(filename="", key="-IMAGE-")],

    [sg.Text(size=(40, 1), key="-TOUT-")],

    [
        sg.Button("ANALYSE", key="-ANA-" ), sg.Button("SAVE", key="-SAV-")
    ],
    [sg.Text(size=(40, 1), key="-R1-")],
    [sg.Text(size=(40, 1), key="-R2-")],
    [sg.Text(size=(40, 1), key="-R3-")]

]

result_column = [
    [sg.Button("Bulan",key="-BUL-"),sg.Button("Tahun",key="-TAH-")],

    [sg.Image(key="-IMAGER1-")],

    [sg.Image(key="-IMAGER2-")],


]

layout = [

    [

        sg.Column(file_text),

        sg.Column(file_input),

        sg.VSeperator(),

        sg.Column(image_viewer_column),

        sg.VSeperator(),

        sg.Column(result_column)

    ]

]

window = sg.Window("SHARE", layout)

ind = 1
tes = 0
k=str()
while True:
    event, values = window.read()
    cascPath = "haarcascade_frontalface_default.xml"

    faceCascade = cv2.CascadeClassifier(cascPath)

    if event == "Exit" or event == sg.WIN_CLOSED:

        break

    objects = ['marah', 'jijik', 'takut', 'bahagia', 'sedih', 'kaget', 'netral']


    if event=="-WEB-":
        cap = cv2.VideoCapture(0)
        cap.set(3, 320)  # atur dimensi lebar
        cap.set(4, 240)  # atur dimensi tinggi
        cap.set(10, 1000)  # ini atur brightness

        for f in range(3):
            success, img = cap.read()

        gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
        faces = faceCascade.detectMultiScale(
            gray,
            scaleFactor=1.1,
            minNeighbors=5,
            minSize=(30, 30),
            flags=cv2.CASCADE_SCALE_IMAGE
        )

        # print("Found {0} faces!".format(len(faces)))

        # Draw a rectangle around the faces

        for (x, y, w, h) in faces:
            roi_color = img[y:y + h, x:x + w]
            cv2.imwrite("webface.jpg", roi_color)
            cv2.rectangle(img, (x, y), (x + w + 10, y + h + 10), (0, 255, 0), 2)

        if len(faces)>1:
            window["-TOUT-"].update("Tolong foto lebih dekat hanya untuk satu wajah",text_color="RED")


        imgbytes = cv2.imencode(".png", img)[1].tobytes()
        tesimg = image.load_img('webface.jpg', grayscale=True, target_size=(48, 48))
        tes=2
        window["-IMAGE-"].update(data=imgbytes)
        cap.release()


    if event=="-PATH-":
        path=values["-PATH-"]
        img=cv2.imread(path)
        gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
        faces = faceCascade.detectMultiScale(
            gray,
            scaleFactor=1.1,
            minNeighbors=5,
            minSize=(30, 30),
            flags=cv2.CASCADE_SCALE_IMAGE
        )

        # print("Found {0} faces!".format(len(faces)))
        if len(faces)>1:
            window["-TOUT-"].update("Tolong foto lebih dekat hanya untuk satu wajah")
        else:
            window["-TOUT-"].update("")

        # Draw a rectangle around the faces

        for (x, y, w, h) in faces:
            roi_color = img[y:y + h, x:x + w]
            cv2.imwrite(path[:-4]+"face.jpg", roi_color)
            cv2.rectangle(img, (x, y), (x + w + 10, y + h + 10), (0, 255, 0), 2)

        img=cv2.resize(img,(200,200))
        imgbytes = cv2.imencode(".png", img)[1].tobytes()
        tesimg = image.load_img(path[:-4]+"face.jpg", grayscale=True, target_size=(48, 48))
        tes=1
        window["-IMAGE-"].update(data=imgbytes)


    if event=="-MED-":
        window.close()
        class MyWidget(QtWidgets.QWidget):
            def __init__(self):
                super().__init__()
                root = tk.Tk()
                screen_width = root.winfo_screenwidth()
                screen_height = root.winfo_screenheight()
                self.setGeometry(0, 0, screen_width, screen_height)
                self.setWindowTitle(' ')
                self.begin = QtCore.QPoint()
                self.end = QtCore.QPoint()
                self.setWindowOpacity(0.3)
                QtWidgets.QApplication.setOverrideCursor(
                    QtGui.QCursor(QtCore.Qt.CrossCursor)
                )
                self.setWindowFlags(QtCore.Qt.FramelessWindowHint)
                self.show()

            def paintEvent(self, event):
                qp = QtGui.QPainter(self)
                qp.setPen(QtGui.QPen(QtGui.QColor('black'), 3))
                qp.setBrush(QtGui.QColor(128, 128, 255, 128))
                qp.drawRect(QtCore.QRect(self.begin, self.end))

            def mousePressEvent(self, event):
                self.begin = event.pos()
                self.end = self.begin
                self.update()

            def mouseMoveEvent(self, event):
                self.end = event.pos()
                self.update()

            def mouseReleaseEvent(self, event):
                self.close()

                x1 = min(self.begin.x(), self.end.x())
                y1 = min(self.begin.y(), self.end.y())
                x2 = max(self.begin.x(), self.end.x())
                y2 = max(self.begin.y(), self.end.y())

                img = ImageGrab.grab(bbox=(x1, y1, x2, y2))
                img.save('capture.png')
                os.system("python D:/cnn/App.py")


        if __name__ == '__main__':
            app = QtWidgets.QApplication(sys.argv)
            window2 = MyWidget()
            app.aboutToQuit.connect(app.deleteLater)
            sys.exit(app.exec_())

    if event=="-ANA-":
        df = pd.read_csv('fer2013.csv')

        emotion_map = {0: 'Marah', 1: 'Jijik', 2: 'Takut', 3: 'Bahagia', 4: 'Sedih', 5: 'Kaget', 6: 'Netral'}
        emotion_counts = df['emotion'].value_counts(sort=False).reset_index()
        emotion_counts.columns = ['emotion', 'number']
        emotion_counts['emotion'] = emotion_counts['emotion'].map(emotion_map)

        def row2image(row):
            pixels, emotion = row['pixels'], emotion_map[row['emotion']]
            img = np.array(pixels.split())
            img = img.reshape(48, 48)
            image = np.zeros((48, 48, 3))
            image[:, :, 0] = img
            image[:, :, 1] = img
            image[:, :, 2] = img
            return np.array([image.astype(np.uint8), emotion])

        plt.figure(0, figsize=(16, 10))
        for i in range(1, 8):
            face = df[df['emotion'] == i - 1].iloc[0]
            img = row2image(face)
            plt.subplot(2, 4, i)

        def getData(filname):
            Y = []
            X = []
            first = True
            for line in open(filname):
                if first:
                    first = False
                else:
                    row = line.split(',')
                    Y.append(int(row[0]))
                    X.append([int(p) for p in row[1].split()])

            X, Y = np.array(X) / 255.0, np.array(Y)
            return X, Y

        X, Y = getData("fer2013.csv")
        num_class = len(set(Y))

        N, D = X.shape
        X = X.reshape(N, 48, 48, 1)

        from sklearn.model_selection import train_test_split

        X_train, X_test, y_train, y_test = train_test_split(X, Y, test_size=0.1, random_state=0)

        from keras.optimizers import *

        from tensorflow.keras.models import load_model

        model = load_model('model_filter.h5', compile=True)


        def emotion_analysis(emotions):
            objects = ['marah', 'jijik', 'takut', 'bahagia', 'sedih', 'kaget', 'netral']
            y_pos = np.arange(len(objects))
            plt.bar(y_pos, emotions, align='center', alpha=0.9)
            plt.tick_params(axis='x', which='both', pad=10, width=4, length=10)
            plt.xticks(y_pos, objects)
            plt.ylabel('percentage')
            plt.title('emotion')


        y_pred = model.predict(X_test)
        x = image.img_to_array(tesimg)
        x = np.expand_dims(x, axis=0)

        x /= 255

        custom = model.predict(x)
        emotion_analysis(custom[0])

        x = np.array(x, 'float32')
        x = x.reshape([48, 48]);

        plt.gray()

        m = 0.000000000000000000001
        a = custom[0]
        for i in range(0, len(a)):
            if a[i] > m:
                m = a[i]
                ind = i
        window["-TOUT-"].update('Expression Prediction:' + objects[ind])

    if event == "-SAV-":
        df=pd.DataFrame(columns=["Tanggal","Bulan","Tahun","Jam","Emosi","Depresi","Stress"])
        Q= (str(values["-Q1-"]) in "12345") and (str(values["-Q1-"]) in "12345") and (str(values["-Q1-"]) in "12345")
        QQ= (str(values["-Q1-"]) in "12345") and (str(values["-Q1-"]) in "12345") and (str(values["-Q1-"]) in "12345")
        if values["-DATE-"].isdigit() and values["-MONTH-"].isdigit() and values["-YEAR-"].isdigit() and values["-TIME-"].isdigit() and Q and QQ:
            df["Tanggal"]=[values["-DATE-"]]
            df["Bulan"]=[values["-MONTH-"]]
            df["Tahun"]=[values["-YEAR-"]]
            df["Jam"]=[values["-TIME-"]]
            df["Emosi"]=[ind]
            if ind in [1,2,4]:
                df["Depresi"]=[-1]
            elif ind == 3:
                df["Depresi"]=[1]
            else:
                df["Depresi"]=[0]
            if ind in [0,2,4]:
                df["Stress"]=[-1]
            elif ind ==3:
                df["Stress"]=[1]
            else:
                df["Stress"]=[0]
            df.to_csv(values["-NAME-"] + "mentah.csv", mode="a", index=False, header=False)
            dfs = pd.read_csv(values["-NAME-"] + "mentah.csv")
            df2 = pd.DataFrame(dfs.values, columns=["Tanggal", "Bulan", "Tahun", "Jam", "Emosi", "Depresi", "Stress"])
            df3 = df2.loc[df2["Bulan"] == int(values["-MONTH-"])]
            tanggal = set(df3["Tanggal"])
            tanggal = list(tanggal)
            df3 = df3.groupby(["Tahun", "Bulan", "Tanggal"]).mean().get("Depresi")
            plt.plot(tanggal, df3, "bo")
            plt.title("Grafik Skala Kondisi Emosi (Depresi) Bulan " + values["-MONTH-"])
            plt.xlabel("Tanggal")
            plt.ylabel("Skala Kondisi Emosi (Depresi)")
            plt.xticks(ticks=tanggal)
            plt.savefig(values["-NAME-"]+values["-YEAR-"] + values["-MONTH-"] + "D.png", dpi=300)
            plt.close()

            df3 = df2.loc[df2["Bulan"] == int(values["-MONTH-"])]
            tanggal = set(df3["Tanggal"])
            tanggal = list(tanggal)
            df3 = df3.groupby(["Tahun", "Bulan", "Tanggal"]).mean().get("Stress")
            plt.plot(tanggal, df3, "ro")
            plt.title("Grafik Skala Kondisi Emosi (Stress) Bulan " + values["-MONTH-"])
            plt.xlabel("Tanggal")
            plt.ylabel("Skala Kondisi Emosi (Stress)")
            plt.xticks(ticks=tanggal)
            plt.savefig(values["-NAME-"]+values["-YEAR-"] + values["-MONTH-"] + "S.png", dpi=300)
            plt.close()

            dfs = pd.read_csv(values["-NAME-"] + "mentah.csv")
            df2 = pd.DataFrame(dfs.values, columns=["Tanggal", "Bulan", "Tahun", "Jam", "Emosi", "Depresi", "Stress"])
            df3 = df2.loc[df2["Tahun"] == int(values["-YEAR-"])]
            bulan = set(df3["Bulan"])
            bulan = list(bulan)
            df3 = df3.groupby(["Tahun", "Bulan"]).mean().get("Depresi")
            plt.plot(bulan, df3, "bo")
            plt.title("Grafik Skala Kondisi Emosi (Depresi) Tahun " + values["-YEAR-"])
            plt.xlabel("bulan")
            plt.ylabel("Skala Kondisi Emosi (Depresi)")
            plt.xticks(ticks=bulan)
            plt.savefig(values["-NAME-"]+values["-YEAR-"] + "D.png", dpi=300)
            plt.close()

            dfs = pd.read_csv(values["-NAME-"] + "mentah.csv")
            df2 = pd.DataFrame(dfs.values, columns=["Tanggal", "Bulan", "Tahun", "Jam", "Emosi", "Depresi", "Stress"])
            df3 = df2.loc[df2["Tahun"] == int(values["-YEAR-"])]
            bulan = set(df3["Bulan"])
            bulan = list(bulan)
            df3 = df3.groupby(["Tahun", "Bulan"]).mean().get("Stress")
            plt.plot(bulan, df3, "ro")
            plt.title("Grafik Skala Kondisi Emosi (Stress) Tahun " + values["-YEAR-"])
            plt.xlabel("bulan")
            plt.ylabel("Skala Kondisi Emosi (Stress)")
            plt.xticks(ticks=bulan)
            plt.savefig(values["-NAME-"]+values["-YEAR-"] + "S.png", dpi=300)
            plt.close()

            q=pd.DataFrame(columns=["Tanggal","Bulan","Tahun","Jam","Q1","Q2","Q3","Q4","Q5","Q6"])
            q["Tanggal"]=[values["-DATE-"]]
            q["Bulan"]=[values["-MONTH-"]]
            q["Tahun"]=[values["-YEAR-"]]
            q["Jam"]=[values["-TIME-"]]
            q["Q1"]=[values["-Q1-"] or 3]
            q["Q2"] = [values["-Q2-"] or 3]
            q["Q3"] = [values["-Q3-"] or 3]
            q["Q4"] = [values["-Q4-"] or 3]
            q["Q5"] = [values["-Q5-"] or 3]
            q["Q6"] = [values["-Q6-"] or 3]
            q.to_csv(values["-NAME-"] + "Q.csv", mode="a", index=False, header=False)

        else:
            window["-INFO-"].update("Wrong Input")

    if event == "-BUL-":
        imgd1 = cv2.imread(values["-NAME-"]+values["-YEAR-"]+values["-MONTH-"]+"D.png")
        imgd1 = cv2.resize(imgd1,(420,300))
        imgd1bytes = cv2.imencode(".png", imgd1)[1].tobytes()
        window["-IMAGER1-"].update(data=imgd1bytes)

        imgs1 = cv2.imread(values["-NAME-"]+values["-YEAR-"] + values["-MONTH-"] + "S.png")
        imgs1 = cv2.resize(imgs1, (420, 300))
        imgs1bytes = cv2.imencode(".png", imgs1)[1].tobytes()
        window["-IMAGER2-"].update(data=imgs1bytes)

        tanggalbaru = int(values["-DATE-"])

        dfs = pd.read_csv(values["-NAME-"] + "mentah.csv")
        df2 = pd.DataFrame(dfs.values,
                           columns=["Tanggal", "Bulan", "Tahun", "Jam", "Emosi", "Depresi", "Stress"])
        dfbaru = df2.loc[(df2["Bulan"] == int(values["-MONTH-"])) & (df2["Tanggal"] == int(values["-DATE-"]))]
        if dfbaru["Depresi"].mean()<0:
            k="Kamu mungkin memiliki simptom depresi ringan"
            window["-R1-"].update(k)
        else:
            window["-R1-"].update("Kamu sehat")

        if dfbaru["Stress"].mean()<0:
            window["-R2-"].update("Kamu memiliki simptom stress")
        else:
            window["-R2-"].update("Kamu sehat")

        sum = 0
        sum2 = 0
        for f in range(max((tanggalbaru - 7), 0), tanggalbaru + 1):
            dfs = pd.read_csv(values["-NAME-"] + "mentah.csv")
            df2 = pd.DataFrame(dfs.values,
                               columns=["Tanggal", "Bulan", "Tahun", "Jam", "Emosi", "Depresi", "Stress"])
            dfbaru = df2.loc[df2["Bulan"] == int(values["-MONTH-"])]
            tanggal = set(dfbaru["Tanggal"])
            tanggal = list(tanggal)
            dfbaru = dfbaru.groupby(["Tahun", "Bulan", "Tanggal"]).mean().get("Depresi")

            if f in tanggal:
                kil = tanggal.index(f)
                if dfbaru[kil] < 0:
                    sum += 1

        if tanggalbaru < 7:
            for f in range((31 - (7 - tanggalbaru)), 31):
                dfs = pd.read_csv(values["-NAME-"] + "mentah.csv")
                df2 = pd.DataFrame(dfs.values,
                                   columns=["Tanggal", "Bulan", "Tahun", "Jam", "Emosi", "Depresi", "Stress"])
                dfbaru = df2.loc[df2["Bulan"] == (int(values["-MONTH-"])-1)]
                tanggal = set(dfbaru["Tanggal"])
                tanggal = list(tanggal)
                dfbaru = dfbaru.groupby(["Tahun", "Bulan", "Tanggal"]).mean().get("Depresi")

                if f in tanggal:
                    kil = tanggal.index(f)
                    if dfbaru[kil] < 0:
                        sum2 += 1
            sum = sum + sum2

        if sum > 4:
            k="Kamu memiliki simptom depresi sedang"
            window["-R1-"].update(k)

        qs = pd.read_csv(values["-NAME-"] + "Q.csv")
        q2 = pd.DataFrame(qs.values, columns=["Tanggal","Bulan","Tahun","Jam","Q1","Q2","Q3","Q4","Q5","Q6"])
        qbaru = q2.loc[(q2["Bulan"] == int(values["-MONTH-"])) & (q2["Tanggal"] == int(values["-DATE-"]))]
        dep = list(qbaru["Q1"])+list(qbaru["Q2"])+list(qbaru["Q3"])

        simptom = 0

        for f in dep:
            if f>3:
                k="Kamu memiliki simptom depresi ringan"
                window["-R1-"].update(k)

                for f in list(qbaru["Q4"]):
                    if f > 3:
                        simptom += 1

                for f in list(qbaru["Q5"]):
                    if f > 3:
                        simptom += 1

                for f in list(qbaru["Q6"]):
                    if f > 3:
                        simptom += 1

                if simptom == 1:
                    k = "Kamu memiliki simptom depresi sedang"
                    window["-R1-"].update(k)

                if simptom > 1:
                    k = "Kamu memiliki simptom depresi parah"
                    window["-R1-"].update(k)


        sum = 0
        sum2 = 0
        for f in range(max((tanggalbaru - 14), 0), tanggalbaru + 1):
            dfs = pd.read_csv(values["-NAME-"] + "mentah.csv")
            df2 = pd.DataFrame(dfs.values,
                               columns=["Tanggal", "Bulan", "Tahun", "Jam", "Emosi", "Depresi", "Stress"])
            dfbaru = df2.loc[df2["Bulan"] == int(values["-MONTH-"])]
            tanggal = set(dfbaru["Tanggal"])
            tanggal = list(tanggal)
            dfbaru = dfbaru.groupby(["Tahun", "Bulan", "Tanggal"]).mean().get("Depresi")

            if f in tanggal:
                kil = tanggal.index(f)
                if dfbaru[kil] < 0:
                    sum += 1

        if tanggalbaru < 14:
            for f in range((31 - (14 - tanggalbaru)), 31):
                dfs = pd.read_csv(values["-NAME-"] + "mentah.csv")
                df2 = pd.DataFrame(dfs.values,
                                   columns=["Tanggal", "Bulan", "Tahun", "Jam", "Emosi", "Depresi", "Stress"])
                dfbaru = df2.loc[df2["Bulan"] == (int(values["-MONTH-"])-1)]
                tanggal = set(dfbaru["Tanggal"])
                tanggal = list(tanggal)
                dfbaru = dfbaru.groupby(["Tahun", "Bulan", "Tanggal"]).mean().get("Depresi")

                if f in tanggal:
                    kil = tanggal.index(f)
                    if dfbaru[kil] < 0:
                        sum2 += 1
            sum = sum + sum2

        if sum > 7:
            window["-R1-"].update(k+" akut")

    if event == "-TAH-":
        imgd2 = cv2.imread(values["-NAME-"]+values["-YEAR-"]+"D.png")
        imgd2 = cv2.resize(imgd2,(420,300))
        imgd2bytes = cv2.imencode(".png", imgd2)[1].tobytes()
        window["-IMAGER1-"].update(data=imgd2bytes)

        imgs2 = cv2.imread(values["-NAME-"]+values["-YEAR-"] + "S.png")
        imgs2 = cv2.resize(imgs2, (420, 300))
        imgs2bytes = cv2.imencode(".png", imgs2)[1].tobytes()
        window["-IMAGER2-"].update(data=imgs2bytes)

        tanggalbaru = int(values["-DATE-"])

        dfs = pd.read_csv(values["-NAME-"] + "mentah.csv")
        df2 = pd.DataFrame(dfs.values,
                           columns=["Tanggal", "Bulan", "Tahun", "Jam", "Emosi", "Depresi", "Stress"])
        dfbaru = df2.loc[(df2["Bulan"] == int(values["-MONTH-"])) & (df2["Tanggal"] == int(values["-DATE-"]))]
        if dfbaru["Depresi"].mean()<0:
            k="Kamu mungkin memiliki simptom depresi ringan"
            window["-R1-"].update(k)
        else:
            window["-R1-"].update("Kamu sehat")

        if dfbaru["Stress"].mean()<0:
            window["-R2-"].update("Kamu memiliki simptom stress")
        else:
            window["-R2-"].update("Kamu sehat")

        sum = 0
        sum2 = 0
        for f in range(max((tanggalbaru - 7), 0), tanggalbaru + 1):
            dfs = pd.read_csv(values["-NAME-"] + "mentah.csv")
            df2 = pd.DataFrame(dfs.values,
                               columns=["Tanggal", "Bulan", "Tahun", "Jam", "Emosi", "Depresi", "Stress"])
            dfbaru = df2.loc[df2["Bulan"] == int(values["-MONTH-"])]
            tanggal = set(dfbaru["Tanggal"])
            tanggal = list(tanggal)
            dfbaru = dfbaru.groupby(["Tahun", "Bulan", "Tanggal"]).mean().get("Depresi")

            if f in tanggal:
                kil = tanggal.index(f)
                if dfbaru[kil] < 0:
                    sum += 1

        if tanggalbaru < 7:
            for f in range((31 - (7 - tanggalbaru)), 31):
                dfs = pd.read_csv(values["-NAME-"] + "mentah.csv")
                df2 = pd.DataFrame(dfs.values,
                                   columns=["Tanggal", "Bulan", "Tahun", "Jam", "Emosi", "Depresi", "Stress"])
                dfbaru = df2.loc[df2["Bulan"] == (int(values["-MONTH-"])-1)]
                tanggal = set(dfbaru["Tanggal"])
                tanggal = list(tanggal)
                dfbaru = dfbaru.groupby(["Tahun", "Bulan", "Tanggal"]).mean().get("Depresi")

                if f in tanggal:
                    kil = tanggal.index(f)
                    if dfbaru[kil] < 0:
                        sum2 += 1
            sum = sum + sum2

        if sum > 4:
            k="Kamu memiliki simptom depresi sedang"
            window["-R1-"].update(k)


        qs = pd.read_csv(values["-NAME-"] + "Q.csv")
        q2 = pd.DataFrame(qs.values, columns=["Tanggal","Bulan","Tahun","Jam","Q1","Q2","Q3","Q4","Q5","Q6"])
        qbaru = q2.loc[(q2["Bulan"] == int(values["-MONTH-"])) & (q2["Tanggal"] == int(values["-DATE-"]))]
        dep = list(qbaru["Q1"])+list(qbaru["Q2"])+list(qbaru["Q3"])

        simptom = 0

        for f in dep:
            if f > 3:
                k = "Kamu memiliki simptom depresi ringan"
                window["-R1-"].update(k)

                for f in list(qbaru["Q4"]):
                    if f > 3:
                        simptom += 1

                for f in list(qbaru["Q5"]):
                    if f > 3:
                        simptom += 1

                for f in list(qbaru["Q6"]):
                    if f > 3:
                        simptom += 1

                if simptom == 1:
                    k = "Kamu memiliki simptom depresi sedang"
                    window["-R1-"].update(k)

                if simptom > 1:
                    k = "Kamu memiliki simptom depresi parah"
                    window["-R1-"].update(k)


        sum = 0
        sum2 = 0
        for f in range(max((tanggalbaru - 14), 0), tanggalbaru + 1):
            dfs = pd.read_csv(values["-NAME-"] + "mentah.csv")
            df2 = pd.DataFrame(dfs.values,
                               columns=["Tanggal", "Bulan", "Tahun", "Jam", "Emosi", "Depresi", "Stress"])
            dfbaru = df2.loc[df2["Bulan"] == int(values["-MONTH-"])]
            tanggal = set(dfbaru["Tanggal"])
            tanggal = list(tanggal)
            dfbaru = dfbaru.groupby(["Tahun", "Bulan", "Tanggal"]).mean().get("Depresi")

            if f in tanggal:
                kil = tanggal.index(f)
                if dfbaru[kil] < 0:
                    sum += 1

        if tanggalbaru < 14:
            for f in range((31 - (14 - tanggalbaru)), 31):
                dfs = pd.read_csv(values["-NAME-"] + "mentah.csv")
                df2 = pd.DataFrame(dfs.values,
                                   columns=["Tanggal", "Bulan", "Tahun", "Jam", "Emosi", "Depresi", "Stress"])
                dfbaru = df2.loc[df2["Bulan"] == (int(values["-MONTH-"])-1)]
                tanggal = set(dfbaru["Tanggal"])
                tanggal = list(tanggal)
                dfbaru = dfbaru.groupby(["Tahun", "Bulan", "Tanggal"]).mean().get("Depresi")

                if f in tanggal:
                    kil = tanggal.index(f)
                    if dfbaru[kil] < 0:
                        sum2 += 1
            sum = sum + sum2

        if sum > 7:
            window["-R1-"].update(k+" akut")





sys.exit()