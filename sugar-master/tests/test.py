import unittest
import sys
import gi
gi.require_version('GConf', '2.0')
from gi.repository import GConf
from cpsection.aboutme import model

class TestUserProfile(unittest.TestCase):
	def test(str):
		model.set_nick(str)
		if model.get_nick() == str:
			print('Pass')
		else:
			print('Fail')
	eval(sys.argv[1])
	
	
