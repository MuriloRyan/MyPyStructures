import pytest

from mypystructures.structures.CircularLinkedList import CircularLinkedList


def create_list():
    lst = CircularLinkedList()

    lst.append("A")
    lst.append("B")
    lst.append("C")

    return lst


def test_empty_list():
    lst = CircularLinkedList()

    assert lst.root is None
    assert lst.tail is None


def test_append_first_element():
    lst = CircularLinkedList()

    lst.append("A")

    assert lst.root.data == "A"
    assert lst.tail.data == "A"

    assert lst.root.next == lst.root
    assert lst.tail.next == lst.root


def test_append_multiple_elements():
    lst = create_list()

    assert lst.root.data == "A"
    assert lst.tail.data == "C"

    assert lst.root.next.data == "B"
    assert lst.root.next.next.data == "C"

    assert lst.tail.next == lst.root


def test_getitem():
    lst = create_list()

    assert lst[0].data == "A"
    assert lst[1].data == "B"
    assert lst[2].data == "C"


def test_getitem_wraps():
    lst = create_list()

    assert lst[3].data == "A"
    assert lst[4].data == "B"
    assert lst[5].data == "C"
    assert lst[6].data == "A"


def test_find_one():
    lst = create_list()

    result = lst.find_one("B")

    assert result["index"] == 1
    assert result["item"] == "B"


def test_find_root():
    lst = create_list()

    result = lst.find_one("A")

    assert result["index"] == 0
    assert result["item"] == "A"


def test_find_last():
    lst = create_list()

    result = lst.find_one("C")

    assert result["index"] == 2
    assert result["item"] == "C"


def test_find_one_not_found():
    lst = create_list()

    with pytest.raises(StopIteration):
        lst.find_one("Z")

def test_iteration():
    lst = create_list()

    values: list[Unknown] = [node.data for node in lst]

    assert values == ["A", "B", "C"]


def test_iteration_empty():
    lst = CircularLinkedList()

    values = [node.data for node in lst]

    assert values == []


def test_repr():
    lst = create_list()

    assert repr(lst) == "Circular['A', 'B', 'C']"


def test_repr_empty():
    lst = CircularLinkedList()

    assert repr(lst) == "Circular[]"


def test_circularity():
    lst = create_list()

    current = lst.root
    values = []

    for _ in range(10):
        values.append(current.data)
        current = current.next

    assert values == [
        "A",
        "B",
        "C",
        "A",
        "B",
        "C",
        "A",
        "B",
        "C",
        "A",
    ]


def test_tail_is_last_node():
    lst = create_list()

    assert lst.tail.data == "C"
    assert lst.tail.next == lst.root


def test_append_after_multiple():
    lst = create_list()

    lst.append("D")

    assert lst.tail.data == "D"
    assert lst.tail.next == lst.root

    assert lst[0].data == "A"
    assert lst[1].data == "B"
    assert lst[2].data == "C"
    assert lst[3].data == "D"
    assert lst[4].data == "A"


def test_many_appends():
    lst = CircularLinkedList()

    for i in range(100):
        lst.append(i)

    assert lst.root.data == 0
    assert lst.tail.data == 99
    assert lst.tail.next == lst.root

    assert lst[0].data == 0
    assert lst[50].data == 50
    assert lst[99].data == 99
    assert lst[100].data == 0