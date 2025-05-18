from common.base import TreeNode


class Solution257:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        ancestor = root
        while True:
            if p.val < ancestor.val and q.val < ancestor.val:
                ancestor = ancestor.left
            elif p.val > ancestor.val and q.val > ancestor.val:
                ancestor = ancestor.right
            else:
                break
        return ancestor


class Solution236:
    def lowestCommonAncestor(self, root: "TreeNode", p: "TreeNode", q: "TreeNode") -> "TreeNode":
        parent :dict[int,TreeNode]= {}
        def dfs(node:TreeNode):
            if not node.left:
                parent[node.left.val] = node
                dfs(node.left)
            if not node.right:
                parent[node.right.val] = node
                dfs(node.right)

        dfs(root)
        visited:set[int] = set()
        while p:
            visited.add(p.val)
            p = parent[p.val]
        while q:
            if q.val in visited:
                return q
            q = parent[q.val]
        return None
