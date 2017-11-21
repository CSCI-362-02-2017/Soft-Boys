import sys

def testInverse(x):
	sys.path.append('../project/sugarlabs-calculate-sugar-0.94')
	from functions import inv

	try:
		output = inv(x)
	except:
		output = "Fail"
	return output
