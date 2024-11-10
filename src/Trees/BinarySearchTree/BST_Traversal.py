from collections import deque


class Node:
    def __init__(self, key):
        self.key = key
        self.left = None
        self.right = None

def height(node):
    if node is None:
        return 0
    else:
        lheight = height(node.left)
        rheight = height(node.right)

        return max(lheight,rheight)+1

def levelOrder(root):
    h=height(root)
    result=[]
    for i in range(1,h+1):
        result.extend(printGivenLevel(root,i))
    print(result)

def printGivenLevel(root,level):
    if root is None:
        return []
    if level==1:
        return [root.key]
    elif level>1:
        left=printGivenLevel(root.left,level-1)
        right=printGivenLevel(root.right,level-1)
    return left+right

def levelOrder_Iterative(root):
    if not root:
        return []
    result=[]
    queue=deque([root])
    while queue:
        current_level=[]

        for i in range(len(queue)):
            node=queue.popleft()
            current_level.append(node.key)
            if node.left:
                queue.append(node.left)
            if node.right:
                queue.append(node.right)

        result.extend(current_level)
    print(result)

def inorder(root):
    if root is not None:
        # Traverse left
        inorder(root.left)

        # Traverse root
        print(str(root.key) + "->", end=' ')

        # Traverse right
        inorder(root.right)
def preorder(root):
    if root is not None:
        # Traverse root
        print(str(root.key) + "->", end=' ')
        # Traverse left
        preorder(root.left)
      # Traverse right
        preorder(root.right)
def postorder(root):
    if root is not None:
        # Traverse left
        postorder(root.left)
        # Traverse right
        postorder(root.right)
        # Traverse root
        print(str(root.key) + "->", end=' ')

def inorder_iterative(root):
    if not root:
        return []
    result=[]
    stack=[]
    current=root
    while stack or current:
        if current:
            stack.append(current)
            current=current.left
        else:
            current=stack.pop()
            result.append(current.key)
            current=current.right
    print(result)

def preorder_iterative(root):
    if not root:
        return []
    result=[]
    stack=[root]
    while stack:
        node=stack.pop()
        if node:
            result.append(node.key)
            stack.append(node.right)
            stack.append(node.left)
    print(result)

def postorder_iterative(root):
    if not root:
        return []
    result=[]
    stack=[root]
    while stack:
        node=stack.pop()
        if node:
            result.append(node.key)
            stack.append(node.left)
            stack.append(node.right)
    print(result[::-1])

def all_traversals(root):
    if not root:
        return [], [], []

    stack = [(root, 1)]
    preorder, inorder, postorder = [], [], []

    while stack:
        node, state = stack.pop()

        if state == 1:  # Preorder
            preorder.append(node.key)
            stack.append((node, state + 1))
            if node.left:
                stack.append((node.left, 1))
        elif state == 2:  # Inorder
            inorder.append(node.key)
            stack.append((node, state + 1))
            if node.right:
                stack.append((node.right, 1))
        else:  # Postorder
            postorder.append(node.key)

    return preorder, inorder, postorder

# Check if a tree is balanced
# It will return height of the tree for balanced tree
# It will return -1 if tree is not balanced
def check_BalancedTree(root):
    if not root:
        return 0
    left=check_BalancedTree(root.left)
    if left==-1:
        return -1
    right=check_BalancedTree(root.right)
    if right==-1:
        return -1
    if abs(left-right)>1:
        return -1
    return max(left,right)+1

def diameterOfBinaryTree(root):
    def diameter(root):
        nonlocal maxi
        if not root:
            return 0
        left=diameter(root.left)
        right=diameter(root.right)
        maxi=max(maxi,left+right)
        return max(left,right)+1
    if not root:
        return 0
    maxi=0
    diameter(root)
    return maxi

def MaximumPathSum(root):
    def helper(root):
        nonlocal sum1;
        if not root:
            return 0
        left=max(helper(root.left),0)
        right=max(helper(root.right),0)
        tmp=root.key+left+right
        sum1=max(sum1,tmp)
        return max(left,right)+root.key;
    if not root:
        return 0
    sum1=0
    helper(root)
    return sum1

if __name__ == '__main__':
    root = Node(-10)
    root.left = Node(2)
    root.right = Node(20)
    root.right.left = Node(15)
    root.right.right = Node(7)
    print(MaximumPathSum(root)) # 15
