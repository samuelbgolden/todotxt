import re
# TODO replace date parsing with python datetime object

class Task:
	def __init__(self, content='', completion=False, priority='', completion_date='', creation_date='', projects=[], contexts=[], metadata={}):
		self.content = content
		self.completion = completion
		self.priority = priority
		self.completion_date = completion_date
		self.creation_date = creation_date
		self.projects = projects
		self.contexts = contexts
		self.metadata = metadata

	def parse_line(self, input):
		self.content = ""

		words = input.split(' ')

		priority_idx = 0
		completion_date_idx = 0
		to_remove = 0

		if words[0] == 'x':
			self.completion = True

			priority_idx = 1
			completion_date_idx = 1

			to_remove += 1

		if self.is_priority(words[priority_idx]):
			self.priority = words[priority_idx][1]
			completion_date_idx += 1

			to_remove += 1

		if self.is_date(words[completion_date_idx]) and self.is_date(words[completion_date_idx+1]):
			self.completion_date = words[completion_date_idx]
			self.creation_date = words[completion_date_idx+1]

			to_remove += 2

		words = words[to_remove:]

		for i,word in enumerate(words):
			if i != 0:
				self.content += ' '
			self.content += word

			if self.is_project(word):
				self.projects.append(word)
			elif self.is_context(word):
				self.contexts.append(word)
			elif self.is_metadatum(word):
				key,val = word.split(':')
				self.metadata[key] = val


	def is_priority(self, word):
		return bool(re.fullmatch("(\([A-Z]\))", word))

	def is_date(self, word):
		return bool(re.fullmatch("(\d{4}-(0\d|1[012])-([012]\d|3[01]))", word))

	def is_project(self, word):
		return bool(re.fullmatch("(\+\S+)", word))

	def is_context(self, word):
		return bool(re.fullmatch("(\@\S+)", word))

	def is_metadatum(self, word):
		return bool(re.fullmatch("([^\s\:]+\:[^\s\:]+)", word))

	def __str__(self):
		s = '{ '
		if self.completion:
			s += 'x '

		if self.priority:
			s += '(' + self.priority + ') '

		if self.completion_date:
			s += self.completion_date + ' ' 

		if self.creation_date:
			s += self.creation_date + ' '

		s += self.content + ' }'
		return s

	def __repr__(self):

		return self.__str__()



