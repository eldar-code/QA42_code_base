from unittest.mock import Mock

# create a Mock object
mock = Mock(side_effect=[100, 200, 300])

the_sum = mock() + mock() + mock()
print(the_sum)
