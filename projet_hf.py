from PyQt5 import QtCore, QtGui, QtWidgets
from math import*
from functools import partial
import matplotlib.pyplot as plt
import cmath



class Ui_projet_HF(object):
    def setupUi(self, projet_HF):
        projet_HF.setObjectName("projet_HF")
        projet_HF.resize(1004, 712)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("unnamed.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        projet_HF.setWindowIcon(icon)
        self.centralwidget = QtWidgets.QWidget(projet_HF)
        self.centralwidget.setObjectName("centralwidget")
        self.gridLayout = QtWidgets.QGridLayout(self.centralwidget)
        self.gridLayout.setObjectName("gridLayout")
        self.frame = QtWidgets.QFrame(self.centralwidget)
        self.frame.setStyleSheet("background-color: rgb(40, 45, 60);")
        self.frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setObjectName("frame")
        self.label = QtWidgets.QLabel(self.frame)
        self.label.setGeometry(QtCore.QRect(200, 30, 481, 20))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(16)
        font.setBold(True)
        font.setItalic(True)
        font.setWeight(75)
        self.label.setFont(font)
        self.label.setStyleSheet("\n"
"color: rgb(255, 228,2);")
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(self.frame)
        self.label_2.setGeometry(QtCore.QRect(60, 100, 101, 16))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(10)
        font.setBold(True)
        font.setItalic(True)
        font.setWeight(75)
        self.label_2.setFont(font)
        self.label_2.setObjectName("label_2")
        self.label_3 = QtWidgets.QLabel(self.frame)
        self.label_3.setGeometry(QtCore.QRect(20, 140, 161, 31))
        self.label_3.setObjectName("label_3")
        self.rl = QtWidgets.QLineEdit(self.frame)
        self.rl.setGeometry(QtCore.QRect(20, 180, 113, 20))
        self.rl.setStyleSheet("\n"
"background-color: rgb(186, 186, 186);")
        self.rl.setObjectName("rl")
        self.xl = QtWidgets.QLineEdit(self.frame)
        self.xl.setGeometry(QtCore.QRect(170, 180, 113, 20))
        self.xl.setStyleSheet("\n"
"background-color: rgb(186, 186, 186);")
        self.xl.setObjectName("xl")
        self.label_4 = QtWidgets.QLabel(self.frame)
        self.label_4.setGeometry(QtCore.QRect(20, 210, 191, 31))
        self.label_4.setObjectName("label_4")
        self.z0 = QtWidgets.QLineEdit(self.frame)
        self.z0.setGeometry(QtCore.QRect(20, 240, 113, 20))
        self.z0.setStyleSheet("background-color: rgb(186, 186, 186);")
        self.z0.setObjectName("z0")
        self.label_5 = QtWidgets.QLabel(self.frame)
        self.label_5.setGeometry(QtCore.QRect(140, 240, 21, 21))
        self.label_5.setObjectName("label_5")
        self.shrt = QtWidgets.QPushButton(self.frame)
        self.shrt.setGeometry(QtCore.QRect(300, 470, 121, 51))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(-1)
        font.setBold(True)
        font.setItalic(True)
        font.setUnderline(False)
        font.setWeight(75)
        font.setStrikeOut(False)
        self.shrt.setFont(font)
        self.shrt.setStyleSheet("QPushButton {\n"
"    background-color:#44c767;\n"
"    border-radius:28px;\n"
"    border:1px solid #18ab29;\n"
"    display:inline-block;\n"
"    cursor:pointer;\n"
"    color:#ffffff;\n"
"    font-family:Arial;\n"
"    font-size:15px;\n"
"    padding:15px 30px;\n"
"    text-decoration:none;\n"
"    text-shadow:0px 1px 0px #2f6627;\n"
"}\n"
"QPushButton:hover {\n"
"    background-color:#5cbf2a;\n"
"}\n"
"QPushButton:active {\n"
"    position:relative;\n"
"    top:1px;\n"
"}\n"
"")
        self.shrt.setObjectName("shrt")
        self.label_6 = QtWidgets.QLabel(self.frame)
        self.label_6.setGeometry(QtCore.QRect(140, 180, 21, 16))
        self.label_6.setObjectName("label_6")
        self.label_7 = QtWidgets.QLabel(self.frame)
        self.label_7.setGeometry(QtCore.QRect(290, 180, 47, 21))
        self.label_7.setObjectName("label_7")
        self.label_8 = QtWidgets.QLabel(self.frame)
        self.label_8.setGeometry(QtCore.QRect(590, 100, 71, 21))
        self.label_8.setObjectName("label_8")
        self.label_9 = QtWidgets.QLabel(self.frame)
        self.label_9.setGeometry(QtCore.QRect(530, 150, 121, 16))
        self.label_9.setObjectName("label_9")
        self.label_10 = QtWidgets.QLabel(self.frame)
        self.label_10.setGeometry(QtCore.QRect(530, 180, 47, 13))
        self.label_10.setObjectName("label_10")
        self.label_12 = QtWidgets.QLabel(self.frame)
        self.label_12.setGeometry(QtCore.QRect(530, 240, 111, 16))
        self.label_12.setObjectName("label_12")
        self.label_13 = QtWidgets.QLabel(self.frame)
        self.label_13.setGeometry(QtCore.QRect(530, 270, 47, 13))
        self.label_13.setObjectName("label_13")
        self.sol2l2 = QtWidgets.QLineEdit(self.frame)
        self.sol2l2.setGeometry(QtCore.QRect(580, 270, 113, 20))
        self.sol2l2.setStyleSheet("background-color: rgb(186, 186, 186);")
        self.sol2l2.setText("")
        self.sol2l2.setObjectName("sol2l2")
        self.label_15 = QtWidgets.QLabel(self.frame)
        self.label_15.setGeometry(QtCore.QRect(780, 270, 47, 21))
        self.label_15.setObjectName("label_15")
        self.sol2d2 = QtWidgets.QLineEdit(self.frame)
        self.sol2d2.setGeometry(QtCore.QRect(830, 270, 113, 20))
        self.sol2d2.setStyleSheet("background-color: rgb(186, 186, 186);")
        self.sol2d2.setText("")
        self.sol2d2.setObjectName("sol2d2")
        self.label_16 = QtWidgets.QLabel(self.frame)
        self.label_16.setGeometry(QtCore.QRect(540, 330, 351, 16))
        self.label_16.setText("")
        self.label_16.setObjectName("label_16")
        self.sol1l1 = QtWidgets.QLineEdit(self.frame)
        self.sol1l1.setGeometry(QtCore.QRect(580, 180, 113, 20))
        self.sol1l1.setStyleSheet("background-color: rgb(186, 186, 186);")
        self.sol1l1.setText("")
        self.sol1l1.setObjectName("sol1l1")
        self.label_17 = QtWidgets.QLabel(self.frame)
        self.label_17.setGeometry(QtCore.QRect(770, 180, 41, 21))
        self.label_17.setObjectName("label_17")
        self.sol1d1 = QtWidgets.QLineEdit(self.frame)
        self.sol1d1.setGeometry(QtCore.QRect(820, 180, 113, 20))
        self.sol1d1.setStyleSheet("background-color: rgb(186, 186, 186);")
        self.sol1d1.setText("")
        self.sol1d1.setObjectName("sol1d1")
        self.label_18 = QtWidgets.QLabel(self.frame)
        self.label_18.setGeometry(QtCore.QRect(540, 310, 411, 221))
        self.label_18.setText("")
        self.label_18.setPixmap(QtGui.QPixmap("unnamed.jpg"))
        self.label_18.setObjectName("label_18")
        self.label_21 = QtWidgets.QLabel(self.frame)
        self.label_21.setGeometry(QtCore.QRect(20, 280, 131, 20))
        self.label_21.setObjectName("label_21")
        self.line = QtWidgets.QFrame(self.frame)
        self.line.setGeometry(QtCore.QRect(461, 80, 20, 561))
        self.line.setStyleSheet("\n"
"background-color: rgb(40, 45, 60);")
        self.line.setFrameShape(QtWidgets.QFrame.VLine)
        self.line.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line.setObjectName("line")
        self.frequency = QtWidgets.QLineEdit(self.frame)
        self.frequency.setGeometry(QtCore.QRect(20, 310, 113, 20))
        self.frequency.setStyleSheet("background-color: rgb(186, 186, 186);")
        self.frequency.setObjectName("frequency")
        self.label_22 = QtWidgets.QLabel(self.frame)
        self.label_22.setGeometry(QtCore.QRect(140, 310, 41, 21))
        self.label_22.setObjectName("label_22")
        self.label_23 = QtWidgets.QLabel(self.frame)
        self.label_23.setGeometry(QtCore.QRect(20, 340, 47, 13))
        self.label_23.setText("")
        self.label_23.setObjectName("label_23")
        self.label_24 = QtWidgets.QLabel(self.frame)
        self.label_24.setGeometry(QtCore.QRect(20, 340, 181, 21))
        self.label_24.setObjectName("label_24")
        self.ebs = QtWidgets.QLineEdit(self.frame)
        self.ebs.setGeometry(QtCore.QRect(20, 370, 113, 20))
        self.ebs.setStyleSheet("background-color: rgb(186, 186, 186);")
        self.ebs.setObjectName("ebs")
        self.label_25 = QtWidgets.QLabel(self.frame)
        self.label_25.setGeometry(QtCore.QRect(140, 380, 47, 13))
        self.label_25.setText("")
        self.label_25.setObjectName("label_25")
        self.open = QtWidgets.QPushButton(self.frame)
        self.open.setGeometry(QtCore.QRect(60, 470, 121, 51))
        self.open.setStyleSheet("QPushButton {\n"
"    background-color:#44c767;\n"
"    border-radius:28px;\n"
"    border:1px solid #18ab29;\n"
"    display:inline-block;\n"
"    cursor:pointer;\n"
"    color:#ffffff;\n"
"    font-family:Arial;\n"
"    font-size:17px;\n"
"    padding:16px 31px;\n"
"    text-decoration:none;\n"
"    text-shadow:0px 1px 0px #2f6627;\n"
"}\n"
"QPushButton:hover {\n"
"    background-color:#5cbf2a;\n"
"}\n"
"QPushButton:active {\n"
"    position:relative;\n"
"    top:1px;\n"
"}\n"
"")
        self.open.setObjectName("open")
        self.line_2 = QtWidgets.QFrame(self.frame)
        self.line_2.setGeometry(QtCore.QRect(10, 400, 461, 16))
        self.line_2.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_2.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_2.setObjectName("line_2")
        self.label_26 = QtWidgets.QLabel(self.frame)
        self.label_26.setGeometry(QtCore.QRect(130, 420, 191, 20))
        self.label_26.setObjectName("label_26")
        self.label.raise_()
        self.label_2.raise_()
        self.label_3.raise_()
        self.rl.raise_()
        self.xl.raise_()
        self.label_4.raise_()
        self.z0.raise_()
        self.label_5.raise_()
        self.shrt.raise_()
        self.label_6.raise_()
        self.label_7.raise_()
        self.label_8.raise_()
        self.label_9.raise_()
        self.label_10.raise_()
        self.label_12.raise_()
        self.label_13.raise_()
        self.sol2l2.raise_()
        self.label_15.raise_()
        self.label_16.raise_()
        self.sol1l1.raise_()
        self.label_17.raise_()
        self.sol1d1.raise_()
        self.label_18.raise_()
        self.sol2d2.raise_()
        self.label_21.raise_()
        self.line.raise_()
        self.frequency.raise_()
        self.label_22.raise_()
        self.label_23.raise_()
        self.label_24.raise_()
        self.ebs.raise_()
        self.label_25.raise_()
        self.open.raise_()
        self.line_2.raise_()
        self.label_26.raise_()
        self.gridLayout.addWidget(self.frame, 0, 1, 1, 1)
        projet_HF.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(projet_HF)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 1004, 21))
        self.menubar.setObjectName("menubar")
        projet_HF.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(projet_HF)
        self.statusbar.setObjectName("statusbar")
        projet_HF.setStatusBar(self.statusbar)
       
        self.shrt.clicked.connect(self.court_circuit)
        self.open.clicked.connect(self.circuit_ouvert)
        self.shrt.clicked.connect(self.create_smith_chart)
        self.open.clicked.connect(self.create_smith_chart)
        
        self.ebs.setText('1')
        self.frequency.setText('1')
        self.rl.setText('1')
        self.xl.setText('1')
        self.z0.setText('1')
        

        self.retranslateUi(projet_HF)
        QtCore.QMetaObject.connectSlotsByName(projet_HF)

    
    def create_smith_chart(self):
        figure,axes=plt.subplots()

        lr=[0,0.2,0.5,1,2,5,50]
        lx=[-5,-2,-1,-0.5,-0.2,0.2,0.5,1,2,5]

        for r in lr :
            cercle=plt.Circle((r/(1+r),0),1/(1+r),fill=False)
            axes.set_aspect(1)
            axes.add_artist(cercle)


        for x in lx :
            cercle1=plt.Circle((1,1/x),1/x,fill=False)
            axes.set_aspect(1)
            axes.add_artist(cercle1)

        axes.set_xlim(-1,1)
        axes.set_ylim(-1,1)
        plt.plot([-1,1],[0,0],color='black')
        resis=float(self.rl.text())
        reac=float(self.xl.text())
        IC=float(self.z0.text())
        

        r=resis/IC
        x=reac/IC
        ZL=complex(r,x)
        ZC=IC/IC
        c=cmath.polar((ZL-ZC)/(ZL+ZC))
        x=c[0]*cos(c[1])
        y=c[0]*sin(c[1])
        plt.plot(x,y,color='red',marker='o')
      

        x1=c[0]*cos(c[1]+pi)
        y1=c[0]*sin(c[1]+pi)
        plt.plot(x1,y1,color='red',marker='o')
        
        plt.show()
    def calcule_charge(self):
        def determinert(a, b):
            if a == Zc:
                t = [-b/(2*Zc),-b/(2*Zc)]
                return t
            else:
                t = [(b+sqrt(a*(((Zc-a)**2)+(b**2))/Zc))/(a-Zc),
                     (b-sqrt(a*(((Zc-a)**2)+(b**2))/Zc))/(a-Zc)]
                return t
        def determinerd(T, x):
            if T[0]>=0:
                a = atan(T[0])*x/(2*pi)
            else:
                a = (pi+atan(T[0]))*x/(2*pi)
            if T[1]>=0:
                b = atan(T[1])*x/(2*pi)
            else:
                b = (pi+atan(T[1]))*x/(2*pi)
            return [a,b]

        def determinerZramenee(D, beta, Zl, Zc):
            tgbD = [tan(beta*D[0]),tan(beta*D[1])]
            Zr = [Zc*(Zl+1j*Zc*tgbD[0])/(Zc+1j*Zl*tgbD[0]),
                  Zc*(Zl+1j*Zc*tgbD[1])/(Zc+1j*Zl*tgbD[1])]
            return Zr
        def determinerB(Zr):
            Y =[0, 0]
            Y[0] =1/Zr[0]
            Y[1] = 1/Zr[1]
            B = [Y[0].imag, Y[1].imag]
            return B
        def determinerl(Zc,x,B):
            L = [(-atan(Zc*B[0]))*x/(2*pi),(-atan(Zc*B[1]))*x/(2*pi),
                 (atan(1/(Zc*B[0])))*x/(2*pi),(atan(1/(Zc*B[1])))*x/(2*pi)]
            for i in range(4):
                if L[i]<0:
                    L[i]=L[i]+(x/2)
            return L

        C=299792458
        eps=float(self.ebs.text())
        freq=float(self.frequency.text())*10**6
        resist=float(self.rl.text())
        react=float(self.xl.text())
        ICL=float(self.z0.text())
        perm=eps
        lamda0=C/freq
        lamda=lamda0/sqrt(perm)
        
        beta = 2*pi/lamda
        Zl = complex(resist, react) 
        Zc = ICL
        Rl = Zl.real
        Xl = Zl.imag
        T = determinert(Rl, Xl)
        D = determinerd(T, lamda)
        Zr = determinerZramenee(D, beta, Zl, Zc)
        m=determinerZramenee(D, beta, Zl, Zc)[0]
        n=determinerZramenee(D, beta, Zl, Zc)[1]
        B = determinerB(Zr)
        L = determinerl(Zc, lamda, B)
        l=((round(D[0],4),round(L[0],4)),(round(D[1],4),round(L[1],4)),(round(D[0],4),round(L[2],4)),(round(D[1],4),round(L[3],4)),(m,n))
        h0=((l[0][0],l[2][1]),(l[3][0],l[3][1]))
        h1=((l[2][0],l[0][1]),(l[3][0],l[2]))
        
        return (h0,h1)
        
        
    def court_circuit(self):
        l=self.calcule_charge()
        
        h=l[0]
        a=h[0][0]
        b=h[0][1]
        c=h[1][0]
        d=h[1][1]
        
        
        self.sol1d1.setText("{}".format(a))
        b=h[0][1]
        self.sol1l1.setText("{}".format(b))
        c=h[1][0]
        self.sol2d2.setText("{}".format(c))
        d=h[1][1]
        self.sol2l2.setText("{}".format(d))
    def circuit_ouvert(self):
        l=self.calcule_charge()
        h=l[1]
        a=h[0][0]
        b=h[0][1]
        c=h[1][0]
        d=h[1][1][0]
        
        self.sol1d1.setText("{}".format(a))
        self.sol1l1.setText("{}".format(b))
        self.sol2d2.setText("{}".format(c))
        self.sol2l2.setText("{}".format(d))
    
    


    def retranslateUi(self, projet_HF):
        _translate = QtCore.QCoreApplication.translate
        projet_HF.setWindowTitle(_translate("projet_HF", "Projet HF"))
        self.label.setText(_translate("projet_HF", "                   Impedance matching Calculator"))
        self.label_2.setText(_translate("projet_HF", "<html><head/><body><p><span style=\" font-size:10pt; font-weight:600; font-style:italic; color:#ff652f;\">Parameters :</span></p></body></html>"))
        self.label_3.setText(_translate("projet_HF", "<html><head/><body><p><span style=\" font-size:12pt; font-style:italic; color:#14a76c;\">Load Impedance Zl :</span></p></body></html>"))
        self.rl.setText(_translate("projet_HF", "0.0"))
        self.xl.setText(_translate("projet_HF", "0.0"))
        self.label_4.setText(_translate("projet_HF", "<html><head/><body><p><span style=\" font-size:12pt; color:#14a76c;\">line impedance Z0 :</span></p></body></html>"))
        self.z0.setText(_translate("projet_HF", "0.0"))
        self.label_5.setText(_translate("projet_HF", "<html><head/><body><p><span style=\" font-size:9pt; color:#ff652f;\">Ω</span></p></body></html>"))
        self.shrt.setText(_translate("projet_HF", "short"))
        self.label_6.setText(_translate("projet_HF", "<html><head/><body><p><span style=\" font-size:9pt; color:#ff652f;\">+j</span></p></body></html>"))
        self.label_7.setText(_translate("projet_HF", "<html><head/><body><p><span style=\" font-size:9pt; color:#ff652f;\">Ω</span></p></body></html>"))
        self.label_8.setText(_translate("projet_HF", "<html><head/><body><p><span style=\" font-size:10pt; font-weight:600; font-style:italic; color:#ff652f;\">Results :</span></p></body></html>"))
        self.label_9.setText(_translate("projet_HF", "<html><head/><body><p><span style=\" font-size:12pt; color:#14a76c;\">Solution 1 :</span></p></body></html>"))
        self.label_10.setText(_translate("projet_HF", "<html><head/><body><p><span style=\" font-size:9pt; color:#ff652f;\">L1(m)</span></p></body></html>"))
        self.label_12.setText(_translate("projet_HF", "<html><head/><body><p><span style=\" font-size:12pt; color:#14a76c;\">Solution 2 :</span></p></body></html>"))
        self.label_13.setText(_translate("projet_HF", "<html><head/><body><p><span style=\" font-size:9pt; color:#ff652f;\">L2(m)</span></p></body></html>"))
        self.label_15.setText(_translate("projet_HF", "<html><head/><body><p><span style=\" color:#ff652f;\">D2(m)</span></p></body></html>"))
        self.label_17.setText(_translate("projet_HF", "<html><head/><body><p><span style=\" font-size:9pt; color:#ff652f;\">D1(m)</span></p></body></html>"))
        self.label_21.setText(_translate("projet_HF", "<html><head/><body><p><span style=\" font-size:12pt; color:#00aa7f;\">Frequency:</span></p></body></html>"))
        self.frequency.setText(_translate("projet_HF", "0.0"))
        self.label_22.setText(_translate("projet_HF", "<html><head/><body><p><span style=\" color:#ff652f;\">MHz</span></p></body></html>"))
        self.label_24.setText(_translate("projet_HF", "<html><head/><body><p><span style=\" font-size:12pt; color:#15b070;\">Relative permettivity</span></p></body></html>"))
        self.ebs.setText(_translate("projet_HF", "0.0"))
        self.open.setText(_translate("projet_HF", "open"))
        self.label_26.setText(_translate("projet_HF", "<html><head/><body><p align=\"center\"><span style=\" font-size:12pt; font-weight:600; color:#ff652f;\">select one mode !!</span></p></body></html>"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    projet_HF = QtWidgets.QMainWindow()
    ui = Ui_projet_HF()
    ui.setupUi(projet_HF)
    projet_HF.show()
    sys.exit(app.exec_())


