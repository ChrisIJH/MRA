import math
from Disp import preTag
import numpy as np
import pandas as pd

"""Python Implemented Examples in Market Risk Analysis by Carol Alexander"""

class VolCorr(object):
	"""Ex II.3.2 page 93"""
	def __init__(self, std, length, autoCorr):
		self.std = std 
		self.length= length 
		self.autoCorr = autoCorr
		h = self.length
		rho= self.autoCorr
		self.ar1sf = math.sqrt( h + 2* rho* (( h-1)*(1- rho) - rho* (1- math.pow(rho, h -1) ))/(math.pow(1- rho,2)))

	def AR1ScaleFactor(self):
		return  self.ar1sf

	def standardVol(self):
		return  self.std * math.sqrt(self.length)

	def correlatedVol(self):
		return self.std * self.ar1sf

	@preTag("Ex II.3.2 page 93")
	def __str__(self):
		return "Standard Volatility : %s , Correlated Volatility: %s " % (self.standardVol(), self.correlatedVol())


class PortVariance(object):
	"""Ex II.3.3 pg 96"""
	def __init__(self, std1, std2, std3, corr12, corr13, corr23):
		#self.weight = np.array(weight) 
		self.C = np.matrix( [ [1, corr12, corr13], [corr12, 1, corr23], [corr13, corr23, 1] ])
		self.D = np.eye(3) * np.array([std1, std2, std3])
		self.V = self.D.dot(self.C).dot(self.D)

	@preTag("Ex II.3.3")
	def __str__(self):
		return "C: \n %s \n D: \n %s \n V: \n %s" % (self.C, self.D, self.V)
	
	@preTag("EX II.3.4")
	def getScaledDecomposed_VCV(self):
		"""Ex II.3.4 pg 97"""
		new_V = self.V/25
		new_D = np.sqrt(new_V)
		an_V = ((new_D).dot(self.C)).dot(new_D)
		result = "10 day V can be obtained by V/25 --> V10\n" 
		result += str(new_V)
		result += "\n" 
		result += "sqrt(V10) is D10" 
		result += "\n" + str(new_D) + "\n" + "D10 * C * D10 is \n" + str(an_V)
		return result

class UnCondVol:
	def __init__(self, data):
		'''
		arg:
		data - dataframe of time series data
		'''
		self.data = data

	def getUnCondVol(self):
		"""Ex II.3.5"""
		self.zero_mean_ret = self.data.pct_change()[1:]
		f = lambda x: x**2
		self.zero_mean_vol = round(np.sqrt((self.zero_mean_ret.applymap(f).sum()/self.zero_mean_ret.shape[0])*250), 3)
		return  self.zero_mean_vol

	def getUnCondVol_no_zero_mean(self):
		"""Ex II.3.6"""
		self.no_zero_mean_ret = self.data.pct_change()[1:]
		mean_ret = self.no_zero_mean_ret.mean()[0]
		f = lambda x: (x - mean_ret)**2
		self.no_zero_mean_vol = round(np.sqrt(ret.applymap(f).sum()/(ret.shape[0]-1))*np.sqrt(250), 3)
		return  self.no_zero_mean_vol
	
	def getCorrCov(self, obj):
		"""Ex II.3.7"""	

		if 'zero_mean_ret' not in self.__dict__:
			self.getUnCondVol()
		if 'zero_mean_ret' not in obj.__dict__:
			obj.getUnCondVol()

		rets = pd.concat([self.zero_mean_ret, obj.zero_mean_ret], axis = 1)
		return rets.corr(), rets.cov()












