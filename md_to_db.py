"""Converts MOMD to database output."""

import datetime


# >> Specify identifiers <<
identifiers = {
	'headers': ['#', '##', '###', '####'],
	'comments': ['%%', 'comment:'],
	'lists': ['+.', '1.', 'i.', 'a.', 'A.'],
	'tags': ['tags:']
}
# print(identifiers)

# >> Create relevant classess <<


# class Text(object)
# 	"""String of text from some file."""
# 	def __init__(self, filename)
# 		self.name = filename


class Note(object):
	"""Note object which consists of text."""

	def __init__(self, text, title, date, tags):
		"""Return a TextSection object whose name is *name*."""
		self.text = text
		self.title = title
		self.date = date
		self.tags = tags

	def __repr__(self):
		"""What to print when printing a note."""
		return "%" % (self.title)

	def store_to_db(self, db):
		"""Store object to database."""
		pass


# >> Create relevant functions <<


def first_word(line):
	"""Isolate first word in line."""
	words = line.split()
	try:
		value = words[0]
	except:
		return
	return value


def extract_info(text):
	"""Find relevant information in file. I.e. title, date and tags."""
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
			for tag in tags:
				tag = tag.strip()
			info['tags'] = tags
	return info  # Return dictionary with title, date and tags!


def generate_text(filename):
	"""Generate text from file."""
	try:
		file = open(filename, 'r')
		text = file.read()
		file.close()
	except TypeError:
		print('File input must be readable.')
	return text


def ignore_identifiers(text_line, possible_identifier):
	"""Ignore the first word in string if it is an identifier."""
	counter = 0
	for identifier_type in identifiers:
		counter += 1
		if possible_identifier in identifiers[identifier_type]:
			start_string = len(possible_identifier) + 1
			text_line = text_line[start_string:]
	return text_line

# >> Execute <<
filename = 'test_file.md'
# filename = input('Specify text file: ')

text = generate_text(filename)
text_info = extract_info(text)

note = Note(text, text_info)
print(note)
