#
# @lc app=leetcode.cn id=1029 lang=python3
#
# [1029] 两地调度
#
from typing import List


# @lc code=start
class Solution:
    def twoCitySchedCost(self, costs: List[List[int]]) -> int:
        costs.sort(key=lambda x: x[0] - x[1])
        ans = 0
        n = len(costs) // 2
        for i in range(n):
            ans += costs[i][0] + costs[i + n][1]
        return ans


# @lc code=end
