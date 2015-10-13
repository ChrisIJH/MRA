import pandas as pd
import numpy as np

class XlConnect(BaseConnect):
	"""docstring for XlConnect"""
	def __init__(self, path, sheet = None):
		super(XlConnect, self).__init__(path, sheet)

	def readExcel(self)
		fi = pd.ExcelFile(self.path)
		self.data = fi.parse(self.sheet, index_col=0) 
		return self.data
		
	def getCorr(self)
		mean_vec = np.mean(self.data, axix=0)
		cov_mat = (a - mean_vec).T.dot((a - mean_vec)) / (a.shape[0]-1)
		