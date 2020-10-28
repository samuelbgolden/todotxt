from tkinter import Frame, Text, INSERT, END
from iohandler import read_todo

class Content(Frame):
	def __init__(self, parent, *args, **kwargs):
		Frame.__init__(self, parent, *args, **kwargs)
		self.parent = parent

		self.text_area = Text(self)

		self.text_area.grid(row=0, column=0, sticky='nsew')

	def refresh(self, filename):
		tasks = read_todo(filename)
		text = '\n'.join([str(t) for t in tasks])

		self.text_area.delete("1.0",END)
		self.text_area.insert("1.0",text)