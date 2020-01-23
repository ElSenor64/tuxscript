from os import * # Import bash run abilities

import gi # Import GTK Stuff
gi.require_version('Gtk', '3.0')
from gi.repository import Gtk
import sys

# The Editor is in charge of the file management. It must save,
# auto-update, and by first publish must have full bash color 
# support. Importing gedit will be fine if it can be made to 
# integrate well with the rest of the app.
class Editor():
    def __init__():
        #NOTE placeholder