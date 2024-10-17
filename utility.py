"""

To provide a interface to communicate with the Node objects and to access member functions directly.

"""

from Node import Node


def addNode(id):
    return Node(int(id))


def joinNodes(l, r):
    l.join(r)


def prettyPrintFT(node):
    node.fingerTable.prettyPrint()


def prettyPrintNode(node):
    node.prettyPrint()


def insertKeyValues(node, key, value):
    node.insert(int(key), value)


def leaveNode(node):
    node.leave()


def findall(node):
    node.findall(node, 0)


def find(node, key):
    node.find(int(key))


def remove(node, key):
    node.remove_function(int(key))
