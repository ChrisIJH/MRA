def preTag(exNum):
	def displ(f):
		def wrapper(arg):
			return "Market Risk Analysis by Carol Alexander \n %s \n  %s\n"%  (exNum, f(arg))
		return wrapper
	return displ

