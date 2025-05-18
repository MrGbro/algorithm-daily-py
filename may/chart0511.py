from typing import Optional, List

from common.base import TreeNode


class Solution1008:
    def bstFromPreorder(self, preorder: List[int]) -> Optional[TreeNode]:
        def build_tree(pre: List[int], pre_start: int, pre_end: int, inorder: List[int], in_start: int,
                       in_end: int) -> Optional[TreeNode]:
            if pre_start > pre_end:
                return None
            root_val = preorder[pre_start]
            root = TreeNode(root_val)
            root_index = inorder.index(root_val)
            root.left = build_tree(pre, pre_start + 1, pre_start + root_index - in_start, inorder, in_start,
                                   root_index - 1)
            root.right = build_tree(pre, pre_start + root_index - in_start + 1, pre_end, inorder, root_index + 1,
                                    in_end)
            return root

        inorder = preorder[:]
        inorder.sort()
        return build_tree(preorder, 0, len(preorder) - 1, inorder, 0, len(inorder) - 1)


class Solution:
    def balanceBST(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        def inorder_traversal(node: Optional[TreeNode], values: List[int]) -> None:
            if node is None:
                return
            inorder_traversal(node.left, values)
            values.append(node.val)
            inorder_traversal(node.right, values)

        def dfs(arr: List[int], start: int, end: int) -> Optional[TreeNode]:
            if start > end:
                return None
            mid = (start + end) // 2
            root = TreeNode(arr[mid])
            root.left = dfs(arr, start, mid - 1)
            root.right = dfs(arr, mid + 1, end)
            return root

        res = []
        inorder_traversal(root, res)
        res.sort()
        return dfs(res, 0, len(res) - 1)


class Solution2196:
    def createBinaryTree(self, descriptions: List[List[int]]) -> Optional[TreeNode]:
        node_map = {}
        parent_set = set()
        child_set = set()
        for parent, child, is_left in descriptions:
            if parent not in node_map:
                node_map[parent] = TreeNode(parent)
            if child not in node_map:
                node_map[child] = TreeNode(child)
            if is_left:
                node_map[parent].left = node_map[child]
            else:
                node_map[parent].right = node_map[child]
            parent_set.add(parent)
            child_set.add(child)
        for k,v in node_map.items():
            if k in parent_set and k not in child_set:
                return v
        return None
