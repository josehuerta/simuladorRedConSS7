from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5 import QtGui


class uiObjetos():
    
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(1200, 720)
       
        self.listUser=[]
        self.listSP=[]
        self.listSTP=[]
        self.listMensajes=[]

        self.crearUsuarios(Dialog)
        self.crearSPs(Dialog)
        self.crearSTPs(Dialog)
        self.crearMensajes(Dialog)

        self.cb_opciones=QtWidgets.QComboBox(Dialog)
        self.lbl_Desactivar=QtWidgets.QLabel(Dialog)

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Simulador de Redes"))
        ancho=45
        alto=15
        self.cb_opciones.setGeometry(QtCore.QRect(400,10,ancho,alto))
        self.lbl_Desactivar.setGeometry(QtCore.QRect(320,10,ancho+15,alto))
        self.lbl_Desactivar.setText("Desactivar:")

        #posicionando usuarios
        self.posicionarUsuarios(_translate,ancho,alto)
        #posicionando SP's
        self.posicionarSP(_translate,ancho,alto)   
        self.posicionarMensajes(_translate,ancho,alto)

    def crearUsuarios(self,Dialog):

        for i in range(0,100):
            nombre="lbl_usr"+str(i)
            nombre=QtWidgets.QLabel(Dialog)
            self.listUser.append(nombre)

    def crearSPs(self,Dialog):
        for i in range(0,4):
            nombre="lbl_sp"+str(i)
            nombre=QtWidgets.QLabel(Dialog)
            self.listSP.append(nombre)
    
    def crearSTPs(self,Dialog):
        for i in range(0,5):
            nombre="lbl_stp"+str(i)
            nombre=QtWidgets.QLabel(Dialog)
            self.listSTP.append(nombre)
    def crearMensajes(self,Dialog):
        for i in range(0,100):
            nombre="lbl_msg"+str(i)
            nombre=QtWidgets.QLabel(Dialog)
            self.listMensajes.append(nombre)

    def posicionarUsuarios(self,_translate,width,height):
        for i in range(0,100):
                
            if i<50:
                x=10 
                y=i*15
            else:
                x=1150
                y=(i-50)*15
            
            self.listUser[i].setGeometry(QtCore.QRect(x,y,width,height))
            self.listUser[i].setObjectName(f"lbl_user{str(i)}")
            self.listUser[i].setText(_translate("Dialog", f"usr_{i}"))
    
    def posicionarSP(self,_translate,width,height):
        for i in range(0,4):
            if i<2:
                x=300
                x1=500
                y=200+(300*i)
            else: 
                x=900
                x1=700
                y=200+(300*i)-600

            self.listSP[i].setGeometry(QtCore.QRect(x,y, width,height))
            self.listSP[i].setObjectName(f"lbl_sp{str(i)}")
            self.listSP[i].setText(_translate("Dialog", f"SP_{i}"))

            self.listSTP[i].setGeometry(QtCore.QRect(x1,y, width, height))
            self.listSTP[i].setObjectName(f"lbl_stp{str(i)}")
            self.listSTP[i].setText(_translate("Dialog", f"STP_{i}"))
        
        self.listSTP[4].setGeometry(QtCore.QRect(580,620, width, height))
        self.listSTP[4].setObjectName(f"lbl_stp{4}")
        self.listSTP[4].setText(_translate("Dialog", f"STP_{4}"))

    def posicionarMensajes(self,_translate,width,height):
        
        for i in range(0,100):
                
            if i<50:
                x=60 
                y=i*15
            else:
                x=1100
                y=(i-50)*15
            
            self.listMensajes[i].setGeometry(QtCore.QRect(x,y,width,height))
            self.listMensajes[i].setObjectName(f"lbl_msg{str(i)}")
            self.listMensajes[i].setText(_translate("Dialog", f"msg_{i}"))
            self.listMensajes[i].setVisible(False)



    
    


      
    
    


        
            

            
        
