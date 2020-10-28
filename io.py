from task import Task

def read_todo(filename):
	f = open(filename, 'r')
	raw = f.read(-1)
	f.close()

	tasks = []

	for line in raw.split('\n'):
		t = Task()
		t.parse_line(line)
		tasks.append(t)

	return tasks