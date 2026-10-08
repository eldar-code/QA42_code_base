from unittest.mock import Mock

# create a Mock object
my_mock = Mock(side_effect=[100, 200, 300])

result = my_mock()
print(result)

result = my_mock()
print(result)

result = my_mock()
print(result)
