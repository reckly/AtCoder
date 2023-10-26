H,W=list(map(int,input().split()))
Glist=[]
for i in range(H):
    temp_list=list(input())
    Glist.append(temp_list)

#print(Glist)

i=1
j=1
flag=0
for sss in range(1000000):
    Gstr=Glist[i-1][j-1]
    #print(Gstr)
    if Gstr=="U" and i!=1:
        i-=1
    elif Gstr=="D" and i!=H:
        i+=1
    elif Gstr=="L" and j!=1:
        j-=1
    elif Gstr=="R" and j!=W:
        j+=1
    else:
        flag=1
        break

print(i,j) if flag==1 else print("-1")