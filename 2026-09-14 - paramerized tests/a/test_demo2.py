import pytest


@pytest.mark.parametrize(
    argnames="val",
    argvalues=[1, 5],
    ids=["positive_test", "edge_case"]
)
def test_limit_is_five(val: int):
    assert val <= 5


@pytest.mark.parametrize(
    argnames="txt, length",
    argvalues=[("Hello", 5), ("Hi", 2), ("AAAB", 4)],
    ids=["run1", "run2", "run3"]
)
def test_text_length(txt: str, length: int):
    assert len(txt) == length


@pytest.mark.parametrize(
    "txt, length",
    [
        pytest.param("Hi", 2, id="run-1"),
        # to skip a test use mark + skip (feature is not supported yet)
        pytest.param("Java", 44, marks=[pytest.mark.skip], id="run-2"),
        # on a known bug use mark + xfail (test is running but failure is not reported)
        pytest.param("Java", 44, marks=[pytest.mark.xfail], id="run-3"),
        # in case xfail passes we get a pass result with xpass flag
        pytest.param("Java", 4, marks=[pytest.mark.xfail], id="run-4"),
        pytest.param("Python", 6,marks=[], id="run-5"),
    ]
)
def test_text_length2(txt: str, length: int):
    assert len(txt) == length
