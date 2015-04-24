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
		self.initialize()
def initialize(self):
		self.topFrameStyle = Style()
		self.topFrameStyle.configure("top.TFrame", background="white")
		self.topFrame = Frame(self.topwin, padding = "20 20 20 20", style = "desc.TFrame")
		#self.topFrame.grid(row = 0, column = 0, rowspan = 3, columnspan = 3, padx = 5, pady = 5)
		self.topFrame.pack(side = TOP)