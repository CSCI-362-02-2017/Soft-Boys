#either find or create testing report
touch ../reports/testingreport.html

#empty testing report
echo ''>../reports/testingreport.html

#change directory to test cases
cd ../testCases


#run each python file, change system output to test report
for entry in ./*
do

 python $entry >> ../reports/testingreport.html

done

#open testing report
xdg-open ../reports/testingreport.html

