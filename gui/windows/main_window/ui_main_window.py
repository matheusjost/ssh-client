
# IMPORT QT CORE
from qt_core import *

# IMPORT THE SSH OUTPUT LABEL
from gui.widgets.py_ssh_text import PyQTextEdit
from gui.widgets.py_ssh_line import PyQLineEdit


# MAIN WINDOW
class UI_MainWindow(object):
    def setup_ui(self, parent):
        if not parent.objectName():
            parent.setObjectName("MainWindow")
        
        # SET INITIAL PARAMETERS
        # ////////////////////////////
        parent.resize(1200, 600)
        parent.setMinimumSize(1200, 600)

        # SET CENTRAL WIDGET
        # ////////////////////////////
        self.central_frame = QFrame()

        # CREATE MAIN LAYOUT
        # ////////////////////////////
        self.main_layout = QHBoxLayout(self.central_frame)
        self.main_layout.setContentsMargins(0,0,0,0)
        self.main_layout.setSpacing(0)

        # CONTENT
        # ////////////////////////////
        self.content = QFrame()
        self.content.setStyleSheet("background-color: #e3e4de")

        # content layout
        self.content_layout = QVBoxLayout(self.content)
        self.content_layout.setContentsMargins(0,0,0,0)
        self.content_layout.setSpacing(0)

        # TOP BAR
        # ////////////////////////////
        self.top_bar = QFrame()
        self.top_bar.setMinimumHeight(30)
        self.top_bar.setMaximumHeight(30)
        self.top_bar.setStyleSheet("background-color: #a3a693; color: white")

        self.top_bar_layout = QHBoxLayout(self.top_bar)
        self.top_bar_layout.setContentsMargins(10,0,10,0)

        self.top_bar_user = PyQLineEdit(is_readonly=False, height=25, placeholder="USER")
        self.top_bar_user.setStyleSheet("font: 700 9pt 'Segoe UI'")
        self.top_bar_pw = PyQLineEdit(is_readonly=False, height=25, placeholder="PASS", is_pass=True)
        self.top_bar_pw.setStyleSheet("font: 700 9pt 'Segoe UI'")

        self.top_spacer = QSpacerItem(20,20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.top_right_label = QLabel("| v 1.0.0")
        self.top_right_label.setStyleSheet("font: 700 9pt 'Segoe UI'")

         # add to layout
        self.top_bar_layout.addWidget(self.top_bar_user)
        self.top_bar_layout.addWidget(self.top_bar_pw)
        self.top_bar_layout.addItem(self.top_spacer)
        self.top_bar_layout.addWidget(self.top_right_label)   
        
        # SSH MAIN MENU
        # ////////////////////////////
        self.ssh_frame = QFrame()
        self.ssh_layout = QVBoxLayout(self.ssh_frame)

        # inputs
        self.ssh_input_top_frame = QFrame()

        self.ssh_input_top_ip = PyQLineEdit(is_readonly=False, height=25, placeholder="IP")
        self.ssh_input_top_port = PyQLineEdit(is_readonly=False, height=25, placeholder="SSH PORT")
        self.ssh_input_top_cmd = PyQLineEdit(is_readonly=False, height=25, placeholder="COMMAND")
        self.ssh_input_top_btn = QPushButton("OK")
        
        self.ssh_input_top_layout = QHBoxLayout(self.ssh_input_top_frame)
        self.ssh_input_top_layout.addWidget(self.ssh_input_top_ip)
        self.ssh_input_top_layout.addWidget(self.ssh_input_top_port)
        self.ssh_input_top_layout.addWidget(self.ssh_input_top_cmd)
        self.ssh_input_top_layout.addWidget(self.ssh_input_top_btn)

        # output paramiko text
        self.ssh_output_frame = QFrame()
        self.ssh_output_text = PyQTextEdit(text= "",is_readonly=True)
        self.ssh_output_layout = QHBoxLayout(self.ssh_output_frame)
        self.ssh_output_layout.addWidget(self.ssh_output_text)

        # add to layout
        self.ssh_layout.addWidget(self.ssh_input_top_frame)
        self.ssh_layout.addWidget(self.ssh_output_frame)

        # BOTTOM BAR
        # ////////////////////////////
        self.bottom_bar = QFrame()
        self.bottom_bar.setMinimumHeight(30)
        self.bottom_bar.setMaximumHeight(30)
        self.bottom_bar.setStyleSheet("background-color: #a3a693; color: white")       
        self.bottom_bar_layout = QHBoxLayout(self.bottom_bar)
        self.bottom_bar_layout.setContentsMargins(10,0,10,0)

        # left label
        self.bottom_left_label = QLabel("Criado por: Matheus Jost")

        # bottom spacer
        self.bottom_spacer = QSpacerItem(20,20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        # right label
        self.bottom_right_label = QLabel("2023")

        # add to layout
        self.bottom_bar_layout.addWidget(self.bottom_left_label)
        self.bottom_bar_layout.addItem(self.bottom_spacer)
        self.bottom_bar_layout.addWidget(self.bottom_right_label)    

        # add content to layout
        self.content_layout.addWidget(self.top_bar)
        self.content_layout.addWidget(self.ssh_frame)
        self.content_layout.addWidget(self.bottom_bar)

        # ADD WIDGETS TO APP
        # ////////////////////////////
        self.main_layout.addWidget(self.content)

        # SET CENTRAL WIDGET
        # ////////////////////////////
        parent.setCentralWidget(self.central_frame)