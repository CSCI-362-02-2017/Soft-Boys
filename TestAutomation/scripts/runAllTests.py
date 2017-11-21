import sys
sys.path.insert(0, '../testCasesExecutables')
import webbrowser
import re
import os
import glob
from testFactorize import testFactorize
from testPow import testPow
from testIsInt import testIsInt
from testb10bin import testb10bin
from testFactorial import testFactorial
from testInverse import testInverse

html = '<!DOCTYPE html><html><head><link rel="stylesheet" href="main.css"></head><body><table><tr><th>Test Case</th><th>Method</th><th>Requirement</th><th>Test Input(s)</th><th>Expected</th><th>Actual</th><th>Results</th></tr>'

#numberFilesList = os.listdir('../testCases')
numberFiles = len(glob.glob1('../testCases','*.txt')) + 1

for x in range (21, numberFiles):
	currentTestCase = '../testCases/testCase' + str(x) 
	testCase = open((currentTestCase + '.txt'), 'r')
	contents = testCase.read()
	caseLines = contents.split('\n')
	caseNum = caseLines[0]
	caseNum = caseNum.replace("Test ID:", "")
	method = caseLines[2]
	method = method.replace("Method Being Tested:", "")
	requirement = caseLines[3]
	requirement = requirement.replace("Requirement Being Tested:", "")
	expected = caseLines[5]
	expected = expected.replace("Expected Outcome:", "")
	arguments = caseLines[4]
	arguments = arguments.replace("Test Input(s):", "")
	actual = 0

	if(method == 'pow'):
		arguments = arguments.split()
		if len(arguments) == 2:
			try:
				actual = testPow(int(arguments[0]),int(arguments[1]))
			except Exception as ex:
				actual = ex.message
				result = "Fail"
		else:
			actual = "Incorrect number of argument(s)"
			result="Fail"
		if (actual == expected):
			result = "Pass"
		else:
			result = "Fail"
	elif(method == 'b10bin'):
		arguments = arguments.split()
		if len(arguments) == 1:
			try:
				actual = testb10bin(int(arguments[0]))
			except Exception as ex:
				actual = ex.message
				result = "Fail"
		else:
			result = "Fail"
		if (actual == expected):
			result = "Pass"
		else:
			result = "Fail"

	elif(method == 'factorize'):
		arguments = arguments.split()
		if len(arguments) == 1:
			try:
				actual = testFactorize(int(arguments[0]))
			except Exception as ex:
				actual = ex.message
				result = "Fail"
		else:
			result = "Fail"
		if (actual == expected):
			result = "Pass"
		else:
			result = "Fail"

	elif(method == 'factorial'):
		arguments = arguments.split()
		if len(arguments) == 1:
			try:
				actual = testFactorial(int(arguments[0]))
			except Exception as ex:
				actual = ex.message
				result = "Fail"
		else:
			result = "Fail"
		if (actual == expected):
			result = "Pass"
		else:
			result = "Fail"
	elif(method =='inverse'):
		arguments = arguments.split()
		if len(arguments) == 1:
			try:
				actual = testInverse(int(arguments[0]))
			except Exception as ex:
				actual = ex.message
				result = "Fail"
		else:
			result = "Fail"
		if (actual == expected):
			result = "Pass"
		else:
			result = "Fail"
	else:
		print("wut")

	html = html+"<tr><td>"+caseNum+"</td><td>"+method+"</td><td>"+requirement+"</td><td>"+str(arguments)+"</td><td>"+str(expected)+"</td><td>"+str(actual)+"</td><td>"+str(result)+"</td></tr>"
html = html + ("</body></table>")
with open("../reports/report.html", "w") as file:
	file.write(str(html))
report = 'report.html'
webbrowser.open_new_tab("../reports/report.html")

