from collections import OrderedDict

N = int(input())
S = [str(input()) for _ in range(N)]

num = []
for i in range(N):
    num.append(S.index(S[i])+1)

print(num)
    
ans = list(OrderedDict.fromkeys(num))

for i in range(len(ans)):
    print(ans[i])



