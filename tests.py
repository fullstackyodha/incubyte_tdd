import pytest
from stringCalculator import StringCalculator

def test_single_number():
    assert StringCalculator().add("1") == 1

def test_two_numbers():
    assert StringCalculator().add("78,2") == 80

def test_multiple_numbers():
    assert StringCalculator().add("12,56,34") == 102

def test_new_line_as_delimiter():
    assert StringCalculator().add("1\n2,3") == 6

def test_custom_delimiter():
    assert StringCalculator().add("//;\n1;2") == 3

def test_negative_numbers():
    with pytest.raises(ValueError, match="negative numbers not allowed -1, -3"):
        StringCalculator().add("1,-1,2,-3")