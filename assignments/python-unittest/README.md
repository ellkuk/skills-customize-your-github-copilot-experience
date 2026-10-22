# 📘 Assignment: Testing Python Applications with unittest

## 🎯 Objective

Write an automated test suite for a small shopping module using Python's built-in `unittest` framework. Practice testing normal results, boundary values, and invalid inputs with clear, focused test cases.

## 📝 Tasks

### 🛠️ Test the Shopping Functions

#### Description
Complete the starter tests for the provided shopping module. Use `python -m unittest` to run the tests and replace each failing placeholder with assertions that verify the expected behavior.

#### Requirements
Completed program should:

- Test `calculate_subtotal()` with multiple prices and confirm the result is rounded to two decimal places
- Test `apply_discount()` with a valid percentage and check the final amount
- Test `qualifies_for_free_shipping()` for an amount below and at the $50 threshold
- Use descriptive test method names and assertions that check specific expected values


### 🛠️ Cover Boundaries and Invalid Inputs

#### Description
Extend the test suite to cover edge cases and invalid values. Use `assertRaises` to verify that invalid input is rejected with `ValueError`.

#### Requirements
Completed program should:

- Test an empty price list, a zero-percent discount, and a 100-percent discount
- Check that negative prices and negative subtotals are rejected
- Check that discount percentages below 0 or above 100 are rejected
- Include at least one test for each public function's boundary behavior
- Run the complete suite successfully with `python -m unittest`