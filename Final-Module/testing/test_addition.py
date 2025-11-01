import addition
import pytest

def test_add():
    assert addition.add(4,5) == 9 

def test_sub():
    assert addition.sub(4,5) == -1

#to run test file, run in terminal
#python -m pytest tester_file_name