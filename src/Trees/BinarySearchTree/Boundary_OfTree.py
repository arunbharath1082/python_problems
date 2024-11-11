class Node:
    def __init__(self, key):
        self.key = key
        self.left = None
        self.right = None

# boundary in anticlockwise
def boundaryOfBinaryTree(root):
    if not root:
        return []
    if not root.left and not root.right:
        return [root.key]

    left_boundary = []
    right_boundary = []
    leaves = []

    def left_boundary1(node):
        if not node or (not node.left and not node.right):
            return
        left_boundary.append(node.key)
        if node.left:
            left_boundary1(node.left)
        else:
            left_boundary1(node.right)

    def right_boundary1(node):
        if not node or (not node.left and not node.right):
            return
        right_boundary.append(node.key)
        if node.right:
            right_boundary1(node.right)
        else:
            right_boundary1(node.left)

    def leaves1(node):
        if not node:
            return
        if not node.left and not node.right:
            leaves.append(node.key)
        leaves1(node.left)
        leaves1(node.right)

    left_boundary1(root.left)
    leaves1(root)
    right_boundary1(root.right)

    return [root.key] + left_boundary + leaves + right_boundary[::-1]

if __name__ == '__main__':
    root = Node(1)
    root.left = Node(2)
    root.left.left = Node(3)
    root.left.right = Node(4)
    root.left.left.left = Node(5)
    root.left.left.right = Node(6)
    root.right = Node(7)
    root.right.left = Node(8)
    root.right.right = Node(9)
    root.right.right.left = Node(10)
    root.right.right.right = Node(11)

    print(boundaryOfBinaryTree(root))