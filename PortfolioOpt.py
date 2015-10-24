import math
from Disp import preTag
import numpy as np
import pandas as pd 

class PO(object):
	"""Portfolio Optimization """
	def __init__(self, data):
		self.data = data

	def cleanData(self):
		if self.data.columns[0] == 'Date':
			self.date = self.data['Date']
			self.data = self.data.drop('Date', 1)
		else:
			self.date = None

	def estimateAssetMoments(self):
		self.CORR = self.data.corr()
		self.CVC = self.data.cov()

		