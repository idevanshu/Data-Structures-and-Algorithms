from collections import deque

class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None



def distanceK(root,target,k):
    parent = {}  
    visited = set()  

    def dfs(node, par=None):
        if node:
            parent[node] = par
            dfs(node.left, node)
            dfs(node.right, node)

    dfs(root)

    queue = deque([(target, 0)])  
    result = []
    while queue:
        node, dist = queue.popleft()
        visited.add(node)

        if dist == k:
            result.append(node.val)
        elif dist < k:
            neighbors = [node.left, node.right, parent[node]]
            for neighbor in neighbors:
                if neighbor and neighbor not in visited:
                    queue.append((neighbor, dist + 1))
                    visited.add(neighbor)

    return result

root = TreeNode(3)
root.left = TreeNode(5)
root.right = TreeNode(1)
root.left.left = TreeNode(6)
root.left.right = TreeNode(2)
root.right.left = TreeNode(0)
root.right.right = TreeNode(8)
root.left.right.left = TreeNode(7)
root.left.right.right = TreeNode(4)

target = root.left
k = 2

print(distanceK(root, target, k))
