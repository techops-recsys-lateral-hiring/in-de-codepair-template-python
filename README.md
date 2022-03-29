# PYTHON TEST EXAMPLE

##Assumptions
- Pip (22.0.4)
- Python 3.9

## Run the following commands on your terminal in the project directory


## Installl virtual env using pip
pip install pipenv

## Start a virtual env  for python3  using virtualenv
pipenv shell


## Install pytest module using pip 
pipenv install 

## Run the unit tests
pipenv run unit-test

you should see an output like this: 1 failed, 1 passed, 1 skipped

One of the test will not run as it is marked skip, follow instructions over test to 
remove the @pytest.mark.skip try to fix it and run it again to pass the test case

One of the test should be failing , Correc the Assertion logic to pass the test case.

Run the pipenv run unit-test again after the fixes and now run the unit tests again.

Now All the 3 test cases should be passing

## Run the spark-submit job
pipenv run spark-submit --master local sum.py

Check sum=20 in the output

## PyCharm
To run tests in pycharm , open the project in pycharm and install the pytest module using settings
and run the test directly using the green arrow next to test cases

## pycharm debug
Go through the following link seriously to know how to debug in pycharm 
##
https://www.jetbrains.com/help/pycharm/debugging-code.html

## Running the tests 
Go through the following link seriously to know how to run tests in pycharm
##
https://www.jetbrains.com/help/pycharm/testing.html


## Summary
Expect similar test cases in the actual coding round
You should be able to run these steps on your machine and Inform the Hiring team once you are able to run these steps successfully


