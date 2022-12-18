# 2 classes ; one for tree and the other for each node

import random
import string

class xmlTreeNode(object):
    "Node of a Tree"
    def __init__(self, name='root', string_val='NULL', children=None, parent=None):
        self.name = name
        self.parent = parent
        self.children = []
        self.string_val = string_val
        if children:
            for child in children:
                self.add_child(child)
            else:
                self.value = string_val

    def __repr__(self):
        return self.name

    def is_root_node(self):     #check whether the node is root or not
        if self.parent:
            return False
        else:
            return True

    def is_leaf_node(self):     #check whether the node is leaf or not
        if len(self.children) == 0:
            return True
        else:
            return False

    def node_depth(self):    # Depth of current node
        if self.is_root_node():
            return 0
        else:
            return 1 + self.parent.node_depth()

    def add_child(self, node):
        node.parent = self
        assert isinstance(node, xml_TreeNode)
        self.children.append(node)

    def node_to_json(self):
        if self.is_leaf_node():
            if isinstance(self.value, str):
                return print('"' + self.name + '":' + '"' + self.string_val + '"')
            else:
                return print('"' + self.name + '":' + self.string_val)

        else:
            if self.children: #single type
                return print('"' + self.name + '": { ' + '"' + self.children.name + '": [' + self.children.node_to_json() + '] }')
            else:
                return print('"' + self.name + '": [{' + self.children.node_to_json())


class xmlTree:

    def __init__(self):
       self.root = None
       self.height = 0
       self.tree_nodes = []

    def insert(self, node, parent):   # Insert a new node to the tree
        if parent is not None:
            parent.add_child(node)
        else:
            if self.root is None:
                self.root = node
        self.tree_nodes.append(node)

    def get_node(self, index):
        return self.tree_nodes[index]

    def root(self):
        return self.root



def xml_to_json (payload):


