H,W = input().split()

a = []
for i in range(int(H)):
    A = input()
    a.append(A)

for i in range(2,int(H)-1):
    n1 =int(a[int(i)-1].find("o"))
    if n1 != -1:
        continue



n2 =int(a[0].find("o"))
print(n1)
print(str(int(H)-1+abs(n1-n2))) 