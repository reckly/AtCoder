N = int(input())
cp = [map(int, input().split()) for _ in range(N)]
C, P = [list(i) for i in zip(*cp)]
Q = int(input())
lr = [map(int, input().split()) for _ in range(Q)]
L, R = [list(i) for i in zip(*lr)]

ans1 = [0]*(N+1)
ans2 = [0]*(N+1) 
for i in range(N):
    ans1[i+1]=ans1[i]
    ans2[i+1]=ans2[i]
    if C[i]==1:
        ans1[i+1]+=(P[i])
    else:
        ans2[i+1]+=(P[i])

for i in range(Q):
    S1 = ans1[R[i]] - ans1[L[i]-1]
    S2 = ans2[R[i]] - ans2[L[i]-1]
    print(str(S1)+" "+str(S2))
    
    
    
