from statistics import median 

A, B, C = input().split()
l =[A,B,C]

if B==median(l):
    print("Yes")
else:
    print("No")

