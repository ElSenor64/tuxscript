from os import * # Import bash run abilities

from editor import Editor # Import our classes from other files
from refpane import ReferencePane
from console import Console

import gi # Import GTK Stuff
gi.require_version('Gtk', '3.0')
from gi.repository import Gtk
import sys

class HomeWindow(Gtk.ApplicationWindow):
    def __init__(self):
        # Construct window
        Gtk.Window.__init__(self, title="Tux Script")
        self.set_border_width(10)

    #NOTE placeholder



win = HomeWindow()
win.connect("destroy", Gtk.main_quit)
win.show_all()
Gtk.main()