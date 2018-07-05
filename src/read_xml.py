import xml.etree.ElementTree

class XmlReader(object):
	"""docstring for XmlReader"""
	def __init__(self, input_file):
		super(, self).__init__()
		self.e = xml.etree.ElementTree.parse(input_file).getroot()
