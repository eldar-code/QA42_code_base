from unittest.mock import Mock

# Accessing an undefined attribute on a Mock automatically creates and returns another Mock.

mock = Mock()

# We can create an attribute and assign a value to it
mock.x = 5
print(mock.x)

# We can configure a callable attribute to return a value
mock.y.return_value = 10
print(mock.y())
