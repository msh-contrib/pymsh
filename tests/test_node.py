import pytest

from msh.node import Node


def test_key():
    node = Node('a')
    assert node.key == 'a'


def test_fail_on_wrong_type():
    with pytest.raises(TypeError):
        Node([])


def test_add_edge():
    a, b = Node('a'), Node('b')
    a.add_edge(b)
    assert b in a.edges


def test_add_edge_wrong_param():
    with pytest.raises(AssertionError):
        Node('a').add_edge([])


def test_get_connections():
    a, b = Node('a'), Node('b')
    a.add_edge(b)
    assert a.get_connections() == [b]
