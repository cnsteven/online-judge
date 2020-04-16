/*
 * @lc app=leetcode.cn id=438 lang=cpp
 *
 * [438] 找到字符串中所有字母异位词
 */
#include "main.h"

// @lc code=start
class Solution {
  public:
    vector<int> findAnagrams(string s, string p) {
        vector<int> res;
        unordered_map<char, int> needs, window;
        for (char c : p)
            ++needs[c];
        int l = 0, r = 0, match = 0;
        while (r < s.size()) {
            char c1 = s[r++];
            if (needs.count(c1)) {
                ++window[c1];
                if (window[c1] == needs[c1])
                    ++match;
            }
            while (match == needs.size()) {
                if (r - l == p.size())
                    res.emplace_back(l);
                char c2 = s[l++];
                if (needs.count(c2)) {
                    --window[c2];
                    if (window[c2] < needs[c2])
                        --match;
                }
            }
        }
        return res;
    }
};
// @lc code=end
