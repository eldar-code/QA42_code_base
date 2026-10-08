from unittest.mock import Mock

# create a Mock object
my_mock = Mock(return_value="Hello Mock World!")
result = my_mock()
print(result)

print(my_mock())
print(my_mock())
print(my_mock())
print(my_mock())
