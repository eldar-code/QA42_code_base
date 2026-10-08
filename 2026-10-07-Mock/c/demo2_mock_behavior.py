from unittest.mock import Mock

# Accessing an undefined attribute on a Mock automatically creates and returns another Mock.

mock = Mock()
print(mock)
print(mock.x)
print(mock.y())

