if __name__ == "__main__":
	import unittest
	from gpacalc import *
	suite1 = unittest.TestLoader().loadTestsFromTestCase(gpaCalcTest)
	suite = unittest.TestSuite([suite1])
	unittest.TextTestRunner(verbosity=2).run(suite)
