from typing import Any, Callable


class BinaryNode:
    value: Any
    left_child: "BinaryNode"
    right_child: "BinaryNode"

    def __init__(self, value: Any):
        self.value = value
        self.left_child = None
        self.right_child = None

    def is_leaf(self):
        if self.left_child is None and self.right_child is None:
            return True
        return False

    def add_left_child(self, value: Any):
        self.left_child = BinaryNode(value)

    def add_right_child(self, value: Any):
        self.right_child = BinaryNode(value)

    def traverse_in_order(self, visit: Callable[[Any], None]):
        """
        visit(self.left_child.left_child.value)
        visit(self.left_child.value)
        visit(self.left_child.right_child.value)
        visit(self.value)
        visit(self.right_child.left_child.value)
        visit(self.right_child.value)
        visit(self.right_child.right_child.value)
        """
        if self.left_child.is_leaf():
            visit(self.value)
        if self.left_child.left_child.is_leaf():
            visit(self.left_child.value)
            visit(self.value)
            visit(self.right_child.value)
        self.traverse_post_order(visit)

    def traverse_post_order(self, visit: Callable[[Any], None]):
        visit(self.left_child.left_child.value)
        visit(self.left_child.right_child.value)
        visit(self.left_child.value)
        visit(self.right_child.left_child.value)
        visit(self.right_child.right_child.value)
        visit(self.right_child.value)
        visit(self.value)

    def traverse_pre_order(self, visit: Callable[[Any], None]):
        visit(self.value)
        visit(self.left_child.value)
        visit(self.left_child.left_child.value)
        visit(self.left_child.right_child.value)
        visit(self.right_child.value)
        visit(self.right_child.left_child.value)
        visit(self.right_child.right_child.value)


b1 = BinaryNode(10)
b1.add_left_child(9)
b1.add_right_child(2)
b1.left_child.add_left_child(1)
b1.left_child.add_right_child(3)
b1.right_child.add_left_child(4)
b1.right_child.add_right_child(6)
b1.traverse_in_order(print)
b1.traverse_post_order(print)
b1.traverse_pre_order(print)
