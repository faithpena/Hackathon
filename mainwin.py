# Main Window

from Tkinter import *
from ttk import *
from PIL import Image, ImageTk
from tkFileDialog import *
from sys import *
from tkMessageBox import *


class mainwin(Frame):
	def __init__(self, parent, caller, c):
		Frame.__init__(self, parent)
		self.topwin = parent
		self.caller = caller
		self.c = c
		self.topwin.title("Gas Calculator")
		self.topwin.geometry("900x550")
		self.topwin.configure(background="sky blue")
		self.topwin.resizable(width=FALSE, height=FALSE) 
		self.topwin.protocol("WM_DELETE_WINDOW", quit)
		self.engineTypes = ["Intake Stroke", "Compression Stroke", "Combustion Stroke", "Exhaust Stroke"]
		self.gasTypes = ["Gasoline", "Diesel", "Petrol", "Compressed Natural Gas", "Ethanol"]
		self.cars = self.c.get_cars
		self.initialize()
	def initialize(self):
		self.topFrameStyle = Style()
		self.topFrameStyle.configure("top.TFrame", background = "white")
		self.topFrame = Frame(self.topwin, padding = "20 20 20 0", style = "desc.TFrame")
		self.topFrame.pack(fill = X)
		self.topLabelStyle = Style()
		self.topLabelStyle.configure("top.TLabel", background = "white", foreground = "black", font = "Consolas", height = 20, anchor = CENTER)
		self.topLabel = Label(self.topFrame, text = "[ Some text here ]", padding = "20 20 20 10", style = "top.TLabel")
		self.topLabel.pack(fill = X)
		self.topLabel1 = Label(self.topFrame, text = "More text. More text. More text. More text.", padding = "20 5 20 20", style = "top.TLabel")
		self.topLabel1.pack(fill = X)
		
		self.borderStyle = Style()
		self.borderStyle.configure("border.TLabel", height = 2, background = "dodger blue")
		self.border = Label(self.topwin, style = "border.TLabel")
		self.border.pack(fill = X)
		
		self.addStyle = Style()
		self.addStyle.configure("add.TLabel", height = 5, background = "light yellow")
		self.distStyle = Style()
		self.distStyle.configure("dist.TLabel", height = 5, background = "light green")
		self.budgetStyle = Style()
		self.budgetStyle.configure("budget.TLabel", height = 5, background = "light pink")
		
		self.addFrameStyle = Style()
		self.addFrameStyle.configure("add.TFrame", background = "light yellow")
		self.addFrame = Frame(self.topwin, style = "add.TFrame", padding = "30 50 50 50")
		self.addFrame.pack(side = LEFT, fill = BOTH)
		self.addLabel = Label(self.addFrame, text = "ADD CAR", style = "add.TLabel")
		self.addLabel.pack(pady = 25)

		self.nameFrame = Frame(self.addFrame, style = "add.TFrame")
		self.nameFrame.pack()
		self.nameLabel = Label(self.nameFrame, text = "Car Name", style = "add.TLabel")
		self.nameLabel.pack(side = LEFT, padx = 15, pady = 5)
		self.nameEntry = Entry(self.nameFrame)
		self.nameEntry.pack(side = LEFT, pady = 5)
		self.cylinderFrame = Frame(self.addFrame, style = "add.TFrame")
		self.cylinderFrame.pack()
		self.cylinderLabel = Label(self.cylinderFrame, text = "Cylinder", style = "add.TLabel")
		self.cylinderLabel.pack(side = LEFT, padx = 20, pady = 5)
		self.cylinderEntry = Entry(self.cylinderFrame)
		self.cylinderEntry.pack(side = LEFT, pady = 5)
		self.torqueFrame = Frame(self.addFrame, style = "add.TFrame")
		self.torqueFrame.pack()
		self.torqueLabel = Label(self.torqueFrame, text = "Torque", style = "add.TLabel")
		self.torqueLabel.pack(side = LEFT, padx = 22, pady = 5)
		self.torqueEntry = Entry(self.torqueFrame)
		self.torqueEntry.pack(side = LEFT, pady = 5)
		self.horseFrame = Frame(self.addFrame, style = "add.TFrame")
		self.horseFrame.pack()
		self.horseLabel = Label(self.horseFrame, text = "Horsepower", style = "add.TLabel")
		self.horseLabel.pack(side = LEFT, padx = 10, pady = 5)
		self.horseEntry = Entry(self.horseFrame)
		self.horseEntry.pack(side = LEFT, pady = 5)
		self.weightFrame = Frame(self.addFrame, style = "add.TFrame")
		self.weightFrame.pack()
		self.weightLabel = Label(self.weightFrame, text = "Car Weight", style = "add.TLabel")
		self.weightLabel.pack(side = LEFT, padx = 12, pady = 5)
		self.weightEntry = Entry(self.weightFrame)
		self.weightEntry.pack(side = LEFT, pady = 5)
		self.engineFrame = Frame(self.addFrame, style = "add.TFrame")
		self.engineFrame.pack()
		self.engineLabel = Label(self.engineFrame, text = "Engine Type", style = "add.TLabel")
		self.engineLabel.pack(side = LEFT, padx = 10, pady = 5)
		self.eType = StringVar()
		self.eType.set(self.engineTypes[0])
		self.engineCombo = Combobox(self.engineFrame, textvariable=self.eType, values=self.engineTypes, width = 17)
		self.engineCombo.pack(side = LEFT, pady = 5)
		self.addButton = Button(self.addFrame, text = "Add Car!", command = self.addButtonClick)
		self.addButton.pack(pady = 10)
		
		self.distFrameStyle = Style()
		self.distFrameStyle.configure("dist.TFrame", background = "light green")
		self.distFrame = Frame(self.topwin, style = "dist.TFrame", padding = "30 50 50 50")
		self.distFrame.pack(side = LEFT, fill = BOTH)
		self.distLabel = Label(self.distFrame, text = "DISTANCE MODE", style = "dist.TLabel")
		self.distLabel.pack(pady = 25)
		
		self.distanceFrame = Frame(self.distFrame, style = "dist.TFrame")
		self.distanceFrame.pack()
		self.carNameFrame = Frame(self.distanceFrame, style = "dist.TFrame")
		self.carNameFrame.pack()
		self.carNameLabel = Label(self.carNameFrame, text = "Car Name", style = "dist.TLabel")
		self.carNameLabel.pack(side = LEFT, padx = 23, pady = 5)
		self.carName = StringVar()
		#self.carName.set(self.cars[0])
		self.carNameCombo = Combobox(self.carNameFrame, textvariable=self.carName, values=self.cars, width = 20)
		self.carNameCombo.pack(side = LEFT, pady = 5)
		self.distanceLabel = Label(self.distanceFrame, text = "Distance", style = "dist.TLabel")
		self.distanceLabel.pack(side = LEFT, padx = 23, pady = 5)
		self.distanceEntry = Entry(self.distanceFrame, width = 22, state = DISABLED)
		self.distanceEntry.pack(side = LEFT, pady = 5)
		self.gasFrame = Frame(self.distFrame, style = "dist.TFrame")
		self.gasFrame.pack()
		self.gasLabel = Label(self.gasFrame, text = "Gas Type", style = "dist.TLabel")
		self.gasLabel.pack(side = LEFT, padx = 22, pady = 5)
		self.gType = StringVar()
		self.gType.set(self.gasTypes[0])
		self.gasCombo = Combobox(self.gasFrame, textvariable=self.gType, values=self.gasTypes, width = 19, state = DISABLED)
		self.gasCombo.pack(side = LEFT, pady = 5)
		self.distButton = Button(self.distFrame, text = "Calculate!", state = DISABLED, command = self.distButtonClick)
		self.distButton.pack(pady = 25)
		
		self.budgetFrameStyle = Style()
		self.budgetFrameStyle.configure("budget.TFrame", background = "light pink")
		self.budgetFrame = Frame(self.topwin, style = "budget.TFrame", padding = "40 50 50 50")
		self.budgetFrame.pack(side = LEFT, fill = BOTH)
		self.budgetLabel = Label(self.budgetFrame, text = "BUDGET MODE", style = "budget.TLabel")
		self.budgetLabel.pack(pady = 25)
		
		self.budFrame = Frame(self.budgetFrame, style = "budget.TFrame")
		self.budFrame.pack()
		self.budLabel = Label(self.budFrame, text = "Budget", style = "budget.TLabel")
		self.budLabel.pack(side = LEFT, padx = 26, pady = 5)
		self.budEntry = Entry(self.budFrame, width = 16, state = DISABLED)
		self.budEntry.pack(side = LEFT, pady = 5)
		self.gFrame = Frame(self.budgetFrame, style = "budget.TFrame")
		self.gFrame.pack()
		self.gLabel = Label(self.gFrame, text = "Gas Type", style = "budget.TLabel")
		self.gLabel.pack(side = LEFT, padx = 22, pady = 5)
		self.gasType = StringVar()
		self.gasType.set(self.gasTypes[0])
		self.gCombo = Combobox(self.gFrame, textvariable=self.gasType, values=self.gasTypes, state = DISABLED)
		self.gCombo.pack(side = LEFT, pady = 5)
		self.budgetButton = Button(self.budgetFrame, text = "Calculate!", state = DISABLED, command = self.budgetButtonClick)
		self.budgetButton.pack(pady = 25)
	def addButtonClick(self):
		self.distanceEntry.configure(state = NORMAL)
		self.gasCombo.configure(state = NORMAL)
		self.budEntry.configure(state = NORMAL)
		self.gCombo.configure(state = NORMAL)
		self.distButton.configure(state = NORMAL)
		self.budgetButton.configure(state = NORMAL)
		self.c.set_car_data(self.nameEntry.get(), self.cylinderEntry.get(), self.torqueEntry.get(), self.horseEntry.get(), self.weightEntry.get(), self.engineCombo.get())
	def distButtonClick(self):
		self.c.set_dist_data(self.distanceEntry.get(), self.gasCombo.get())
	def budgetButtonClick(self):
		self.c.set_budget_data(self.budEntry.get(), self.gCombo.get())
		
		
		
		
		
		