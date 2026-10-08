from unittest.mock import Mock

# create a Mock object that raises an error when called
mock = Mock(side_effect=ValueError("This is a value error from mock"))
# mock = Mock(side_effect=[1, 2, 3])
try:
    mock()
    print("An error was not called! Why")
except ValueError as e:
    print(e)
"""
Side effect with error is good for negative tests
"""
