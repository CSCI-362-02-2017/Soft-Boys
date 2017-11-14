import sys

def testPow(x,y):
	sys.path.append('../project/sugarlabs-calculate-sugar-0.94')
	from functions import pow

	try:
		output = pow(x,y)
	except:
		output = "Fail"
	return output
