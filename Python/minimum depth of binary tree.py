def minDepth(root):
    if root is None:
        return 0
    
    def dfs(node):
        if node is None:
            return float("inf")
        if node.left is None and node.fight is None:
            return 1
        
        return min(dfs(node.left),dfs(node.right)) + 1

    return dfs(root)