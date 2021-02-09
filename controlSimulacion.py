import sys
from PyQt5 import QtWidgets
from vistaSimulacion import uiObjetos
from PyQt5 import QtGui
import time
import threading
from PyQt5 import QtCore


class operacionRed(QtWidgets.QDialog):

    def __init__(self):
        super().__init__()
        self.ui=uiObjetos()
        self.ui.setupUi(self)

        self.btn_empezar=QtWidgets.QPushButton("Empezar",self)
        self.btn_empezar.setGeometry(590,10,60,25)
        self.btn_empezar.clicked.connect(self.empezarSimulacion)
        
        self.llenarOpciones()

        
        self.show()
    
    def paintEvent(self,event):
        painter=QtGui.QPainter()
        painter.begin(self)
        self.asociarUsuarios(painter)
        self.asociarSTP(painter)
        painter.end()
    
    def asociarUsuarios(self,painter):
        coordenadas_usr0=self.obtenerCoordenadas(self.ui.listUser[0])
        
        coordenadas_usr50=self.obtenerCoordenadas(self.ui.listUser[50])
        coordenadas_sp0=self.obtenerCoordenadas(self.ui.listSP[0])
        coordenadas_sp1=self.obtenerCoordenadas(self.ui.listSP[1])
        coordenadas_sp2=self.obtenerCoordenadas(self.ui.listSP[2])
        coordenadas_sp3=self.obtenerCoordenadas(self.ui.listSP[3])


        
        for i in range(0,100):
            
            if i<50:

                height=coordenadas_usr0[3]
                width=coordenadas_usr0[2]
                y=coordenadas_usr0[1]
                x1=width
                aumento=(y+height)/2
                x2=coordenadas_sp0[0]
               
                y1=height*i

                if i<25:
                    y2=coordenadas_sp0[1]+aumento
                else:
                    y2=coordenadas_sp1[1]+aumento         
            else:
                height=coordenadas_usr50[3]
                y=coordenadas_usr50[1]
                x1=coordenadas_usr50[0]
                aumento=(y+height)/2
                y1=height*(i-50)

                x2=coordenadas_sp2[0]+coordenadas_sp2[2]
                
                if i<75:
                    y2=coordenadas_sp2[1]+aumento
                else:
                    y2=coordenadas_sp3[1]+aumento  
            
            
            y1=y1+aumento
            painter.drawLine(x1,y1,x2,y2)

    def asociarSTP(self,painter):

        pen = QtGui.QPen(QtCore.Qt.black, 2, QtCore.Qt.SolidLine)
        painter.setPen(pen)
        coord_sp0=self.obtenerCoordenadas(self.ui.listSP[0])
        coord_sp1=self.obtenerCoordenadas(self.ui.listSP[1])
        coord_sp2=self.obtenerCoordenadas(self.ui.listSP[2])
        coord_sp3=self.obtenerCoordenadas(self.ui.listSP[3])

        coord_stp0=self.obtenerCoordenadas(self.ui.listSTP[0])
        coord_stp1=self.obtenerCoordenadas(self.ui.listSTP[1])
        coord_stp2=self.obtenerCoordenadas(self.ui.listSTP[2])
        coord_stp3=self.obtenerCoordenadas(self.ui.listSTP[3])
        coord_stp4=self.obtenerCoordenadas(self.ui.listSTP[4])

        #a
        painter.drawLine(coord_sp0[0],coord_sp0[1],coord_stp0[0],coord_stp0[1])
        painter.drawLine(coord_sp1[0],coord_sp1[1],coord_stp1[0],coord_stp1[1])
        painter.drawLine(coord_sp2[0],coord_sp2[1],coord_stp2[0],coord_stp2[1])
        painter.drawLine(coord_sp3[0],coord_sp3[1],coord_stp3[0],coord_stp3[1])
        #e
        painter.drawLine(coord_sp0[0],coord_sp0[1],coord_sp0[0],coord_sp0[1]-50)
        painter.drawLine(coord_stp2[0],coord_stp2[1],coord_stp2[0],coord_stp2[1]-50)
        painter.drawLine(coord_sp0[0],coord_sp0[1]-50,coord_stp2[0],coord_stp2[1]-50)

        painter.drawLine(coord_sp3[0],coord_sp3[1],coord_sp3[0],coord_sp3[1]+40)
        painter.drawLine(coord_stp1[0],coord_stp1[1],coord_stp1[0],coord_stp1[1]+40)
        painter.drawLine(coord_stp1[0],coord_stp1[1]+40,coord_sp3[0],coord_sp3[1]+40)
       #b
        painter.drawLine(coord_stp0[0],coord_stp0[1],coord_stp2[0],coord_stp2[1])
        painter.drawLine(coord_stp3[0],coord_stp3[1],coord_stp1[0],coord_stp1[1])
        #d
        painter.drawLine(coord_stp1[0],coord_stp1[1],coord_stp4[0],coord_stp4[1])
        painter.drawLine(coord_stp3[0],coord_stp3[1],coord_stp4[0]+coord_stp4[2],coord_stp4[1])

        #c
        pen.setStyle(QtCore.Qt.DashLine)
        painter.setPen(pen)
        painter.drawLine(coord_stp0[0],coord_stp0[1],coord_stp1[0],coord_stp1[1])
        painter.drawLine(coord_stp3[0],coord_stp3[1],coord_stp2[0],coord_stp2[1])

        #linea divisora
        pen.setStyle(QtCore.Qt.DotLine)
        painter.setPen(pen)
        painter.drawLine(600,40,600,700)

    def obtenerCoordenadas(self,objeto):
        height=objeto.geometry().height()
        width=objeto.geometry().width()
        y=objeto.geometry().y()
        x=objeto.geometry().x()
        coordenadas=[x,y,width,height]
        return coordenadas
    
    def empezarSimulacion(self):
        self.visualizarMensajes()
        time.sleep(1)
        thread0=threading.Thread(target=self.rutaMensaje,kwargs={"inicio":0,"final":1})
        thread1=threading.Thread(target=self.rutaMensaje,kwargs={"inicio":1,"final":2})
        thread2=threading.Thread(target=self.rutaMensaje,kwargs={"inicio":2,"final":3})
        thread3=threading.Thread(target=self.rutaMensaje,kwargs={"inicio":3,"final":0})
        
        thread0.start()
        thread1.start()
        thread2.start()
        thread3.start()

        
    def visualizarMensajes(self):
        tamano=len(self.ui.listMensajes)
        for i in range(0,100): 
            if i<50:
                x=60 
                y=i*15
            else:
                x=1100
                y=(i-50)*15
            self.ui.listMensajes[i].setGeometry(QtCore.QRect(x,y,45,15))
        
        for i in range(0,tamano):
            self.ui.listMensajes[i].setVisible(True)
    
    def enviarMensaje(self,ruta,seccion):
        coordenadas_sp0=self.obtenerCoordenadas(self.ui.listSP[0])
        width=coordenadas_sp0[2]
        height=coordenadas_sp0[3]
       
        tamano_ruta=len(ruta)
        
        if seccion==0:
            for i in range(0,tamano_ruta):
                for j in range(0,10):
                    aumento=j*height
                    y=aumento+ruta[i][1]
                    self.ui.listMensajes[j].setGeometry(ruta[i][0],y,width,height)
                
                time.sleep(1.5)
            
            for i in range(0,10):
                self.ui.listMensajes[i].setVisible(False)

        
        elif seccion==1:
            for i in range(0,tamano_ruta):
                for j in range(25,35):
                    aumento=(j-25)*height
                    y=aumento+ruta[i][1]
                    self.ui.listMensajes[j].setGeometry(ruta[i][0],y,width,height)
                
                time.sleep(1.5)
            for i in range(25,35):
                
                self.ui.listMensajes[i].setVisible(False)

        elif seccion==2:
            for i in range(0,tamano_ruta):
                for j in range(50,60):
                    aumento=(j-50)*height
                    y=aumento+ruta[i][1]
                    self.ui.listMensajes[j].setGeometry(ruta[i][0],y,width,height)
                
                time.sleep(1.5)
            for i in range(50,60):
                
                self.ui.listMensajes[i].setVisible(False)
        else:
            for i in range(0,tamano_ruta):
                for j in range(75,85):
                    aumento=(j-75)*height
                    y=aumento+ruta[i][1]
                    self.ui.listMensajes[j].setGeometry(ruta[i][0],y,width,height)
                time.sleep(1.5)
            
            for i in range(75,85):
                
                self.ui.listMensajes[i].setVisible(False)


    def rutaMensaje(self,inicio,final):
        coordenadas_sp0=self.obtenerCoordenadas(self.ui.listSP[0])
        coordenadas_sp1=self.obtenerCoordenadas(self.ui.listSP[1])
        coordenadas_sp2=self.obtenerCoordenadas(self.ui.listSP[2])
        coordenadas_sp3=self.obtenerCoordenadas(self.ui.listSP[3])

        coordenadas_stp0=self.obtenerCoordenadas(self.ui.listSTP[0])
        coordenadas_stp1=self.obtenerCoordenadas(self.ui.listSTP[1])
        coordenadas_stp2=self.obtenerCoordenadas(self.ui.listSTP[2])
        coordenadas_stp3=self.obtenerCoordenadas(self.ui.listSTP[3])

       
        width=coordenadas_sp0[2]
        height=coordenadas_sp0[3]

        x_sp0=coordenadas_sp0[0]+width
        y_sp0=coordenadas_sp0[1]

        x_sp1=coordenadas_sp1[0]+width
        y_sp1=coordenadas_sp1[1]

        x_sp2=coordenadas_sp2[0]+width
        y_sp2=coordenadas_sp2[1]

        x_sp3=coordenadas_sp3[0]+width
        y_sp3=coordenadas_sp3[1]

        x_stp0=coordenadas_stp0[0]+width
        y_stp0=coordenadas_stp0[1]

        x_stp1=coordenadas_stp1[0]+width
        y_stp1=coordenadas_stp1[1]

        x_stp2=coordenadas_stp2[0]+width
        y_stp2=coordenadas_stp2[1]

        x_stp3=coordenadas_stp3[0]+width
        y_stp3=coordenadas_stp3[1]

        a0=[(x_stp0+x_sp0)/2,y_sp0-height]
        a1=[(x_stp1+x_sp1)/2,y_sp1-height]
        a2=[(x_sp2+x_stp2)/2,y_sp2-height]
        a3=[(x_sp3+x_stp1)/2,y_sp3-height]

        b0=[(x_stp2+x_stp0)/2,y_stp0-height]
        b1=[(x_stp3+x_stp1)/2,y_stp1-height]

        c0=[x_stp0-width,y_stp0+height]
        c1=[x_stp2-width,y_stp2+height]
        
        x_d=(x_stp3-x_stp1)/4
        x_d0=(2*x_d)+x_stp1
        x_d1=(x_d/10)+x_stp1
        
        d0=[x_d0,y_stp3+(2*height)]
        d1=[x_d1,y_stp3+(2*height)]
        
        e0=[(x_sp0+x_stp2)/2,y_stp0-(5*height)]
        e1=[(x_stp1+x_sp3)/2,y_stp1+(2*height)]
        ruta=[]
        #desactivar canal
        
        opc_seleccionada=self.ui.cb_opciones.currentIndex()
        codigo_desactivacion=[0,0]
        if opc_seleccionada==1:
            a0=codigo_desactivacion
        elif opc_seleccionada==2:
            a1=codigo_desactivacion
        elif opc_seleccionada==3:
            a2=codigo_desactivacion
        elif opc_seleccionada==4:
            a3=codigo_desactivacion
        elif opc_seleccionada==5:
            b0=codigo_desactivacion
        elif opc_seleccionada==6:
            b1=codigo_desactivacion
        elif opc_seleccionada==7:
            c0=codigo_desactivacion
        elif opc_seleccionada==8:
            c1=codigo_desactivacion
        elif opc_seleccionada==9:
            c0=codigo_desactivacion
        elif opc_seleccionada==10:
            d0=codigo_desactivacion
        elif opc_seleccionada==11:
            d1=codigo_desactivacion
        elif opc_seleccionada==12:
            e0=codigo_desactivacion
        elif opc_seleccionada==13:
            e1=codigo_desactivacion


        #rutas
        #0
        ruta0_1=[[a0,c0,a1],[a0,b0,c1,b1,a1],[e0,c1,b1,a1]]
        ruta0_2=[[a0,b0,a2],[e0,a2]]
        ruta0_3=[[a0,b0,c1,a3],[a0,c0,b1,a3],[e0,c1,a3],[a0,c0,d1,d0,a3]]

        #1
        ruta1_0=[[a1,c0,a0],[a1,b1,c1,b0,a0]]
        ruta1_2=[[a1,c0,b0,a2],[a1,b1,c1,a2],[a1,e1,a3,c1,a2]]
        ruta1_3=[[a1,b1,a3],[a1,c0,b0,c1,a3]]
        #2
        ruta2_0=[[a2,b0,a0],[a2,e0,a0]]
        ruta2_1=[[a2,b0,c0,a1],[a2,c1,b1,a1],[a2,c1,a3,e1,a1]]
        ruta2_3=[[a2,c1,a3],[a2,b0,c0,b1,a3]]
        #3
        ruta3_0=[[a3,c1,b0,a0],[a3,b1,c0,a0],[a3,c1,e0],[a3,d0,d1,c0,a0],[a3,c1,e0,]]
        ruta3_1=[[a3,b1,a1],[a3,c1,b0,c0,a1]]
        ruta3_2=[[a3,c1,a2],[a3,b1,c0,b0,a2]]

       
        ruta=0
        seccion=0

        seccion0=[x_sp0-(5*width),y_sp0-(6*height)]
        seccion1=[x_sp1-(5*width),y_sp1-(6*height)]
        seccion2=[x_sp2+(2*width),y_sp2-(6*height)]
        seccion3=[x_sp3+(2*width),y_sp3-(6*height)]

        if inicio==0:
            
            if final==1:
                
                if codigo_desactivacion not in ruta0_1[0]:
                    ruta=ruta0_1[0][:]

                elif codigo_desactivacion not in ruta0_1[1]:
                    ruta=ruta0_1[1][:]

                else:
                    ruta=ruta0_1[2][:]

                ruta.append(seccion1)

            elif final==2:
                
                if codigo_desactivacion not in ruta0_2[0]:
                    ruta=ruta0_2[0][:]

                elif codigo_desactivacion not in ruta0_2[1]:
                    ruta=ruta0_2[1][:]

                ruta.append(seccion2)
            else:
                #3
                if codigo_desactivacion not in ruta0_3[0]:
                    ruta=ruta0_3[0][:]

                elif codigo_desactivacion not in ruta0_3[1]:
                    ruta=ruta0_3[1][:]
                elif codigo_desactivacion not in ruta0_3[2]:
                    ruta=ruta0_3[2][:]

                else:
                    ruta=ruta0_3[3][:]
                ruta.append(seccion3)
            
        elif inicio==1:
            seccion=1
            if final==0:
                if codigo_desactivacion not in ruta1_0[0]:
                    ruta=ruta1_0[0][:]
                else:
                    ruta=ruta1_0[1][:]
                ruta.append(seccion0)
            elif final==2:
                if codigo_desactivacion not in ruta1_2[0]:
                    ruta=ruta1_2[0][:]
                elif codigo_desactivacion not in ruta1_2[1]:
                    ruta=ruta1_2[1][:]
                else:
                    ruta=ruta1_2[2][:]
                ruta.append(seccion2)
            else:
                #3
                if codigo_desactivacion not in ruta1_3[0]:
                    ruta=ruta1_3[0][:]
                else:
                    ruta=ruta1_3[1][:]
                ruta.append(seccion3)
            

        elif inicio==2:
            seccion=2
            if final==0:
                if codigo_desactivacion not in ruta2_0[0]:
                    ruta=ruta2_0[0][:]
                else:
                    ruta=ruta2_0[1][:]
              
                ruta.append(seccion0)
            elif final==1:
                if codigo_desactivacion not in ruta2_1[0]:
                    ruta=ruta2_1[0][:]
                elif codigo_desactivacion not in ruta2_1[1]:
                    ruta=ruta2_1[1][:]
                else:
                    ruta=ruta2_1[2][:]
                ruta.append(seccion1)
            else:
                #3
                if codigo_desactivacion not in ruta2_3[0]:
                    ruta=ruta2_3[0][:]
                else:
                    ruta=ruta2_3[1][:]
                ruta.append(seccion3)
            
            
        else:
            #3
            seccion=3
            if final==0:
                if codigo_desactivacion not in ruta3_0[0]:
                    ruta=ruta3_0[0][:]
                elif codigo_desactivacion not in ruta3_0[1]:
                    ruta=ruta3_0[1][:]
                elif codigo_desactivacion not in ruta3_0[2]:
                    ruta=ruta3_0[2][:]
                elif codigo_desactivacion not in ruta3_0[3]:
                    ruta=ruta3_0[3][:]
                else:
                    ruta=ruta3_0[4][:]
                ruta.append(seccion0)
            elif final==1:
                if codigo_desactivacion not in ruta3_1[0]:
                    ruta=ruta3_1[0][:]
                else:
                    ruta=ruta3_1[1][:]
                ruta.append(seccion1)
            else:
                #2
                if codigo_desactivacion not in ruta3_2[0]:
                    ruta=ruta3_2[0][:]
                else:
                    ruta=ruta3_2[1][:]
                ruta.append(seccion2)

        
        self.enviarMensaje(ruta,seccion)
        

    def llenarOpciones(self):
        opciones=[" ","a0","a1","a2","a3","b0","b1","c0","c1","d0","d1","e0","e1"]
        self.ui.cb_opciones.addItems(opciones)
    
    



app=QtWidgets.QApplication(sys.argv)
obj=operacionRed()
obj.show()
sys.exit(app.exec_())
