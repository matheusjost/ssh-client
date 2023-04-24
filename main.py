# IMPORT MODULES
import sys
import os

# IMPORT QTCORE
from qt_core import *

# IMPORT MAIN WINDOW
from gui.windows.main_window.ui_main_window import *

# IMPORT SSH CLASS FROM APP
from app.app import SSH

# MAIN WINDOW
class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        # SET WINDOW TITLE
        self.setWindowTitle("SSH CLIENT")

        # SETUP MAIN WINDOW
        self.ui = UI_MainWindow()
        self.ui.setup_ui(self)

        # SETUP BUTTON OK
        self.ui.ssh_input_top_btn.clicked.connect(self.exec_button)

        # SHOW APP
        self.show()

    def exec_button(self):
        ip = self.ui.ssh_input_top_ip.text().split(';')
        port = self.ui.ssh_input_top_port.text().split(';')
        cmd = self.ui.ssh_input_top_cmd.text()
        user = self.ui.top_bar_user.text()
        pw = self.ui.top_bar_pw.text()

        for i, j in zip(ip, port):
            ssh = SSH(i, int(j), user, pw)
            output = ssh.exec_cmd(cmd)
            self.ui.ssh_output_text.append("-----------------\n" + output)

if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = MainWindow()
    sys.exit(app.exec())