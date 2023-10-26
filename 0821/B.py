N,M,T=list(map(int,input().split()))
Alist=list(map(int,input().split()))
dict={}
for i in range(M):
    X,Y=list(map(int,input().split()))
    dict[X]=Y

#print(N,M,T)
#print(Alist)
#print(dict)

room=1
for i in range(len(Alist)):
    T-=Alist[i]
    #print(T)
    if T<=0:
        break
    else:
        room+=1
    #print("増加判定")
    try:
        T+=dict[room]
    except:
        None

print("Yes") if T>0 else print("No")