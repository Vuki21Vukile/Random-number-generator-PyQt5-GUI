
import sys
import random #importing modules (sys & random)

from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import (QApplication, QMainWindow, QLabel, QPushButton) #importing from PyQt5 package


class MainWindow(QMainWindow):  #creating the MainWindow class with QMainWindow as its parent class
    def __init__(self):
        super().__init__()  #calls the initializer for the parent class
        self.x = random.randint(1, 100) #here I am setting my first random number that will apper when we open the app
        self.setGeometry(1400, 450, 500, 500) #setting geometry for my main window(position, height and width of my app)
        self.setWindowTitle("App") #title of the app
        self.title = QLabel("Random number generator", self) #label for my title
        self.button = QPushButton("GENERATE", self) #button and its name
        self.number = QLabel(f"Random number: {self.x}", self) #label for outputing the random number
        self.initui() #calls method initui

        self.setStyleSheet("background-color:#18181B;") #some styling for my background

    def initui(self):       #initui function where all my ui stuff is
        self.title.setGeometry(0,20,500,80)
        self.title.setStyleSheet("""
            font-family: "Segoe UI";
            font-size: 35px;
            font-weight: 600;
            color: #E5EDF8;
        """)
        self.title.setAlignment(Qt.AlignHCenter | Qt.AlignVCenter) #layout allignment of my title

        self.button.setGeometry(150,120,200,100)
        self.button.setStyleSheet("""
                                  font-size: 20px;
                                  background-color:#A3E635;
                                  color:#27272A;
                                  font-family: "Consolas";
                                  """)

        self.button.clicked.connect(self.on_click) #when I click the button I want to call the function on_click

        self.number.setGeometry(125,220,250,150)
        self.number.setStyleSheet("""
            font-family: "Consolas";
            font-size: 25px;
            font-weight: bold;
            color: #38BDF8;
        """)
        self.number.setAlignment(Qt.AlignHCenter | Qt.AlignVCenter)

    def on_click(self):     #function for clicking the button
        self.x = random.randint(1, 100) #random number
        self.number.setText(f"Random number: {self.x}") #here is the output of the random number

def main():     #main function and some boilerplate code for app so it can run
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec_())

if __name__ == "__main__":  #runs the application when this file is executed directly
    main()