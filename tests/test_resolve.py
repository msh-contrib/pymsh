from msh.resolve import resolve
from msh.graph import Graph
from msh.node import Node


def test_resolve():
    graph = Graph()
    graph.add_node('a')
    graph.add_node('b')
    graph.add_node('c')
    graph.add_node('d')

    graph.add_edge('a', 'b')
    graph.add_edge('b', 'c')
    graph.add_edge('c', 'a')
    # graph.add_edge('a', 'c')
    # graph.add_edge('a', 'd')


    assert list(map(lambda node: node.id, resolve(
        graph.get_node('a')))) == ['b', 'a']
