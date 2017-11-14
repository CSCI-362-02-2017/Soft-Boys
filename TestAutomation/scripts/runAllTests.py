
import sys
import webbrowser
sys.path.append('../testCaseExecutables')
from testFactorize import testFactorize
from testPow import testPow
from test_isInt import testIs_int
from testb10bin import testb10bin
sys.path.append('../testCases')

for x in range (1, 25)
    currentTestCase = '/testCases/testCase' + str(x) 
    testCase = open((currentTestCase + '.txt'), 'r')
    contents = testCase.read()
    caseLines = contents.split('\n')
    method = caseLines[3]

    if(method == 'pow')
        print("Pow!")

    elif(method == 'b10bin')
        print("Binary")

    elif(method == 'factorize')
        print("Factor")

    elif(method == 'is_int')
        print("Int")