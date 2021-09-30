# Diwas Lamsal - st122324
# 2021-September-29 Data Structures and Algorithms Week 8
# Question: Binary Search Tree Assignment

# --------------------------------------------------------------------------------------------------------------

class Node:
    def __init__(self, val):
        self.l = None
        self.r = None
        self.v = val


class Tree:
    def __init__(self):
        self.root = None

    def getRoot(self):
        return self.root

    def add(self, val):
        if self.root is None:
            self.root = Node(val)
        else:
            self._add(val, self.root)

    def _add(self, val, node):
        if val < node.v:
            if node.l is not None:
                self._add(val, node.l)
            else:
                node.l = Node(val)
        else:
            if node.r is not None:
                self._add(val, node.r)
            else:
                node.r = Node(val)

    def find(self, val):
        if self.root is not None:
            return self._find(val, self.root)
        else:
            return None

    def _find(self, val, node):
        if val == node.v:
            return node
        elif val < node.v and node.l is not None:
            return self._find(val, node.l)
        elif val > node.v and node.r is not None:
            return self._find(val, node.r)

    def deleteTree(self):
        self.root = None

    def printTree(self):
        if self.root is not None:
            self._printTree(self.root)

    def _printTree(self, node):
        if node is not None:
            self._printTree(node.l)
            print(str(node.v), end=" ")
            self._printTree(node.r)

    # ----------------------------- My solution begins here -----------------------------
    # The printTree function prints in ascending order, so, I have written another function to
    # print the tree in descending order

    # -------------------------------------------- DESCENDING PRINT --------------------------------------------
    def printDescending(self):
        if self.root is not None:
            self._printDescending(self.root)

    # The idea is to just reverse the order of visiting the left and right nodes
    def _printDescending(self, node):
        if node is not None:
            self._printDescending(node.r)
            # https://www.geeksforgeeks.org/print-without-newline-python/
            print(str(node.v), end=" ")
            self._printDescending(node.l)

    # -------------------------------------------- DELETE NODE --------------------------------------------

    # Finding the parent in a binary tree
    # Reference taken from
    # https://stackoverflow.com/questions/43774655/how-can-i-get-the-parent-in-binary-tree
    # Prateek Arora's answer
    def findParent(self, rootNode, elem):
        if rootNode is None:
            return None
        if rootNode.l is None and rootNode.r is None:
            return None
        if rootNode.l == elem or rootNode.r == elem:
            return rootNode
        searchRight = self.findParent(rootNode.r, elem)
        if searchRight is not None:
            return searchRight
        searchLeft = self.findParent(rootNode.l, elem)
        if searchLeft is not None:
            return searchLeft
        return None

    # Pseudocode from the book
    def treeMinimum(self, x):
        while x.l is not None:
            x = x.l
        return x

    # Pseudocode from the book
    def transplant(self, u, v):
        uParent = self.findParent(self.root, u)

        if uParent is None:
            self.root = v
        elif u == uParent.l:
            uParent.l = v
        else:
            uParent.r = v
        if v is not None:
            vParent = self.findParent(self.root, v)
            vParent = uParent

    # Pseudocode from the book
    def delete(self, value):
        node = tree.find(value)
        if node is None:
            print("Node not found")
            return
        if self.root is None:
            print("Tree is empty")
            return
        if node.l is None:
            self.transplant(node, node.r)
        elif node.r is None:
            self.transplant(node, node.l)
        else:
            y = self.treeMinimum(node.r)
            if self.findParent(self.root, y) is not node:
                self.transplant(y, y.r)
                y.r = node.r
                yrParent = self.findParent(self.root, y.r)
                yrParent = y
            self.transplant(node, y)
            y.l = node.l
            ylParent = self.findParent(self.root, y.r)
            ylParent = y

    # Find Successor
    # Pseudocode from book
    def treeSuccessor(self, value):
        node = self.find(value)
        if node is None:
            return None
        if node.r is not None:
            return self.treeMinimum(node.r)
        y = self.findParent(self.root, node)
        while y is not None and node == y.r:
            node = y
            y = self.findParent(self.root, y)
        return y


# --------------------------------------- TEST ------------------------------------------

tree = Tree()
tree.add(3)
tree.add(4)
tree.add(0)
tree.add(8)
tree.add(2)
tree.printTree()
print(f"\n{tree.find(3).v}")
print(tree.find(10))
tree.deleteTree()
tree.printTree()

# Ascending sort was already done for us, so, I am doing descending sort
# Delete node is also implemented

tree = Tree()
for i in range(0, 22, 2):
    tree.add(i)
for i in range(21, 1, -2):
    tree.add(i)

print("Ascending: ", end="")
tree.printTree()
print("\n-----------------------------------")
print("Testing Successor")
print("Successor of 6:", tree.treeSuccessor(6) if tree.treeSuccessor(6) is None else tree.treeSuccessor(6).v)
print("Successor of 5:", tree.treeSuccessor(5) if tree.treeSuccessor(5) is None else tree.treeSuccessor(5).v)
print("Successor of 8:", tree.treeSuccessor(8) if tree.treeSuccessor(8) is None else tree.treeSuccessor(8).v)
print("Successor of 4:", tree.treeSuccessor(4) if tree.treeSuccessor(4) is None else tree.treeSuccessor(4).v)
print("Successor of 18:", tree.treeSuccessor(18) if tree.treeSuccessor(18) is None else tree.treeSuccessor(18).v)
print("Successor of 21:", tree.treeSuccessor(21) if tree.treeSuccessor(21) is None else tree.treeSuccessor(21).v)
print("-----------------------------------")

print("Find 6 before delete: ", end=" ")
print(tree.find(6).v)
print("Tree Descending before delete: ", end="")
tree.printDescending()
print()
print("Delete 6, 8, 20, and 0")
tree.delete(6)
tree.delete(8)
tree.delete(20)
tree.delete(0)
print("Find 6 after delete: ", end="")
print(tree.find(6))
print("Tree Descending after delete: ", end="")
tree.printDescending()
print("\n-----------------------------------", end="")
