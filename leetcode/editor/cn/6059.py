
from collections import *
testcaset=[["(","(",")","(",")","(","(",")","(","(",")",")",")",")",")","(",")","(","(",")","(","(",")",")",")",")",")","(","(","(","("],[")","(","(","(",")","(",")","(","(",")",")",")",")","(",")",")","(","(",")",")","(",")","(",")","(","(",")","(",")","(","("],[")",")","(","(",")","(","(",")",")",")",")","(","(",")",")","(",")","(",")",")","(","(","(",")",")",")","(",")",")","(",")"],["(","(",")","(",")","(","(",")","(","(","(",")",")","(",")","(",")",")",")",")",")",")","(","(",")","(",")","(",")","(","("],[")",")","(",")",")","(","(","(",")",")","(",")","(",")",")",")","(","(","(",")",")","(",")","(",")",")","(","(","(","(",")"],[")",")","(","(",")","(",")","(",")","(",")","(",")",")","(",")","(",")",")","(",")","(","(","(",")","(",")",")",")","(","("],[")","(","(","(","(","(","(",")",")","(","(",")","(",")",")","(",")",")",")","(","(","(",")","(","(",")",")","(",")","(",")"],[")",")","(","(","(","(","(","(","(",")",")","(","(","(","(","(","(","(","(","(","(","(","(",")",")","(","(",")",")","(",")"],["(",")",")",")","(","(",")",")",")",")","(",")",")","(",")",")","(","(","(","(","(","(","(",")",")","(","(",")",")","(","("],["(","(",")","(",")",")",")",")","(","(","(",")",")",")","(",")","(","(",")","(","(","(",")","(","(","(","(","(",")",")",")"],["(",")","(","(","(","(",")","(","(",")",")","(","(",")","(","(","(",")","(","(","(",")",")","(",")",")","(",")","(","(",")"],[")",")","(","(","(","(",")","(","(",")",")","(",")",")","(",")","(","(","(","(","(","(","(",")","(","(",")",")","(","(","("],["(",")",")",")","(",")","(","(","(",")",")",")","(",")","(",")",")","(","(","(","(",")","(",")",")",")",")",")",")","(","("],["(","(","(","(","(","(",")",")","(",")","(","(","(",")",")","(",")","(",")","(",")","(","(","(",")",")",")","(",")","(","("],["(",")",")",")",")","(","(",")",")",")",")",")",")","(","(",")","(",")",")","(",")","(",")",")",")","(","(",")","(","(","("],["(",")",")","(","(",")",")","(",")",")","(","(","(",")",")",")",")","(","(","(",")",")","(",")","(","(","(","(",")",")",")"],[")","(","(",")","(","(",")",")",")","(","(","(","(",")","(",")",")",")","(",")","(",")","(","(",")","(","(","(","(","(","("],["(",")","(",")","(","(",")",")",")",")",")","(","(",")",")","(",")","(",")",")",")",")","(","(","(",")","(",")","(",")",")"],["(",")","(",")",")",")","(","(","(",")","(",")","(","(",")",")","(",")","(",")","(",")","(","(","(","(","(",")","(",")","("],[")",")",")",")",")","(",")",")","(","(",")","(",")",")","(",")",")","(","(","(","(",")","(","(","(","(",")",")",")",")","("],[")","(","(","(","(","(",")","(",")",")",")",")","(","(","(",")",")","(",")",")","(","(","(","(","(","(",")",")","(","(","("],["(","(","(",")",")","(",")","(",")",")",")",")","(",")",")",")",")","(",")","(","(","(","(",")","(","(","(","(","(","(",")"]]

def hasValidPath(grid: list[list[str]]) -> bool:
    # 剪枝
    n,m=len(grid),len(grid[0])
    if grid[0][0]==')' or grid[n-1][m-1]=="(":return False
    dp=defaultdict(set) #dp 记录标志位可能遇到的组合情况.
    dp['0-0']=set([1])
    for i in range(0,n):
        for j in range(0,m):
            c="{}-{}".format(i,j)
            # 从左往右走
            if i>0:
                pre_c="{}-{}".format(i-1,j)
                # 当前是）的话就对前面来的所有组合去减1
                if grid[i][j]==")":
                    for pre in dp[pre_c]:
                        dp[c].add(pre-1)
                else:
                    for pre in dp[pre_c]:
                        dp[c].add(pre+1)
            # 从上往下走
            if j>0:
                pre_c="{}-{}".format(i,j-1)
                if grid[i][j]==")":
                    for pre in dp[pre_c]:
                        dp[c].add(pre-1)
                else:
                    for pre in dp[pre_c]:
                        dp[c].add(pre+1)
    # print(dp)
    # print(len(dp),m*n)
    print(n,m)
    if 0 in dp[str(n-1)+'-'+str(m-1)]:
        return True
    return False

a=hasValidPath(testcaset)
print(a)