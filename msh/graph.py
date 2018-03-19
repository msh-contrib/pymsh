from .node import Node


class Graph:
    def __init__(self):
        self._graph = {}

    def add_node(self, key, params=None):
        if not isinstance(key, str):
            raise TypeError('key should a str')

        if key in self._graph:
            return self._graph[key]

        self._graph[key] = Node(key, params)
        return self._graph[key]

    def get_node(self, key):
        return self._graph.get(key)

    def add_edge(self, start, end):
        self.add_node(start).add_edge(self.add_node(end))

    def get_connections(self, key):
        if key not in self._graph:
            return []

        return self._graph[key].get_connections()
