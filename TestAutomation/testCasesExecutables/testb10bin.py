import sys

def testb10bin(x):
	sys.path.append('../project/sugarlabs-calculate-sugar-0.94')
	from functions import b10bin

	try:
		output = b10bin(x)
	except:
		output = "Fail"
	return output
