import ClassicVolCorr
import unittest
from MRAConnect import XlConnect


class UnCondVolTest1(unittest.TestCase):

	xl = XlConnect("/Users/hwang/Copy/EBOOK-K-Z/Quant/Market_Risk_Analysis/alexander_c_market_risc_analysis_practical_financial_econome/vol_2/content/II.3/Examples_II.3.xls","EX_II.3.5&8")
	xl.read()
	xl.readUpTo(12,2)
	pair = (xl.data, 0.343 )
	def test(self):

		res = ClassicVolCorr.UnCondVol(self.xl.data).getUnCondVol_no_zero_mean()
		self.assertEqual(self.pair[1], res)

if __name__ == "__main__":
	unittest.main()