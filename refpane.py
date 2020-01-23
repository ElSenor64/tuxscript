from os import * # Import bash run abilities

import gi # Import GTK Stuff
gi.require_version('Gtk', '3.0')
from gi.repository import Gtk
import sys

# The reference pane allows users to click and drag 
# code snippets into their script.
class ReferencePane():
    def __init__(self):
        #NOTE placeholder