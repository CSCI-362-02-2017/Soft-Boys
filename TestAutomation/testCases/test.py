#The HTML formatting must take place in the script, not here
import unittest
import sys
import gi
gi.require_version('GConf', '2.0')
from gi.repository import GConf
from cpsection.aboutme import model

#Temporary array of test cases, still unable to pass by parameter from script
cases = ['', ' ','Jim Bowring', '@', '2']

class TestUserProfile(unittest.TestCase):
	#def test(str):
	#HTML table creation
	print('<table border="1">')
	print("<tr><th>Method</th><th>Input</th><th>Output</th><th>Expected</th></tr>")
	#Runs through every case in the array
	for testCase in cases:
		print("<tr>")
		#Does a try to assure the test cases are valid
		try:
			model.set_nick(testCase)
			#if model.get_nick() == " ":
			print("<td>model.set_nick(testCase)</td>")
			print("<td>" + testCase + "</td>")
			print('<td>Pass</td>')
			print('<td>Pass</td>') #Temporary place holder, should compare with text case file
		#Error handler
		except ValueError:
			print("<td>model.set_nick(testCase)</td>")
			print("<td>" + testCase + "</td>")
			print('<td>Fail</td>')
			print('<td>Fail</td>') #Temporary place holder, should compare with text case file
		#eval(sys.argv[1])
		print("</tr>")
	print("</table>")
	
