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

def tmp(root,ans):
    if root.left is None and root.right is None:
        ans.append(root.key)
        print(ans)
    if root.left:
        tmp(root.left,ans)
    if root.right:
        tmp(root.right,ans)



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
    return result

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
    return result

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
    return result[::-1]

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

def zigzagLevelOrder(root):
    if not root:
        return []
    result=[]
    queue=deque([root])
    level=0
    while queue:
        current_level=[]
        for i in range(len(queue)):
            node=queue.popleft()
            current_level.append(node.key)
            if node.left:
                queue.append(node.left)
            if node.right:
                queue.append(node.right)
        if level%2==1:
            current_level=current_level[::-1]
        result.extend(current_level)
        level+=1
    print(result)

def boundaryOfBinaryTree(root):
    if not root:
        return []
    if not root.left and not root.right:
        return [root.key]
    left_boundary=[]
    right_boundary=[]
    leaves=[]
    def left_boundary1(root):
        if not root or (not root.left and not root.right):
            return
        left_boundary.append(root.key)
        if root.left:
            left_boundary1(root.left)
        else:
            left_boundary1(root.right)
    def right_boundary1(root):
        if not root or (not root.left and not root.right):
            return
        right_boundary.append(root.key)
        if root.right:
            right_boundary1(root.right)
        else:
            right_boundary1(root.left)
    def leaves1(root):
        if not root:
            return
        if not root.left and not root.right:
            leaves.append(root.key)
        leaves1(root.left)
        leaves1(root.right)
    left_boundary1(root.left)
    leaves1(root)
    right_boundary1(root.right)
    return [root.key]+left_boundary+leaves+right_boundary[::-1]

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

# Check if two trees are same
def Check_trees(root1,root2):
    if not root1 and not root2:
        return True
    if not root1 or not root2:
        return False
    return root1.key==root2.key and Check_trees(root1.left,root2.left) and Check_trees(root1.right,root2.right)

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
    print(tmp(root,[]))