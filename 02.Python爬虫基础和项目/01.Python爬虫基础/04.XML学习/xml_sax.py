import string
from xml.parsers.expat import ParserCreate

class DefaultSaxHandle:
	pass

handler = DefaultSaxHandle()
parser = ParserCreate()
parser.StartElementHandler