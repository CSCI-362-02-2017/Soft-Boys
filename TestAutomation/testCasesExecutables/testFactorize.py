import sys

def testFactorize(x):
	sys.path.append('../project/sugarlabs-calculate-sugar-0.94')
	from functions import factorize

	try:
		output = factorize(x)
	except:
		output = "Fail"
	return output
