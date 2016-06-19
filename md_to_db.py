"""Converts MOMD to database output."""

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

	def __init__(self, title, date, tags, text):
		"""Return a TextSection object whose name is *name*."""
		self.name = title
		self.date = date
		self.tags = tags
		self.text = text

	def store_to_db(self, db):
		"""Store object to database."""
		pass


# >> Create relevant functions <<


def first_word(line):
	"""Isolate first word in line."""
	words = line.split()
	# print(words)
	try:
		value = words[0]
	except:
		return
	return value


def extract_info(text):
	"""Find relevant information in file. I.e. title, date and tags."""
	text_lines = text.split('\n')
	text_lines = [x for x in text_lines if x != '']

	info = {'title': "", 'date': "", 'tags': []}
	counter = 0
	for text_line in text_lines[0:9]:
		counter += 1
		possible_identifier = first_word(text_line).lower()
		if counter == 1:  # Extract title
			info['title'] = ignore_identifiers(text_line, possible_identifier)
		elif counter == 2:  # Extract date
			info['date'] = text_line
		elif possible_identifier in identifiers['tags']:  # Extract tags
			tags = ignore_identifiers(text_line, possible_identifier)
			tags = tags.split(',')
			for tag in tags:
				tag = tag.strip()
			info['tags'] = tags
	return info  # Return dictionary with title, date and tags!


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
file = open(filename, 'r')

text = file.read()
file.close()

file_info = extract_info(text)

print(file_info)
