# A basic binary tree can have utmost 2 children

class Node:
    def __init__(self, key):
        self.left = None
        self.right = None
        self.val = key

    # Traverse preorder(Root, Left, Right)
    def traversePreOrder(self):
        print(self.val, end=' ')
        if self.left:
            self.left.traversePreOrder()
        if self.right:
            self.right.traversePreOrder()

    # Traverse inorder(Left, Root, Right)
    def traverseInOrder(self):
        if self.left:
            self.left.traverseInOrder()
        print(self.val, end=' ')
        if self.right:
            self.right.traverseInOrder()

    # Traverse postorder(Left, Right, Root)
    def traversePostOrder(self):
        if self.left:
            self.left.traversePostOrder()
        if self.right:
            self.right.traversePostOrder()
        print(self.val, end=' ')

    # Traverse using Breadth First traversal
    def levelOrder(self):
        q = []
        q.append(self)
        while q:
            count = len(q)
            while count > 0:
                temp = q.pop(0)
                print(temp.val, end=' ')
                if temp.left:
                    q.append(temp.left)
                if temp.right:
                    q.append(temp.right)
                count -= 1


def maxDepth(node):
    # Can be done in one line
    # return 1 + max(depth_of_tree(tree.left), depth_of_tree(tree.right)) if tree else 0
    if node is None:
        return 0
    else:
        lDepth = maxDepth(node.left)
        rDepth = maxDepth(node.right)

        if (lDepth > rDepth):
            return lDepth+1
        else:
            return rDepth+1


def is_full_binary_tree(tree):
    if not tree:
        return True
    if tree.left and tree.right:
        return is_full_binary_tree(tree.left) and is_full_binary_tree(tree.right)
    else:
        return not tree.left and not tree.right


root = Node(1)

root.left = Node(2)
root.right = Node(3)

root.left.left = Node(4)
root.left.right = Node(5)

root.right.left = Node(6)
root.right.right = Node(7)

print("Pre order Traversal: ", end="")
root.traversePreOrder()
print("\nIn order Traversal: ", end="")
root.traverseInOrder()
print("\nPost order Traversal: ", end="")
root.traversePostOrder()
print("\nLevel order Traversal: ", end="")
root.levelOrder()
print()
print("Depth of Node: ", maxDepth(root))
print("Is a full Binary Tree: ", is_full_binary_tree(root))
