# Main Window

from Tkinter import *
from ttk import *
from PIL import Image, ImageTk
from tkFileDialog import *
from sys import *
from tkMessageBox import *


class mainwin(Frame):
	def __init__(self, parent, caller):
		Frame.__init__(self, parent)
		self.topwin = parent
		self.caller = caller
		self.topwin.title("Gas Calculator")
		self.topwin.geometry("900x550")
		self.topwin.configure(background="sky blue")
		self.topwin.resizable(width=FALSE, height=FALSE) 
		self.topwin.protocol("WM_DELETE_WINDOW", quit)
	#	self.initialize()
	#def initialize(self):
		