import sys
from PyQt5.QtWidgets import *
from PyQt5.QAxContainer import *


class Window(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("PyStock")
        self.setGeometry(300, 300, 300, 200)

        self.kiwoom = QAxWidget("KHOPENAPI.KHOpenAPICtrl.1")

        self.kiwoom.OnEventConnect.connect(self.on_event_connect)

        login_btn = QPushButton("로그인", self)
        login_btn.move(20, 20)
        login_btn.clicked.connect(self.on_login_clicked)

        check_state_btn = QPushButton("접속 체크", self)
        check_state_btn.move(20, 70)
        check_state_btn.clicked.connect(self.on_check_state_clicked)

        self.text_edit = QTextEdit(self)
        self.text_edit.setGeometry(10, 120, 280, 50)
        self.text_edit.setEnabled(False)

    def on_event_connect(self, err_code):
        if err_code == 0:
            self.text_edit.append("로그인 성공")

    def on_login_clicked(self):
        ret = self.kiwoom.dynamicCall("CommConnect()")

    def on_check_state_clicked(self):
        if self.kiwoom.dynamicCall("GetConnectState()") == 0:
            self.statusBar().showMessage("Not connected")
        else:
            self.statusBar().showMessage("Connected")


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = Window()
    window.show()
    app.exec_()
