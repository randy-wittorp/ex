#This is example code from Mike Orsega's python course
#available through Gale Courses
#
#This must be run in python3

from Tkinter import *


class MyFrame(Frame):
  """MyFrame class merely inherits the tkinter Frame class"""
  def __init__(self):
    Frame.__init__(self)
    self.myCanvas = Canvas(width=300, height=200, bg='blue')
    self.myCanvas.grid()
    self.myCanvas.create_rectangle(10, 10, 100, 100)

frame02 = MyFrame()
frame02.mainloop()
