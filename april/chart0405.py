from typing import List, Callable, Optional

from common.base import TreeNode, Node


def subsetXORSum1863(self, nums: List[int]) -> int:
    def dfs(ls: List[int], idx: int, current_xor: int) -> int:
        # 当前子集的 XOR 值加入结果
        res = current_xor
        for i in range(idx, len(ls)):
            # 回溯：计算当前元素加入后的 XOR 值
            next_xor = current_xor ^ ls[i]
            # 递归处理下一个元素
            res += dfs(ls, i + 1, next_xor)
        return res

    # 起始状态：从索引 0 开始，初始 XOR 值为 0
    return dfs(nums, 0, 0)


def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
    if root is None:
        return None
    left = self.invertTree(root.left)
    right = self.invertTree(root.right)
    # 交换左右子树
    root.left, root.right = right, left
    # 返回根节点
    return root


class Solution116:
    # 116 填充每个节点的下一个右侧节点指针
    def connect(self, root: 'Optional[Node]') -> 'Optional[Node]':
        if not root:
            return root
        queue = [root]
        while queue:
            sz = len(queue)
            for i in range(sz):
                node = queue.pop(0)
                if i < sz - 1:
                    node.next = queue[0]
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)
        return root

    def connect2(self, root: 'Optional[Node]') -> 'Optional[Node]':
        if not root:
            return root
        self.traversForConnect(root.left, root.right)
        return root

    def traversForConnect(self, node1: 'Optional[Node]', node2: 'Optional[Node]'):
        if node1 is None or node2 is None:
            return
        node1.next = node2
        self.traversForConnect(node1.left, node1.right)
        self.traversForConnect(node2.left, node2.right)
        self.traversForConnect(node1.right, node2.left)


class Solution114:
    # 114 二叉树展开为链表
    def flatten(self, root: Optional[TreeNode]) -> None:
        """
        Do not return anything, modify root in-place instead.
        """
        if root is None:
            return None
        self.flatten(root.left)
        self.flatten(root.right)
        left = root.left
        right = root.right
        root.left = None
        root.right = left
        p = root
        while p.right:
            p = p.right
        p.right = right


class Solution654:
    def constructMaximumBinaryTree(self, nums: 'List[int]') -> Optional[TreeNode]:
        return self.build_tree(nums, 0, len(nums) - 1)

    def build_tree(self, nums: List[int], start: int, end: int) -> Optional[TreeNode]:
        if start > end:
            return None
        max_index = start
        for i in range(start + 1, end + 1):
            if nums[i] > nums[max_index]:
                max_index = i

        root = TreeNode(nums[max_index])
        root.left = self.build_tree(nums, start, max_index - 1)
        root.right = self.build_tree(nums, max_index + 1, end)
        return root


# 105 从前序与中序遍历序列构造二叉树
class Solution105:

    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        index_mp: dict[int, int] = {}
        for i, val in enumerate(inorder):
            index_mp[val] = i
        return self.build_tree(preorder, inorder, 0, len(preorder) - 1, 0, len(inorder) - 1, index_mp)

    def build_tree(self,
                   preorder: List[int],
                   inorder: List[int],
                   pre_start: int,
                   pre_end: int,
                   in_start: int,
                   in_end: int,
                   idx_map: dict[int, int]) -> Optional[TreeNode]:
        if pre_start > pre_end:
            return None
        root_val = preorder[pre_start]
        root_idx = idx_map[root_val]
        left_size = root_idx - in_start
        root = TreeNode(root_val)
        root.left = self.build_tree(preorder, inorder, pre_start + 1, pre_start + left_size, in_start, root_idx - 1,
                                    idx_map)
        root.right = self.build_tree(preorder, inorder, pre_start + left_size + 1, pre_end, root_idx + 1, in_end,
                                     idx_map)
        return root

# 106 从后序与中序遍历序列构造二叉树
class Solution106:
    def buildTree(self, inorder: List[int], postorder: List[int]) -> Optional[TreeNode]:
        idx_map : dict[int, int] = {}
        for idx, v in enumerate(inorder):
            idx_map[v] = idx
        return self.build_tree(inorder, postorder, 0, len(inorder) - 1, 0, len(postorder) - 1, idx_map)

    def build_tree(self,
                   inorder: List[int],
                   postorder: List[int],
                   in_start: int,
                   in_end: int,
                   post_start: int,
                   post_end: int,
                   idx_map: dict[int, int]) -> Optional[TreeNode]:
        if in_start > in_end:
            return None
        root_val = postorder[post_end]
        root_idx = idx_map[root_val]
        left_size = root_idx - in_start
        root = TreeNode(root_val)
        root.left = self.build_tree(inorder, postorder, in_start, root_idx - 1, post_start, post_start + left_size - 1,
                                    idx_map)
        root.right = self.build_tree(inorder, postorder, root_idx + 1, in_end, post_start + left_size, post_end - 1,
                                    idx_map)
        return root