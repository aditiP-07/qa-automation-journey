import pytest

@pytest.mark.parametrize("text, expected", [
    ("hello", "olleh"),
    ("aditi", "itida")
])

def test_reverse_str(text, expected):
    assert reverse_str(text) == expected

def reverse_str(text):
    rev_text = text[::-1]
    return rev_text