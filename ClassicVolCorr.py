import math
from Disp import preTag
import numpy as np

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




		