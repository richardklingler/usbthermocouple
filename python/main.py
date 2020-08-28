import sys, time
from PyQt5.QtCore import Qt, QSettings, QSize, QCoreApplication, QRect, QIODevice, pyqtSlot
from PyQt5.QtGui import QPixmap, QPainter, QPen, QCursor, QColor
from PyQt5.QtWidgets import QApplication, QLabel, QMainWindow, QFileDialog, QListWidget, QCheckBox, QProgressBar, QSlider, QPushButton, QFrame, QDialog
from PyQt5 import QtSerialPort
from PIL.ImageQt import ImageQt

from datetime import datetime

from modules.MainWindow import Ui_Logger

ORGANIZATION_NAME = 'Klingler Engineering'
ORGANIZATION_DOMAIN = 'klingler.net'
APPLICATION_NAME = 'USB Thermologger'

LOGGERPID = 21252
LOGGERVID = 4617


class Logger(QMainWindow, Ui_Logger):
    def __init__(self):
        super().__init__()

        self.setupUi(self)

        self.button_connect.pressed.connect(self.connect)
        self.button_date.pressed.connect(self.setDateTime)

        self.counter = 10
        self.old_y1 = 0
        self.old_y2 = 0

        self.show()

        available_ports = QtSerialPort.QSerialPortInfo.availablePorts()
        ports = []
        for port in available_ports:
            pid = port.productIdentifier()
            vid = port.vendorIdentifier()
            print(pid, vid, port.portName())
            if pid == LOGGERPID and vid == LOGGERVID:
                ports.append(port)
                self.combo_ports.addItem(port.portName())

        self.drawAxis()

    def drawAxis(self):
        print("Draw some nice axes here")

        canvas = QPixmap(760, 360)
        canvas.fill(QColor('black'))
        self.plotter.setPixmap(canvas)

        painter = QPainter(self.plotter.pixmap())
        pen = QPen()
        pen.setColor(QColor('green'))
        pen.setWidth(1)
        painter.setPen(pen)

        height = self.plotter.height()
        width = self.plotter.width()

        painter.drawLine(10, 0, 10, height)
        painter.drawLine(0, height - 10, width, height - 10)

        for x in range(1, int(width / 10)):
            painter.drawLine(x * 10, height - 10, x * 10, height - 5)
        for y in range(1, int(height / 10)):
            painter.drawLine(5, y * 10, 10, y * 10)

        painter.end()
        self.plotter.update()


    def set_date(self):
        self.setDateTime()

    @pyqtSlot()
    def setDateTime(self):
        currentDate = datetime.now().strftime("D%y%m%d")
        currentTime = datetime.now().strftime("T%H%M%S")
        print("Sending %s" % currentTime)
        self.serial.write(currentTime.encode())
        time.sleep(1)
        print("Sending %s" % currentDate)
        self.serial.write(currentDate.encode())

    @pyqtSlot()
    def connect(self):
        port = self.combo_ports.currentText()
        print("Connecting to %s" % port)

        self.serial = QtSerialPort.QSerialPort(port, baudRate=QtSerialPort.QSerialPort.Baud9600, readyRead=self.receive)

        if not self.serial.open(QIODevice.ReadWrite):
            self.button_connect.setText('Connect')
        else:
            self.button_connect.setText('Disconnect')
            if(self.check_date.checkState()):
                self.setDateTime()

    @pyqtSlot()
    def receive(self):
        while self.serial.canReadLine():
            text = self.serial.readLine().data().decode()
            text = text.rstrip()
            print(text)
            csv = text.split(',')
            print(len(csv))
            if(len(csv) == 3):
                # Time to draw something
                self.temp1.display(csv[1])
                self.temp2.display(csv[2])
                painter = QPainter(self.plotter.pixmap())

                pen = QPen()
                pen.setColor(QColor('yellow'))
                pen.setWidth(2)
                painter.setPen(pen)
                y = round(self.plotter.height() - float(csv[1]))
                if self.old_y1 == 0:
                    painter.drawPoint(self.counter, y)
                    self.old_y1 = y
                else:
                    painter.drawLine(self.counter - 1, self.old_y1, self.counter, y)
                    self.old_y1 = y

                pen.setColor(QColor('purple'))
                pen.setWidth(2)
                painter.setPen(pen)
                y = round(self.plotter.height() - float(csv[2]))
                if self.old_y2 == 0:
                    painter.drawPoint(self.counter, y)
                    self.old_y2 = y
                else:
                    painter.drawLine(self.counter - 1, self.old_y2, self.counter, y)
                    self.old_y2 = y

                painter.end()
                self.plotter.update()
                self.counter = self.counter + 1
                if self.counter >= 760:
                    self.counter = 10
                    self.drawAxis()

if __name__ == "__main__":
    import sys

    # To ensure that every time you call QSettings not enter the data of your application, 
    # which will be the settings, you can set them globally for all applications
    QCoreApplication.setApplicationName(ORGANIZATION_NAME)
    QCoreApplication.setOrganizationDomain(ORGANIZATION_DOMAIN)
    QCoreApplication.setApplicationName(APPLICATION_NAME)

    settings = QSettings()

    app = QApplication(sys.argv)
    mw = Logger()
    mw.show()
    sys.exit(app.exec())
