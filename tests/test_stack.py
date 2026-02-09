import pytest
from mypystructures.structures.stack import Stack

@pytest.fixture
def stack():
    return Stack()

def test_push(stack):
    stack.push(1)
    stack.push(2)
    assert stack.peak().value == 2

def test_pop(stack):
    stack.push(1)
    stack.pop()
    assert stack.peak().value == None

def test_len(stack):
    stack.push(1)
    stack.push(2)
    stack.push(3)
    assert len(stack) == 3
