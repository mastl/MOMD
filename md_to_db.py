"""Converts MOMD to database outputs."""

# >> Specify identifiers <<
headers = ('#', '##', '###', '####')
comments = ('%%')
lists = ('+.', '1.', 'i.', 'a.', 'A.')
identifiers = [headers, comments, lists]
print(identifiers[0])

# >> Create relevant classess <<


class Note(object):
	"""Create Note object."""

	def __init__(self, name):
		"""Return a TextSection object whose name is *name*."""
		self.name = name


# >> Create relevant functions <<


def create_element(possible_identifier, identifier_type, text_line):
	"""Create an element."""
	if identifier_type == 'header':
		header_type = len(possible_identifier)
		# CURRENTLY HERE
	return


def first_word(line):
	"""Isolate first word in line."""
	words = line.split()
	# print(words)
	try:
		value = words[0]
		# print(type(value))
	except ValueError:
		print('Pagebreak lines have not been properly sorted.')
	return value


def header(line):
	"""Do relevant manipulations with header."""
	pass


# >> Manipulate text <<
filename = 'test_file.md'
file = open(filename, 'r')

text = file.read()
file.close()

text_lines = text.split('\n')
text_lines = [x for x in text_lines if x != '']
# print(text_lines)

counter = 0
for text_line in text_lines:
	counter += 1
	print(counter)
	possible_identifier = first_word(text_line)
	print(possible_identifier)
	if possible_identifier in headers:
		identifier_type = 'header'
	elif possible_identifier in comments:
		pass  # Specify what needs to happen for comments.
	elif possible_identifier in lists:
		pass  # Specify what needs to happen for lists.
	else:
		pass  # Amend textline to current element.
