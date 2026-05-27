import pytest

@pytest.fixture
def username():
    return "Aditi"

def test_name(username):
    assert username == "Aditi"

def test_length(username):
    assert len(username) == 5

def test_first_letter(username):
    assert username[0] == "A"