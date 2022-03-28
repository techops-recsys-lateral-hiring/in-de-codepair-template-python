# PYTHON TEST EXAMPLE

## Run the following commands on your terminal in the project directory


## Installl virtual env using pip
pip install pipenv

## Start a virtual env  for python3  using virtualenv
pipenv shell


## Install pytest module using pip 
pipenv install 

## Run the unit tests
pipenv run unit-test

One of the test should will not run as it is marked skip,    remove the @pytest.mark.skip try to fix it and run it again to pass all the test cases

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


