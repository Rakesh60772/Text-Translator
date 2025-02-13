from PyQt5.QtWidgets import QApplication, QFileDialog, QPushButton, QGroupBox, QVBoxLayout, QHBoxLayout,QDialog, QSplitter,QTextEdit
import sys                  
from PyQt5.QtGui import QFont
from PyQt5.QtCore import Qt
from googletrans import Translator
import pyttsx3

class Window(QDialog):
    def __init__(self):
        super().__init__()
        self.title = "Trans-Voice-Saver "
        self.left = 400
        self.top = 300
        self.width = 1000
        self.height = 400
        
        self.store =[]
        self.store2 =[]
        self.pre = -1

        self.InitWindow()
        self.show()

    def InitWindow(self):
        self.setWindowTitle(self.title)
        self.setGeometry(self.left, self.top, self.width, self.height )
        self.setStyleSheet("background-color:silver")

        self.CreateButton()
        vbox = QVBoxLayout()

        font = QFont()
        font.setPointSize(12)

        splitter1 = QSplitter(Qt.Horizontal)

        # Add some widgets to the splitter
        self.textEdit1 = QTextEdit("")
        self.textEdit1.setPlaceholderText("Write some text here:")
        self.textEdit1.setStyleSheet("background-color:white")
        self.textEdit1.setFont(font)
        self.textEdit2 = QTextEdit("")
        self.textEdit2.setStyleSheet("background-color:white")
        self.textEdit2.setFont(font)

        splitter1.addWidget(self.textEdit1)
        splitter1.addWidget(self.textEdit2)
        vbox.addWidget(splitter1)
        
        vbox.addWidget(self.groupBox)
        self.setLayout(vbox)
        self.translator = Translator()

    def CreateButton(self):
        self.groupBox =QGroupBox()
        groupBox2 = QGroupBox()
        hbox = QHBoxLayout()
        self.groupBox.setStyleSheet("background-color:gray")
        vboxlayout = QVBoxLayout()

        font = QFont()
        font.setPointSize(12)

        button1 = QPushButton("Translate")
        button1.clicked.connect(self.translate_text)
        button1.setStyleSheet("background-color:lightgreen")
        button1.setFont(font)
        button1.setMinimumHeight(40)
        vboxlayout.addWidget(button1)

        button2 = QPushButton("Text To Voice")
        button2.clicked.connect(self.text_to_speech)
        button2.setStyleSheet("background-color:lightgreen")
        button2.setFont(font)
        button2.setMinimumHeight(40)
        vboxlayout.addWidget(button2)

        button3 = QPushButton("Save Text")
        button3.clicked.connect(self.save_text)
        button3.setStyleSheet("background-color:lightgreen")
        button3.setFont(font)
        button3.setMinimumHeight(40)
        vboxlayout.addWidget(button3)

        button4 = QPushButton("Previous")
        button4.clicked.connect(self.previous_text)
        button4.setStyleSheet("background-color:lightgreen")
        button4.setFont(font)
        hbox.addWidget(button4)

        button5 = QPushButton("Next")
        button5.clicked.connect(self.next_text)
        button5.setStyleSheet("background-color:lightgreen")
        button5.setFont(font)
        hbox.addWidget(button5)

        groupBox2.setLayout(hbox)
        vboxlayout.addWidget(groupBox2)


        self.groupBox.setLayout(vboxlayout)

    def translate_text(self):
        text = self.textEdit1.toPlainText()
        if text:
            self.store.append(text)
            self.pre = self.pre + 1
            self.temp = self.pre
            translation = self.translator.translate(text, dest='hi')
            self.textEdit2.setText(translation.text)
            text2 = self.textEdit2.toPlainText()
            self.store2.append(text2)

    def previous_text(self):
        if not self.store:
            self.textEdit1.setPlaceholderText("Write some text here:")
        
        if self.pre<0:
                self.textEdit1.setPlaceholderText("no history")
                self.pre = self.temp

        else:
            self.textEdit1.setText("")
            self.pre = self.pre - 1
            pre_text = self.store[self.pre]
            self.textEdit1.setText(pre_text)

            pre_text2 = self.store2[self.pre]
            self.textEdit2.setText(pre_text2)

    def next_text(self):
        if not self.store:
            self.textEdit1.setPlaceholderText("Write some text here:")
        
        if self.pre==self.temp:
                self.textEdit1.setPlaceholderText("next word")

        else:
            self.textEdit1.setText("")
            self.pre = self.pre + 1
            pre_text = self.store[self.pre]
            self.textEdit1.setText(pre_text)

            pre_text2 = self.store2[self.pre]
            self.textEdit2.setText(pre_text2)

    def text_to_speech(self):
         speakOut = pyttsx3.init()
         text = self.textEdit1.toPlainText()
         speakOut.say(text)
         speakOut.runAndWait()

    def save_text(self):
         
         options = QFileDialog.Options()
         options |= QFileDialog.DontUseNativeDialog  # Example option
         fileName, _ = QFileDialog.getSaveFileName(self, "Save File", "", "Text Files (*.txt);;All Files(*)", options=options)

         if fileName:
              with open(fileName,'w',encoding='utf-8') as file:
                   file.write(self.textEdit1.toPlainText() + "\n")
                   file.write(self.textEdit2.toPlainText())



if __name__ =="__main__":
    App = QApplication(sys.argv)
    window = Window()
    sys.exit(App.exec())
