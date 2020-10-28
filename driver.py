import tkinter as tk
from settings import Settings

class App(tk.Frame):
	def __init__(self, parent, *args, **kwargs):
		tk.Frame.__init__(self, parent, *args, **kwargs)
		self.parent = parent
		self.parent.title('todo.txt')

		self.settings = Settings(self)
		self.parent.configure(menu=self.settings)


if __name__ == "__main__":
	root = tk.Tk()
	app = App(root)
	app.pack(fill='both', expand=True)
	root.mainloop()