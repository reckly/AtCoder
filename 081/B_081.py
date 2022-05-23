N = int(input())
x = list(map(int, input().split()))
count = 0
for i in range(200):
    for j in range(N):
        if x[j]%2==0:
            x[j]=x[j]/2
            count+=1
        else:
            break

print(int(count/N))

