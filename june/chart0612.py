from typing import List


class Solution1704:
    def findLongestSubarray(self, array: List[str]) -> List[str]:
        prefix_sum = {0: -1}
        start_index = -1
        max_len = 0
        s = 0

        for i,v in enumerate(array):
            if "0"<=v[0]<="9":
                s += 1
            else:
                s-=1
            if s in prefix_sum:
                first_index = prefix_sum[s]
                if i - first_index > max_len:
                    max_len = i - first_index
                    start_index = first_index + 1
            else:
                prefix_sum[s] = i
        if max_len == 0:
            return []
        return array[start_index:start_index+max_len]
