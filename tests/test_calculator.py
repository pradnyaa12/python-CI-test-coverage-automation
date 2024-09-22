import pytest
from pytest_bdd import scenarios, given, when, then
from calculator import Calculator

# Link the Gherkin feature file to python test file
scenarios('features/calculator.feature')


#In the context of Behavior-Driven Development (BDD) and testing frameworks like pytest-bdd, 
# "context" refers to the initial state or environment required for the test scenarios to execute properly. 
# It sets up the necessary conditions or objects so that the test can be carried out as described in the scenario.



# Step definitions -The step definitions implement the logic behind the steps from the feature file. 


#This is a pytest fixture that creates an instance of the Calculator class.
#The fixture provides the calculator object to each test, so the same object can be reused across the test steps.
@pytest.fixture
def calculator():
    return Calculator()

@given('a calculator')
def calc(calculator):
    pass  # Calculator is already instantiated by the fixture

@when('I add 3 and 3')
def add_numbers(calculator):
    calculator.result = calculator.add(3, 3)

@when('I subtract 5 from 10')
def subtract_numbers(calculator):
    calculator.result = calculator.subtract(10, 5)

@when('I multiply 4 and 5')
def multiply_numbers(calculator):
    calculator.result = calculator.multiply(4, 5)

@when('I divide 10 by 2')
def divide_numbers(calculator):
    calculator.result = calculator.divide(10, 2)

@when('I divide 10 by 0')
def divide_by_zero(calculator):
    try:
        calculator.result = calculator.divide(10, 0)
    except ValueError:
        calculator.result = "ValueError"
               
@when('I Calculate the power of 2 and 3')
def power(calculator):
    calculator.result= calculator.power(2,3)
        


@then('the result should be 6')
def check_result_6(calculator):
    assert calculator.result == 6
    
@then('the result should be 5')
def check_result_5(calculator):
    assert calculator.result == 5

@then('the result should be 20')
def check_result_20(calculator):
    assert calculator.result == 20

@then('a ValueError should be raised')
def check_value_error(calculator):
    assert calculator.result == "ValueError"
    
@then('the result should be 8')
def check_result_8(calculator):
    assert calculator.result == 8




# python -m pytest
# coverage run -m pytest
# coverage report   
# coverage html 
#pytest --html=test_report.html 
