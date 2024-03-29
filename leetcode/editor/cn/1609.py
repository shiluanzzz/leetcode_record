#
# @lc app=leetcode.cn id=1609 lang=python3
#
# [1609] 奇偶树
#

from platform import node


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isEvenOddTree(self, root) -> bool:
        if not root: return False
        nodeList = [root]

        def check():
            if len(check) == 0: return True
            for i in range(0, len(nodeList)):
                if nodeList[i].val % 2 != (depth + 1) % 2:
                    return False
                if i == 0: continue
                if nodeList[i].val > nodeList[i - 1].val != ((depth + 1) % 2 == 0):
                    return False
            return True

        depth = 0
        while nodeList:
            child = []
            for each in nodeList:
                if each.left:
                    child.append(each.left)
                if each.right:
                    child.append(each.right)
            nodeList = child
            depth += 1
            if not check(): return False
        return True

    def solve2(self, root):
        nodes = [root]

        def dfs(nodes, depth):
            new_nodes = []
            for i, v in enumerate(nodes):
                if i != 0 and nodes[i].val > nodes[i - 1].val != depth % 2 == 0:
                    return False
                if v.val % 2 == 0 != depth % 2 == 0:
                    return False
                if v.left: new_nodes.append(v.left)
                if v.right: new_nodes.append(v.right)
            if new_nodes == []: return True
            return dfs(new_nodes, depth + 1)
        return dfs(nodes, 0)

# @lc code=end
