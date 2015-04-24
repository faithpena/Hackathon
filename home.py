# Home Window

from Tkinter import *
from ttk import *
from PIL import Image, ImageTk
from tkFileDialog import *
from sys import *
from tkMessageBox import *
from mainwin import *


class home(Frame):
   def __init__(self, topwin):
      Frame.__init__(self, topwin)
      self.topwin = topwin
      self.topwin.title("Gas Calculator")
      self.topwin.geometry("900x550")
      self.topwin.configure(background="sky blue")
      self.topwin.resizable(width=FALSE, height=FALSE) 
      self.topwin.protocol("WM_DELETE_WINDOW", quit)
      self.initialize()
   def initialize(self):
      im = Image.open('homebanner.jpg')
      im = im.resize((896, 50))
      tkimage = ImageTk.PhotoImage(im)
      self.banner = Label(self.topwin, image=tkimage)
      self.banner.image = tkimage
      self.banner.grid(row=0, column=0, columnspan=4)
      
      self.descFrameStyle = Style()
      self.descFrameStyle.configure("desc.TFrame", background="dodger blue")
      self.descFrame = Frame(self.topwin, padding = "20 20 20 20", style = "desc.TFrame")
      self.descFrame.grid(row = 1, column = 0, rowspan = 6, padx = 5)

      self.logoFrameStyle = Style()
      self.logoFrameStyle.configure("logo.TFrame", background="dodger blue", relief = RIDGE)
      self.logoFrame = Frame(self.topwin, padding = "60 20 60 20", style = "logo.TFrame")
      self.logoFrame.grid(row = 2, column = 3, rowspan = 5, columnspan = 3, padx = 50, pady = 65)
      im1 = Image.open('logo.jpg')
      im1 = im1.resize((150, 150))
      tkimage1 = ImageTk.PhotoImage(im1)
      self.logo = Label(self.logoFrame, image=tkimage1)
      self.logo.image = tkimage1
      self.logo.grid(row = 2, column = 3, rowspan = 2, pady = 30)
      self.startButton = Button(self.logoFrame, text = "Start!", width = 25, command = self.startClick)
      self.startButton.grid(row = 5, column = 3, pady = 30)
   def startClick(self):
      self.top = Toplevel()
      self.topwin.withdraw()
      mainwin(self.top, self.topwin)

	  
