from os import * # Import bash run abilities

import gi # Import GTK Stuff
gi.require_version('Gtk', '3.0')
from gi.repository import Gtk
import sys

# The console allows one to view the debugging output 
# and add commands to the end of the their script via 
# text input.
class Console(): 
    def __init__(self):
        #NOTE placeholder