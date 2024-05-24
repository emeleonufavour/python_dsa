from typing import Optional
import collections

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def print_tree(root: Optional[TreeNode], level=0, label="."):
    # Base case: if the tree is empty
    if root is None:
        return
    
    # Print the current node
    indent = " " * (4 * level)
    print(f"{indent}{label}: {root.val}")
    
    # Recursively print the left and right subtrees
    if root.left or root.right:
        if root.left:
            print_tree(root.left, level + 1, "L")
        else:
            print(f"{indent}    L: None")
        if root.right:
            print_tree(root.right, level + 1, "R")
        else:
            print(f"{indent}    R: None")
        
def list_to_tree(array: list[int]) -> Optional[TreeNode]:
    root_value = array[0]
    root = TreeNode(root_value)
    queue = collections.deque()
    queue.append(root)
    current_index = 0
    
    while queue and current_index < len(array):
        node = queue.popleft()
        
        if (2 * current_index) + 1 < len(array):
            left_value = array[(2 * current_index) + 1]
            node.left = TreeNode(left_value)
            queue.append(node.left)
      
        if (2 * current_index) + 2 < len(array):
            right_value = array[(2 * current_index) + 2]
            node.right = TreeNode(right_value)
            queue.append(node.right)    
        current_index += 1

    return root
      
class Solution:
    def removeLeafNodes(self, root: Optional[TreeNode], target: int) -> Optional[TreeNode]:
        def post_order_traversal(node: Optional[TreeNode]):
            if not node:
                return None
            
            node.left = post_order_traversal(node.left)
            node.right = post_order_traversal(node.right)
            
            if not node.left and not node.right and node.val == target:
                return None
            
            return node
        
        return post_order_traversal(root)
            
        
    
def tree_traverse(root: Optional[TreeNode]):
    if root is None:
        return
    if root.left is None and root.right is None:
        print(f"{root.val}")
    tree_traverse(root.left)
    tree_traverse(root.right)
    

 
if __name__ == "__main__":
    sol = Solution()
    my_list = [1,2,3,2,None,2,4]
    my_list2 = [1,3,3,3,2]
    tree = list_to_tree(my_list2)
    
    result = sol.removeLeafNodes(tree, 3)
    print_tree(result)
    # tree_traverse(tree)
    # print(answer)