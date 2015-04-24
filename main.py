# Main

from Tkinter import *
from home import *
from control import *

def main():
   root = Tk()
   c = Control()
   home(root, c)
   root.mainloop()

if __name__ == "__main__":
   main()
