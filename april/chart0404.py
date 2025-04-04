from typing import Optional

from common.base import TreeNode


class Result:
    def __init__(self, node: Optional[TreeNode], depth: int):
        self.node = node
        self.depth = depth


def dfs(node: Optional[TreeNode]):
    if node is None:
        return Result(None, 0)
    left_result: Result = dfs(node.left)
    right_result: Result = dfs(node.right)
    if left_result.depth == right_result.depth:
        return Result(node, left_result.depth + 1)
    if left_result.depth > right_result.depth:
        return Result(left_result.node, left_result.depth + 1)
    return Result(right_result.node, right_result.depth + 1)


def lcaDeepestLeaves1123(root: Optional[TreeNode]):
    """
    :type root: Optional[TreeNode]
    :rtype: Optional[TreeNode]
    """

    if root is None:
        return None
    result: Result = dfs(root)
    return result.node
