from tkinter import Menu
from tkinter.filedialog import askopenfilename
from pathlib import Path

class Settings(Menu):
	def __init__(self, parent, content, *args, **kwargs):
		Menu.__init__(self, parent, *args, **kwargs)
		self.parent = parent
		self.content = content

		# data
		self.todo_file = ''

		# top level cascades
		self.settingsMenu = Menu(self, tearoff=0)

		self.cascades = [
			{
				'name': 'settings',
				'menu': self.settingsMenu,
				'choices': [
					("set 'todo.txt' file", self.set_todo_file),
					("refresh from file", self.refresh_from_file)
				]
			},
		]

		for cascade in self.cascades:
			print(cascade)
			choices = cascade.get('choices')
			for choice in choices:
				cascade.get('menu').add_command(label=choice[0], command=choice[1])
			self.add_cascade(label=cascade.get('name'), menu=cascade.get('menu'))


	def set_todo_file(self):
		print('set_todo_file')
		initialdir = str(Path.home())
		new_todo_file = askopenfilename(
			initialdir=initialdir,
			title="Set 'todo.txt' file",
			filetypes=(("TXT File", "*.txt"), ("all files", "*.*"))
		)
		
		if not new_todo_file:
			return
		
		self.todo_file = new_todo_file

		self.refresh_from_file()

	def refresh_from_file(self):
		self.content.refresh(self.todo_file)