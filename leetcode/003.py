# -*- coding:utf-8 -*-
# __author__ = "shitou6"


def lengthOfLongestSubstring(s: str) -> int:
    ll=[] # max str item
    max_num=0
    q,p=0,0
    while q<len(s) and p<len(s):
        q=p
        if s[p] in ll:
            max_num=max(max_num,len(ll))
            print('ll:',str(ll))
            ll=[s[p]]
            q=p
            p+=1
        else:
            ll.append(s[p])
            p+=1
            q+=1
    print(ll)
    max_num=max(max_num,len(ll))
    return max_num if len(s)>1 else len(s)


def lengthOfLongestSubstring2(s: str) -> int:
    if len(s) == 0:
        return 0
    a=1
    lens=len(s) #
    substr=s[0] # 当前比较的子串
    max_sub=0 # 最大子串长度
    # 遍历
    while(a<lens):
        if s[a] not in substr:
            substr=substr+s[a]
            a+=1
        else:
            print("old str:",substr)
            max_sub= len(substr) if len(substr)>max_sub else max_sub
            split_index=substr.find(s[a])
            substr=substr[split_index+1:]+s[a]
            print("new str:",substr)
            a+=1
    print("max_sub",substr)
    max_sub= len(substr) if len(substr)>max_sub else max_sub
    return max_sub

a=lengthOfLongestSubstring2("abcabcbb")
print(a)