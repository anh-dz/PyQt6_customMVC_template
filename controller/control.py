from PyQt6.QtCore import *
from PyQt6.QtWidgets import *
from PyQt6.QtGui import *

class AppControl:
    def __init__(self, widgets):
        global wgs
        wgs = widgets
        self.initialize_variables()
        self.initialize_ui()
        self.initialize_events()

    def initialize_variables(self):
        pass

    def initialize_ui(self):
        pass

    def initialize_events(self):
        pass