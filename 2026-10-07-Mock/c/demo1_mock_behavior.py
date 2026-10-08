from unittest.mock import Mock

# A Mock is callable by default, and its default return value is another Mock.
mock = Mock()
print(mock)
print(mock())
print(mock()())
print(mock()()())
print(mock()()()())
print(mock()()()()())

