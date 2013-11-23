import sys, random, math
from PyQt4 import QtGui, QtCore

class Example(QtGui.QMainWindow):
    def __init__(self):
        super(Example, self).__init__()

        self.width = 600
        self.height = 450
        self.x = 300
        self.y = 300
        
        self.initUI()
        
    def initUI(self):
        exitAction = QtGui.QAction('Exit', self)
        exitAction.setShortcut('Ctrl+Q')
        exitAction.setStatusTip('Exit application')
        exitAction.triggered.connect(self.close)

        self.statusBar()

        menubar = self.menuBar()
        fileMenu = menubar.addMenu('&File')
        fileMenu.addAction(exitAction)
        
        self.setGeometry(self.x, self.y, self.width, self.height)
        self.setWindowTitle('TESTING')
        self.show()

    def paintEvent(self, e):
        qp = QtGui.QPainter()
        qp.begin(self)
        self.drawLines(qp)
        qp.end()
        
    def drawLines(self, qp):
        n = (self.width-40)/(1+math.sin(math.pi/6))
        n2 = (self.height-40)/(1+math.cos(math.pi/6))
        print(n,n2)
        # h = n(1+math.sin30)
        # w = n(1+math.cos30)

        qp.drawLine(20, 40, self.width-20, 40) # top line
        qp.drawLine(20, self.height-20, self.width-20, self.height-20) # bottom line
        qp.drawLine(20, 40, 20, self.height-20) # left line
        qp.drawLine(self.width-20, 40, self.width-20, self.height-20) # right line

    def close(self, event):
        reply = QtGui.QMessageBox.question(self, 'Message',
            "Are you sure to quit?", QtGui.QMessageBox.Yes | 
            QtGui.QMessageBox.No, QtGui.QMessageBox.No)

        if reply == QtGui.QMessageBox.Yes:
            QtCore.QCoreApplication.instance().quit()
        
def main():
    app = QtGui.QApplication(sys.argv)
    ex = Example()
    sys.exit(app.exec_())


if __name__ == '__main__':
    main()