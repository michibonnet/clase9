from PyQt5.QtGui import QPixmap
from PyQt5.QtWidgets import QMainWindow, QDesktopWidget, QLabel, QHBoxLayout, QApplication
from PyQt5 import QtGui
import sys
class Ventana1(QMainWindow):

    # Hacer el metodo de construcion de la ventana:
    def __init__(self, parent=None):
        super(Ventana1, self).__init__(parent)

        # poner el titulo:
        self.setWindowTitle("Formularios de registros")

        # poner el icono:
        self.setWindowIcon(QtGui.QIcon("imagenes/Fondo cutecore.pn"))

        # Establecer las propiedades de ancho y alto:
        self.ancho = 1000
        self.alto = 700

        # establecer el tamaño de la ventana
        self.resize(self.ancho, self.alto)

        # hacer que la ventana se vea en el centro
        self.pantalla = self.frameGeometry()
        self.centro = QDesktopWidget().availableGeometry().center()
        self.pantalla.moveCenter(self.centro)
        self.move(self.pantalla.topLeft())

        # fijar el ancho y el alto de la ventana:
        self.setFixedWidth(self.ancho)
        self.setFixedWidth(self.alto)

        # establecemos el fondo principal:
        self.fondo = QLabel(self)

        # definimos la imagen de fondo:
        self.imagenFondo = QPixmap("imagenes/__MY IDOL BOYFRIEND__ KIM TAEHYUNG FF__ X BTS__✔ - ~☆ONE☆_.png")

        # agregamos la imagen en el fondo:
        self.fondo.setPixmap(self.imagenFondo)

        # establecer el modo para escalar la imagen:
        self.fondo.setScaledContents(True)

        # el tamaño de la imagen se adapta al tamaño de su contenedor
        self.resize(self.imagenFondo.width(), self.imagenFondo.height())

        # establecemos la ventana fondo como la ventana control
        self.setCentralWidget(self.fondo)

        # establecemos la distribucion de los elementos en layout horizontal:
        self.horizontal = QHBoxLayout()

        # le ponemos las margenes
        self.horizontal.setContentsMargins(30, 30, 30, 30)



        # ---------  ojo IMPORTANTE PONER AL FINAL  ---------

        # indicamos que el layout principak del fondo es horizontal:
        self.fondo.setLayout(self.horizontal)

if __name__ == "__main__":

    app = QApplication(sys.argv)

    ventana1 = Ventana1()

    ventana1.show()

    sys.exit(app.exec_())








