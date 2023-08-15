import sys
import os
from PyQt5.QtWidgets import *
from PyQt5 import *



def przyciskRobic():
    print("test1")



def window():



    app=QApplication(sys.argv)
    widget=QWidget()

    label1=QLabel(widget)
    #labell.setText("labelTestt")
    label1.setText("<p style=' font-size:50px;'>Duzy tekst</p>")
    label1.setText("<img src='pies.jpeg' alt='' width='500' height='600'>")

    BPrzycisk = QPushButton(widget)
    BPrzycisk.setEnabled(True)
    BPrzycisk.setText("Przycisk")
    BPrzycisk.move(100,80)
    BPrzycisk.clicked.connect(przyciskRobic)

    
    

    widget.setGeometry(50,50,320,320)
    widget.show()
    sys.exit(app.exec_())

if __name__=="__main__":
    window()

