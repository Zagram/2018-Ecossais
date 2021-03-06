# -*- coding: utf-8 -*-
"""
Created on Sun Apr  2 20:38:26 2017

@author: toumiab
"""

import sys
from PyQt5 import QtGui, QtCore, QtWidgets,uic
from ecosysteme import Ecosysteme


# l'approche par héritage simple de la classe QMainWindow (même type de notre fenêtre 
# créée avec QT Designer. Nous configurons après l'interface utilisateur 
# dans le constructeur (la méthode init()) de notre classe

class MonAppli(QtWidgets.QMainWindow):
    def __init__(self):
        super().__init__()
        # Configuration de l'interface utilisateur.
        QtWidgets.QMainWindow.__init__(self)
        self.ui = uic.loadUi('interface.ui',self)
        # TO DO
        palette = QtGui.QPalette()
        pixmap = QtGui.QPixmap("arrierPlan.png")
        palette.setBrush(QtGui.QPalette.Background,QtGui.QBrush(pixmap))
        self.setPalette(palette)

        

        y = self.ui.conteneur.height()
        x=  self.ui.conteneur.width()
        self.ecosys = Ecosysteme(60,150,x*y//200, x,y)
        # Connexion entre lles boutons et les méthodes
        self.ui.bouton_pas.clicked.connect(self.un_pas) 
        self.ui.bouton_gen.clicked.connect(self.generer) 
        self.ui.bouton_sim.clicked.connect(self.simuler)
        
        self.timer = QtCore.QTimer()
        self.timer.timeout.connect(self.un_pas)
        
    def un_pas(self) :
#        print("un pas")
#        self.ecosys.unTour()
#        self.ui.centralwidget.update()
         if self.ecosys.nbtour > 0:
            print("Tourné")
            self.ecosys.unTour()
            self.ecosys.nbtour -= 1
            self.ui.centralwidget.update() # nécessaire pour la MAJ de l’IHM
         else:
            self.timer.stop()
            print("Fini")

    def generer(self) :
        print("Genérer")
        self.ecosys=Ecosysteme(60,50,100, self.ui.conteneur.width(),self.ui.conteneur.height())
        self.ui.centralwidget.update()
    
#    def simuler(self):
#        print("Simuler")
#        self.ecosys.simuler()
#        self.ui.centralwidget.update()
            
    def simuler(self):
        self.timer.start(100)
        
    
    def paintEvent(self, e):

        qp = QtGui.QPainter(self.ui.conteneur)
        qp.begin(self)
#        self.drawEcosysteme1(qp)
        self.drawEcosysteme1(qp)
        qp.end()
        
    def drawEcosysteme(self, qp):
        
#        qp.setPen(QtCore.Qt.red)
        for ins in self.ecosys:
             # qp.drawEllipse(ins.x,ins.y, 10,5)  
             if ins.car() == 'F' :
               qp.setPen(QtCore.Qt.green)
               qp.drawRect(ins.x,ins.y, 10,5)
             else:
               qp.setPen(QtCore.Qt.red)
               qp.drawEllipse(ins.x,ins.y, 10,5)

    def drawEcosysteme1(self, qp):
        
        for ins in self.ecosys:
#             ins.dessin(qp)  
             ins.dessinimage(qp)
        nour = self.nouriture()
        for n in nour :
            qp.setPen(QtCore.Qt.red)
            qp.drawEllipse(n[0],n[1], 1,1)
            
        # affichage de la nouriture 
        
    def nouriture(self):
       lstN=[]
       (x,y) =self.ecosys.dims
       for i in range(x) :
           for j in range (y) :
               if self.ecosys.case(i,j)==1:
                   lstN.append((i,j))
         
       return lstN


if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    window = MonAppli()
    window.show()
    app.exec_()
