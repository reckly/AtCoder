import math
N, K = map(int, input().split())
x = list(map(int, input().split()))
y = list(map(int, input().split()))
dif = 0

for i in range(N):
  dif += math.fabs(y[i]-x[i])

if K % 2 == dif % 2 and K>=dif:
  print("Yes")
else:
  print("No")


