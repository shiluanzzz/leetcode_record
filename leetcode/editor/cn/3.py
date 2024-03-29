# -*- coding:utf-8 -*-
# __author__ = "shitou6"


def lengthOfLongestSubstring(s: str) -> int:
    ll = []  # max str item
    max_num = 0
    q, p = 0, 0
    while q < len(s) and p < len(s):
        q = p
        if s[p] in ll:
            max_num = max(max_num, len(ll))
            print('ll:', str(ll))
            ll = [s[p]]
            q = p
            p += 1
        else:
            ll.append(s[p])
            p += 1
            q += 1
    print(ll)
    max_num = max(max_num, len(ll))
    return max_num if len(s) > 1 else len(s)


def lengthOfLongestSubstring2(s: str) -> int:
    if len(s) == 0:
        return 0
    a = 1
    lens = len(s)  #
    substr = s[0]  # 当前比较的子串
    max_sub = 0  # 最大子串长度
    # 遍历
    while (a < lens):
        if s[a] not in substr:
            substr = substr + s[a]
            a += 1
        else:
            print("old str:", substr)
            max_sub = len(substr) if len(substr) > max_sub else max_sub
            split_index = substr.find(s[a])
            substr = substr[split_index + 1:] + s[a]
            print("new str:", substr)
            a += 1
    print("max_sub", substr)
    max_sub = len(substr) if len(substr) > max_sub else max_sub
    return max_sub


import collections


class Solution:
    def lengthOfLongestSubstring1(self, s: str) -> int:
        ans = 0
        c = collections.defaultdict(int)
        temp_ans = 0
        repead_char_idx = 0
        # temp_ans 就是记录下一个无重复子串的长度，什么时候重新计算，当遇到重复字符的时候就重新计算
        for i, v in enumerate(s, 1):
            if v in c and c[v] >= repead_char_idx:
                ans = max(ans, temp_ans)
                temp_ans = i - c[v]
                # 当有重复字符的时候，重复字符前面的全废了
                repead_char_idx = c[v]
                c[v] = i
            else:
                temp_ans += 1
                c[v] = i
        return max(ans, temp_ans)

    def lengthOfLongestSubstring(self, s: str) -> int:
        # TODO 做了3次还是错
        # 这个思路想的是如果有重复字符出现，那么重复字符就是一个新的开始位置，重新计算。
        # 但是dvdf这种情况就不对。 修正方法：把prev的赋值改成history[v]+1
        # 这样还是不行，tmmzuxt就不行，因为当遇到重复字符m的时候，m前面的t应该也要失效。所以必须记录一个repeat_char_idx
        # 还是不行 abcabcbb不能过,repeat_char_idx的赋值搞错了 不是i
        history = collections.defaultdict(int)
        ans, prev = 0, 0
        repeat_char_idx = 0
        for i, v in enumerate(s):
            if v in history and history[v] >= repeat_char_idx:
                prev = history[v] + 1
                repeat_char_idx = history[v]  # 这个应该是history[v]不是i
            else:
                ans = max(ans, i - prev + 1)
            history[v] = i
        return ans

# if __name__ == '__main__':
#     """
#     """
#     params = """
#     "tmmzuxt"
#         "dvdf"
#     "pwwkew"
#     "bbbbb"
#     "abcabcbb"
#     "abcabcbb"
#     """
#     from leetcode.tools import test_func_batch
#
#     test_func_batch(Solution().lengthOfLongestSubstring, params)
