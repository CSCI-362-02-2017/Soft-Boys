import unittest
import sys
import gi
gi.require_version('GConf', '2.0')
from gi.repository import GConf
from cpsection.aboutme import model

cases = ['', ' ','Jim Bowring', '@', '2']

class TestUserProfile(unittest.TestCase):
	#def test(str):
	for testCase in cases:
		try:
			model.set_nick(testCase)
			#if model.get_nick() == " ":
			print('Pass')
		except ValueError:
			print('Fail')
		#eval(sys.argv[1])
	
	
