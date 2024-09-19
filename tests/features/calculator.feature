Feature: Calculator Operations

  Scenario: Add two numbers
    Given a calculator
    When I add 3 and 3
    Then the result should be 6

  Scenario: Subtract two numbers
    Given a calculator
    When I subtract 5 from 10
    Then the result should be 5

  Scenario: Multiply two numbers
    Given a calculator
    When I multiply 4 and 5
    Then the result should be 20

  Scenario: Divide two numbers
    Given a calculator
    When I divide 10 by 2
    Then the result should be 5

  Scenario: Divide by zero
    Given a calculator
    When I divide 10 by 0
    Then a ValueError should be raised

  Scenario: Calculate power of two numbers
    Given a calculator
    When I Calculate the power of 2 and 3
    Then the result should be 8

  
