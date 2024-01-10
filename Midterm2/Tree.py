from TreeNode import TreeNode
from linkedlist import LinkedList
"""
This is an implementation of a taxonomy tree.
@author: CS RIT
"""

class Tree:
    _slots_ = 'root', 'nodeLookup'
    root: TreeNode
    nodeLookup: dict[str, TreeNode]

    def _init_(self) -> None:  # do not modify
        self.root = None
        self.nodeLookup = dict()

    def _str_(self) -> str:  # do not modify
        if self.root:
            return str(self.root)
        return "[empty]"

    def _repr_(self) -> str:  # do not modify
        if self.root:
            return repr(self.root)
        return "[empty]"

    def getNodeByValue(self, value: str) -> TreeNode:  # do not modify
        return self.nodeLookup[value]

    def addRoot(self, value: str) -> None:  # do not modify
        """
        Creates a new node using the value and places it at the root
        :param value: the value of the root
        """
        assert value not in self.nodeLookup and not self.root
        node = TreeNode(value)
        self.nodeLookup[value] = node
        self.root = node

    def addChildTo(self, newChildValue: str, parentValue: str) -> None:
        """
        Creates a new node using the newChildValue and adds it to the node representing the parentValue
        :param newChildValue: The value of the new child node
        :param parentValue: The value of the intended parent

        """
        assert parentValue in self.nodeLookup and newChildValue not in self.nodeLookup
        if parentValue is not None and newChildValue is not None:
            parent_node = self.nodeLookup[parentValue]
            node = TreeNode(newChildValue)
            node.parent = parentValue
            parent_node.children.append(node)
            self.nodeLookup[newChildValue] = node

    def getPathToAncestor(self, nodeValue: str, ancValue: str) -> LinkedList:
        """
         Finds the path between the node specified by nodeValue and the ancestor node specified by ancValue
        :param nodeValue: The value of the node
        :param ancValue: The value of the ancestor node
        :return: A list of nodes representing the path between the node and its ancestor
        """
        assert nodeValue in self.nodeLookup and ancValue in self.nodeLookup
        path = LinkedList()
        node = self.nodeLookup[nodeValue]
        while node is not None and (node.value != ancValue):
            path.prepend(node)
            node = self.nodeLookup[node.parent]
        if node is None:
            path = None
        else:
            path.prepend(self.nodeLookup[ancValue])
        return path

    def getPathToRoot(self, nodeValue: str) -> LinkedList:  # do not modify
        """
         Finds the path between the node specified by nodeValue and the root of the tree
        :param nodeValue: The value of the node
        :return: A list of nodes representing the path between the node and the root of the tree
        """
        assert nodeValue in self.nodeLookup
        return self.getPathToAncestor(nodeValue, self.root.value)



    def getLCA(self, node1Value: str, node2Value: str) -> str:
        """
            Finds the least common ancestor of the nodes specified by the two arguments
            (i.e. the first common ancestor you would encounter when moving up the tree from node1 and node2).
            :param node1Value: The value of node1
            :param node2Value: The value of node2
            :return: The value of the least common ancestor node
        """
        assert node1Value in self.nodeLookup and node2Value in self.nodeLookup
        path_1 = self.getPathToRoot(node1Value)
        path_2 = self.getPathToRoot(node2Value)
        pTH = None
        d1 = path_1.start()
        while d1 is not None:
            d2 = path_2.start()
            while d2 is not None:
                if d1.value == d2.value:
                    pTH = d2
                d2 = d2.link
            d1 = d1.link
        return pTH





def test() -> None:
    t = Tree()
    t.addRoot("thing")
    # add children here
    t.addChildTo("animal", "thing")
    t.addChildTo("plant", "thing")
    t.addChildTo("mammal", "animal")
    t.addChildTo("fish", "animal")
    t.addChildTo("dog", "mammal")
    t.addChildTo("cat", "mammal")
    t.addChildTo("human", "mammal")
    t.addChildTo("tuna", "fish")

    # testing part 3
    print("Testing taxonomy..........")
    print(repr(t))
    print()
    # testing part 4
    print("Testing getPathToAncestor function..........")
    # path to root
    print("getPathToRoot('animal') =", t.getPathToRoot("animal"))
    print("getPathToRoot('thing') =", t.getPathToRoot("thing"))
    print("getPathToRoot('cat') =", t.getPathToRoot("cat"))
    # path to ancestor
    print("getPathToAncestor('animal','animal') =", t.getPathToAncestor('animal', 'animal'))
    print("getPathToAncestor('dog','animal') =", t.getPathToAncestor('dog', 'animal'))
    print("getPathToAncestor('dog','mammal') =", t.getPathToAncestor('dog', 'mammal'))
    print()
    # testing part 5
    print("Testing getLCA function..........")
    # LCA
    print("LCA('animal','thing') =", t.getLCA("animal", "thing"))
    print("LCA('thing','animal') =", t.getLCA("thing", "animal"))
    print("LCA('cat','tuna') =", t.getLCA("cat", "tuna"))
    print("LCA('tuna','cat') =", t.getLCA("tuna", "cat"))
    print("LCA('tuna','mammal') =", t.getLCA("tuna", "mammal"))
    print("LCA('cat','cat') =", t.getLCA("cat", "cat"))


if __name__ == '__main__':
    test()
