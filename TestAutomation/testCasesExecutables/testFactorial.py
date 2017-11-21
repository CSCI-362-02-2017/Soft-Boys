import sys

def testFactorial(x):
	sys.path.append('../project/sugarlabs-calculate-sugar-0.94')
	from functions import factorial

	try:
		output = factorial(x)
	except:
		output = "Fail"
	return output