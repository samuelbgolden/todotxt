from tkinter import Menu

class Settings(Menu):
	def __init__(self, parent, *args, **kwargs):
		Menu.__init__(self, parent, *args, **kwargs)
		self.parent = parent

		self.settingsMenu = Menu(self, tearoff=0)

		self.cascades = [
			{
				'name': 'settings',
				'menu': self.settingsMenu,
				'choices': [
					("set 'todo.txt' file", self.set_todo_file),
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