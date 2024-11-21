#
# @lc app=leetcode.cn id=961 lang=python3
#
# [961] 在长度 2N 的数组中找出重复 N 次的元素
#
# https://leetcode.cn/problems/n-repeated-element-in-size-2n-array/description/
#
# algorithms
# Easy (70.49%)
# Likes:    204
# Dislikes: 0
# Total Accepted:    89.4K
# Total Submissions: 126.8K
# Testcase Example:  '[1,2,3,3]'
#
# 给你一个整数数组 nums ，该数组具有以下属性：
#
#
#
#
# nums.length == 2 * n.
# nums 包含 n + 1 个 不同的 元素
# nums 中恰有一个元素重复 n 次
#
#
# 找出并返回重复了 n 次的那个元素。
#
#
#
# 示例 1：
#
#
# 输入：nums = [1,2,3,3]
# 输出：3
#
#
# 示例 2：
#
#
# 输入：nums = [2,1,2,5,3,2]
# 输出：2
#
#
# 示例 3：
#
#
# 输入：nums = [5,1,5,2,5,3,5,4]
# 输出：5
#
#
#
#
#
#
# 提示：
#
#
# 2 <= n <= 5000
# nums.length == 2 * n
# 0 <= nums[i] <= 10^4
# nums 由 n + 1 个 不同的 元素组成，且其中一个元素恰好重复 n 次
#
#
#
from typing import List


# @lc code=start
class Solution:
    def repeatedNTimes(self, nums: List[int]) -> int:
        s = set()
        for num in nums:
            if num in s:
                return num
            s.add(num)
        return -1


# @lc code=end
