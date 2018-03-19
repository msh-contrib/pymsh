from .node import Node


def resolve(node):
    if not isinstance(node, Node):
        raise ValueError('value should be instance of Node')

    unresolved, resolved = [], []

    def traverse(node, resolved, unresolved):
        unresolved.append(node)
        connections = node.get_connections()
        for edge in connections:
            if edge not in resolved:
                if edge in unresolved:
                    return
                traverse(edge, resolved, unresolved)

        resolved.append(node)
        unresolved.remove(node)

    traverse(node, resolved, unresolved)

    return resolved
