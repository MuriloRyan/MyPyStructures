import pytest
from mypystructures.structures.stack import Stack

def test_empty_stack():
    stack = Stack()

    assert stack.is_empty()
    assert len(stack) == 0
    assert repr(stack) == "Stack()"


def test_create_with_value():
    stack = Stack(10)

    assert not stack.is_empty()
    assert len(stack) == 1
    assert stack.peak().value == 10


def test_push():
    stack = Stack()

    stack.push(1)

    assert len(stack) == 1
    assert stack.peak().value == 1


def test_push_multiple():
    stack = Stack()

    stack.push(1)
    stack.push(2)
    stack.push(3)

    assert len(stack) == 3
    assert stack.peak().value == 3


def test_pop():
    stack = Stack()

    stack.push(1)
    stack.push(2)
    stack.push(3)

    assert stack.pop() == 3
    assert len(stack) == 2
    assert stack.peak().value == 2


def test_pop_until_empty():
    stack = Stack()

    stack.push(1)
    stack.push(2)

    assert stack.pop() == 2
    assert stack.pop() == 1

    assert stack.is_empty()
    assert len(stack) == 0


def test_pop_empty():
    stack = Stack()

    assert stack.pop() is None
    assert stack.is_empty()


def test_peek():
    stack = Stack()

    stack.push("A")
    stack.push("B")

    assert stack.peak().value == "B"
    assert len(stack) == 2


def test_getitem():
    stack = Stack()

    stack.push("A")
    stack.push("B")
    stack.push("C")

    assert stack[1].value == "A"
    assert stack[2].value == "B"
    assert stack[3].value == "C"


def test_getitem_out_of_range():
    stack = Stack()

    stack.push(1)

    with pytest.raises(IndexError):
        stack[2]


def test_getitem_invalid_type():
    stack = Stack()

    with pytest.raises(Exception):
        stack["1"]


def test_iteration():
    stack = Stack()

    stack.push(1)
    stack.push(2)
    stack.push(3)

    values = [node.value for node in stack]

    assert values == [1, 2, 3]


def test_repr_strings():
    stack = Stack()

    stack.push("A")
    stack.push("B")

    assert repr(stack) == "Stack('A','B')"


def test_push_none():
    stack = Stack()

    stack.push(None)

    assert len(stack) == 1
    assert stack.peak().value is None