# Last updated: 9/1/2026, 11:56:49 AM
1class Solution:
2    def findingUsersActiveMinutes(self, logs: List[List[int]], k: int) -> List[int]:
3        users={}
4        for user,minute in logs:
5            if user not in users:
6                users[user]=set()
7            users[user].add(minute)
8        ans=[0]*k
9        for u in users:
10            act=len(users[u])
11            ans[act-1]+=1
12        return ans
13