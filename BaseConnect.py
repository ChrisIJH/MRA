import abc

class BaseConnect(object):
	"""Abstract class for connection to data"""

	__metaclass__ = abc.ABCMeta

	def __init__(self, path, sheet):
		self.path = path 
		self.sheet = sheet
		
	@abc.abstractmethod
	def readExcel(self):
		pass
'''
	@abc.abstractmethod
	def readDatabase(self):
		pass
'''
	