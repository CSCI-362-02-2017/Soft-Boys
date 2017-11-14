import sys
import webbrowser
import re
from testFactorize import testFactorize
from testPow import testPow
from testIsInt import testIsInt
from testb10bin import testb10bin
#Move these later, yeah?

html = "<table><tr><th>Test Case</th><th>Method</th><th>Requirement</th><th>Test Input(s)</th><th>Expected</th><th>Results</th></tr>"

for x in range (1, 26):
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

	if(method == 'pow'):
		arguments = arguments.split()
		if len(arguments) == 2:
			try:
				result = testPow(arguments[0],arguments[1])
				
			except:
				result = "Fail"
		else:
			result="Fail"

	elif(method == 'b10bin'):
		arguments = arguments.split()
		if len(arguments) == 1:
			try:
				result = testb10bin(arguments)
			except:
				result = "Fail"
		else:
			result = "Fail"

	elif(method == 'factorize'):
		arguments = arguments.split()
		if len(arguments) == 1:
			try:
				result = testFactorize(arguments)
			except:
				result = "Fail"
		else:
			result = "Fail"

	elif(method == 'is_int'):
		print(arguments)
		if len(arguments) == 1:
			try:
				result = testIsInt(arguments)
			except:
				result = "Fail"
		else:
			result = "Fail"
	else:
		print("wut")
	#t.rows.append([caseNum, method, requirement, arguments, expected, result])
	html = html+"<tr><td>"+caseNum+"</td><td>"+method+"</td><td>"+requirement+"</td><td>"+str(arguments)+"</td><td>"+expected+"</td><td>"+str(result)+"</td></tr>"
html = html.join("</table>")
with open("test.html", "w") as file:
	file.write(str(html))


