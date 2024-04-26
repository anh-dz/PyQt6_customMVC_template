#!/usr/bin/env python3

import sys
from PyQt6.QtWidgets import QApplication
from view import *
from controller import *
# import os
# os.environ["QT_FONT_DPI"] = "72" # DPI MACOS
# os.environ["QT_FONT_DPI"] = "96" # DPI WINDOWS
# os.environ["QT_AUTO_SCREEN_SCALE_FACTOR"] = "1"

def main():
    app = QApplication(sys.argv)
    main_window = ViewControl()
    model_obj = AppControl(main_window.ui)
    main_window.show()
    app.exec()

if __name__ == '__main__':
    main()