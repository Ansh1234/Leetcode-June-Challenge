class Solution:
    def invertTree(self, root: TreeNode) -> TreeNode:
        self.traverse(root)
        return root
        
    def traverse(self, node):
        if (node == None):
            return
        self.traverse(node.left)
        self.traverse(node.right)
        node.left, node.right = node.right, node.left
        
