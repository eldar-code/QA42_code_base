import pytest


@pytest.mark.parametrize("val", [2, 4, 6, 10])
def test1(val: int):
    print()
    print(val)

@pytest.mark.parametrize("txt, length", [
    ("Hello", 5),
    ("Hi", 2),
    ("AAA", 3),
])
def test_text_length(txt: str, length: int):
    assert len(txt) == length
