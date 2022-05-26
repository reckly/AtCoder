N,M = map(int, input().split())
a = [list(map(int, input().split())) for l in range(N)]
Vsum = []
Hsum = []

for i in range(N):
    sum=0
    for j in range(M):
        sum+=a[i][j]
    Vsum.append(sum)
        
for i in range(M):
    sum=0
    for j in range(N):
        sum+=a[j][i]
    Hsum.append(sum)

for i in range(N):
    for j in range(M):
        if(j==M-1):
            print(str(Vsum[i]+Hsum[j]-a[i][j]),end="")
        else:
            print(str(Vsum[i]+Hsum[j]-a[i][j])+" ",end="")
    print("")


