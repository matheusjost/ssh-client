import os

# IMPORT QTCORE
from qt_core import *

class PyQTextEdit(QTextEdit):
    def __init__(
            self,
            text = "",
            text_color = "#000000",
            is_readonly = True,
            height = 500,
            placeholder = ""
    ):
        super().__init__()

        # SET DEFAULT PARAMETERS
        self.setText(text)
        self.setReadOnly(is_readonly)
        self.setMaximumHeight(height)
        self.setMinimumHeight(height)
        self.setPlaceholderText(placeholder)

        # CUSTOM PARAMETERS
        self.text_color = text_color

        self.set_style(
            text_color = self.text_color,
        )

    def set_style(
        self,
        text_padding = 15,
        text_color = "#000000",
    ):
        style = f"""
        QTextEdit {{
            color: {text_color};
            font: 700 9pt 'Segoe UI';
        }}
        """

        self.setStyleSheet(style)