x,y,n=list(map(int,input().split()))
print(((n//3)*y)+((n%3)*x)) if y//3 < x else print(n*x)