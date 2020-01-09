# from dll_stack import Stack
# from dll_queue import Queue
# import sys
# sys.path.append('../queue_and_stack')

# Questions:
# can binary search trees contain negative numbers, only ints?
# >= goes right.
# need to traverse to delete and find
# when deleting the next smallest child becomes the parent


class BinarySearchTree:
    def __init__(self, value):  # just using value. key is value
        self.value = value
        self.left = None
        self.right = None
        self.root = None

    # Insert the given value into the tree
    # need to traverse to find spot to insert
    def insert(self, value):
        if value < self.value:
            if not self.left:
                self.left = BinarySearchTree(value)
            else:
                self.left.insert(value)

        if value >= self.value:
            if not self.right:
                self.right = BinarySearchTree(value)
            else:
                self.right.insert(value)
        # if self.root is None:
        #     self.root = value
        # else:
        #     self._insert(value, self.root)

    # def _insert(self, value, cur_node):
    #     if value < cur_node.value:
    #         if cur_node.left is None:
    #             cur_node.left = value
    #         else:
    #             self._insert(value, cur_node.left)

    #     elif value > cur_node.value:
    #         if cur_node.right is None:
    #             cur_node.right = value
    #         else:
    #             self._insert(value, cur_node.right)
    #     else:
    #         print("value is already present.")

    # Return True if the tree contains the value
    # False if it does not
    # start from root and traverse the tree. we can stop at the first instance of a value. we know its not found if we get to a node that does not have children

    def contains(self, target):
        if target == self.value:
            return True
        if target < self.value:
            if self.left is None:
                return False
            else:
                return self.left.contains(target)

        else:
            if self.right is None:
                return False
            else:
                return self.right.contains(target)

    #     if self.root:
    #         is_found = self._find(target, self.root)
    #         if is_found:
    #             return True
    #         return False
    #     else:
    #         return None

    # def _find(self, target, cur_node):
    #     if target > cur_node.target and cur_node.right:
    #         return self._find(target, cur_node.right)
    #     elif target < cur_node.target and cur_node.left:
    #         return self._find(target, cur_node.left)
    #     if target == cur_node.target:
    #         return True

    # Return the maximum value found in the tree
    def get_max(self):
        if self.right:
            return self.right.get_max()
        else:
            return self.value

    # Call the function `cb` on the value of each node
    # You may use a recursive or iterative approach
    #
    def for_each(self, cb):
        cb(self.value)
        if self.left:
            self.left.for_each(cb)
        if self.right:
            self.right.for_each(cb)

    # DAY 2 Project -----------------------

    # Print all the values in order from low to high
    # Hint:  Use a recursive, depth first traversal
    def in_order_print(self, node):
        pass

    # Print the value of every node, starting with the given node,
    # in an iterative breadth first traversal
    def bft_print(self, node):
        pass

    # Print the value of every node, starting with the given node,
    # in an iterative depth first traversal
    def dft_print(self, node):
        pass

    # STRETCH Goals -------------------------
    # Note: Research may be required

    # Print In-order recursive DFT
    def pre_order_dft(self, node):
        pass

    # Print Post-order recursive DFT
    def post_order_dft(self, node):
        pass
