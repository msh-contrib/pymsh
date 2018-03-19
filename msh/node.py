class Node:
    def __init__(self, key, params=None):
        if not isinstance(key, str):
            raise TypeError('key should be str')

        self.key = key
        if params is None:
            params = {}
        self.params = params
        self.edges = []

    @property
    def id(self):
        return self.key

    def add_edge(self, node):
        assert isinstance(node, Node)
        if node not in self.edges:
            self.edges.append(node)

    def get_connections(self):
        return self.edges
