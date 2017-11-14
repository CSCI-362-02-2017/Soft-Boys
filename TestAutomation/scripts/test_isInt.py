import sys

def testIs_int(x):
	sys.path.append('../project/sugarlabs-calculate-sugar-0.94')
	from functions import is_int

	try:
		output = is_int(x)
	except:
		output = "Fail"
	return output
