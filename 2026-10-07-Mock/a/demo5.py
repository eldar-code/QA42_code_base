from unittest.mock import Mock

def add(a, b):
    return a + b

# mock callable with parameters
mock = Mock(side_effect=add)
result = mock(3, 6)
print(result)

