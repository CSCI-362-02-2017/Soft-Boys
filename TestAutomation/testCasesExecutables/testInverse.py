import sys

def testInverse(x):
	sys.path.append('../project/sugarlabs-calculate-sugar-0.94')
	from functions import inverse

	try:
		output = inv(x)
	except:
		output = "Fail"
	return output