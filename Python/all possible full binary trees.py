class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

    
    def print_tree(self):
       
        def inorder_traversal(node):
            if node:
                inorder_traversal(node.left)
                print(node.val, end=" ")
                inorder_traversal(node.right)

        inorder_traversal(self)
        print()  

def allPossibleFBT(n):
    dp = {0 : [], 1 : [TreeNode()]} # list of FBT

    def backtrack(n):
        if n in dp:return dp[n]
        ans = []

        #Brute force
        for left in range(n):
            right = n - 1 - left
            leftTree,rightTree = backtrack(left), backtrack(right)

            for i in leftTree:
                for j in rightTree:
                    ans.append(TreeNode(0, i, j) )   
        dp[n] = ans
        return ans
        
    return backtrack(n)

trees = allPossibleFBT(7)
for tree in trees:
    tree.print_tree()