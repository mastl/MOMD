"""Converts MOMD to database output."""

import datetime
import os.path


# >> Specify identifiers <<
identifiers = {
	'headers': ['#', '##', '###', '####'],
	'comments': ['%%', 'comment:'],
	'lists': ['+.', '1.', 'i.', 'a.', 'A.'],
	'tags': ['tags:', 'tags']
}
# print(identifiers)

# >> Create relevant classess <<


# class Text(object)
# 	"""String of text from some file."""
# 	def __init__(self, filename)
# 		self.name = filename


class Note(object):
	"""Note object which consists of text."""

	def __init__(self, filename):
		"""Create note from text file."""
		try:
			file = open(filename, 'r')
			text = file.read()
			file.close()
		except TypeError:
			print('File input must be readable.')
		text_info = extract_info(text)
		self.text = text
		self.title = text_info['title']
		self.date = text_info['date']
		self.tags = text_info['tags']

	def __repr__(self):
		"""What to print when printing a note."""
		return str(self.title)

	def store_to_db(self, db):
		"""Store object to database."""
		pass


# >> Create relevant functions <<


def first_word(line):
	"""Isolate first word in line."""
	if type(line) is not str:
		print('Input to must be a string.')
	words = line.split()
	try:
		value = words[0]
	except:
		return
	return value


def extract_info(text):
	"""Find relevant information in file. I.e. title, date and tags."""
	if type(text) is not str:
		print('Input to must be a string.')
	info = {
		'title': "",
		'date': datetime.datetime.today().strftime("%Y-%m-%d %H:%M:%S"),
		'tags': []
	}

	text_lines = text.split('\n')
	text_lines = [x for x in text_lines if x != '']

	counter = 0
	for text_line in text_lines[0:9]:
		counter += 1
		possible_identifier = first_word(text_line).lower()
		if counter == 1:  # Extract title
			info['title'] = ignore_identifiers(text_line, possible_identifier)
		elif possible_identifier in identifiers['tags']:  # Extract tags
			tags = ignore_identifiers(text_line, possible_identifier)
			tags = tags.split(',')
			tags = [tag.strip() for tag in tags]
			info['tags'] = tags
	return info  # Return dictionary with title, date and tags!


def ignore_identifiers(text_line, possible_identifier):
	"""Ignore the first word in string if it is an identifier."""
	if type(text_line) is not str:
		print('Input to must be a string.')
	counter = 0
	for identifier_type in identifiers:
		counter += 1
		if possible_identifier in identifiers[identifier_type]:
			start_string = len(possible_identifier) + 1
			text_line = text_line[start_string:]
	return text_line


# >> Execute <<
fname = 'resources_used.md'
# counter = 0
# fname = input('Input text file: ')
# while os.path.isfile(fname) == 0:
# 	fname = input('Please input text file that exists: ')
# 	counter += 1
# 	if counter == 10:
# 		break

note = Note(fname)

# print(note.title)
# print(note.date)
print(note.tags)
