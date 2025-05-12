from typing import List, Counter, Optional

from common.base import TreeNode


class Solution2094:
    def findEvenNumbers(self, digits: List[int]) -> List[int]:
        cnt = Counter(digits)
        ans = []
        # 枚举所有三位数偶数
        for i in range(100, 1000, 2):
            # digits 有充足的数字组成 i
            if Counter(map(int, str(i))) <= cnt:
                ans.append(i)
        return ans

    def findEvenNumbers2(self, digits: List[int]) -> List[int]:
        digits.sort()
        res = []
        trace = []
        used = [False] * len(digits)

        def back_trace(arr: List[int]):
            if len(trace) == 3:
                if trace[0] != 0 and trace[-1] % 2 == 0:
                    res.append(trace[0] * 100 + trace[1] * 10 + trace[0])
                return
            for i in range(len(arr)):
                if used[i]:
                    continue
                if i > 0 and arr[i] == arr[i - 1] and used[i] is False:
                    continue
                trace.append(arr[i])
                used[i] = True
                back_trace(arr)
                used[i] = False
                trace.pop(-1)

        back_trace(digits)
        res.sort()
        return res


class Solution889:
    def constructFromPrePost(self, preorder: List[int], postorder: List[int]) -> Optional[TreeNode]:
        def build_tree(preorder: List[int], pre_start, pre_end, postorder: List[int], post_start, post_end) -> Optional[
            TreeNode]:
            if pre_start > pre_end:
                return None
            if pre_start == pre_end:
                return TreeNode(preorder[post_start])
            value = preorder[pre_start]
            left_root = preorder[pre_start + 1]
            idx = postorder[left_root]
            left_size = idx - post_start + 1
            root = TreeNode(value)
            root.left = build_tree(preorder, pre_start + 1, pre_start + left_size, postorder, post_start, idx)
            root.right = build_tree(preorder, pre_start + left_size + 1, pre_end, postorder, idx + 1, post_end - 1)
            return root

        return build_tree(preorder, 0, len(preorder) - 1, postorder, 0, len(postorder) - 1)


class Solution1028:
    def recoverFromPreorder(self, traversal: str) -> Optional[TreeNode]:
        arr :List[str]= traversal.split("-")
        def build_tree(array:List[str])->Optional[TreeNode]:
            if len(array) == 0:
                return None
            value = array.pop(0)
            if value == "":
                return None
            root = TreeNode(int(value))
            root.left = build_tree(array)
            root.right = build_tree(array)
            return  root
        return build_tree(arr)


a = "1-2--3--4-5--6--7"
arr:List[str] = a.split("-")
print(arr)