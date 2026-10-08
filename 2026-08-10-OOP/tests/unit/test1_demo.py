# we want to write test cases
from unittest import TestCase
# ==============================================
# lets say we want to test this unit
class Calculator:
    def __init__(self):
        self.result = 0.0

    def add(self, val: float):
        self.result += val
# ==============================================
class MyTests(TestCase):

    def test_initial_state(self):
        calc = Calculator()
        # I want to assert that calc.result is 0.0
        self.assertEqual(0.0, calc.result)

    def test_add(self):
        # 1. get the object under testing
        calc = Calculator()
        # 2. perform an action you want to test
        calc.add(17.3)
        # 3. set the expected result
        expected = 17.3
        # 4. get the actual result
        actual = calc.result
        # 5. set an error message in case something fails
        err_msg = "Add method failed"
        # 6. assert we get what was expected
        self.assertEqual(expected, actual, err_msg)

    def test_multiple_add_actions(self):
        calc = Calculator()
        self.assertEqual(0.0, calc.result, "wrong initial state")
        calc.add(3)
        self.assertEqual(3.0, calc.result, "add failed on attempt 1")
        calc.add(5)
        self.assertEqual(8.0, calc.result, "add failed on attempt 2")
