import abc
import pandas as pd
import numpy as np

class BaseConnect(object):
	"""Abstract class for connection to data"""

	__metaclass__ = abc.ABCMeta

	def __init__(self, url = None, path = None, sheet = None):
		self.url = url 
		self.path = path 
		self.sheet = sheet 
		
	@abc.abstractmethod
	def read(self):
		pass

class XlConnect(BaseConnect):
	""""""
	def __init__(self, path, sheet ):
		super(XlConnect, self).__init__(None, path, sheet)

	def read(self ):
		fi = pd.ExcelFile(self.path)
		self.data = fi.parse(self.sheet, index_col=0) 

	def readUpTo(self, row, col=None):
		"""Only some part of the sheet is Data.
		row: the last line of the data to be used.(excel's row num)
		col: the last column of the data to be used.
		"""

		self.row = row-1
		self.col = col-1
		if 'data' not in self.__dict__:
			self.read()

		self.data = self.data.ix[ :self.row, :self.col ]
	


"""	
	def getCorr(self)
		mean_vec = np.mean(self.data, axix=0)
		cov_mat = (a - mean_vec).T.dot((a - mean_vec)) / (a.shape[0]-1)
"""