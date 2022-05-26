A, B, C = map(int, input().split())

def gcd(a ,b):
  if b == 0: 
    return a 
  else:
    return gcd(b, a % b)

max = gcd(A,gcd(B,C))

ans=((A//max)-1)+((B//max)-1)+((C//max)-1)

print(ans)
