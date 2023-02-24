# iterator
class NodeIter:
    def __init__(self, node):
        self.current_node = node

    def __next__(self):
        # if current_node is None
        if self.current_node is None:
            raise StopIteration
        else:
            # next node
            node, self.current_node = self.current_node, self.current_node.next_node
        return node

    def __iter__(self):
        return self

# iterable
class Node:
    def __init__(self, name):
        self.name = name
        self.next_node : Node = None
    
    def __iter__(self):
        return NodeIter(self)

node1 = Node("node1")
node2 = Node("node2")
node3 = Node("node3")

node1.next_node = node2
node2.next_node = node3

for node in node1:
    print(node.name)

# print(dir(NodeIter))

# list()