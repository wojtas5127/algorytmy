from typing import Any, Callable

class BinaryNode:
    value: Any
    left_child: 'BinaryNode'
    right_child: 'BinaryNode'

    def __init__(self,value: Any):
        self.value = value
        self.left_child = None
        self.right_child = None

    def __str__(self):
        w = str(self.value)
        return w

    def is_leaf(self):
        if(self.left_child is None and self.right_child is None):
            return True
        else:
            return False

    def add_left_child(self,value: Any):
        self.left_child = value

    def add_right_child(self,value: Any):
        self.right_child = value

    def in_order(self, visit: Callable[[Any],None]):
        if(self.left_child):
            self.left_child.in_order(visit)
        visit(self)
        if(self.right_child):
            self.right_child.in_order(visit)

    def pre_order(self,visit: Callable[[Any],None]):
        visit(self)
        if(self.left_child):
            self.left_child.pre_order(visit)
        if(self.right_child):
            self.right_child.pre_order(visit)

    def post_order(self, visit: Callable[[Any],None]):
        if(self.left_child):
            self.left_child.post_order(visit)
        if(self.right_child):
            self.right_child.post_order(visit)
        visit(self)



class BinaryTree:
    root: BinaryNode

    def __init__(self,root):
        self.root = root

    def in_order(self,visit: Callable[[Any],None]):
        self.root.in_order(visit)

    def pre_order(self,visit: Callable[[Any],None]):
        self.root.pre_order(visit)

    def post_order(self,visit: Callable[[Any],None]):
        self.root.post_order(visit)


def fun(y):
    print(y)



dz = BinaryNode(10)

tree = BinaryTree(dz)

dzie = BinaryNode(9)
dz.add_left_child(dzie)

j = BinaryNode(1)
dzie.add_left_child(j)

tr = BinaryNode(3)
dzie.add_right_child(tr)

d = BinaryNode(2)
dz.add_right_child(d)

cz = BinaryNode(4)
d.add_left_child(cz)

s = BinaryNode(6)
d.add_right_child(s)


# dz.in_order(fun)
# dz.pre_order(fun)
# dz.post_order(fun)

# tree.in_order(fun)
# tree.pre_order(fun)
# tree.post_order(fun)


